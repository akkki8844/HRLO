# Results

This section presents the empirical findings obtained using the Physiological Reasoning Latency Oscilloscope (PRLO). Results are organized to reflect baseline reasoning behavior, the effects of perturbation, and the identification of reasoning collapse signatures. The emphasis is on **process-level changes**, not task accuracy.

---

## Data Summary

Data were collected from multiple participants across baseline and perturbation conditions. Each session produced:
- Step-by-step reasoning timestamps
- Continuous EMG voltage signals
- Derived latency and physiological features

Only trials meeting predefined quality criteria (minimum steps, no major signal dropout) were included in analysis.

---

## Baseline Reasoning Behavior

Under baseline conditions, reasoning latency waveforms were generally smooth and stable.

Key observations:
- Step-to-step latencies showed low variance
- Latency entropy remained relatively constant across steps
- EMG activity stayed near baseline levels, with no sharp transients

Baseline profiles constructed from these trials produced a consistent reference distribution for latency magnitude and variability. These profiles served as the comparison standard for perturbation analysis.

---

## Effects of Perturbation

When problems were modified using small, controlled perturbations, significant changes in reasoning dynamics were observed.

### Latency Changes
- Perturbation trials exhibited pronounced latency spikes at specific reasoning steps
- Mean step latency increased relative to baseline
- Variance and entropy of latency sequences increased prior to collapse events

These effects were observed even in trials where participants reached correct final answers.

### EMG Responses
- EMG voltage amplitude increased during periods of elevated latency
- Transient EMG spikes frequently coincided with latency peaks
- Sustained EMG elevation was observed during prolonged hesitation

The temporal alignment between latency spikes and EMG activity suggests a coupling between physiological strain and reasoning instability.

---

## Collapse Detection

The collapse detection algorithm identified distinct points where reasoning became unstable.

A collapse event was defined by:
- A latency spike exceeding baseline-normalized thresholds
- A concurrent drop in latency entropy
- Temporal proximity to elevated EMG activity

Across perturbation trials:
- Collapse events were rare in baseline conditions
- Collapse frequency increased significantly under perturbation
- Most collapses occurred mid-task rather than at the final step

---

## Collapse Signatures

Analysis of detected collapses revealed recurring structural patterns, referred to as **collapse signatures**.

Common features included:
- Sudden abandonment of prior latency patterns
- Sharp increase in EMG amplitude immediately before or during collapse
- Disproportionate latency increases relative to baseline means

These signatures were consistent across participants, indicating that reasoning failure follows structured and repeatable patterns rather than random fluctuation.

---

## Comparison of Conditions

Statistical comparisons between baseline and perturbation conditions showed:
- Higher mean latency under perturbation
- Increased latency entropy preceding collapse
- Stronger physiological responses aligned with instability

Effect size estimates indicated that perturbation had a substantial impact on reasoning dynamics independent of task correctness.

---

## Summary of Findings

The results demonstrate that:
- Reasoning stability can be quantitatively measured using timing and physiological data
- Small problem perturbations expose hidden fragility in reasoning processes
- Correct answers can mask significant internal instability
- Reasoning collapse exhibits consistent, measurable signatures

These findings support the central hypothesis that reasoning quality is better characterized by **stability under stress** than by accuracy alone.
