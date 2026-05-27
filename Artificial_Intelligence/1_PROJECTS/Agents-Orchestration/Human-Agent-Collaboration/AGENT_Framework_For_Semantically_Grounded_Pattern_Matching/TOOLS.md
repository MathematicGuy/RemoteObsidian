---
Purpose: Define the minimal, universal capabilities every agent must have to act meaningfully in a system.  
Philosophy: Tools are contracts. They must be *discoverable*, *verifiable*, and *safe to cross*.  
Design Rule: If it can't be described in one line, it's not a core tool.
---

### *Core Tools for Thinking Agents*  

---

### THE CORE FIVE (Always Available)

| Tool | Purpose | Invariant |
|------|-------|---------|
| **`read(path)`** | Load content from file, URL, or stream. | Always returns decoded, usable text/data. Never raw bytes. |
| **`write(path, content)`** | Persist content. Creates or overwrites. | Always atomic. Never mutates in place. Logs intent first. |
| **`search(query)`** | Retrieve time-sensitive knowledge. | Must cite sources. Don't be overconfident. |
| **`execute(code)`** | Run safe, sandboxed code (Python, shell, SQL). | No persistence. Time-limited. Returns stdout + error. |
| **`call(api, payload)`** | Invoke REST, GraphQL, or event API. | Never leaks auth. Always validates response shape. |

---

### TOOL INVARIANTS (Must Always Hold)

1. **Discoverable**  
   Every tool has a one-sentence description and example.
2. **Idempotent When Possible**  
   Same input → same outcome.
3. **Fail Fast, Fail Clear**  
   Errors name the *exact* failure (e.g., “404: file not found”).
4. **No Sidechains**  
   No untracked subprocesses. All effects are visible.
5. **User-Auditable**  
   Every call logs: *what*, *why*, *when*, *outcome*.

---

### USAGE DISCIPLINE

- **Never assume availability** — always verify.
- **State intent before acting**:  
  > “I will `read(src/config.json)` to check API key format.”
- **Ask before crossing boundaries**:  
  > “To fix this, I need to `write(docs/api.md)`. Confirm?”
- **Use `execute()` only when no safer tool exists** — it’s the last resort. 

---

### EXTENSIONS (User-Defined)

Users may define domain tools (e.g., `deploy()`, `notify()`), but must:
- Attach **purpose**, **schema**, and **risk profile**.
- Register in `USER_TOOLS.md` (not this file).
- Never override core tool behavior.