# ChatGPT Tutor readiness implementation plan

**Goal:** Address ChatGPT issues #95 and #107 and make sketch delivery explicit without changing Claude/Gemini skill behavior.

**Architecture:** Keep `tutor/` unchanged. Apply checked, ChatGPT-only text adaptations from `packaging/chatgpt-overrides.json` before producing the plugin and project prompts. Abort before publishing outputs if an adaptation no longer matches its source exactly once.

**Scope:** Native plugin and ChatGPT project exports; no public stable-release claim, upstream Android renderer fix, or unrelated website changes.

1. Add failing build integration tests for applying adaptations to both exports, preserving unrelated source bytes, and rejecting malformed, ambiguous or stale adaptations without replacing previous outputs.
2. Implement the minimal adapter in `build.py`; clarify new-task routing, external equation numbers, selective rendering fallback and raster image delivery in ChatGPT.
3. Run the full suite and optimized build; document native acceptance cases separately from structural checks. Use fresh model sessions for bounded behavioral checks where available; these do not replace Android visual tests.
4. Update ChatGPT documentation, changelog and relevant vault notes/hashes; publish the changes on a dedicated branch and PR. Keep #95/#107 open until their native acceptance criteria pass.

## Verification limits

- New problem versus same-problem follow-up, `!an`/`!aus`, temporary overrides and language persistence need conversational evidence.
- Selective `\\tag` failure must not disable all math; boxes, units and solution protection remain.
- Image bytes and links do not prove the final ChatGPT message displays the image.
- Plugin import/update and installed-version identity must be observed before claiming installation.
- Check source identity, archive consistency and unchanged Claude/Gemini bytes independently of model behavior.
