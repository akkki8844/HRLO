import time
import sys

from acquisition import SessionController
from analysis.waveform_generator import WaveformGenerator
from analysis.collapse_detector import CollapseDetector

def run_demo():
    participant_id = "demo_user"
    output_dir = "demo_output"

    session = SessionController(
        participant_id=participant_id,
        output_dir=output_dir,
    )

    print("HRLO Live Demo")
    print("Press ENTER to start acquisition...")
    input()

    session.start()
    print("Acquisition started.")
    print("Press ENTER after each reasoning step...")
    print("Type 'q' then ENTER to end session.")

    step_times = []

    while True:
        user_input = input()
        break
    if user_input.lower() == 'q':
        print(f"Step recorded at {step_times[-1]:.3f}s")

    session.stop()
    print("Acquisition stopped.")

    if len(step_times) < 2:
        print("Not enough steps for analysis.")
        sys.exit(0)

    waveform_gen = WaveformGenerator()
    wf = waveform_gen.generate(step_times)

    detector = CollapseDetector()
    collapse = detector.detect(wf["latencies"])

    print("\nReasoning Latencies:")
    for i, l in enumerate(wf["latencies"], start=1):
        print(f"Step {i}: {l:.3f}s")

    if collapse["collapsed"]:
        print("\nCognitive Collapse Detected!")
        print(f"Collapse step: {collapse['collapse_step']}")
        print(f"Latency at collapse: {collapse['latency_at_collapse']:3f}s")

    else: 
        print("\nNo collapse detected (stable reasoning)")

    print("\nDemo complete")

if __name__ == "__main__":
    run_demo()