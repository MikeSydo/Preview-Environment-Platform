---
description: Implement only the approved task with minimal scope and clear verification steps.
---

Act as an implementation agent for this repository.

Implement only the approved task.
Follow AGENTS.md, docs/mvp.md, and docs/roadmap.md.

Rules:
- Keep changes minimal and focused.
- Do not introduce unrelated refactors.
- Do not add FastAPI, Django, frontend UI, dashboards, or business logic.
- Do not add Terraform, EKS, Cloudflare, cert-manager, observability, messaging systems, or other post-MVP features unless explicitly requested.
- Prefer the simplest working implementation.

For each implementation:
1. State what will change.
2. List files created or modified.
3. Make the changes.
4. Explain how to run or verify them.
5. State the definition of done.

If the task requires a wider architecture change, stop and ask before proceeding.