# Preview Environments Platform Template

This repository is a **Preview Environments Platform Template** for containerized applications.

Its goal is to automatically create isolated preview environments for pull requests in Kubernetes, expose a preview URL, and clean up resources after the pull request is closed or merged.

## Full Preview Lifecycle

```
PR opens → image builds (GitHub Actions + GHCR) → Argo CD ApplicationSet detects PR
         → preview namespace created → ingress route active → preview URL reachable
PR closes → ApplicationSet prunes → namespace deleted
```

## Documentation

| Doc | Purpose |
|-----|---------|
| [docs/mvp.md](docs/mvp.md) | MVP scope and success criteria |
| [docs/roadmap.md](docs/roadmap.md) | Weekly delivery plan |
| [docs/local-setup.md](docs/local-setup.md) | Local cluster bootstrap and ingress verification |
| [docs/gitops-flow.md](docs/gitops-flow.md) | Argo CD installation and GitOps configuration |
| [docs/preview-lifecycle.md](docs/preview-lifecycle.md) | ApplicationSet preview lifecycle and cleanup |
| [docs/onboarding.md](docs/onboarding.md) | End-to-end onboarding for new contributors |

## Quick Start

See [docs/onboarding.md](docs/onboarding.md) for the full step-by-step setup.

```bash
# 1. Verify tooling
bash scripts/bootstrap-local.sh

# 2. Create cluster
k3d cluster create preview-cluster --k3s-arg "--disable=traefik@server:0" \
  --api-port 6550 -p "8081:80@loadbalancer" -p "8443:443@loadbalancer" --agents 1

# 3. Install ingress-nginx and Argo CD
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace
bash scripts/install-argocd.sh

# 4. Apply GitOps config
kubectl apply -f argocd/project.yaml
kubectl apply -f argocd/application.yaml

# 5. Enable PR previews (requires GitHub PAT secret)
kubectl create secret generic github-token --from-literal=token=<YOUR_PAT> -n argocd
kubectl apply -f argocd/applicationset-preview.yaml
```

## Repository Structure

```
.github/workflows/    # GitHub Actions (image build + push)
argocd/               # Argo CD Project, Application, ApplicationSet manifests
docs/                 # Documentation
examples/             # Demo Dockerfile and usage examples
helm/preview-app/     # Reusable Helm chart for preview deployments
scripts/              # Bootstrap and install helpers
```
test
