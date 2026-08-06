# Markdown Quick Guide

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/markdown-guide.md)

`REPORT.md` and `TEAM.md` are plain text files written in **Markdown** — a lightweight way to add formatting (headings, bold, lists, tables, links) using plain characters, no menus or toolbars needed. GitHub renders it automatically wherever the file is viewed, so what you type is what your team and instructor will see.

This covers everything you'll actually need for `REPORT.md`. For the full spec, see [GitHub's own Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) — but you shouldn't need much beyond this page.

## Headings

```markdown
# Biggest heading (used once, for the title)
## Section heading
### Subsection heading
```

`REPORT.md` already has all its headings in place — you're filling in the text under them, not usually adding new ones.

## Bold, italic, inline code

```markdown
**bold text**
*italic text*
`inline code`, like a variable name: `crew.kickoff()`
```

## Lists

```markdown
- Bullet one
- Bullet two
  - Indented sub-bullet (two spaces)

1. First step
1. Second step (Markdown numbers these automatically — you don't need to write 2., 3., ...)
```

## Links

```markdown
[link text](https://example.com)
[a file in this repo](src/research_crew/crew.py)
```

## Tables

Used throughout `REPORT.md`, most importantly the **Sprint Progression** table:

```markdown
| Sprint | Added | What changed |
| --- | --- | --- |
| 0 | Setup | First LLM call |
| 1 | Prompting | Baseline zero-shot prompt |
```

Renders as:

| Sprint | Added | What changed |
| --- | --- | --- |
| 0 | Setup | First LLM call |
| 1 | Prompting | Baseline zero-shot prompt |

Tip: you don't need to manually align the `|` columns — GitHub renders it correctly either way, and most editors (see below) auto-format the spacing for you.

## Code blocks

For more than one line of code, or to show a full snippet:

````markdown
```python
agent = Agent(role="Researcher", goal="...", backstory="...")
```
````

The language name after the first ` ``` ` (`python`, `bash`, `yaml`, ...) enables syntax highlighting — optional, but makes code easier to read.

## Blockquotes

Used in `REPORT.md` for notes and instructions (the italicized `_(...)_` guidance text and the `>` callouts):

```markdown
> A note or callout, like the ones already in REPORT.md explaining what to write in each section.
```

## Horizontal rule

`REPORT.md` uses `---` on its own line to separate major sections — already in place, nothing you need to add yourself.

## Previewing what you write

- **In VS Code:** open the `.md` file, then click the preview icon in the top-right corner of the editor (or press `Ctrl+Shift+V` / `Cmd+Shift+V`) to see it rendered side-by-side as you type.
- **On github.com:** open the file and click the **"Preview"** tab before committing, if you're editing directly in the browser.

If you'd rather not think about the syntax at all: VS Code's **"Markdown All in One"** extension adds keyboard shortcuts (`Ctrl+B` for bold, etc.) and auto-formatting on top of what's on this page. For a fully WYSIWYG experience — formatting renders live as you type, no `#`/`**`/`|` visible — try [Obsidian](https://obsidian.md) (free) or [Typora](https://typora.io) (paid); both just edit the same `.md` file in your cloned repo, so committing and pushing still happens through VS Code as usual.
