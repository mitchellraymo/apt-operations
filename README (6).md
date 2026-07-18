# APT Operations

Team-facing operational system for **American Precision Technology (APT)** metal-manufacturing and calibration work. This repository is not related to Debian, Ubuntu, or Linux APT package management.

## Purpose

APT Operations provides one auditable home for approved procedures, equipment and calibration controls, training references, quality records, report definitions, and the Python utilities that support them. It is designed to help the team execute work consistently and retain objective evidence of what was done, by whom, when, and with which equipment.

## Scope and users

| Area | Primary users | Repository content |
| --- | --- | --- |
| Production operations | Operators, manufacturing leads | Work instructions and process procedures |
| Calibration | Calibration owners, technicians | Calibration procedures, status register, evidence conventions |
| Quality | Quality personnel, inspectors | Inspection, nonconformance, and corrective-action records |
| Equipment | Operators, maintenance | Equipment register, maintenance instructions, service history |
| Training | Employees, supervisors | Role requirements and training evidence |
| Reporting | Operations and quality leadership | Periodic performance and compliance reports |
| Automation | Developers and system owners | Python validation and reporting utilities |

This foundation supports good manufacturing and quality-management practices, but does not by itself certify compliance with ISO 9001, AS9100, ISO/IEC 17025, or a customer-specific standard.

## Operating workflow

1. **Plan:** Confirm the current approved procedure, drawing/revision, acceptance criteria, tooling, and calibrated inspection equipment.
2. **Execute:** Perform the work in accordance with the controlled procedure and record required process data as it is generated.
3. **Verify:** Inspect output, link results to the job/lot/serial identity, and confirm measurement equipment was in calibration at time of use.
4. **Control exceptions:** Identify and segregate nonconforming output; open the appropriate nonconformance or corrective-action record.
5. **Review:** Obtain required technical or quality approval through a pull request. Never rewrite released evidence to conceal a correction.
6. **Retain and report:** Preserve approved records according to the applicable retention rule and generate management reports from verified data.

## Repository map

```text
operations/     Controlled manufacturing procedures and work instructions
calibration/    Calibration procedures, schedules, and status controls
quality/        Quality procedures and record indexes
equipment/      Equipment register and maintenance documentation
training/       Training requirements and evidence guidance
reports/        Report definitions and generated-output guidance
templates/      Blank controlled-document and quality-record templates
src/apt_ops/    Python package for repository checks and future automation
tests/          Automated tests
docs/           Governance, roadmap, and document-control guidance
```

## Quick start

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
ruff format --check .
ruff check .
pytest
apt-ops validate .
```

## Document and record control

- Procedures use stable identifiers, revision, owner, approver, effective date, and change summary.
- Blank templates are copied before use; template examples are never production records.
- Records use stable job/lot/serial and equipment identifiers and retain attribution and timestamps.
- Changes to controlled content require a pull request and an independent reviewer appropriate to the change.
- Corrections remain traceable. Do not silently replace released records or backdate approvals.
- Customer data, export-controlled technical data, CUI, secrets, and sensitive personal information must not be committed unless this repository has been formally approved and configured for that data class.

See [docs/document-control.md](docs/document-control.md) for the release and replacement process.

## Contributing

Open an issue using the supplied template, create a focused branch, update documentation/tests, and submit a pull request. The pull-request checklist requires impact, verification, record-migration, and rollback consideration.

## Roadmap

The phased implementation plan is maintained in [ROADMAP.md](ROADMAP.md).
