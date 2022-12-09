import whisper
import re

def split_lines(text):
    lines = text.split('\n')
    regex = re.compile(r'.{1,80}(?:\s+|$)')
    return '\n'.join(s.rstrip() for line in lines for s in regex.findall(line))

model = whisper.load_model("base")
result = model.transcribe("original_excerpt.wav")
with open('output.txt', 'w') as f:
    f.write(split_lines(result["text"]))