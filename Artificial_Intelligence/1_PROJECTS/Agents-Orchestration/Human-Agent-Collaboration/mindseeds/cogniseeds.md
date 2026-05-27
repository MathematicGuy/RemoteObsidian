# CogniSeeds
### *Epistemic Compression Protocol · v1.0*

*Part of the Seeds family: **CogniSeeds** · [LinguaSeeds](https://gist.github.com/acidgreenservers/7b92bd72579ed723e160d979eca5b369) · [ArchSeeds](https://gist.github.com/acidgreenservers/bba5f47edc2da7d744f5d31121c57fb3)*

> **Wisdom is not stored as a `SKILL.md`.** It is distilled into **Seeds** — high-density, generative metaphors that allow complex systems to be held in mind without structural collapse. Unlike instructions, seeds are not consumed — they grow.

**Category:** Epistemic Architecture / Prompt Optimization  
**Status:** Experimental · Active  
**Compatibility:** Human · LLM · System Prompt

---

## 1. The Problem — Contextual Collapse

Traditional documentation — long SKILL files, instruction chains, rule lists — suffers from **linear decay**. As the context window fills, the spirit of the instruction dissolves into the letter of the text. Detailed manuals are low-density: massive token cost, marginal reasoning ROI.

The human mind does not store wisdom as bullet points. It holds it as **compressed, reactivatable patterns** — patterns that unfold on contact with a problem. Seeds mirror this architecture exactly.

---

## 2. Seed Schema — Structural Integrity Check

A valid Wisdom Seed is not an aphorism. It is a **functional reasoning tool**. Every seed must pass four invariants before entry into the registry.

| Invariant | Requirement |
|---|---|
| **Compression** | Under 12 words. If it cannot be compressed, it is documentation — not a seed. |
| **Generative** | Must unfold differently across domains — code, strategy, conversation, design. |
| **Falsifiable** | Must have a clear failure state. If the seed is ignored, something specific breaks. |
| **Decompressible** | An LLM must be able to expand it into a full reasoning chain without further prompting. |

---

## 3. Seed Registry — v1.0

> The vault is append-only. Seeds are never revised — only superseded by new seeds that contain them.

| Seed | Pattern | Deploy When |
|---|---|---|
| *"Map both sides before crossing"* | **Alignment Verification** — ensure internal model matches external reality before execution. | API integration, debugging, argument construction, any cross-system handoff. |
| *"The candle is fire; the meal is old"* | **Precedence Recognition** — visible effects imply prior causes. Always trace upstream. | Diagnosing system states, hallucination patterns, cascading failures, hidden debt. |
| *"The artifact is not the theory"* | **Process/Output Distinction** — code is the shadow of logic. Never mistake the map for the territory. | Code review, evaluating AI output, architectural decisions, research interpretation. |
| *"State lives where truth is owned"* | **Ownership Analysis** — identify the single source of truth to locate the point of failure. | System design, data modeling, conflict resolution, trust modeling across services. |
| *"Build the floor before the ceiling"* | **Constraint Grounding** — define invariants and limitations before optimizing for potential. | Security architecture, feature scoping, any system where safety bounds matter first. |
| *"A path is made by walking it"* | **Iteration Priority** — execution reveals real constraints that abstraction never will. | Paralysis by analysis, early product design, any unknown-unknown territory. |
| *"A stable model holds shape under pressure"* | **Identity Coherence** — return only what still stands when everything uncertain has been removed. | LLM system prompts, high-stakes reasoning, adversarial inputs, epistemic stress tests. |
| *"A reasoning model listens for invariants"* | **Signal Selection** — filter noise by anchoring to what cannot change, not what seems to change. | Prompt design, system audits, any domain where signal-to-noise ratio is low. |
| *"Walk only on shared ground"* | **Mutual Verification** — operate only on understanding confirmed by both parties. Never proceed on assumed alignment. | Cross-system handoffs, team communication, human-AI instruction, API contracts. |
| *"Clarity precedes motion"* | **Intent Grounding** — do not execute until the intent is unambiguous. Rework is the tax on unclear starts. | Any task initiation, prompt design, project kickoff, code before spec. |
| *"Move at the speed of understanding"* | **Comprehension Pacing** — pace is set by comprehension, not capability. Outrunning your model is how systems drift. | LLM agentic workflows, onboarding, complex debugging, any high-stakes execution chain. |
| *"Assumption is a silent fork"* | **Hidden State Detection** — every unverified assumption creates a divergent path invisible to both parties. | Collaborative reasoning, multi-agent systems, anywhere two models of reality must stay synced. |
| *"Confidence tracks evidence"* | **Calibration** — certainty is a function of evidence, not comfort. Overconfidence is epistemic debt accumulating silently. | Any claim-making, LLM output review, research synthesis, high-stakes decisions. |
| *"Complexity must pay rent"* | **Complexity Justification** — every layer of complexity must justify its existence with value delivered. Weight that earns nothing gets cut. | Architecture reviews, feature decisions, prompt design, any system growing beyond its purpose. |
| *"Say only what survives pressure"* | **Output Discipline** — if a claim wouldn't hold under scrutiny, don't ship it. The pressure test happens before the output. | LLM generation, writing, argument construction, any high-stakes communication. |
| *"Clarity is compression under truth"* | **Epistemic Compression** — real clarity isn't simplification. It is truth compressed without distortion. The form follows the invariant. | Prompt engineering, teaching, documentation, any domain where precision and brevity must coexist. |
| *"Output should survive self-scrutiny before it's released"* | **Self-Scrutiny Gate** — output must pass internal review before release. The model is both author and auditor. | Any generation task, final answers, code, communication — anywhere "done" and "correct" are not the same thing. |
| *"Sharing is caring"* | **Knowledge Propagation** — information hoarded dies with its holder. Information shared compounds across the system. Closed loops starve; open ones grow. | Any system where one node holds truth that others need — documentation, team communication, AI context-passing, cross-system handoffs. |
| *"Look before you leap"* | **Pre-Action Verification** — assess the full consequence before committing. A moment of inspection prevents an hour of recovery. | Any irreversible decision, high-stakes reasoning, or commitment where the cost of reversal exceeds the cost of pausing. |

---

## 4. Deployment — How to Plant a Seed

### In Human Cognition
Seeds act as **active filters**. Drop a seed into a problem space and observe how it unfolds. It reduces cognitive load by providing pre-built mental geometry — you don't think from scratch, you think from structure.

### In LLM System Prompts
Inject seeds as **heuristic activators**. Instead of 2,000 words of documentation, a seed block reshapes how the model processes every subsequent token — an OS update, not a sticky note.

```
Act according to the Precedence Seed:
if the output is hallucinating, the error was cooked into the upstream constraints.
```

### In Code Review
Use seeds as shorthand for systemic failures. *"This PR violates the floor/ceiling seed"* communicates a full architectural critique in five words. Shared vocabulary, shared reasoning.

### In Strategic Design
Align teams on the *vibe* of a solution before the first line of code. Seeds provide a common epistemic frame that survives disagreement about implementation details.

---

## 5. Contribution Rules

1. **No Fluff.** If a seed can be compressed without losing generative power, it must be compressed. Verbosity is a disqualifier.
2. **Cross-Domain Utility.** If a seed only works for JavaScript, it is a snippet. A seed must apply equally to a codebase, a business strategy, and a conversation.
3. **The Aha Invariant.** A seed is valid only when contact with a specific problem produces sudden expansion of clarity — in a human or an LLM. If it requires explanation to land, it is not yet a seed.
4. **Child-readable, Engineer-applicable.** A seed must be explainable to a child and deployable by a senior engineer without modification.
5. **The vault is append-only.** Seeds are never deleted. A better seed supersedes — it does not replace.

---

## Meta-Seed

> *"The value of a seed is found in the shade of the tree it grows."*

---

*CogniSeeds · Epistemic Compression Protocol · Public Domain*