# Governance

## Purpose

This document defines the governance model of the **Riemann Research Workspace**.

The objective is to ensure:

- Scientific rigor
- Transparency
- Reproducibility
- Traceability
- Reviewability
- Long-term maintainability

This repository is intended to function as a research laboratory rather than a collection of disconnected notes or experiments.

---

# Core Principles

## Principle 1: Truth Before Novelty

Novel ideas are valuable.

Correct ideas are essential.

Contributors must prioritize correctness over originality.

---

## Principle 2: Reproducibility

Every result must be reproducible.

Any claim based on:

- numerical experiments,
- computations,
- simulations,
- generated datasets,

must include enough information for independent verification.

---

## Principle 3: Explicit Assumptions

All assumptions must be documented.

No hidden assumptions should appear in:

- proofs,
- experiments,
- reviews,
- publications.

---

## Principle 4: Negative Results Matter

Failed approaches are valuable.

Rejected arguments must be preserved and documented rather than silently removed.

Documenting failure prevents repetition of mistakes and provides useful knowledge.

---

## Principle 5: Transparency

The status of every research result must be visible.

Possible states include:

```text
OPEN
PARTIAL
PROVED
REFUTED
BLOCKED
VERIFIED
```

No claim may be promoted beyond its actual verification status.

---

# Repository Governance Structure

## Maintainer

The maintainer is responsible for:

- repository organization;
- contribution approval;
- release management;
- governance updates;
- quality control.

The maintainer does not possess authority to declare mathematical correctness without supporting evidence.

---

## Contributors

Contributors may:

- submit code;
- submit documentation;
- propose lemmas;
- propose conjectures;
- submit experiments;
- provide reviews.

All submissions are subject to validation.

---

## Reviewers

Reviewers are responsible for:

- checking logical consistency;
- identifying hidden assumptions;
- searching for counterexamples;
- verifying references;
- assessing reproducibility.

The reviewer role is independent from authorship.

---

# Scientific Object Lifecycle

Every scientific object must follow a lifecycle.

Examples:

- Definition
- Claim
- Lemma
- Proposition
- Theorem
- Experiment
- Dataset

Lifecycle:

```text
Draft
 ↓
Review
 ↓
Revision
 ↓
Verification
 ↓
Publication
```

---

# Claim Governance

All research claims must be registered.

Examples:

```text
CLAIM-0001
LEM-0001
PROP-0001
THM-0001
```

Every claim must include:

- unique identifier;
- statement;
- assumptions;
- dependencies;
- status;
- supporting evidence.

---

## Claim Status Rules

### OPEN

Work has started.

No proof available.

### PARTIAL

Some components are verified.

Major steps remain unresolved.

### BLOCKED

Dependent on unresolved questions.

### PROVED

A complete mathematical proof exists.

### VERIFIED

Proof independently reviewed.

### REFUTED

Counterexample or logical error identified.

---

# Proof Governance

## Requirements

A proof must:

- state hypotheses explicitly;
- define notation;
- justify every implication;
- cite dependencies.

---

## Mandatory Checks

The following must be verified:

### Convergence

- absolute convergence;
- uniform convergence;
- exchange of limits.

### Analytic Continuation

- validity of domain transitions;
- singularity handling.

### Error Terms

- asymptotic control;
- explicit bounds.

### Circular Reasoning

Special attention must be given to hidden 