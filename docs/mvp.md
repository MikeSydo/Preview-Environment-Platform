# MVP Scope

## Overview

This repository delivers the first working version of a **Preview Environments Platform Template** for containerized applications.

The MVP exists to prove one core workflow:

`Pull Request -> image build -> preview deployment in Kubernetes -> reachable preview URL -> cleanup on PR close or merge`

The goal is not to build a full platform, a control plane, or a cloud production setup.
The goal is to achieve a small, reproducible, well-documented working system.

## Problem

Development teams often rely on a shared staging environment or manual local testing, which slows down review and makes it harder to validate changes safely.

This MVP solves that by creating isolated preview environments for pull requests using Kubernetes and GitOps-based deployment flow.

## Target user

The primary user is a developer or small team that wants to preview pull request changes in an isolated environment before merge.

The secondary user is the repository owner who wants a reusable template for setting up preview deployments for any containerized web application.

## In scope

The MVP includes only the capabilities required to prove the core preview workflow.

### Core workflow

- A pull request exists in GitHub
- A container image is built for the pull request
- The image is pushed to GHCR
- Argo CD detects the pull request through ApplicationSet Pull Request Generator
- A preview environment is created in Kubernetes
- The deployed service becomes reachable through ingress
- The preview environment is cleaned up when the pull request is closed or merged

### Technical scope

- GitHub repository-based workflow
- GitHub Actions for image build and push
- GHCR as image registry
- Local Kubernetes cluster via k3d or kind
- Kubernetes namespaces for preview isolation
- Helm chart for reusable deployment packaging
- ingress-nginx for HTTP routing
- Argo CD for GitOps deployment
- ApplicationSet Pull Request Generator for PR-based dynamic environments
- bootstrap scripts for local setup
- README and docs for onboarding and verification

## Must-have

These items must work for MVP completion:

- A reproducible local cluster bootstrap flow
- A reusable Helm chart for a containerized web service
- GitHub Actions workflow that builds and pushes an image
- GHCR image tagging strategy for preview deployments
- Argo CD installation and sync working locally
- ApplicationSet configuration for pull request-driven preview environments
- Namespace-per-PR or equivalent simple preview isolation
- Reachable preview URL through ingress
- Automatic cleanup after PR close or merge
- Clear setup and usage documentation

## Nice-to-have but not required

These items are useful, but they do not block MVP completion:

- Label-gated preview deployment such as `preview` or `preview-ready`
- Simple smoke test after deployment
- Better naming conventions for namespaces and preview hosts
- Example external app integration config
- Small helper scripts for repeated local tasks
- Basic troubleshooting section in docs

## Out of scope

The following are explicitly out of scope for MVP:

- Terraform
- AWS EKS
- Cloudflare
- ExternalDNS
- cert-manager
- wildcard TLS
- staging/preprod promotion model
- observability stack such as Prometheus, Grafana, Loki
- control-plane API
- dashboards
- FastAPI or Django business logic
- RabbitMQ, Kafka, or other messaging systems
- multi-service preview architecture
- cluster-per-preview or vCluster isolation
- reusable CLI scaffolding

These can be added only after the local MVP preview lifecycle is fully working.

## Assumptions

This MVP assumes:

- the target application is already containerized or can be represented by a demo container image
- one preview environment per pull request is enough
- a local cluster is sufficient for the first validation of the architecture
- GitHub is the source control system
- GHCR is the initial image registry
- the project optimizes for learning and working proof, not for production hardening

## Repository deliverables

By the end of MVP, the repository should contain:

- `AGENTS.md`
- `README.md`
- `.github/workflows/`
- `helm/preview-app/`
- `argocd/`
- `scripts/`
- `docs/`
- `examples/` if needed

The repository should remain a platform template and must not include unrelated application code.

## Success criteria

The MVP is successful if the following can be demonstrated from a clean repository clone:

1. A local Kubernetes cluster can be created with the documented setup steps.
2. ingress-nginx and Argo CD can be installed successfully.
3. A generic Helm chart can deploy a containerized web application.
4. A pull request can trigger image build and push to GHCR.
5. Argo CD ApplicationSet can create a preview deployment for the pull request.
6. The preview deployment becomes reachable through ingress.
7. Closing or merging the pull request removes the preview environment.
8. Another developer can follow the documentation and reproduce the flow.

## Definition of done

The MVP is considered done when:

- the full preview lifecycle works end to end
- the implementation follows the current MVP boundaries
- the repository remains reusable and template-oriented
- setup and validation are documented clearly
- no post-MVP infrastructure or application logic has been added prematurely

## Non-goals

This MVP is not intended to:

- be production-ready
- solve every cloud deployment case
- support every Git provider
- include enterprise security and observability layers
- become a full internal developer platform
- replace a full release strategy

Its purpose is to deliver a focused, working first version that proves the platform concept and creates a strong foundation for later phases.