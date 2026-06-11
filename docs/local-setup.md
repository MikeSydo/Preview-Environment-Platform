# Local Setup Plan

This document outlines the local setup plan for the Preview Environments Platform.

## Architecture

We use a local Kubernetes cluster for MVP testing. The selected tool is **k3d** (or **kind**).
- **Cluster Tool:** k3d
- **Ingress Controller:** ingress-nginx (mapped to local ports 80/443)
- **Deployment:** Helm charts deployed locally before Argo CD integration.

## Port Mapping

When creating the k3d cluster, we map port 80 and 443 to the host:
- `80:80@loadbalancer`
- `443:443@loadbalancer`

## Verification

To verify the setup:
1. Run the `scripts/bootstrap-local.sh` script to verify required tools.
2. Create the k3d cluster (commands will be provided in the bootstrap script).
3. Validate the `helm/preview-app` chart using `helm lint`.
