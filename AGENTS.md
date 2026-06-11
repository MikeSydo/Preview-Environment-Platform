# AGENTS.md

## Project overview

This repository is a **Preview Environments Platform Template** for containerized applications.

Its goal is to automatically create isolated preview environments for pull requests in Kubernetes, expose a preview URL, and clean up resources after the pull request is closed or merged.

This is a **platform/template repository**, not an application repository.
Do not add business application code such as FastAPI, Django, frontend product UI, dashboards, or unrelated service logic here.

## Current scope

The project follows a strict **MVP-first** approach.

Current MVP goal:

`PR opens -> image builds -> preview environment deploys in Kubernetes -> preview URL becomes reachable -> resources are cleaned up on PR close/merge`

At the current stage, focus only on a **local or minimal shared-cluster implementation** of this flow.

## Allowed MVP stack

Use these technologies by default unless explicitly told otherwise:

- Docker
- GitHub Actions
- GHCR
- k3d or kind
- Kubernetes
- Helm
- ingress-nginx
- Argo CD
- Argo CD ApplicationSet Pull Request Generator

## Out of scope for MVP

Do **not** introduce the following unless explicitly requested after MVP is complete:

- Terraform
- AWS EKS
- Cloudflare
- ExternalDNS
- cert-manager
- Wildcard TLS
- Observability stacks such as Prometheus, Grafana, Loki
- RabbitMQ, Kafka, NATS, or other messaging systems
- Control-plane API or dashboard
- FastAPI/Django application code
- CLI scaffolding
- Multi-service demo applications
- vCluster or cluster-per-preview approaches

## Repository intent

This repository should provide reusable platform building blocks for preview environments, such as:

- GitHub Actions workflows
- Helm charts
- Argo CD manifests
- ApplicationSet configuration
- bootstrap scripts
- examples
- documentation

It should not become a starter app or a monolithic demo product.

## Preferred architecture decisions

Prefer the simplest working implementation.

Use these defaults unless there is a strong reason not to:

- one shared Kubernetes cluster
- namespace-per-PR isolation
- one generic Helm chart for a containerized web app
- Argo CD as the deployment engine
- ApplicationSet Pull Request Generator for preview lifecycle
- GHCR for container image storage

Avoid speculative abstractions and “future-proofing” that increase complexity without helping the current MVP.

## Working style

For every meaningful task or change:

1. State the goal.
2. List files to create or modify.
3. Explain the smallest implementation that solves it.
4. Provide commands to run.
5. Provide validation steps.
6. State the definition of done.

If there are multiple possible implementations, propose the **simplest MVP-safe option first**.

## Safety rules

Never do any of the following without explicit approval:

- destructive shell commands
- deleting large parts of the repository
- rewriting git history
- force pushes
- cluster teardown/reset
- Docker system cleanup
- broad refactors not directly related to the current task

Prefer review-first behavior for risky commands.

## File and code boundaries

When creating files, prefer this structure:

- `.github/workflows/` for CI workflows
- `helm/preview-app/` for reusable Helm charts
- `argocd/` for Argo CD and ApplicationSet manifests
- `scripts/` for setup/bootstrap helpers
- `docs/` for deeper documentation
- `examples/` for usage examples

Do not place unrelated files at the repository root unless they are standard root files such as:

- `README.md`
- `AGENTS.md`
- `.gitignore`

## Documentation requirement

A task is not complete until the usage is documented.

Any new script, workflow, manifest, or chart change should be reflected in one of:

- `README.md`
- `docs/`
- inline comments only if truly necessary

Prefer concise documentation that helps a new contributor run the project from a clean clone.

## Validation expectations

Changes should be verifiable with concrete steps.

When relevant, validation should include:

- cluster bootstrap works from a clean state
- manifests render correctly
- Helm chart installs successfully
- Argo CD sync works
- preview environment becomes reachable
- cleanup works after PR close/merge

## Escalation rule

If a requested change conflicts with the MVP scope, project boundaries, or architecture rules in this file, explicitly say so and propose:

1. the MVP-safe option now
2. the more advanced option later