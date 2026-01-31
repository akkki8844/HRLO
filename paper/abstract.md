# Abstract

Traditional assessments evaluate reasoning through accuracy and speed, but they fail to capture how reasoning *unfolds* and destabilizes under cognitive stress. This project introduces the **Physiological Reasoning Latency Oscilloscope (PRLO)**, a novel hardware–software instrument that measures reasoning as a dynamic, time-based signal rather than an outcome.

PRLO synchronizes step-wise reasoning input with physiological measurements obtained from electromyography (EMG), using an ESP32 microcontroller and a Raspberry Pi. Participants solve problems step by step, marking each cognitive transition with a physical button press, while EMG signals capture involuntary muscle tension associated with cognitive load and hesitation. Reasoning is visualized as latency waveforms, and controlled perturbations to problems are used to test reasoning stability.

The system introduces new quantitative metrics, including reasoning latency entropy and collapse signatures, which identify points where reasoning becomes unstable or breaks down. Experimental results show that small structural changes to problems produce characteristic latency spikes and EMG responses that are absent in baseline conditions, even when final answers remain correct.

By reframing reasoning as a measurable signal rather than a static score, PRLO provides a new method for studying cognitive stability, learning fragility, and failure modes in problem solving. This approach offers applications in education research, human–computer interaction, and cognitive science, and demonstrates that low-cost physiological sensing can reveal hidden dynamics of human reasoning.
