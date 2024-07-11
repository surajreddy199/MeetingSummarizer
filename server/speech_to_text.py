from io import BytesIO
import shutil
import speech_recognition as sr
import os 
import sys
from bson import ObjectId
from pydub import AudioSegment
from pydub.silence import split_on_silence
from LLM_model import model_summarizer
    
def automatic_speech_recognition(filePath):
    try:
        
        audio = AudioSegment.from_file(filePath, format="mp3")

        # Export as WAV
        wav_file_path = os.path.splitext(filePath)[0] + '.wav'
        audio.export(wav_file_path, format="wav")

        recognizer = sr.Recognizer()
        # Use Google Web Speech API
        with sr.AudioFile(wav_file_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                print("Text:", text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        # format = open("output_format.txt",'r')
        # formatTxt = format.read()
        # prompt = formatTxt.replace("<<<CHUNK>>>",text)

        output = model_summarizer(text + " SUMMARIZE THE MEETING TRANSCRIPT IN 100 WORDS")
        print(output)
     
        return output
    except Exception as e:
        print(e)
        return "Error Occurred in ASR"