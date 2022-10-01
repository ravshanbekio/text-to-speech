from gtts import gTTS
from playsound import playsound

audio_file = 'speech-fast.mp3'

language = 'en'

speech = gTTS(text='Hello!',lang=language, slow=True)

speech.save(audio_file)
playsound(audio_file)