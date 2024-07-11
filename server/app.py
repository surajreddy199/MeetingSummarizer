from flask import Flask, jsonify, request
from speech_to_text import automatic_speech_recognition
from text_summarisation import text_summary
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def homepage():
    return "HELLO"

@app.route("/speechtotext", methods=['POST'])
def speechToText():
    print(request,request.files['file'].filename)
    
    # Create directory if it doesn't exist
    upload_dir = '/uploadedFiles/'
    os.makedirs(upload_dir, exist_ok=True)

    audio_file=request.files['file']
    temp_file_path = os.path.join(upload_dir, audio_file.filename)
    # Example temporary file path
    audio_file.save(temp_file_path)
    speechTranscript = automatic_speech_recognition(temp_file_path)
    response = jsonify(speechTranscript)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/textsummarisation", methods=['POST'])
def textSummarisation():
    data=request.files['file']
    data.save(secure_filename(data.filename))
    textSummary = text_summary(data.filename,"")
    # print(textSummary)
    response = jsonify(textSummary)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)