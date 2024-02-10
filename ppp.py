import os
import speech_recognition as sr
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, TextClip

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_sphinx(audio)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))
        return ""

def create_srt(video_path, output_srt_path):
    video_clip = VideoFileClip(video_path)

    # Create an empty SRT file
    with open(output_srt_path, 'w') as srt_file:
        pass

    # Split the audio from the video
    video = mp.VideoFileClip(video_path) 

    audio_file = video.audio 
    audio_file.write_audiofile("temp_audio.wav") 

    # Transcribe audio to text
    subtitles_text = transcribe_audio("temp_audio.wav")

    # Cleanup temporary audio file
    #os.remove("temp_audio.wav")

    # Write subtitles to the SRT file
    with open(output_srt_path, 'a') as srt_file:
        srt_file.write("1\n")  # Subtitle number
        srt_file.write("00:00:00,000 --> {end_time},000\n".format(end_time=str(video_clip.duration*1000)))  # Time duration
        srt_file.write(subtitles_text + "\n\n")

if __name__ == "__main__":
    video_path = "abc.mp4"  # Replace with the path to your video file
    output_srt_path = "ijk.srt"  # Replace with the desired output SRT file path

    # Create the SRT file
    create_srt(video_path, output_srt_path)
