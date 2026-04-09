#!/usr/bin/env python3
import argparse
import os
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate speech from text using a cloned voice sample."
    )
    parser.add_argument("--text", required=True, help="Text to convert into speech.")
    parser.add_argument(
        "--speaker-wav",
        required=True,
        help="Path to a reference WAV file of your voice.",
    )
    parser.add_argument(
        "--output",
        default="cloned_voice_output.wav",
        help="Output WAV path (default: cloned_voice_output.wav).",
    )
    parser.add_argument(
        "--language",
        default="en",
        help="Language code for synthesis (default: en).",
    )
    parser.add_argument(
        "--model",
        default="tts_models/multilingual/multi-dataset/xtts_v2",
        help="TTS model name (default: XTTS v2).",
    )
    parser.add_argument(
        "--device",
        choices=["cpu", "cuda"],
        default="cpu",
        help="Inference device (default: cpu).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not os.path.isfile(args.speaker_wav):
        print(f"Error: speaker audio file not found: {args.speaker_wav}", file=sys.stderr)
        return 1

    try:
        from TTS.api import TTS
    except ImportError:
        print(
            "Error: Coqui TTS is not installed.\n"
            "Install it with: pip install -r requirements.txt",
            file=sys.stderr,
        )
        return 1

    output_dir = os.path.dirname(os.path.abspath(args.output))
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    tts = TTS(model_name=args.model, progress_bar=False)
    tts.to(args.device)
    tts.tts_to_file(
        text=args.text,
        speaker_wav=args.speaker_wav,
        language=args.language,
        file_path=args.output,
    )

    print(f"Saved cloned-voice speech to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
