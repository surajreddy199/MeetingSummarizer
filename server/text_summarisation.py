# from bson import ObjectId

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
import google.generativeai as genai
from LLM_model import model_summarizer

def text_summary(fileName,transcript):
    try:

        file = open(fileName,'r')
        fileContent = file.read()

        format = open("output_format.txt",'r')
        formatTxt = format.read()

        prompt = formatTxt.replace("<<<CHUNK>>>", fileContent)
        # print(sentences)
        # prompt = input("Enter prompt: ")
        # words = input("Enter number of words to summarize in(default=100): ")
        # if prompt == "":
        #   prompt = "SUMMARIZE THE ABOVE MEETING TRANSCRIPT IN "
        # if words == "":
        #   words = "100"
        # print(prompt + words + " WORDS")
        response = model_summarizer(prompt)
        output = response.replace("*","")
        return output

    except Exception as e:
        print(e)
        return "Error Occurred in Summariser"
