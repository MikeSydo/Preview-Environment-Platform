# Preview Environments Platform Template

This repository is a **Preview Environments Platform Template** for containerized applications.

Its goal is to automatically create isolated preview environments for pull requests in Kubernetes, expose a preview URL, and clean up resources after the pull request is closed or merged.

## Documentation

- [MVP Scope](docs/mvp.md)
- [Roadmap](docs/roadmap.md)
- [Local Setup](docs/local-setup.md)

## Quick Start (Local Setup)

To bootstrap a local k3d cluster and install prerequisites, run:

```bash
bash scripts/bootstrap-local.sh
```
