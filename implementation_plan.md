# Implementation Plan - Week 1: Repository Foundation Skeleton

This plan outlines the steps to initialize the repository structure and create skeletons/documentation for the Preview Environments Platform Template.

## User Review Required

> [!IMPORTANT]
> - We are setting up skeletons and planning for local setup.
> - No active Argo CD or CI workflows are introduced yet.
> - The bootstrap script will be a shell script skeleton (`scripts/bootstrap-local.sh`) that checks for local prerequisites (Docker, kubectl, helm, k3d) and outlines the setup commands.

## Proposed Changes

We will introduce the standard directory layout as defined in `AGENTS.md`:

```
.
├── README.md
├── docs/
│   ├── mvp.md
│   ├── roadmap.md
│   └── local-setup.md (NEW)
├── scripts/
│   └── bootstrap-local.sh (NEW)
└── helm/
    └── preview-app/ (NEW)
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── deployment.yaml
            ├── service.yaml
            └── ingress.yaml
```

---

### Root Layout

#### [NEW] [README.md](file:///C:/Users/misha/Projects/Preview-Environment-Platform/README.md)
Introduce the platform template, explain the directory structure, and provide quick commands to bootstrap the skeleton.

---

### Documentation

#### [NEW] [local-setup.md](file:///C:/Users/misha/Projects/Preview-Environment-Platform/docs/local-setup.md)
Document the plan for local setup using k3d (the default local Kubernetes stack), including how Ingress-Nginx will map ports, and how the preview Helm chart will be verified.

---

### Scripts

#### [NEW] [bootstrap-local.sh](file:///C:/Users/misha/Projects/Preview-Environment-Platform/scripts/bootstrap-local.sh)
A bash script that:
- Verifies required CLI tools are installed (`docker`, `kubectl`, `helm`, `k3d`).
- Provides placeholder/skeleton commands to spin up a k3d cluster and install `ingress-nginx`.

---

### Helm Chart

#### [NEW] [Chart.yaml](file:///C:/Users/misha/Projects/Preview-Environment-Platform/helm/preview-app/Chart.yaml)
Standard Helm chart metadata.

#### [NEW] [values.yaml](file:///C:/Users/misha/Projects/Preview-Environment-Platform/helm/preview-app/values.yaml)
Default values for the container image (using a public nginx demo image like `nginxdemos/hello:plain-text`), replicas, service ports, and ingress host.

#### [NEW] [deployment.yaml](file:///C:/Users/misha/Projects/Preview-Environment-Platform/helm/preview-app/templates/deployment.yaml)
Simple deployment template.

#### [NEW] [service.yaml](file:///C:/Users/misha/Projects/Preview-Environment-Platform/helm/preview-app/templates/service.yaml)
Simple service template mapping to target port.

#### [NEW] [ingress.yaml](file:///C:/Users/misha/Projects/Preview-Environment-Platform/helm/preview-app/templates/ingress.yaml)
Simple ingress template to route external traffic to the service.

---

## Verification Plan

### Automated Tests
- Since this is a skeleton structure, we will run `helm lint helm/preview-app` to verify the Helm chart structure and syntax are valid.

### Manual Verification
- Execute `scripts/bootstrap-local.sh` to check for dependency verification output.
- Verify files are placed in correct paths matching `AGENTS.md`.
