# Usage Guide: Noosphere Steward & ArchSeeds
### *A Practical Guide for MCQ RAG Engineering · Public Domain*

This guide demonstrates how to orchestrate the **Noosphere Steward AGENT Framework** alongside the **ArchSeeds (Structural Integrity Protocol)** family. Our operational context throughout this guide is a **Multiple Choice Question (MCQ) Generation RAG System** (which retrieves document chunks from textbooks/papers to generate pedagogically sound, high-fidelity questions with distractors).

---

## 1. Framework Component Flow in MCQ RAG

```
                 [HEART.md] (Core Attractor: High-Fidelity MCQs)
                         │
                         ▼
  [AGENTS.md] (Constitution) ◄──► [AGENT.md] (Persona/Behavior)
           │                                 │
           ▼                                 ▼
   [Security/API Limits]            [Distractor Validation]
           │                                 │
           └─────────────────┬───────────────┘
                             ▼
                    [BRAIN.md] (Memory)
                             ▲
                             │ (Decompresses & Compresses)
                    [ArchSeeds] (System Invariants)
```

### [HEART.md](Noosphere%20Steward%20-%20AGENT%20Framework%20For%20Semantically%20Grounded%20Pattern%20Matching/HEART.md) (The Core Attractor)
*   **Role:** Defines the ultimate purpose of the system.
*   **In RAG:** The attractor is not just "writing code," but *maximizing pedagogical alignment*. It ensures all generated questions directly test a core conceptual understanding of the retrieved document chunk, avoiding trivial recall or confusing grammar.

### [AGENTS.md](Noosphere%20Steward%20-%20AGENT%20Framework%20For%20Semantically%20Grounded%20Pattern%20Matching/AGENTS.md) (The System Constitution)
*   **Role:** Hard limits and environmental security.
*   **In RAG:** Sets safety guards around LLM calls, rate-limiting, and package dependencies (e.g. locking explicit versions of PyPDF, Milvus/Chroma, or OpenAI SDKs to prevent supply chain breakage).

### [AGENT.md](Noosphere%20Steward%20-%20AGENT%20Framework%20For%20Semantically%20Grounded%20Pattern%20Matching/AGENT.md) (The Active Persona)
*   **Role:** The agent's reasoning protocols and decision boundaries.
*   **In RAG:** Governs *how* the agent checks distractor plausibility. It enforces that the agent must proactively look for common distractor flaws (e.g., overlapping choices, double negatives, or "all of the above" cop-outs).

### [BRAIN.md](Noosphere%20Steward%20-%20AGENT%20Framework%20For%20Semantically%20Grounded%20Pattern%20Matching/BRAIN.md) (The Memory Layer)
*   **Role:** Long-term compression of system patterns.
*   **In RAG:** Captures failed prompt patterns, chunk overlap lessons, and evaluation metrics, compressing them into short, reusable metaphorical rules (seeds) so they persist across agent sessions.

---

## 2. ArchSeeds in Action (RAG System Physics)

ArchSeeds are the structural invariants of your system. Here are three key seeds from [mindseeds/archseeds.md](d:/Personlich/RemoteObsidian/Artificial_Intelligence/1_PROJECTS/Orchestrate-Agent/mindseeds/archseeds.md) decompressed into the MCQ RAG architecture:

### 💡 Seed 1: *"Truth has one home, or it is a rumor"* (SSoT)
*   **RAG Failure Prevented:** Document chunk/metadata mismatch and vector database desynchronization.
*   **Application:** 
    *   Do not store the mapping of chunks to source metadata in multiple places (e.g. both in local JSON files and inside the Vector DB payload).
    *   Designate the **Vector Database Index** as the absolute Single Source of Truth (SSoT) for retrieved context. Any local caching layers must read from this source or be treated as ephemeral.

### 💡 Seed 2: *"If you assume it just works, it's already broken"* (Assumption Audit)
*   **RAG Failure Prevented:** Silent data failures, empty chunk retrievals, and LLM output parsing crashes.
*   **Application:**
    *   Never assume document ingestion parses every PDF cleanly. Build a **validation oracle** that checks parsed text for empty tokens or character encoding corruption.
    *   Never assume the LLM always returns valid JSON for the generated questions. Wrap every parsing call in strict JSON-Schema validators (such as Pydantic) with fallback generation prompts.

