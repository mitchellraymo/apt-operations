# APT Operating System Foundation

## Objective

Create one practical operating layer for American Precision Technology that brings business priorities, manufacturing, calibration, software, partner collaboration, documentation, and automated build status into a single auditable system.

## Core operating loop

1. Capture an idea, request, measurement, problem, or opportunity.
2. Classify it into an APT program and assign an owner.
3. Convert it into a defined objective with acceptance criteria.
4. Execute through a controlled task, branch, procedure, or customer job.
5. Verify results with tests, measurements, review, or approval.
6. Record evidence, decisions, blockers, and next actions.
7. Surface the current status on the executive dashboard.

## Initial modules

| Module | Purpose | First deliverable |
| --- | --- | --- |
| Executive dashboard | Show priorities, blockers, builds, and next actions | Static dashboard specification and data contract |
| Daily objectives | Convert roadmap items into a small daily work queue | Daily objective template |
| Overnight build monitor | Prevent silent loops and preserve checkpoints | Overnight execution policy and progress log |
| Manufacturing operations | Procedures, equipment, RFQs, quality, and training | Existing repository controls |
| Display intelligence | Calibration workflow, signal path, measurements, and reports | Program registry and integration roadmap |
| HomeOS | Home inventory, maintenance, consumables, and purchasing | Program registry and MVP boundary |
| Partner workspace | Give partners business context without personal-chat access | Partner onboarding and project-interest assessment |
| Customer operations | Leads, jobs, scheduling, reports, and follow-up | Customer workflow specification |
| Financial overview | Track runway, purchases, revenue experiments, and ROI | Minimal metrics definition |
| Research library | Preserve findings, assumptions, sources, and experiments | Research intake template |

## Dashboard minimum viable view

The first dashboard should answer these questions without opening multiple applications:

- What are the three highest-priority objectives today?
- What changed since the last review?
- What is blocked and who owns the blocker?
- Which local or cloud builds are running, completed, failed, or stale?
- Which tests or quality checks failed?
- What files, branches, pull requests, and procedures changed?
- What should Mitchell and his partner review next?

## Implementation phases

### Phase 1 — Control and visibility

- Create the program registry.
- Create daily and overnight progress templates.
- Define dashboard data fields.
- Add GitHub issues for each module.
- Require checkpointing and bounded commands for unattended automation.

### Phase 2 — Working dashboard

- Build a local dashboard that reads project status from repository files.
- Show objectives, blockers, recent commits, test status, and build logs.
- Keep the first version read-only and simple.

### Phase 3 — Connected operations

- Add customer jobs, calibration records, equipment status, and partner updates.
- Connect GitHub and approved business-workspace documents.
- Add role-based views and controlled write actions.

### Phase 4 — Automation and intelligence

- Generate recommended daily objectives.
- Detect stalled builds and missing evidence.
- Summarize changes and prepare review packages.
- Add guarded automation only after the underlying workflows are stable.

## Guardrails

- Do not place personal legal, medical, family, or unrelated financial information in the shared business repository.
- Do not store customer-sensitive, export-controlled, CUI, secret, or regulated data without an approved storage and access design.
- Prefer small reversible changes, tests, and pull-request review.
- A stopped build with a clear checkpoint is better than an indefinite loop.
