import os
import pydub

# Set settings
source = "original.mp3"

sound = pydub.AudioSegment.from_mp3(source) # load source
sound = sound.set_channels(1) # mono
sound = sound.set_frame_rate(16000) # 16000Hz

# We could also chose here .mp3
# For the sake of comparison with Vosk, I convert it to .wav
# Extract the first 60 seconds
excrept = sound[0:60000]
output_path = os.path.splitext(source)[0]+"_excerpt.wav"
excrept.export(output_path, format="wav")