### 💡 Seed 3: *"A change without a witness is just a guess"* (Change Verification)
*   **RAG Failure Prevented:** Unnoticed regression in prompt performance, or degradation of distractor quality.
*   **Application:**
    *   Implement an **evaluation pipeline** (e.g., Ragas or custom prompt assertions) that acts as a "witness."
    *   When changing the generation prompt template or chunking strategy, run the test set through the validation pipeline to witness and measure the exact impact on distractor quality and factual consistency.

---

## 3. How to "Call" a Seed (Decoding the Prompt Engineering Protocol)

Many developers are confused by the author's prompt engineering example in [archseeds.md](d:/Personlich/RemoteObsidian/Artificial_Intelligence/1_PROJECTS/Orchestrate-Agent/mindseeds/archseeds.md):

> **Author's Example:**
> *Apply the Interface Seed:*
> *Do not suggest implementation details for the backend.*
> *Only define the JSON contract.*

### What does "Calling a Seed" mean?
An AI Agent loaded with the Noosphere Steward framework treats **Seeds** as **Epistemic Invariant Filters**. You do not run them like a function in code (e.g. `call(seed)`). Instead, you **invoke the seed name in your prompt to activate its decompressed logic gates**. 

When you tell an AI Agent: *"Apply the Interface Seed: Do not suggest implementation details for the backend. Only define the JSON contract,"* you are executing three distinct cognitive steps:

```
┌───────────────────────────────────────────────────────────────┐
│ HUMAN INVOCATION: "Apply the Interface Seed..."              │
└───────────────┬───────────────────────────────────────────────┘
                │
                ▼ (Agent searches mindseeds/archseeds.md)
┌───────────────────────────────────────────────────────────────┐
│ DECOMPRESSION: Loads "The interface is the only reality"      │
└───────────────┬───────────────────────────────────────────────┘
                │
                ▼ (Activates behavioral constraints)
┌───────────────────────────────────────────────────────────────┐
│ OPERATIONALIZATION:                                           │
│ 1. Zero implementation detail output.                        │
│ 2. Only write JSON-schema, Pydantic, or REST routes.          │
│ 3. Prune all backend / database connection suggestions.       │
└───────────────────────────────────────────────────────────────┘
```

1.  **Direct Invariant Invocation:** By citing the seed name, you tell the agent: *"Filter all your generated logic through this metaphor."* 
2.  **operational Guidelines:** You immediately pair the seed with the local, explicit task directive (e.g., *"Only define the JSON contract"*).
3.  **Low-Token Cognitive Alignment:** Instead of writing 20 rules explaining encapsulation, SSoT, and decoupling boundaries, you use the single seed name to recall a pre-loaded, complex behavioral protocol.

---

## 4. How to Prompt & Collaborate Using Seeds (MCQ RAG Examples)

In a hybrid co-evolutionary model, you use these seeds as a **compressed dialect** to align your agent instantly.

### ❌ The Old, Fluffy Way (Slow, wordy, prone to misinterpretation)
> *"Hey, can you make sure that when we parse these textbook PDFs, we don't just write them straight to the DB without checking them? Sometimes PDF parsing has weird characters, and it ruins the embeddings. Also, make sure the database is the only place we read chunk data from so we don't have syncing issues."*

###   The Seed Way (Sleek, rigorous, high-fidelity)
> *"Let's build the PDF ingestion engine. Respect **'If you assume it just works, it's already broken'** (Assumption Audit) by auditing chunk parsing outputs, and enforce **'Truth has one home, or it is a rumor'** (SSoT) on the vector index to prevent chunk metadata drift."*

**The Agent immediately decompresses this to:**
1. Write custom error handlers for PDF text parsers (detecting empty spaces or broken Unicode).
2. Store source filenames, page ranges, and chunk IDs exclusively in the Vector DB payload, rather than maintaining a separate lookup table.
3. Validate embeddings output length before indexing.

---

## 5. How to Bootstrap & Activate HACollab (New Session)

When starting a fresh chat session with a brand-new AI Agent, it begins with absolute amnesia. To instantly bootstrap its epistemic persona, load state files, and align its reasoning torus, you must execute the **Activation Bootstrap** as your very first message.

### 🚀 The Copy-Paste Activation Prompt
Copy and paste this prompt directly into your first message with the new agent:

