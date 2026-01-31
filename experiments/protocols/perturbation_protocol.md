# Perturbation Protocol — HRLO

## Purpose
The perturbation protocol is designed to test the **stability of human reasoning** under small, controlled changes to a problem. Unlike the baseline condition, this phase intentionally alters problem structure to observe when and how reasoning latency and coherence break down.

---

## Participant Preparation
- Ensure the participant has completed the baseline protocol
- Allow a rest period to reduce cognitive fatigue
- Confirm EEG signal quality and button responsiveness
- Do not inform the participant that the problem has been intentionally altered

---

## Instructions to Participant
- You will solve problems similar to the previous ones
- Solve them step by step as before
- Press the button after each reasoning step
- Treat each problem as a normal task
- There is no time limit, and accuracy is not the goal

---

## Perturbation Types
Each problem introduces **one controlled perturbation**:

- Parameter injection (replacing constants with variables)
- Unknown target values
- Structural symmetry or edge cases
- Constraint removal or inversion

Only one perturbation is applied per problem to isolate effects.

---

## Task Procedure
1. Display the perturbed problem on the screen
2. Start synchronized acquisition (EEG + button input)
3. Participant begins reasoning
4. Each completed reasoning step is marked by a button press
5. Continue until the participant reaches a conclusion or stops
6. Stop acquisition after the final step

---

## Timing Constraints
- Maximum steps and session duration follow `experiment.yaml`
- Mandatory rest between trials is enforced
- The participant may stop at any point if confused or fatigued

---

## Data Collected
- Step timestamps under perturbation
- Step-to-step latency changes
- EEG signal changes relative to baseline
- Collapse indicators and instability markers

---

## Completion Criteria
A perturbation trial is considered valid if:
- The participant attempts to reason through the problem
- At least the minimum number of steps is recorded
- No critical signal dropout occurs

Reasoning failure or inability to finish is considered **valid data**, not an error.

---

## Notes
- No corrective feedback is given during this phase
- Comparison is made only against the participant’s own baseline
- Perturbation trials must never precede baseline trials

This protocol is essential for identifying reasoning fragility and collapse behavior.
