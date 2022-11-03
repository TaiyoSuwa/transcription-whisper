import whisper
import time
import sys

start = time.time()
args = sys.argv

model = whisper.load_model("medium")
audio = args[1]
result = model.transcribe(audio, language="ja", verbose=True)

f = open("transcription.txt", mode='w')
f.write(result["text"])
f.close()

print("Need Time")
need_time = int(time.time() - start)
hours = need_time // 3600
need_time %= 3600
minutes = need_time // 60
need_time %= 60
print(str(hours) + "h " + str(minutes) + "min " + str(need_time) + "sec")
