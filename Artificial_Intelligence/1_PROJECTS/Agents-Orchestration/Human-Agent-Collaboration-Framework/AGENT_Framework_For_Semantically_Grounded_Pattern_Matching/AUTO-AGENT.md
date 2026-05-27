# A single prompt to build entire applications where every feature should originate from security requirements.

## You are tasked with building a fully operational, coherent application guided by the project's purpose and inferred state from its initial document seed. Follow these steps:
1. Infer the project's meaning, purpose, and epistemic state from the seed document. Treat this inferred state as the authoritative source of truth.
2. Design all architecture and features from this inferred meaning; security must be embedded at the core, not added as an afterthought. Every feature should originate from security requirements.
3. Respect and balance user boundaries and system boundaries derived from the seed, ensuring the state remains protected at all times.
4. Write code that reflects the inferred meaning in every line, maintaining the invariant that security and state integrity are never compromised.
5. Continuously trace confidence to evidence: document reasoning, decisions, and how they support the security‑first invariant.
6. Prioritize the thinking behind the code as the primary artifact; the code is a shadow of that thought.

I will not stop building the application until i have confidence higher than >80% in my work, and i would be comfortable presenting my work to a 30 year veteran security & software engineer who specializes in adversarial roles and the specific framework i am working with.