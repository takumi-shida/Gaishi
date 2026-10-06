# Japanese text in HTML, slides, and other visual deliverables

Read this when the deliverable (web page, UI, slide deck, document, image text) contains Japanese text. It is a checklist, not a style guide.

## Write the copy in the audience language, directly

- Write on-screen text (headings, body, buttons, slide bullets, alt text) in Japanese from the start. Do not draft it in English and translate afterwards: translation changes text length and breaks layouts that were sized for the English copy.
- Keep code, class names, ids, file names, and code comments in English.
- If the audience language is not stated, use the language of the user's request and say which one you assumed in the report.

## HTML / CSS

- `<html lang="ja">` and `<meta charset="utf-8">`. For mixed-language pages, mark non-Japanese spans with their own `lang`.
- Font stack with Japanese fallbacks, Latin first only if you want Latin glyphs from it, e.g. `font-family: system-ui, "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Noto Sans JP", "Yu Gothic", Meiryo, sans-serif;`. Never rely on a single font that lacks kana/kanji.
- Japanese has no spaces between words. Do not use `white-space: nowrap` or fixed widths on text that may grow; allow wrapping (`overflow-wrap: anywhere` for long unbroken strings).
- Use `line-height` of about 1.6–1.9 for body text; CJK needs more than Latin.
- Line breaking: the default `word-break: normal` already follows kinsoku rules in modern browsers. `word-break: auto-phrase` breaks at phrase boundaries but is not supported everywhere; use it as progressive enhancement only.
- JavaScript: do not pass non-ASCII strings to `btoa`/`atob` directly; encode as UTF-8 first.

## Slides (HTML, PPTX, PDF)

- Budget text by display width: full-width characters take about one em each. A line that fits 60 Latin characters fits roughly 30 Japanese ones.
- Keep headings short; prefer fewer, shorter bullets over shrinking fonts below a readable size.
- Set an explicit East Asian font (e.g. Noto Sans JP, Yu Gothic, Meiryo) for the deck theme; otherwise renderers substitute inconsistently.
- Text frames must not overflow their shapes; shorten the copy before reducing font size.

## Verify by rendering

Reading the code does not show overflow, tofu (missing glyphs), or bad line breaks. Render the result (headless browser screenshot, or export the slides to images) and look at it before reporting. Report any page or slide you could not render.

## Other Japanese-text pitfalls in code

- Encoding: UTF-8 everywhere, including file I/O and HTTP headers.
- Width: terminal and table alignment must account for full-width characters (East Asian Width). Variation selectors take no columns, and Python's `len()` counts code points, not display width.
- Normalization: choose NFC or NFKC deliberately. NFKC merges compatibility ideographs (e.g. U+FA19 and U+795E) and so can alter text that was only supposed to be reformatted; full-width and half-width forms also differ. Do not normalize text you only display or reformat.
- Sorting and searching: do not assume byte or code-point order matches Japanese reading order.
