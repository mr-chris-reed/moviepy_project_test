# 1. Import required libraries
from gtts import gTTS # Google's text to speech library
from moviepy.editor import * # MoviePy library to manipulate video
import speech_recognition as sr # Google's speech to text library

# 2. Bring video into moviepy
video = VideoFileClip("IMG_1115.MOV")

# 2.1 Get size of video clip and print it out
video_size = video.size
print(video_size[0])

# 3. Extract audio and write it out
audio = AudioFileClip("IMG_1115.MOV")
audio.write_audiofile("audio_out.wav")

# 4. Convert audio to text
r = sr.Recognizer()
text = ""
with sr.AudioFile("audio_out.wav") as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# 5. Convert text to generic speech
generic_speech = gTTS(text=text, lang='es', slow=True)
generic_speech.save("generic_audio_out.mp3")

# 6. Paste text on top of video
text_clip = TextClip(text, color='white', fontsize=75, size=((600,0)), method='caption')
text_clip = text_clip.set_position((video_size[0] / 2, 450)).set_duration(5)
video = CompositeVideoClip([video, text_clip])

# 7. Resize and edit video
video = video.resize((300,400))

# Write video out
video.write_videofile("output.mp4")
video.close()

print(text)
