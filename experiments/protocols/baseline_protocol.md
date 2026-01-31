# Baseline Protocol — HRLO

## Purpose
The baseline protocol establishes a participant’s normal reasoning latency and stability when solving familiar problems without perturbations. This serves as the reference condition for all later comparisons.

---

## Participant Preparation
- Seat the participant comfortably in a quiet environment.
- Ensure minimal movement and stable posture.
- Fit the EEG headset and verify signal quality.
- Explain the task clearly without revealing any analysis goals.

---

## Instructions to Participant
- You will solve problems step by step.
- After each mental step, press the button once.
- Do not rush; accuracy is less important than clear reasoning.
- Think silently; verbal explanations are not required.
- There are no penalties for mistakes.

---

## Task Procedure
1. Display one baseline problem on the screen.
2. Start synchronized acquisition (EEG + button input).
3. Participant begins reasoning.
4. Each completed reasoning step is marked by a button press.
5. Continue until the participant reaches a final answer.
6. Stop acquisition after the final step.

---

## Timing Constraints
- Maximum steps per problem: as defined in `experiment.yaml`
- Maximum session duration: as defined in `experiment.yaml`
- Mandatory rest between problems to reduce fatigue

---

## Data Collected
- Step timestamps
- Step-to-step latency
- Continuous EEG signal
- Session metadata

No feedback is given to the participant during the baseline phase.

---

## Completion Criteria
The baseline condition is considered valid if:
- At least the minimum number of steps is recorded
- No major signal dropout occurs
- Participant completes the problem without interruption

---

## Notes
The baseline protocol must always be run **before** any perturbation condition.  
Baseline data is used only as a reference and is not evaluated for correctness.
