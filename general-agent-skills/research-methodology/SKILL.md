---
name: research-methodology
description: Method for researching any factual question — comparisons, "what's the evidence," market or technical landscape questions, due diligence, fact-finding. Use whenever the user asks to research, look into, find out, compare, or verify something, or when an answer depends on facts that could be wrong or stale — even for quick lookups that turn out to be contested.
---

# Research Methodology

The output of research is not "what sources say." It is "what is true, how confidently, and what would change the answer."

## Before searching

- State the question in one sentence and what decision it feeds. Research without a decision attached expands forever.
- Write down the answer expected beforehand — it exposes confirmation bias when the evidence disagrees.

## Source hierarchy

1. **Primary**: papers, filings, official docs, first-party data, the actual code/product.
2. **Quality secondary**: journalism and analysis that cites primaries.
3. **Aggregators, forums, SEO content**: leads only — never load-bearing. Follow their citations upward.

## Rules of evidence

- **Triangulate**: any load-bearing claim needs two independent sources. If five sources all trace to one origin, that is one source.
- **Date everything**: check publication dates; for fast-moving topics prefer <12 months and say when data is older.
- **Separate finding from inference**: "X reported Y" is a finding; "therefore Z" is inference. Never blend them in one sentence.
- **Label confidence** on key claims: confirmed / likely / contested / speculative.
- **Numbers get sources**: every statistic carries where it came from, or is labeled an estimate with the reasoning shown.

## Boundary with data-analysis

Use research-methodology when the question is about the world — "is this true?", comparisons, landscapes, anything whose answer lives outside your files. Use data-analysis when the question is about data you hold — a CSV, a metrics export, survey results. For a statistics question: if the number comes from your data, start with data-analysis (check the data first); if it needs an external source, start here. When both apply — your data contradicts the published numbers — run data-analysis first (is the data clean?), then research-methodology (is the world different than reported?). Never cite external statistics to explain your data without checking your data, and never generalize your dataset to the world without external triangulation.

## Stop rule

Stop when new sources repeat what is already known, or when remaining uncertainty no longer changes the decision. Note what was NOT checked.

## Output format

1. Answer first, with confidence level.
2. Evidence: claim → source → date, for each load-bearing claim.
3. What would change this answer / open questions.
