# WikiLLM Governance Schema

## Page Thresholds
- **Entity/Concept Pages**: Create a unique file ONLY if the entity/concept is central to at least 1 raw source, OR is mentioned across >= 2 separate sources. Passing footnotes or minor references do not warrant a separate page.

## YAML Frontmatter Rules
Every concept page must use this frontmatter:
```yaml
---
title: "Concept: [Name]"
type: concept
aliases: [[Shorthand]]
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
confidence: [Decimal 0.0 - 1.0]
tags: [#concept, #relevant-tag]
---
````

