#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import shutil
import sys
import urllib.request
from pathlib import Path
from typing import Any


def fail_missing_dependency() -> None:
    print(
        "Missing dependency: Pillow. Install with `pip install Pillow`.",
        file=sys.stderr,
    )
    raise SystemExit(2)


try:
    from PIL import Image, ImageOps
except ImportError:
    fail_missing_dependency()


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def parse_ratio(value: str) -> tuple[int, int]:
    if ":" in value:
        left, right = value.split(":", 1)
        return max(1, int(left)), max(1, int(right))
    numeric = float(value)
    return max(1, int(numeric * 1000)), 1000


def target_size(width: int | None, height: int | None, ratio: tuple[int, int]) -> tuple[int, int]:
    if width and height:
        return width, height
    if width:
        return width, max(1, round(width * ratio[1] / ratio[0]))
    if height:
        return max(1, round(height * ratio[0] / ratio[1])), height
    return 1600, max(1, round(1600 * ratio[1] / ratio[0]))


def safe_stem(value: str, fallback: str) -> str:
    stem = "".join(char.lower() if char.isalnum() else "-" for char in value).strip("-")
    while "--" in stem:
        stem = stem.replace("--", "-")
    return stem[:64] or fallback


def source_id(source: str, explicit: str | None = None) -> str:
    if explicit:
        return safe_stem(explicit, "image")
    path_name = Path(source).stem if not source.startswith(("http://", "https://")) else source.rsplit("/", 1)[-1]
    digest = hashlib.sha1(source.encode("utf-8")).hexdigest()[:8]
    return f"{safe_stem(path_name, 'image')}-{digest}"


def guess_extension(url: str, content_type: str | None = None) -> str:
    path_ext = Path(url.split("?", 1)[0]).suffix.lower()
    if path_ext in IMAGE_EXTENSIONS:
        return ".jpg" if path_ext == ".jpeg" else path_ext
    if content_type:
        guessed = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
        if guessed and guessed.lower() in IMAGE_EXTENSIONS:
            return ".jpg" if guessed.lower() == ".jpeg" else guessed.lower()
    return ".jpg"


def download(url: str, destination: Path) -> Path:
    request = urllib.request.Request(url, headers={"User-Agent": "ppt-writer-image-prep/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        content_type = response.headers.get("Content-Type")
        ext = guess_extension(url, content_type)
        final_path = destination.with_suffix(ext)
        final_path.write_bytes(response.read())
    return final_path


def copy_local(path: Path, destination: Path) -> Path:
    ext = ".jpg" if path.suffix.lower() == ".jpeg" else path.suffix.lower()
    final_path = destination.with_suffix(ext if ext in IMAGE_EXTENSIONS else ".jpg")
    shutil.copy2(path, final_path)
    return final_path


def collect_from_scan_dirs(scan_dirs: list[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            continue
        for path in sorted(scan_dir.rglob("*")):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
                records.append({"source": str(path), "id": source_id(str(path))})
    return records


def load_manifest(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("images", [])
    if not isinstance(data, list):
        raise ValueError("manifest must be a list or an object with an images list")
    records = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("each manifest image must be an object")
        records.append(item)
    return records


def prepare_raw(record: dict[str, Any], raw_dir: Path) -> tuple[Path, str]:
    source = str(record.get("source") or record.get("path") or record.get("url") or "").strip()
    if not source:
        raise ValueError("image record missing source/path/url")
    image_id = source_id(source, str(record.get("id")) if record.get("id") else None)
    destination = raw_dir / image_id
    if source.startswith(("http://", "https://")):
        return download(source, destination), source

    local_path = Path(source).expanduser()
    if not local_path.exists():
        raise FileNotFoundError(f"image source not found: {source}")
    return copy_local(local_path, destination), str(local_path)


def crop_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def resize_contain(image: Image.Image, size: tuple[int, int], background: tuple[int, int, int] = (255, 255, 255)) -> Image.Image:
    contained = ImageOps.contain(image, size, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, background)
    left = (size[0] - contained.width) // 2
    top = (size[1] - contained.height) // 2
    canvas.paste(contained.convert("RGB"), (left, top))
    return canvas


def process_image(raw_path: Path, output_path: Path, *, size: tuple[int, int], fit: str) -> dict[str, Any]:
    with Image.open(raw_path) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        original_size = image.size
        if fit == "contain":
            processed = resize_contain(image, size)
        else:
            processed = crop_cover(image, size)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        processed.save(output_path, quality=92, optimize=True)
    return {"original_width": original_size[0], "original_height": original_size[1], "width": size[0], "height": size[1]}


def build_records(args: argparse.Namespace) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if args.manifest:
        records.extend(load_manifest(args.manifest))
    records.extend({"source": str(path)} for path in args.input)
    records.extend({"url": url} for url in args.url)
    records.extend(collect_from_scan_dirs(args.scan_dir))
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="Download/copy, crop and resize PPT image assets.")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--input", type=Path, action="append", default=[])
    parser.add_argument("--url", action="append", default=[])
    parser.add_argument("--scan-dir", type=Path, action="append", default=[])
    parser.add_argument("--output-dir", type=Path, default=Path("materials/images"))
    parser.add_argument("--aspect-ratio", default="16:9")
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--fit", choices=("cover", "contain"), default="cover")
    args = parser.parse_args()

    records = build_records(args)
    if not records:
        print("prepare_images.py: no images requested", file=sys.stderr)
        return 2

    raw_dir = args.output_dir / "raw"
    processed_dir = args.output_dir / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, Any]] = []
    warnings: list[str] = []
    for record in records:
        try:
            ratio = parse_ratio(str(record.get("aspect_ratio") or args.aspect_ratio))
            size = target_size(
                int(record["width"]) if record.get("width") else args.width,
                int(record["height"]) if record.get("height") else args.height,
                ratio,
            )
            fit = str(record.get("fit") or args.fit)
            raw_path, original_source = prepare_raw(record, raw_dir)
            image_id = source_id(original_source, str(record.get("id")) if record.get("id") else None)
            processed_path = processed_dir / f"{image_id}-{size[0]}x{size[1]}.jpg"
            dimensions = process_image(raw_path, processed_path, size=size, fit=fit)
            manifest.append(
                {
                    "id": image_id,
                    "source": original_source,
                    "raw_path": str(raw_path),
                    "processed_path": str(processed_path),
                    "alt": str(record.get("alt") or record.get("caption") or ""),
                    "caption": str(record.get("caption") or ""),
                    "aspect_ratio": f"{ratio[0]}:{ratio[1]}",
                    "fit": fit,
                    **dimensions,
                }
            )
        except Exception as exc:
            warnings.append(f"{record}: {exc}")

    output = {"images": manifest, "warnings": warnings}
    manifest_path = args.output_dir / "image_manifest.json"
    manifest_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {manifest_path} with {len(manifest)} image(s)")
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    return 0 if manifest else 2


if __name__ == "__main__":
    raise SystemExit(main())
