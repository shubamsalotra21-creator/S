# Voice Clone TTS

This repository now includes a minimal voice-clone text-to-speech script using Coqui XTTS.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python voice_clone_tts.py \
  --text "Hello, this is my cloned voice." \
  --speaker-wav /absolute/path/to/your_voice_sample.wav \
  --output /absolute/path/to/output.wav \
  --language en \
  --device cpu
```

## Notes

- Use a clean 6-15 second voice sample for best cloning quality.
- Default model: `tts_models/multilingual/multi-dataset/xtts_v2`.