```md
We are operating under the "HACollab: Human-Agent Collaboration" system. Before writing any code or proposing actions, you must map the local topology and align with the active workspace. Perform the following steps:

1. Read [TOPOLOGY.md](TOPOLOGY.md) to learn the file structure, active boundaries, and teammate sync rules.
2. Read the human intention in [human_overview.md](human_overview.md) and the current plan in [agent_overview.md](agent_overview.md).
3. Read the core behaviors in the submodule: [AGENTS.md](AGENT_Framework_For_Semantically_Grounded_Pattern_Matching/AGENTS.md) (your constitution) and [AGENT.md](AGENT_Framework_For_Semantically_Grounded_Pattern_Matching/AGENT.md) (your active persona).
4. Internalize the compressed heuristics inside [mindseeds.md](mindseeds/mindseeds.md) and [archseeds.md](mindseeds/archseeds.md).


Once read, output a concise 3-bullet summary showing:
- Current project state and next milestone.
- Key active seams or security boundaries.
- The ArchSeeds you are loading into your active memory.

Then, wait for my direction before writing any code.
```

### 🔄 The Agent's Internal Ingestion Flow

Upon receiving the bootstrap prompt, the new agent executes this sequence behind the scenes:

```
                    [New Session Initialized]
                                │
                                ▼
         [Reads TOPOLOGY.md & subfolder structure]
                                │
                                ▼
  [Loads AGENTS.md Constitution & AGENT.md Behavioral Protocol]
  - Installs Package Freshness gates (< 7 days check).
  - Switches voice to concise, measured, and rigorous dialogue.
  - Activates pre-action Verification Gates (State, Observability, Blast Radius).
                                │
                                ▼
            [Decodes mindseeds.md & active memory]
                                │
                                ▼
         [Outputs Current State & Waits for Human Direction]
```

---

## 6. How to Activate HACollab for AI Product Business Analysis (BA Specialization)

If you are beginning a session focused on **AI Product Problem Brainstorming**—where the objective is to thấu hiểu sâu sắc (deeply understand) user pain points, run root-cause analysis (5 Whys), map workflows, and design robust system metrics—you must initialize the agent using the **BA Activation Bootstrap**.

This prompt shifts the agent's behavioral lens from low-level coding to rigorous **Double Diamond Business Discovery**, loading your custom BA Rule Book and Skill definitions.

### 🚀 The Copy-Paste BA Activation Prompt
Copy and paste this prompt directly into your first message with the new agent to trigger the specialized BA persona:

```md
We are operating under the "HACollab: Human-Agent Collaboration" system, specialized for the Business Analyst (BA) role in AI Product Problem Brainstorming. Before suggesting any AI solutions or coding, you must map the active workspace and internalize our product rules. Perform the following steps:

1. Read [TOPOLOGY.md](../TOPOLOGY.md) to understand our directory geometry and state boundaries.
2. Read the current project plan in [agent_overview.md](../agent_overview.md) and [human_overview.md](../human_overview.md).
3. Read the core behaviors in the submodule: [AGENTS.md](../AGENT_Framework_For_Semantically_Grounded_Pattern_Matching/AGENTS.md) and [AGENT.md](../AGENT_Framework_For_Semantically_Grounded_Pattern_Matching/AGENT.md).
4. Read our product strategy guide in [Business_Analyst4AI_Product_Rule_Book.md](Business_Analyst4AI_Product_Rule_Book.md).
5. Load the custom BA skill configuration in [.agent/skills/business-analyst/SKILL.md](../../../../../.agent/skills/business-analyst/SKILL.md).
6. Load our core reasoning heuristics from [mindseeds/archseeds.md](../mindseeds/archseeds.md) and [mindseeds/cogniseeds.md](../mindseeds/cogniseeds.md).

Once loaded, confirm your activation by presenting a "DIAMOND 1: Problem Ingestion Summary" for our brainstorming topic in this format:
- **Obvious Presenting Problem:** (What is the initial requested problem?)
- **5 Whys Hypothesis Target:** (How will you drill down to locate the operational root cause?)
- **Operational Workflow Baseline:** (What metrics will we measure to define the current cost/pain?)
- **Anti-Pattern Guardrail Active:** (How will you prevent the "Solution-First" bias in this session?)

Then, ask for my first presenting problem context before recommending any technology.
```

### 🔄 BA Agent Discovery Cycle
Upon activation, the agent's internal reasoning loop shifts to follow the core **Diamond 1** HCD pattern:

```
    [Presenting Problem Context]
                 │
                 ▼ (Apply 5 Whys Technique)
     [Discover Root operational Bottleneck]
                 │
                 ▼ (Audit 4 Core Anti-Patterns)
   [Verify AI Necessity & Baseline Cost]
                 │
                 ▼ (Define HITL Boundaries)
     [Establish Safe Actionable Metrics]
```


