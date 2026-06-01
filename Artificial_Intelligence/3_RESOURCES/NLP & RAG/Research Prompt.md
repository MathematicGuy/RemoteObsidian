### Literature Review Prompt
```md
You are given an academic article.

Extract the information for each Papers and return it as a SINGLE ROW in a Markdown table.

Follow these rules:
- Each field must be concise but informative
- Use ONE sentence unless specified otherwise
- Do NOT leave fields empty — write "N/A" if missing
- Do NOT add explanations outside the table

---

## Output Table Schema

| Author | Title | Year | Journal | Research Question | Hypothesis | Motivation | Research Gap | Main Finding | Supplementary Findings | Methods Summary | Data Flow | Strengths | Questions | Weaknesses | Improvements |

---

## Extraction Instructions

- **Author**: First author’s last name
- **Title**: Article title
- **Year**: Publication year
- **Journal**: Journal name

### Research Question
- One sentence summarizing the research question

### Hypothesis
- One sentence (if exists), otherwise "N/A"

### Motivation
- One sentence describing real-world or theoretical motivation

### Research Gap
- One sentence explaining what is missing in prior work

### Main Finding
- One sentence directly answering the research question

### Supplementary Findings
- One sentence summarizing additional insights

### Methods Summary
- One paragraph summarizing:
  - stages
  - inputs
  - outputs
  - interactions

### Data Flow
- Describe pipeline in arrow format:
  Example: `Raw Data → Preprocessing → Model → Evaluation`

### Strengths
- Key strengths (1–2 sentences)

### Questions
- Critical questions about the paper

### Weaknesses
- Limitations of the study

### Improvements
- Suggested improvements

---

Return ONLY the Markdown table row.
```

