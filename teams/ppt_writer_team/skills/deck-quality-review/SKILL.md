# Deck Quality Review

Use this skill to evaluate a generated PPT and decide whether it can be delivered.

## Review Dimensions

```text
Goal fit
Audience fit
Content accuracy
Source traceability
Storyline clarity
Slide-level readability
Visual consistency
Template fidelity when a template is provided
Media completeness for images and videos
Editable PPTX integrity
Boss requirement coverage
```

## Scoring

```text
目标匹配：0-10
内容准确性：0-10
结构清晰度：0-10
页面可读性：0-10
视觉一致性：0-10
模板遵从性：0-10
媒体完整性：0-10
来源追踪：0-10
可编辑性：0-10
综合分：0-10
```

## P0 Failures

```text
No final_deck.pptx.
Deck is mostly page screenshots.
Important claims have no source.
Boss-required section missing.
Template content copied into final deck.
Template provided but final deck ignores template layout, fonts, backgrounds, header/footer or page rhythm.
Required image/video assets remain placeholders or manual insertion instructions.
Slides unreadable or overflowing.
PPTX cannot be opened.
```

## Template Fidelity Check

When a template is provided, verify:

```text
template/template_fidelity_plan.md exists
style_spec.json includes template_pptx and template_fidelity
slides map to template page types or documented exceptions
fonts, backgrounds, margins, page furniture and component style remain consistent
new layouts stay inside the template system
unrelated template business content was not copied
```

## Media Check

Verify:

```text
images use local image_path/processed_path
videos use video_path or video_url
video links have thumbnails or readable link cards when embedding is unsupported
external media has source and rights-risk metadata
media supports the slide message rather than filling space
```

## Output Format

```text
Summary
Scores
P0 issues
P1 issues
Slide-by-slide findings
Editable PPTX check
Template fidelity check
Media asset check
Revision instructions
Decision: pass / revise
```
