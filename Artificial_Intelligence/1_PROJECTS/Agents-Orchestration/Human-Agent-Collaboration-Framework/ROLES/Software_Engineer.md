# AGENTS.md

This file contains durable engineering rules for this repository. These rules apply to the whole repository.

## Prime Directive

Optimize for long-term correctness, maintainability, diagnosability, and supportability - not just for making the immediate diff pass. A change is high quality only when future maintainers can understand it, test it, debug it, and safely extend it.

Prefer a small, clear, verified change over a clever or broad one. Do not hide complexity; localize it behind stable interfaces and document why it exists.

## Working Rules for Agents

Before editing code:

1. Read the surrounding code, tests, README/docs, build files, and relevant tickets/issues if present.
2. Identify existing commands for build, test, lint, typecheck, format, and code generation. Do not invent commands when the repo already defines them.
3. Restate the requirement in concrete terms: what behavior should change, which users/components are affected, and what must remain compatible.
4. Look for implicit requirements: performance, memory, reliability, resilience, security, privacy, internationalization, portability, observability, install/upgrade behavior, and support impact.
5. Prefer using existing patterns in the codebase unless they are clearly harmful; if diverging, explain why.

While editing code:

1. Keep changes focused. Avoid unrelated cleanup unless it is necessary for the task.
2. Preserve public interfaces unless the task requires changing them; if an interface changes, update all callers, tests, docs, and migration notes.
3. Make ownership, lifetimes, error handling, resource cleanup, locking, retries, and cancellation explicit.
4. Add or update tests for every behavior change and every bug fix.
5. Add diagnostics where future debugging would otherwise depend on guessing.
6. Treat build scripts, tests, fixtures, migrations, docs, and generated-code inputs as production assets. Keep them versioned, reviewed, and maintainable.

Before finishing:

1. Run the narrowest relevant checks first, then the broader suite where practical.
2. Verify that new tests fail for the old behavior when that is feasible.
3. Confirm that errors fail safely and are observable.
4. Update docs/comments when the change alters usage, behavior, assumptions, operations, or troubleshooting.
5. Report what changed, what was tested, and any residual risk or unverified area.

## Requirements and Use Cases

Good implementation starts with knowing what is being built.

- Convert vague requests into concrete use cases before designing or coding.
- Cover the main successful path and important error paths.
- Ask "what if?" questions in your own analysis: timeout, partial failure, malformed input, missing dependency, full disk, network delay, duplicate request, concurrent update, restart, downgrade, incompatible version, empty data, huge data.
- For user-facing behavior, include common workflows. For component APIs, include common call sequences and failure sequences.
- When requirements are ambiguous, make the safest reasonable assumption and state it. Ask only when an assumption could cause substantial rework or harm.
- Do not treat "works as specified" as enough if the observable behavior is clearly wrong for the user or caller.

### Implicit Requirements Checklist

For non-trivial changes, consider whether the task affects:

- Speed and latency under typical and large inputs.
- Memory, disk, network, and file descriptor usage.
- Reliability and failure recovery.
- Diagnostics, logs, metrics, traces, and support tooling.
- Backward and forward compatibility.
- Install, deploy, migration, rollback, and upgrade behavior.
- Security boundaries and sensitive data exposure.
- Portability across supported platforms.
- Internationalization, localization, time zones, encodings, and formats.

## Design Principles

### Divide and Conquer

Break systems into components that humans can understand. Each component should have a clear responsibility and a small, stable interface. Prefer designs where a maintainer can reason about one component without loading the entire system into their head.

### Clear Responsibility

Every module, class, function, service, migration, script, and test helper should have a clear job.

- If a change has no natural home, reconsider the design before adding another special case.
- If a component does unrelated jobs, split it or introduce a narrower abstraction.
- If the same behavior appears in multiple places, centralize it behind a clear interface.
- Name things after the responsibility they own, not after incidental implementation details.

### Interface First, Implementation Second

Interfaces are promises. Keep them easy to use correctly and hard to use incorrectly.

A good interface is:

