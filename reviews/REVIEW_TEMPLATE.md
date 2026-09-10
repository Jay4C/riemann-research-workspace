# Scientific Review Template

---

# Review Metadata

## Review Identifier

```text
REV-XXXX
```

## Date

```text
YYYY-MM-DD
```

## Reviewer

```text
Name:
Institution:
Expertise:
```

## Review Type

- [ ] Mathematical
- [ ] Computational
- [ ] Formal Verification
- [ ] Literature Review
- [ ] Reproducibility Review
- [ ] Adversarial Review
- [ ] Independent Replication

---

# Reviewed Object

## Identifier

```text
CLAIM-XXXX
LEM-XXXX
PROP-XXXX
THM-XXXX
EXP-XXXX
```

## Title

```text
Title of the reviewed object
```

## Current Status

- [ ] OPEN
- [ ] PARTIAL
- [ ] PROVED
- [ ] BLOCKED
- [ ] REFUTED

---

# Executive Summary

Provide a concise summary of the result.

Questions:

- What is being claimed?
- Why is it important?
- What are the dependencies?
- What does the review conclude?

Summary:

```text
...
```

---

# Statement Verification

## Exact Statement

Copy the exact mathematical statement.

```text
...
```

## Is the statement unambiguous?

- [ ] Yes
- [ ] No

Comments:

```text
...
```

## Are all symbols defined?

- [ ] Yes
- [ ] No

Comments:

```text
...
```

---

# Dependency Analysis

List every theorem, lemma or proposition used.

| ID | Dependency | Verified |
|------|------|------|
| | | |
| | | |

Questions:

- Are references complete?
- Are assumptions explicit?
- Is any dependency missing?

Analysis:

```text
...
```

---

# Logical Verification

## Proof Structure

Does the proof have a clearly defined structure?

- [ ] Yes
- [ ] No

Comments:

```text
...
```

---

## Logical Flow

Verify every implication:

\[
A \implies B
\]

\[
B \implies C
\]

\[
C \implies D
\]

Is every implication justified?

- [ ] Yes
- [ ] No

Comments:

```text
...
```

---

# Circular Reasoning Check

One of the most common issues in alleged RH proofs is circularity.

Verify whether:

- RH is assumed directly.
- RH is assumed indirectly.
- An equivalent proposition is used.
- A stronger conjecture is used.

Result:

- [ ] No circular reasoning found
- [ ] Suspicion of circularity
- [ ] Circular reasoning detected

Analysis:

```text
...
```

---

# Analytic Verification

## Convergence

Review:

- Series
- Integrals
- Products
- Limits

Check:

- [ ] Absolute convergence
- [ ] Conditional convergence
- [ ] Uniform convergence

Analysis:

```text
...
```

---

## Analytic Continuation

Review whether any analytic continuation is applied.

Questions:

- Is continuation justified?
- Is the domain specified?
- Are singularities handled?

Analysis:

```text
...
```

---

## Singularities

Check:

- Poles
- Branch points
- Essential singularities

Result:

```text
...
```

---

# Interchange Operations

Review all operations involving:

\[
\lim
\leftrightarrow
\sum
\]

\[
\int
\leftrightarrow
\sum
\]

\[
\frac{d}{ds}
\leftrightarrow
\int
\]

\[
\frac{d}{ds}
\leftrightarrow
\sum
\]

Each interchange must reference a theorem.

Verification:

| Location | Operation | Justified |
|-----------|-----------|------------|
| | | |
| | | |

---

# Uniformity Analysis

Review whether bounds remain valid under all parameter ranges.

Questions:

- Is the estimate uniform?
- Does a hidden dependency appear?
- Is the asymptotic regime controlled?

Analysis:

```text
...
```

---

# Computational Review

Applies only if computations are involved.

## Environment

```yaml
python:
mpmath:
numpy:
machine:
precision:
```

---

## Reproducibility

Can the computation be reproduced?

- [ ] Yes
- [ ] No

Comments:

```text
...
```

---

## Precision

Check:

- Working precision
- Error estimates
- Stability

Result:

```text
...
```

---

## Numerical Evidence vs Proof

Determine whether a numerical observation is incorrectly interpreted as proof.

- [ ] Distinction respected
- [ ] Distinction unclear
- [ ] Numerical evidence presented as proof

Comments:

```text
...
```

---

# Counterexample Search

A review should actively try to refute the claim.

Strategies:

- Edge cases
- Singular values
- Asymptotic limits
- Known pathological examples

Counterexamples found:

```text
...
```

Result:

- [ ] No counterexample found
- [ ] Potential counterexample
- [ ] Valid counterexample

---

# Literature Review

Verify alignment with known literature.

References checked:

| Reference | Verified |
|------------|------------|
| | |
| | |
| | |

Questions:

- Has this idea already appeared?
- Is the result already known?
- Is the result known to be false?

Analysis:

```text
...
```

---

# Formal Verification Potential

Could this result be formalized in:

## Lean

- [ ] Yes
- [ ] No

## Coq

- [ ] Yes
- [ ] No

## Isabelle

- [ ] Yes
- [ ] No

Comments:

```text
...
```

---

# Strength Assessment

Rate the following:

| Criterion | Score (1-5) |
|------------|------------|
| Clarity | |
| Mathematical rigor | |
| Originality | |
| Reproducibility | |
| Literature support | |
| Formalizability | |

---

# Weaknesses

List all weaknesses identified.

```text
...
```

---

# Recommendations

Recommended actions:

- [ ] Rewrite proof
- [ ] Add references
- [ ] Improve notation
- [ ] Strengthen estimates
- [ ] Add numerical validation
- [ ] Attempt formalization
- [ ] Search for counterexamples
- [ ] Obtain specialist review

Details:

```text
...
```

---

# Final Verdict

## Review Outcome

- [ ] ACCEPT
- [ ] ACCEPT WITH MINOR REVISIONS
- [ ] ACCEPT WITH MAJOR REVISIONS
- [ ] REJECT
- [ ] REFUTED

---

## Updated Status Recommendation

- [ ] OPEN
- [ ] PARTIAL
- [ ] PROVED
- [ ] VERIFIED
- [ ] BLOCKED
- [ ] REFUTED

---

# Reviewer Certification

I certify that I have reviewed the submitted material according to the standards specified in this repository.

Reviewer:

```text
...
```

Date:

```text
...
```

Signature:

```text
...
```

---

# Review Archive Metadata

```yaml
review_id:
reviewer:
review_type:
object_reviewed:
date:
outcome:
status_recommendation:
```