# Roadmap

## Overview

This roadmap describes the MVP delivery plan for the **Preview Environments Platform Template**.

The project is designed as a platform/template repository that enables pull request-based preview deployments for containerized applications.

The roadmap is intentionally strict and sequential:
each phase must produce a working result before moving to the next one.

## Project goal

Deliver a working MVP for the following lifecycle:

`Pull Request -> image build -> image push -> preview deployment in Kubernetes -> reachable preview URL -> cleanup on PR close or merge`

The first version is focused on a local or minimal shared-cluster setup.
It is not intended to be production-grade.

## Timeline

Planned duration: **4 weeks**

Planned effort: **5 weekdays per week, 6 hours per day**

Total estimated effort: **120 hours**

## Guiding principles

- Finish one working layer before starting the next
- Prefer simple implementations over extensible abstractions
- Keep the repository template-oriented
- Do not add business application code
- Document usage continuously
- Treat anything outside the current MVP scope as deferred work

## MVP stack

The roadmap assumes the following stack:

- Docker
- GitHub Actions
- GHCR
- k3d or kind
- Kubernetes
- Helm
- ingress-nginx
- Argo CD
- Argo CD ApplicationSet Pull Request Generator

## Week 1 — Local Kubernetes foundation

### Goal

Create a working local Kubernetes foundation that can run a containerized web service through Helm and ingress.

### Learning focus

- Kubernetes basics
- kubectl workflow
- namespace, deployment, service, ingress
- Helm chart structure
- local cluster usage with k3d or kind

### Tasks

- initialize repository structure
- install and verify local tooling
- create a local Kubernetes cluster
- install ingress-nginx
- deploy a simple demo container manually
- create the first reusable Helm chart
- expose the service through ingress
- create local bootstrap scripts
- document local setup

### Deliverables

- `scripts/bootstrap-local.sh`
- `helm/preview-app/`
- `docs/local-setup.md`
- updated `README.md`

### Success criteria

- local cluster can be created from documented steps
- ingress-nginx installs successfully
- a demo containerized service is deployed through Helm
- the service is reachable through ingress

## Week 2 — GitOps foundation with Argo CD

### Goal

Introduce GitOps-based deployment using Argo CD and make the Helm-based deployment reproducible through Git-managed manifests.

### Learning focus

- Argo CD basics
- application reconciliation
- sync and prune behavior
- Git as desired state
- repository organization for platform manifests

### Tasks

- install Argo CD in the cluster
- connect to Argo CD UI or CLI
- create an Argo CD project
- create an Argo CD application for the Helm chart
- validate sync behavior
- organize `argocd/` manifests
- add install/upgrade helper scripts
- document the GitOps deployment flow

### Deliverables

- `argocd/` manifests
- `scripts/install-argocd.sh`
- `docs/gitops-flow.md`
- updated `README.md`

### Success criteria

- Argo CD installs successfully
- Argo CD can sync the Helm chart from Git
- deployment changes can be applied through Git-managed manifests
- the local service remains reachable through ingress

## Week 3 — Pull request preview lifecycle

### Goal

Turn the repository into a real preview environments template by using Argo CD ApplicationSet Pull Request Generator.

### Learning focus

- ApplicationSet concepts
- pull request generator behavior
- naming strategy for preview apps
- namespace-per-PR isolation
- preview cleanup lifecycle

### Tasks

- read and apply ApplicationSet Pull Request Generator patterns
- define naming conventions for applications and namespaces
- create ApplicationSet manifest for pull request-driven deployments
- configure token/secret access for PR discovery
- wire template fields for PR number and branch slug
- validate open, update, reopen, and close scenarios
- verify automatic cleanup on PR close or merge
- document the preview lifecycle

### Deliverables

- `argocd/applicationset-preview.yaml`
- supporting secret or setup documentation
- `docs/preview-lifecycle.md`
- updated `README.md`

### Success criteria

- opening a pull request creates a preview environment
- a preview application gets an isolated namespace
- updating the pull request updates the preview deployment
- closing or merging the pull request removes the preview environment

## Week 4 — CI integration and end-to-end MVP completion

### Goal

Close the full loop from pull request to image build and preview deployment.

### Learning focus

- GitHub Actions workflow design
- GHCR permissions and image publishing
- image tagging strategy
- end-to-end validation
- onboarding documentation

### Tasks

- create GitHub Actions workflow for image build
- push built image to GHCR
- define image tag convention for preview deployments
- connect image tags to the deployment configuration
- run end-to-end validation for the full preview lifecycle
- add smoke-check steps if needed
- clean up repository structure
- improve onboarding documentation for new users

### Deliverables

- `.github/workflows/preview-build.yml`
- GHCR image strategy documentation
- `docs/onboarding.md`
- updated `README.md`
- optional `examples/` usage examples

### Success criteria

- a pull request can trigger image build and push
- the preview deployment uses the correct image
- the preview URL becomes reachable
- closing or merging the pull request cleans up resources
- another developer can reproduce the setup from the documentation

## Weekly review checkpoints

At the end of each week, validate:

- what was completed
- what is still blocked
- what assumptions changed
- what should be cut instead of added
- whether the next phase should begin

Do not begin the next week’s implementation if the current week’s success criteria are not met.

## Risks

### Scope creep

The main risk is introducing advanced infrastructure too early, such as Terraform, EKS, Cloudflare, cert-manager, observability, or dashboards.

### Tooling overload

Too many moving parts can make debugging difficult.
Prefer the smallest possible working setup.

### Documentation drift

If the setup changes but the docs do not, the repository becomes much less reusable.

### Hidden complexity in preview naming and cleanup

Namespace naming, image tagging, and cleanup lifecycle are easy to underestimate and should be tested carefully.

## Deferred work after MVP

The following items are intentionally deferred until the MVP is complete:

- cert-manager and wildcard TLS
- ExternalDNS and Cloudflare integration
- Terraform for EKS
- staging and pre-production environment strategy
- observability stack
- reusable CLI scaffolding

## Final MVP definition of done

The MVP is complete when all of the following are true:

1. the repository remains a platform/template repository
2. the documented local setup works from a clean clone
3. the Helm chart can deploy a containerized application
4. Argo CD sync works from Git-managed manifests
5. opening a pull request creates a preview environment
6. the preview becomes reachable through ingress
7. image build and push work through GitHub Actions and GHCR
8. closing or merging the pull request cleans up the preview resources
9. the workflow is documented clearly enough for another developer to reproduce it