# Platform limits: Custom GPT, ChatGPT Project, Gemini Gem

Research for #11 (part of #9). All sources accessed **2026-10-15**. Help-center pages carry relative "updated" stamps only; the stamp seen on the access date is noted.

Legend: **[P]** primary (official OpenAI / Google page), **[P-old]** first-party but dated announcement, **[S]** secondary only (forum, third-party blog), **[—]** not found in any source.

## Headline: two of the three targets are being retired

- **Custom GPTs are being retired.** OpenAI: new GPT creation and publishing is "not available on personal ChatGPT accounts, including Free, Go, Plus, and Pro"; only Business/Enterprise/Edu workspaces can still create GPTs. Shutdown planned for **11 Dec 2026** (approved Enterprise deferrals: 11 Feb 2027). Migration target is "Plugins": GPT instructions become a *skill*, knowledge files become plugin *reference files*. [P] [Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts) (updated "16 days ago"); [Custom GPT retirement and migration FAQ](https://help.openai.com/articles/20001519) (updated "11 days ago").
- **Gemini Gems are being replaced by skills.** "Starting in November 2026, Gems will transition to skills in Gemini Apps for personal Google Accounts"; Workspace business/enterprise/non-profit: March 2027; Workspace education: June 2027. Gems and supported files migrate automatically. [P] [About the transition from Gems to skills](https://support.google.com/gemini/answer/18560919?hl=en); [Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop).

Consequence for the project: a Custom GPT or Gem target has at most weeks of life left on personal accounts. ChatGPT Projects are the only one of the three targets with no announced end.

## Summary table

| | Custom GPT | ChatGPT Project | Gemini Gem |
|---|---|---|---|
| Instruction field limit | 8,000 chars **[S]** | **[—]** (personal custom instructions: 1,500 Free/Go, 5,000 paid [P]; not stated to apply to projects) | **[—]** |
| Knowledge file count | 20 [P] **vs** 10 [P] (OpenAI pages conflict) | Free 5 · Go/Plus 25 · Pro/Business/Enterprise/Edu 40; max 10 per upload batch [P] | 10 [P-old, 2024] / [S] |
| Knowledge file size | 512 MB/file; text/docs 2M tokens/file; spreadsheets ~50 MB; images 20 MB [P] | same as GPT (shared FAQ) [P] | 100 MB/file [P-old, 2024]; Gemini Apps general: 100 MB, video 2 GB [P] |
| Knowledge file types | "most common document, spreadsheet, image, text, and code file types" [P]; general upload table: DOCX, PDF, TXT, XLSX, XLS, CSV, TSV, PPTX [P] | PDFs, spreadsheets, docs, images, pasted text [P] | TXT, DOC, DOCX, PDF, RTF, DOT, DOTX, HWP, HWPX, Google Docs, XLS, XLSX, CSV, TSV, Google Sheets [P-old, 2024]; Markdown [S] |
| `$$` display math | renders (KaTeX) **[S]** | same renderer as ChatGPT chat **[S]** | **[—]** for chat; Canvas has a LaTeX mode [P] |
| `<details>` collapsible | **[—]** (no source; expect raw HTML not to render) | **[—]** | **[—]** |
| Markdown tables | **[—]** official; renders [S] | **[—]** official; renders [S] | renders: "Export to Sheets" exists for "responses that have a table" [P] |

## ChatGPT Custom GPT

### Instructions
- **No official character limit found.** The official GPT builder article covers how to write instructions but states no number. [—] in primary sources. [Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)
- **8,000 characters** is reported consistently by users: the editor refuses to save above it. **[S]** [OpenAI community: increase ceiling beyond 8000 characters](https://community.openai.com/t/how-can-i-increase-the-ceiling-for-gpt-instructions-beyond-8000-characters/801867); [Can't update GPTs close to 8k chars](https://community.openai.com/t/cant-update-gpts-that-have-close-to-8k-chars-in-instructions-please-halp-smart-ppl/503566).

### Knowledge files
- "You can attach up to **20 files** to a GPT. Each file can be up to **512 MB**." [P] [Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)
- **Conflict:** "You can upload up to **10 knowledge files per GPT** for the lifetime of that GPT. File-size restrictions and user or organization usage caps also apply." [P] [Uploading files and audio to ChatGPT](https://help.openai.com/en/articles/8555545-file-uploads-faq) (updated "7 days ago", i.e. newer than the GPT article). Treat **10** as the safe budget.
- Types: "most common document, spreadsheet, image, text, and code file types. Accepted file types can vary by model, and some file types are only available if ... Code Interpreter & Data Analysis is enabled." [P] (same GPT article)
- General upload limits (apply to GPTs and Projects): documents/presentations 512 MB per file; text and document files capped at **2 million tokens per file** (not spreadsheets); CSV/spreadsheets ~50 MB; images 20 MB; shared storage 25 GB/user, 100 GB/org. Listed formats: DOCX, PDF, TXT; XLSX, XLS, CSV, TSV; PPTX. `.md` is **not** in the listed table (TXT is). [P] [Uploading files and audio to ChatGPT](https://help.openai.com/en/articles/8555545-file-uploads-faq)
- OpenAI's own advice: "Use knowledge for reference material, not rules or behavior. Put rules, tone, and workflow guidance in instructions." [P] (GPT article). Relevant for the core-prompt / knowledge split.

## ChatGPT Project

### Instructions
- Set via ••• > Project settings. "Project instructions apply only within that project and override your global custom instructions." [P] [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) (updated "25 days ago")
- **No character limit stated for project instructions.** [—]
- Nearest official figure, for *personal* custom instructions (Settings > Customize ChatGPT): "Free and Go users can save up to 1,500 characters ... Plus, Pro, Enterprise, Business, and Education users can save up to 5,000 characters." [P] [ChatGPT Custom Instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions). Not stated to apply to project instructions; must be tested in the UI.

### Files
- "Free: 5 files per project · Go, Plus: 25 files per project · Edu, Pro, Business, Enterprise: 40 files per project"; "only 10 files can be uploaded at the same time"; unlimited projects. [P] [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), section "Plans and limits".
- Types: "PDFs, spreadsheets, docs, images, or by pasting text". Size/token caps as in the shared upload FAQ above. [P]

## Gemini Gem

### Instructions
- **No character limit stated** on any official Gem page (Use Gems, Tips for creating custom Gems, Gems-to-skills transition). [—] [Tips for creating custom Gems](https://support.google.com/gemini/answer/15235603?hl=en)
- The skills page also sets no instruction length; only: up to 100 skills active at once, names lowercase-hyphenated. [P] [Gems to skills](https://support.google.com/gemini/answer/18560919?hl=en)

### Knowledge files
- Current Gem help page gives no numbers; it links to the general file-upload page. [P] [Use Gems](https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop)
- General Gemini Apps upload page: "Up to 10 files (subject to availability) can be uploaded in the same prompt"; "Each video can be up to 2 GB. All other supported file types can be up to 100 MB."; "Gemini Apps support most file types" (no full list). [P] [Upload & analyze files in Gemini Apps](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop). This is per *prompt*, not explicitly per Gem.
- Gem-specific: "up to 10 files", each "up to 100 MB", types TXT, DOC, DOCX, PDF, RTF, DOT, DOTX, HWP, HWPX, Google Docs, XLS, XLSX, CSV, TSV, Google Sheets. **[P-old]** first-party but dated Nov 2024: [Workspace Updates, 12 Nov 2024](https://workspaceupdates.googleblog.com/2024/11/upload-google-docs-and-other-file-types-to-gems.html). A current 10-file-per-Gem cap and Markdown support are confirmed only by third parties **[S]**: [fast.io](https://fast.io/resources/gemini-gems-file-limit/).
- How much of the knowledge Gemini can read at once depends on plan context window: no plan 32k tokens, AI Plus 128k, AI Pro/Ultra 1M. [P] [Gemini Apps limits](https://support.google.com/gemini/answer/16275805?hl=en)

## Rendering ($$ math, `<details>`, tables)

No official OpenAI or Google page documents which Markdown/LaTeX/HTML the chat UI renders. Findings:

- **ChatGPT (GPT and Project share the chat renderer).**
  - Math: users report KaTeX rendering; the model emits `\( \)` / `\[ \]` by default, `$$ ... $$` also renders. **[S]** [OpenAI community: properly shown mathematical equations](https://community.openai.com/t/new-feature-properly-shown-mathematical-equations/73833). Canvas reportedly does not render LaTeX **[S]** [community](https://community.openai.com/t/canvas-for-latex-formatted-math-texts/983018).
  - `<details>`: no source found **[—]**. Renderers that sanitize HTML usually show it as text; must be tested.
  - Tables: no official statement **[—]**; GFM tables render in practice **[S]**.
- **Gemini.**
  - Math in normal chat: no official statement **[—]**. Canvas has an explicit LaTeX mode, and "you can copy any Gemini response that includes LaTeX and it will include the unrendered LaTeX code", which implies responses render LaTeX. [P] [Canvas](https://support.google.com/gemini/answer/16047321?hl=en&co=GENIE.Platform%3DDesktop)
  - `<details>`: no source **[—]**.
  - Tables: render. "Export to Sheets ... is only available for responses that have a table." [P] [Export responses from Gemini Apps](https://support.google.com/gemini/answer/14184041?hl=en)

## Not verified / open

1. GPT instruction limit (8,000) comes only from community reports.
2. GPT knowledge file count: official pages conflict (20 vs 10).
3. Project-instruction character limit: undocumented. Test in UI.
4. Gem instruction limit: undocumented. Test in UI.
5. Gem knowledge cap and types: only a 2024 first-party post plus third parties.
6. `$$` rendering in ChatGPT and Gemini chat, `<details>` anywhere, and ChatGPT tables: no primary source. Needs a manual render test with one sample message on each platform.
7. Plugins (OpenAI) and skills (Gemini), the replacements, were not researched for limits.

## Implication for the core prompt

If the core prompt must fit the smallest *documented* field, the binding number is **1,500 characters** (ChatGPT custom instructions, Free/Go), or **5,000** for paid tiers, *if* project instructions share that limit. That is unverified. The GPT field (8,000, [S]) is larger. Gem has no known limit. Note: `build.py` currently enforces 8,000 chars for `dist/system-prompt-kurz.md` (7,907). That cap rests on the secondary-source GPT figure, and the GPT target is being retired. Budget for ≤10 knowledge files to stay under every platform's cap, and avoid relying on `<details>`.
