# Overnight Automation Policy

## Purpose

Allow Codex and other approved automation to make useful unattended progress without waiting forever, repeating the same failed action, or losing completed work.

## Required behavior

Every overnight task must:

1. Break work into independently verifiable phases.
2. Create or update `OVERNIGHT-PROGRESS.md` before beginning.
3. Record the current phase, files changed, tests run, blockers, and next safe action.
4. Checkpoint completed work after each major phase using a commit or clearly preserved local changes.
5. Use non-interactive commands with explicit time limits whenever possible.
6. Stop a command that produces no useful output for five minutes.
7. Retry the same failed command or approach no more than once.
8. Avoid leaving development servers, file watchers, interactive prompts, or login flows running in the foreground.
9. Continue to another independent task when safe; otherwise stop cleanly and report the blocker.
10. Never discard existing work to recover from a stall.

## Prohibited unattended patterns

- Infinite or unbounded loops.
- Test watch mode.
- Foreground development servers treated as completed steps.
- Repeated dependency installation without diagnosing the failure.
- Waiting indefinitely for user input, browser authentication, elevated permission, hardware, or a disconnected service.
- Rebuilding the entire project after a partial failure when completed work can be preserved.

## Standard progress record

```markdown
# Overnight Progress

- Started:
- Last checkpoint:
- Current phase:
- Status: planned | running | blocked | completed
- Files changed:
- Verification performed:
- Passed:
- Failed:
- Blockers:
- Next safe action:
```

## Standard overnight instruction

```text
Work autonomously in small phases. Preserve existing files. Update OVERNIGHT-PROGRESS.md after each phase. Run only bounded, non-interactive commands. If a command produces no useful output for five minutes, terminate it, record the failure, try one safe alternative once, and then continue to another independent task or stop cleanly. Never retry the same failing approach more than twice. Do not leave development servers, watchers, or interactive prompts running. Checkpoint completed work before moving to the next phase.
```

## Morning review

The reviewer should inspect:

- `OVERNIGHT-PROGRESS.md`;
- uncommitted changes and recent commits;
- test and workflow status;
- commands that timed out;
- blockers requiring a human decision;
- whether the next phase is still aligned with the roadmap.
