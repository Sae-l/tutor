# Issue tracker: GitHub

Issues and specs for this project live as GitHub issues in `Sae-l/tutor` (the current repo; `physik-mathe-tutor` is legacy and gets none). Use the [`gh`](https://cli.github.com/) CLI for all operations, always with `--repo Sae-l/tutor`, because the working folder is a parent of two repos.

## Conventions

- **Create an issue**: `gh issue create --repo Sae-l/tutor --title "..." --body "..."`. Use a heredoc for multi-line bodies.
- **Read an issue**: `gh issue view <number> --repo Sae-l/tutor --comments`. Add `--json ...` for machine-readable output.
- **List issues**: `gh issue list --repo Sae-l/tutor --json number,title,labels,assignees,state` with `--label` filters.
- **Comment on an issue**: `gh issue comment <number> --repo Sae-l/tutor --body "..."`.
- **Apply / remove labels**: `gh issue edit <number> --repo Sae-l/tutor --add-label "..."` / `--remove-label "..."`.
- **Close**: `gh issue close <number> --repo Sae-l/tutor --comment "..."`; the closing comment is optional.
- **Pull requests**: `gh pr create`, `gh pr view`, `gh pr comment`.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external pull requests as feature requests; `/triage` reads this flag.)_

## When a skill says "publish to the issue tracker"

Create a GitHub issue in `Sae-l/tutor`.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --repo Sae-l/tutor --comments`.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single issue with **child** issues as tickets.

- **Map**: a single issue labelled `wayfinder:map`, holding the Destination / Notes / Decisions-so-far / Not-yet-specified / Out-of-scope body. Create the `wayfinder:*` labels once: `gh label create "wayfinder:map" --repo Sae-l/tutor` (same for `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`, `wayfinder:task`).
- **Child ticket**: a GitHub **sub-issue** of the map, labelled `wayfinder:<type>`. Create the issue first, then attach it: `gh api repos/Sae-l/tutor/issues/<map>/sub_issues -f sub_issue_id=<child-id>`, where `<child-id>` is the numeric id from `gh api repos/Sae-l/tutor/issues/<child> --jq .id` (not the issue number). Fallback if sub-issues are unavailable: put `Part of #<map>` at the top of the body.
- **Blocking**: GitHub's **native dependency**, shown in the UI: `gh api repos/Sae-l/tutor/issues/<child>/dependencies/blocked_by -f issue_id=<blocker-id>` (numeric id again). Fallback: a `Blocked by: #<n>, #<n>` line at the top of the body. A ticket is unblocked when every blocker is closed.
- **Frontier query**: list the map's open sub-issues (`gh api repos/Sae-l/tutor/issues/<map>/sub_issues`), drop any with an open blocker (`gh api repos/Sae-l/tutor/issues/<n>/dependencies/blocked_by`, or the `Blocked by` line) or an assignee; first in map order wins.
- **Claim**: `gh issue edit <n> --repo Sae-l/tutor --add-assignee @me`, the session's first write.
- **Resolve**: `gh issue comment <n> --repo Sae-l/tutor --body "<answer>"`, then `gh issue close <n> --repo Sae-l/tutor`, then append a context pointer (gist + link) to the map's Decisions-so-far with `gh issue edit <map> --repo Sae-l/tutor --body-file <file>`.
- **Numbers**: GitHub shares one number space for issues and PRs, so `#42` is unambiguous only inside `Sae-l/tutor`.
