# Methodology

This project follows an experimental, instrument-based methodology to study human reasoning as a dynamic process. The Physiological Reasoning Latency Oscilloscope (PRLO) was designed to capture synchronized behavioral and physiological signals during step-wise problem solving and to analyze how these signals change under controlled perturbations.

---

## System Design

PRLO consists of three integrated components:

1. **Reasoning Step Capture**  
   Participants indicate the completion of each internal reasoning step by pressing a physical button connected to an ESP32 microcontroller. Each button press generates a precise timestamp, creating an explicit segmentation of the reasoning process.

2. **Physiological Signal Acquisition**  
   Electromyography (EMG) is used to measure involuntary muscle activity associated with cognitive effort and hesitation. An EMG sensor module connected to the ESP32 samples muscle signals continuously. EMG was selected as a low-cost, non-invasive physiological correlate of cognitive load.

3. **Central Control and Synchronization**  
   A Raspberry Pi runs the acquisition and analysis software. All data streams are synchronized using a shared high-resolution software clock to ensure alignment between reasoning steps and EMG signals.

---

## Participants

Participants were volunteers recruited from a similar educational background. All participants provided informed consent prior to participation. No personally identifiable information was collected. Participants were seated comfortably in a quiet environment to minimize movement and electrical noise.

---

## Experimental Tasks

The tasks involved solving structured problems (e.g., linear equations) using step-by-step reasoning. Participants were instructed to:
- Solve each problem silently
- Press a button after completing each mental step
- Focus on reasoning clarity rather than speed or correctness

---

## Experimental Conditions

### Baseline Condition
Participants solved familiar problems without any modifications. This condition established each participant’s normal reasoning latency and physiological response patterns.

### Perturbation Condition
Problems were modified using small, controlled perturbations, such as:
- Introducing symbolic parameters
- Removing or altering constraints
- Creating structural edge cases

Only one perturbation was applied per problem to isolate its effect on reasoning stability.

---

## Data Collection

For each trial, the following data were recorded:
- Timestamped button press events
- Continuous EMG voltage samples
- Session metadata (condition, trial number)

Data were stored in raw form and later processed for analysis.

---

## Signal Processing

### Reasoning Latency
Step-to-step latencies were computed as differences between consecutive button press timestamps. These latencies form the basis of the reasoning waveform.

### EMG Processing
Raw EMG signals were converted to voltage values and analyzed using amplitude-based features, including:
- Root mean square (RMS) energy
- Variance
- Transient spikes aligned with reasoning steps

Calibration trials were conducted to establish baseline EMG statistics for each session.

---

## Feature Extraction

The following metrics were derived:
- **Latency Waveforms:** Smoothed representations of step-to-step latency
- **Latency Entropy:** A measure of variability and unpredictability across reasoning steps
- **Physiological Coupling:** Temporal alignment between latency spikes and EMG activity

---

## Collapse Detection

A collapse detection algorithm was applied to latency sequences to identify points of reasoning instability. A collapse was defined by:
- A significant latency spike relative to baseline
- A concurrent drop in latency entropy
- Temporal proximity to elevated EMG activity

Detected events were stored as collapse signatures for further analysis.

---

## Analysis and Validation

Baseline profiles were constructed from unperturbed trials and used as reference distributions. Perturbed trials were compared against these baselines to identify deviations. Statistical analyses were performed to compare conditions and assess consistency across participants.

---

## Ethical Considerations

All procedures were non-invasive and posed minimal risk. Participants were free to withdraw at any time. The system was used solely as a measurement instrument and does not make diagnostic or evaluative claims about individuals.

---

## Reproducibility

All hardware configurations, software components, and analysis pipelines were documented. The use of low-cost components and open-source software ensures that the methodology can be reproduced and extended in future studies.
