from gtts import gTTS
import subprocess

text = "막혀 있습니다 우회합니다."
filename = "say.mp3"

tts = gTTS(text, lang='ko') 
tts.save(filename)

with subprocess.Popen(['play', 'say.mp3']) as p: #Popen([리눅스 명령어, filename])
    p.wait()
