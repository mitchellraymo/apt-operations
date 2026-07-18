# Document and Record Control

## Controlled-document lifecycle

1. Copy the appropriate file from `templates/` and assign the next approved identifier.
2. Replace every `SAMPLE`, `TBD`, and bracketed instruction. Do not delete a field merely because it is inconvenient; mark it not applicable with justification.
3. Set revision to `A` for first release, identify the owner/approver, and summarize the change.
4. Verify technical content and linked forms, then obtain independent approval by pull request.
5. On approval, set the effective date and communicate/train affected users before use.
6. Revise through a new pull request. Preserve history; do not rewrite released Git history.

## Records

A template becomes a record when it is populated as evidence of work. Store production records only in an approved record system with access, backup, retention, and correction controls. Repository examples are instructional and must contain fictitious data only.

Minimum record attributes are a stable record ID, related job/part/lot/serial identifiers, author, event date/time with time zone, applicable procedure/drawing revision, results, disposition or acceptance, and approval where required.

## Correction rules

Never obscure the original value. Record the correction, reason, author, timestamp, and approval where required. If a committed file contains sensitive data, stop distribution and follow the security incident process; a normal deletion commit does not remove it from history.

## Naming

- Procedures: `AREA-PRO-###-short-title.md`
- Work instructions: `AREA-WI-###-short-title.md`
- Forms/templates: `AREA-FRM-###-short-title.md`
- Registers: `AREA-REG-###-short-title.csv`

The quality owner maintains identifier allocation and retention requirements.
