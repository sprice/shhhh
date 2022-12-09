import whisper

model = whisper.load_model("base")
result = model.transcribe("original_excerpt.wav")
with open('output.txt', 'w') as f:
    f.write(result["text"])