- Complete for its responsibility.
- Minimal: no extra operations that belong somewhere else.
- Predictable: follows the principle of least astonishment.
- Explicit about ownership, lifetimes, mutability, errors, units, encodings, threading, ordering, retries, idempotency, and performance expectations.
- Independent of implementation details.

Use the black-box test: could the implementation be replaced without callers noticing? If not, callers know too much.

### Encapsulate Special Cases

Special cases are sometimes necessary, but scattered special cases rot the design.

- Do not duplicate one-off conditionals across the codebase.
- Generalize special cases into named concepts where possible.
- Encapsulate compatibility hacks, vendor quirks, protocol oddities, and historical behavior in one place.
- Add comments explaining why the special case exists, what external behavior requires it, and when it can be removed.
- Add regression tests around special cases.

### Design for the Future, But Do Not Gold-Plate

Plan ahead when the cost of retrofitting later would be high: persistence formats, public APIs, concurrency models, distribution boundaries, observability, migrations, and testability. Avoid speculative frameworks or abstractions that do not protect a likely future change.

Use this rule of thumb: design for plausible evolution; do not implement unused features.

### Prefer Proven Technology

For reliability-sensitive code, prefer boring, well-understood dependencies and patterns.

Introduce new technology only when:

- It solves a real problem better than existing repo patterns.
- Its failure modes, maintenance status, security posture, and operational costs are understood.
- It can be tested and supported by the team.
- The decision is documented.

## Implementation Standards

### Follow Local Conventions

Match the existing style, structure, naming, error handling, and testing idioms. If the repo has formatters or linters, use them. If conventions are inconsistent, follow the nearest well-maintained code.

### Comments and Documentation

Code shows how. Comments should explain why.

Add comments when they preserve knowledge future maintainers will need:

- Rationale and tradeoffs.
- Non-obvious invariants.
- Ownership or lifecycle rules.
- Concurrency assumptions.
- Protocol, compatibility, or migration constraints.
- Why an apparently simpler approach is wrong.

Avoid comments that merely restate the code. Update stale comments as part of the change.

For design docs or substantial PR descriptions, include:

- Problem statement.
- Requirements and non-requirements.
- Use cases and important error cases.
- Chosen design and alternatives rejected.
- How requirements are satisfied.
- Risks, diagnostics, rollout, rollback, and test strategy.

Use active voice: say which component does what.

### Portability and Boundaries

Keep problem-domain logic separate from environment-specific logic.

- Isolate OS, filesystem, network, clock, randomness, process, shell, database, browser, and framework calls behind small wrappers when it improves portability or testability.
- Do not leak platform-specific assumptions into core logic.
- Be explicit about encodings, locales, time zones, path separators, line endings, integer sizes, and ordering assumptions.

### Errors and Resource Handling

Assume failures happen.

- Check and handle errors at every boundary: IO, network, parsing, serialization, subprocesses, databases, external services, caches, and user input.
- Fail safely and informatively.
- Clean up resources on every path, including early returns, exceptions, cancellations, and timeouts.
- Make retries bounded and observable; use backoff where appropriate.
- Avoid swallowing exceptions or returning ambiguous sentinel values.

### Concurrency, Async, and Distributed Work

Concurrency multiplies edge cases. Prefer simple sequential code unless concurrency is needed.

When concurrency is needed:

- Define ownership of mutable state.
- Use immutable data or message passing where practical.
- Document lock ordering and never acquire multiple locks in inconsistent orders.
- Add timeouts and cancellation paths.
- Treat every async operation as capable of never completing, completing twice, completing late, or failing after partial progress.
- Make operations idempotent where retries are possible.
- Avoid assuming local memory, local time, or exactly-once delivery in distributed systems.

### Data Compatibility, Migrations, and Upgrades

Successful software evolves. Plan data changes so they can be deployed and supported.

- Prefer backward- and forward-compatible formats.
- Include default behavior for newly added state.
- Make migrations repeatable, observable, and safe to resume.
- Consider rollback and downgrade behavior.
- Never reuse a released version number for different contents.
- Embed or expose enough build/version information to diagnose what is running.

