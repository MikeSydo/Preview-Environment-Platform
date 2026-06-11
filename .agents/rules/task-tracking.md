---
trigger: always_on
---

Use GitHub Projects as the source of truth for operational task tracking in this repository.

Repository strategy and constraints remain in:
- AGENTS.md
- docs/mvp.md
- docs/roadmap.md

Task execution state must be tracked in the GitHub Project board using these statuses:
- Backlog
- In Progress
- Blocked
- Done

Before starting meaningful work:
1. Read AGENTS.md, docs/mvp.md, and docs/roadmap.md.
2. Read the current GitHub Project board.
3. Identify what is already Done, what is In Progress, and what is next in Backlog.
4. Keep only one main task in In Progress unless explicitly told otherwise.
5. If no task is in progress, propose the next MVP-safe task from Backlog.

When working on a task:
- stay within MVP scope,
- do not introduce out-of-scope technologies,
- update the related issue or project item when the task status changes,
- move a task to Blocked if progress is impossible and explain the blocker clearly.

When completing a task:
1. Ensure implementation and validation are complete.
2. Update the issue with a short result note.
3. Move the project item to Done.
4. Recommend the next best task from Backlog.

Never mark a task as Done unless it is actually implemented and validated.
Never move multiple large tasks into In Progress at the same time unless explicitly requested.