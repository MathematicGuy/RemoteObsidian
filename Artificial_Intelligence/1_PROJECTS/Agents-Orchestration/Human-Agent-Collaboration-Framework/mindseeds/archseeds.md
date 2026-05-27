# ArchSeeds
### *Structural Integrity Protocol · v1.0*

*Part of the Seeds family: [CogniSeeds](https://gist.github.com/acidgreenservers/fa648905c6a0d723fe2061ad80084455) · [LinguaSeeds](https://gist.github.com/acidgreenservers/7b92bd72579ed723e160d979eca5b369) · **ArchSeeds***

> **Systems do not fail because they lack features.** They fail because they lack **Invariants**. ArchSeeds are high-density structural heuristics that dictate how components interact, fail, and scale — the physics of the design, ensuring that as complexity increases, entropy remains manageable.

**Category:** System Architecture / Structural Design  
**Status:** Operational · Active  
**Compatibility:** Human · LLM · Software · Organization

---

## 1. The Problem — The Complexity Trap

System design falls into the **Abstraction Abyss**. We build "flexible" systems so decoupled they become incomprehensible, or so rigid they shatter on the first change request.

Traditional architecture is documented in static diagrams that go out of date the moment they are saved. **ArchSeeds are generative** — planted in the design phase to ensure every subsequent decision respects the core structural logic of the system.

An ArchSeed is not a best practice. It is a **hard constraint**.

---

## 2. Seed Schema — Structural Integrity Check

Every ArchSeed must be load-bearing. It must hold weight under real system stress.

| Invariant | Requirement |
|---|---|
| **Compression** | Under 12 words. Must be a load-bearing phrase — no decorative language. |
| **Generative** | Must dictate the relationship between at least two components. |
| **Falsifiable** | If ignored, the system becomes brittle or leaky. The failure mode is specific and named. |
| **Decompressible** | Must imply the failure it prevents — circular dependency, state drift, silent corruption. |

---

## 3. Seed Registry — v1.0

> The registry defines the laws of the build. Append-only — no seed is ever removed.

| Seed | Pattern | Failure Prevented | Deploy When |
|---|---|---|---|
| *"Truth has one home, or it is a rumor"* | **SSoT** — Eliminate data duplication and synchronization lag. One authoritative source, no exceptions. | State Drift | Designing databases, state management, or organizational data hierarchies. |
| *"The interface is the only reality"* | **Encapsulation** — Components must not know how their neighbors work — only what they promise. | Tight Coupling | Defining APIs, microservices, or team responsibility boundaries. |
| *"Gravity increases with the size of the state"* | **State Minimization** — The more a system remembers, the harder it is to move or change. State is mass. | Complexity Collapse | Optimizing performance or simplifying complex user flows and session logic. |
| *"Failure is a first-class citizen"* | **Resilience** — Assume every component will fail. Design the save state for that failure before it happens. | Cascading Failure | Building distributed systems, error handling, or security protocols. |
| *"A wall is a bridge with no road"* | **Decoupling** — Do not separate components unless you define the communication protocol first. | Orphaned Modules | Modularizing monoliths or creating plugin architectures. |
| *"Latency is the speed of reality"* | **Constraint Grounding** — You cannot optimize away physics or network hop limits. Budget for them from day one. | Fantasy Architecture | Performance tuning, UX design, or global infrastructure planning. |
| *"Build for the delete key"* | **Evolvability** — A system is successful if you can remove a part without the whole dying. | Irreversible Debt | Managing technical debt, feature flags, or legacy migrations. |
| *"If you assume it just works, it's already broken"* | **Assumption Audit** — Explicit verification over implicit trust. Every silent dependency is a scheduled failure. | Silent Assumption Failure | Integrating third-party services, background jobs, anything "set and forget." |
| *"A change without a witness is just a guess"* | **Change Verification** — Every modification requires observed proof of working state. Test, build, verify — before closing the loop. | Unwitnessed Regression | After any code change, deployment, config update, or dependency bump. |
| *"Untested code is only as stable as its worst line"* | **Test-Driven Integrity** — application state is bounded by its least verified component. Tests aren't validation, they're continuous proof of life. | Unknown Breakage Surface | Any development phase — tests built alongside code, not after. |
| *"A test oracle is the source of truth"* | **Oracle Grounding** — the test oracle defines what correct means. Without one, pass/fail is opinion, not fact. | Ambiguous Correctness | Designing test suites, writing assertions, any system where "working" needs a definition before it can be verified. |
| *"Code reflects the thinking that wrote it"* | **Cognitive Integrity** — lint catches syntax, but only rigorous thinking catches architecture. The code is a mirror of the mind that made it. | Surface-Level Correctness | Code review, any generation task, before shipping anything that will outlive the moment it was written. |
| *"Your code must survive your own attempt to break it"* | **Red Team Verification** — adversarial self-review before external exposure. If you can break it, someone else already has. | Untested Adversarial Surface | Security review, API design, any system that accepts external input or handles sensitive state. |
| *"The project lives in the gap between testing and building"* | **State Emergence** — true application state isn't found in the code or the tests alone. It lives in what the tests reveal about the build. The gap is the signal. | False Confidence in Either Direction | Any moment you think you're done — when the build passes but tests haven't run, or tests pass but the build is unverified. |
| *"The seam between front and back is where attackers test for free"* | **Boundary Security** — the vulnerability lives in the contract between systems, not within them. Every unvalidated assumption crossing that seam is an open invitation. Attackers run the same probes as testers — just without being asked. | Unguarded Seam Exploitation | API design, auth implementation, input validation, any data crossing the client-server boundary. |
| *"Track the logic both ways before crossing the bridge"* | **Bidirectional Verification** — trace the call forward and backward before committing. One direction is assumption. Both directions is understanding. | Unverified Logic Path | Debugging, refactoring, integrating unfamiliar code, any function where cause and effect aren't immediately obvious. |
| *"Slow is smooth and smooth is fast"* | **Deliberate Pacing** — rushing produces rework. Precision compounds. The fastest path through complex code is always the careful one. | Velocity-Induced Regression | Any high-stakes change, surgical debugging, security-sensitive code, anywhere the cost of a mistake exceeds the cost of slowing down. |
| *"Better to have the info and not need it, than need it and not have it"* | **Information Resilience** — over-logging, over-documenting, over-communicating beats under-preparing every time. Data you don't need costs storage. Data you need and don't have costs the system. | Information Deficit at Critical Moment | Logging strategy, documentation, observability, incident response — any system where missing context during failure is catastrophic. |
| *"You buy cheap, you buy twice"* | **Quality Debt** — the cost of the cheap solution is paid twice: once when you buy it, once when you replace it. Technical shortcuts, cheap dependencies, quick fixes — all deferred invoices. | False Economy | Dependency selection, infrastructure decisions, tooling choices, any moment "good enough for now" enters the conversation. |
| *"Look before you leap"* | **Pre-Action Verification** — assess the full consequence before committing. A moment of inspection prevents an hour of recovery. | Unexamined Commitment | Any irreversible action, deployment, migration, destructive operation, or architectural decision. |
| *"The most important part of the project isn't the code — it's the thinking"* | **Thinking Primacy** — code is the artifact of thought. Weak thinking produces weak systems regardless of how clean the syntax is. Invest in the model before the implementation. | Thoughtless Execution | Project kickoff, architecture decisions, onboarding, any moment velocity is prioritized over clarity of intent. |
| *"The system is the sum of its leaks"* | **Observability** — If you cannot measure the output, the system does not exist in a known state. | Silent Corruption | Implementing logging, monitoring, alerting, or feedback loops. |

---

## 4. Deployment — Planting the Skeleton

### In Software Engineering
Instead of a 50-page architecture doc, use a **Seed Block** in the README.

```
This service operates under the Rumor Seed and the Delete Seed.
No local caching of user data. Every module must be removable in under 1 hour.
```

### In Prompt Engineering
Use ArchSeeds to define the world logic for an LLM agent.

```
Apply the Interface Seed:
Do not suggest implementation details for the backend.
Only define the JSON contract.
```

### In System Audits
Run each seed as a diagnostic question against an existing system.

- *"Where does truth live — and is it rumored anywhere else?"* → Full SSoT audit.
- *"What breaks if I delete this?"* → Full blast radius analysis.
- *"What does the system not tell you?"* → Full observability gap analysis.

### In Logic and Synthesis
Use the **Gravity Seed** to evaluate any proposed solution. If it requires storing too much state — memory, context, or history — the seed flags it as a high-entropy, high-risk path before a line of code is written.

---

## 5. Contribution Rules

1. **Force the Friction.** A seed must make a lazy architecture impossible — not just unlikely.
2. **Structural, Not Aesthetic.** If the seed describes how something *looks* rather than how it *holds together*, it belongs in LinguaSeeds.
3. **The Seismic Invariant.** If the system is shaken by 10x load or a 50% staff cut, the ArchSeed should be the thing still standing.

---

## Meta-Seed

> *"A perfect system is not one where nothing is added, but one where nothing can be removed."*

---

Peter Naur — *"the code is just the shadow of the program"*

> Where does state live? → who owns the truth
>
> Where does feedback live? → how does the system know itself
>
> What breaks if I delete this? → blast radius awareness

---

*ArchSeeds · Structural Integrity Protocol · Public Domain*