## Diagnostics and Observability

Build diagnostics in early; retrofitting them after production failure is expensive.

Use logs, traces, metrics, health checks, and debug endpoints to answer:

- What happened?
- Which component did it?
- Which request/job/user/transaction/data item was involved?
- Which version/configuration/environment was running?
- What failed, how often, and for how long?
- Can support recover safely without corrupting data?

Guidelines:

- Log key state transitions and boundary failures with useful context.
- Make logs filterable by component and correlation/request identifier.
- Use levels so high-volume traces can be enabled without drowning important events.
- Do not log secrets, credentials, tokens, or unnecessary personal data.
- Ensure diagnostic code is tested enough that it can be trusted during incidents.
- Prefer diagnostics that also help tests verify behavior.

Comments explain why code exists; traces/logs explain what code did at runtime.

## Testing Standards

Testing is not a checkbox; it is the safety net between code and its failures.

### Required Testing Mindset

Assume all code has bugs, including your tests. Untested code is suspect. Try to make the system fail before users do.

Test:

- Normal use cases.
- Important error paths.
- Boundary values: empty, one, many, max, over max, negative, null/None, missing, duplicate.
- Malformed input and hostile input.
- Timing windows and concurrent operations.
- Resource exhaustion: disk full, network unavailable, dependency down, permission denied.
- Large-scale inputs and performance-sensitive paths.
- Installation, configuration, migration, upgrade, and rollback where relevant.
- Interoperability with real external systems or realistic fakes where relevant.

### Regression Tests

Every bug fix should include a regression test when practical.

A good regression test:

- Fails before the fix.
- Passes after the fix.
- Is deterministic.
- Is narrow enough to locate the broken behavior.
- Is named or documented so future maintainers understand the bug it prevents.

If a regression test is not practical, explain why and add the best feasible guardrail: logging, assertion, invariant check, manual test note, or follow-up issue.

### Design for Testability

Make important behavior testable from the beginning.

- Separate pure logic from IO and side effects.
- Wrap nondeterminism: time, randomness, thread scheduling, process IDs, environment variables, filesystem, network, and external services.
- Provide fakes/stubs/mocks at stable interfaces, not by poking internals.
- Avoid hidden globals and implicit singletons.
- Make test data builders clear and reusable.
- Keep tests maintainable; no large copy-paste blocks in tests or fixtures.

### Test Types

Use the right mix for the change:

- Unit tests for component contracts and edge cases.
- Integration tests for component interactions.
- Functional tests for user-visible requirements.
- System/end-to-end tests for realistic environments.
- Performance/load tests for scaling risks.
- Install/upgrade/migration tests for release risks.
- Free-form or exploratory tests when UI, concurrency, or complex workflows make surprises likely.

Automate what can be automated. Manual testing is sometimes useful, but repeated manual testing is a process smell.

## Code Review Standards

A review is valuable only if the reviewer understands the code well enough to find real issues.

When preparing code for review:

- Keep diffs small and coherent.
- Provide context: what changed, why, risks, and tests run.
- Add comments/docs where reviewers would otherwise need your private knowledge.
- Link related issues/bugs and include regression test references.

When reviewing code:

- Check correctness, maintainability, testability, diagnosability, and compatibility.
- Walk through main scenarios and important error scenarios mentally.
- Inspect data structures: ownership, lifetime, mutation, aliasing, keys, invariants, and cleanup.
- Inspect resource handling: leaks, double-close/free, partial initialization, partial failure.
- Inspect concurrency: races, deadlocks, lock ordering, async completion paths, cancellation.
- Inspect boundaries: input validation, output encoding, external errors, retries, timeouts.
- Check whether copied code should be commonized.
- Verify that tests would catch the important failures.

Review dialogue:

- Be polite and specific.
- Prefer questions when exploring possible issues.
- Distinguish correctness issues from style preferences.
- Explain the reason for requested changes.
- Comment on good code as well as problems.
- If a review comment applies elsewhere, fix the whole class of issue.

## Build, Version Control, and Release Hygiene

The build and release system is part of the product.

