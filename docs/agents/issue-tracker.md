# Issue tracker: GitHub

Work tickets and new implementation specs produced by the engineering skills live in GitHub Issues for `jasoncjordan/cyan-rockbox`. Use the `gh` CLI from this clone; outside it, specify `--repo jasoncjordan/cyan-rockbox`.

These conventions describe how to perform authorized work. Follow the external-write authorization requirements in `AGENTS.md` before creating or changing GitHub content.

## Existing project specifications

Root `PRD.md` remains the authoritative product requirements and roadmap. Supporting design, implementation, validation, and milestone records remain in the repository, indexed by `docs/README.md`.

For reviews of work that predates GitHub tickets, explicitly use `PRD.md` and the relevant design or milestone records as the spec source. Completed milestone reports remain historical evidence. Track unfinished work in GitHub with links to the existing procedures and acceptance criteria.

## Conventions

- **Create an issue**: `gh issue create --title "..." --body-file <body-file>`.
- **Read an issue**: `gh issue view <number> --json number,title,body,labels,comments`.
- **List issues**: `gh issue list --state open --json number,title,body,labels,comments`; add appropriate `--label` or `--state` filters.
- **Comment on an issue**: `gh issue comment <number> --body-file <body-file>`.
- **Apply / remove labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`. Use the role mapping in `docs/agents/triage-labels.md`.
- **Close**: `gh issue close <number>`. If a closing explanation is needed, add it as a comment first.

For multiline bodies, write the exact Markdown to a temporary file and pass it with `--body-file`.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as feature requests; `/triage` reads this flag.)_

When set to `yes`, use the corresponding `gh pr` operations:

- **Read**: `gh pr view <number> --comments` and `gh pr diff <number>`.
- **List external PRs**: `gh api --paginate 'repos/jasoncjordan/cyan-rockbox/pulls?state=open'`; retain only `author_association` values `CONTRIBUTOR`, `FIRST_TIME_CONTRIBUTOR`, or `NONE`, excluding `OWNER`, `MEMBER`, and `COLLABORATOR`.
- **Comment / label / close**: `gh pr comment <number> --body-file <body-file>`, `gh pr edit <number> --add-label "..."` / `--remove-label "..."`, and `gh pr close <number>`.

GitHub shares one number space across issues and PRs. A bare `#42` may be either: resolve with `gh pr view 42` and fall back to `gh issue view 42`.

## When a skill says "publish to the issue tracker"

Create a GitHub issue after the required authorization.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --comments`; use the JSON form above when labels or structured comments are needed.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single issue with **child** issues as tickets. The same authorization requirements apply to all writes below.

- **Map**: an issue labelled `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body.
- **Child ticket**: an issue linked to the map as a GitHub sub-issue using `gh api`. Where sub-issues are unavailable, add the child to a task list in the map body and put `Part of #<map>` at the top of the child body. Use `wayfinder:<type>` labels (`research`, `prototype`, `grilling`, or `task`).
- **Blocking**: use native GitHub issue dependencies. Add an edge with `gh api --method POST repos/jasoncjordan/cyan-rockbox/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`. Use the blocker's numeric database ID from `gh api repos/jasoncjordan/cyan-rockbox/issues/<number> --jq .id`, not its issue number or node ID. `issue_dependencies_summary.blocked_by` counts open blockers. Where dependencies are unavailable, put `Blocked by: #<n>, #<n>` at the top of the child body. A ticket is unblocked when every blocker is closed.
- **Frontier query**: list the map's open children, scoped to its sub-issues or task list, and exclude children with an open blocker (`issue_dependencies_summary.blocked_by > 0`, or an open issue in the fallback `Blocked by` line) or an assignee. First in map order wins.
- **Claim**: `gh issue edit <number> --add-assignee @me`.
- **Resolve**: comment with the answer, close the child, then append a concise context pointer and link to the map's Decisions-so-far.
