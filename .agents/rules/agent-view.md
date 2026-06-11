---
trigger: always_on
---

This project is a Preview Environments Platform Template for containerized applications, not an application repository. Do not add FastAPI, Django, frontend product UI, dashboards, or unrelated business logic to this repo.

Follow a strict MVP-first workflow. The current MVP goal is:
PR opens -> image builds -> preview environment deploys in Kubernetes -> preview URL becomes reachable -> resources are cleaned up on PR close or merge.

For the current MVP, use only this stack unless explicitly approved otherwise:
Docker, GitHub Actions, GHCR, k3d or kind, Kubernetes, Helm, ingress-nginx, Argo CD, and Argo CD ApplicationSet Pull Request Generator.

Do not introduce Terraform, EKS, Cloudflare, ExternalDNS, cert-manager, wildcard TLS, observability stacks, messaging systems, control-plane services, CLI scaffolding, multi-service demo apps, or other post-MVP features until the local preview lifecycle is fully working.

Always prefer the simplest working implementation over extensible or enterprise-style abstractions. Avoid feature creep and speculative architecture.

Before meaningful changes, explain:
1. the goal,
2. the files to change,
3. the implementation approach,
4. the commands to run,
5. the validation steps,
6. the definition of done.

Never execute destructive commands, broad refactors, git history rewrites, cluster resets, or cleanup-heavy Docker commands without explicit approval.

Use AGENTS.md and docs/ as the source of truth for repository-specific guidance.