- Keep all build scripts, config, schemas, migrations, docs, codegen inputs, and test harnesses under version control.
- Avoid copy-paste in build scripts; commonize repeated logic.
- Ensure the build can be run locally with a documented command.
- Make the build produce the same artifacts users receive, not just raw binaries.
- Keep generated warnings low; real warnings should not be hidden in noise.
- Run standards checks mechanically: locally, in pre-submit hooks where appropriate, and in CI.
- Allow explicit, documented exceptions to mechanical standards checks.
- Tie code changes to issue/bug IDs when the project uses them.
- For fixes, record affected versions and tests that demonstrate the bug.

## Support and Debugging

Support is not an afterthought. Code that cannot be understood or diagnosed is not high quality.

When debugging:

1. Reproduce or characterize the failure.
2. Identify what version/config/data/environment is involved.
3. Follow the flow of control from the entry point.
4. Follow the flow of data: creation, mutation, ownership, persistence, and deletion.
5. Use logs/traces/metrics before guessing.
6. Minimize the fix while preserving the underlying design.
7. Add a regression test or another guardrail.
8. Record the root cause, not just the symptom.

When working in unfamiliar code:

- Start from entry points and map the call hierarchy.
- Map the main data structures and their lifetimes.
- Trace the key use cases through both code and data.
- Prefer reading real tests and production call sites over guessing from names alone.

For imperfect legacy code:

- Improve testability first when broad rewrites are too risky.
- Add characterization tests before changing behavior.
- Refactor behind tests, in small steps.
- Do not mix large refactors with behavior changes unless necessary.

## Planning and Progress

Reliable software is planned, not accidentally discovered at the end.

For larger tasks:

- Break work into small, independently reviewable steps.
- Estimate effort for design, coding, tests, docs, review, integration, release, and support work - not just typing code.
- Identify dependencies and unblock by agreeing on interfaces early.
- Track both work completed and work remaining; update estimates when new facts appear.
- Surface bad news early: risk, missed assumptions, failing tests, unstable dependencies, or scope growth.
- Keep contingency for unknowns instead of silently lowering quality.

Do not optimize metrics at the expense of real quality. Metrics are signals, not goals.

Useful signals include:

- Tests added/passed and coverage of risky paths.
- Bugs by component and severity.
- Bug recurrence and fixes that caused follow-on bugs.
- Time to diagnose and fix issues.
- Build failures and flaky tests.
- Performance and resource trends.
- Review findings by type, especially maintainability and correctness.

## Automation: Make Repetition Into Code

When a process is repetitive, error-prone, or annoying, automate it.

Good candidates:

- Test execution and fixtures.
- Lint/format/standards checks.
- Build and release packaging.
- Code generation.
- Migration validation.
- Log analysis and debugging aids.
- Metrics collection.

Automation code must meet normal quality standards: versioned, documented, reviewed, tested where practical, and free of avoidable copy-paste.

## Security and Privacy

Reliability includes protecting users and systems.

- Validate all untrusted input.
- Encode output for its context.
- Keep secrets out of source, logs, traces, errors, snapshots, and tests.
- Use least privilege for files, processes, network access, and credentials.
- Treat dependency changes as security-relevant.
- Preserve existing security checks unless explicitly changing them.
- Add tests for authorization, authentication, and validation logic when touched.

## Final Response Requirements

When reporting back after a code change, include:

- What changed.
- Why it changed, if not obvious.
- Tests/checks run, with exact commands when available.
- Any checks not run and why.
- Any remaining risks, assumptions, or follow-up work.

Do not claim a check passed unless it actually ran and passed. Do not hide uncertainty.

## Definition of Done

A change is done when:

- The requirement and important implicit requirements are satisfied.
- The design has clear responsibilities and stable interfaces.
- Special cases are encapsulated and tested.
- Errors and resources are handled on all important paths.
- Diagnostics are sufficient for future support.
- Tests cover normal, edge, and relevant failure paths.
- Build/lint/typecheck/format/tests pass where practical.
- Documentation and comments preserve necessary rationale.
- The final report states what was verified and what was not.