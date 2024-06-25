from flask import Flask, request, jsonify
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename
import torch
import os
import psycopg2

app = Flask(__name__)

# Initialize Whisper model and processor
model_name = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)

# PostgreSQL database connection details
dbname = "tahadb"
user = "postgres"
password = "root"
host = "localhost"
port = "5432"

# Establish PostgreSQL connection
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# Define directory paths
UPLOAD_DIRECTORY = os.path.join(os.path.dirname(__file__), 'uploads')
AUDIO_DIRECTORY = os.path.join(os.path.dirname(__file__), 'audio')
CONTENT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'content')

# Ensure directories exist
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
os.makedirs(AUDIO_DIRECTORY, exist_ok=True)
os.makedirs(CONTENT_DIRECTORY, exist_ok=True)

@app.route('/upload-video', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    video_path = os.path.join(UPLOAD_DIRECTORY, filename)

    # Save the video file locally
    file.save(video_path)

    try:
        # Load the video
        video = VideoFileClip(video_path)

        # Extract audio
        audio = video.audio
        audio_path = os.path.join(AUDIO_DIRECTORY, 'audio.mp3')

        # Write audio file
        audio.write_audiofile(audio_path)

        print(f'Audio file saved at {audio_path}')

        # Transcribe audio using Whisper
        speech_array, _ = processor.audio_to_array(audio_path)
        inputs = processor(speech_array, return_tensors="pt", sampling_rate=16000)
        with torch.no_grad():
            predicted_ids = model.generate(inputs.input_features, max_new_tokens=256)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

        # Store video metadata in PostgreSQL
        cur.execute("INSERT INTO videos (filename, transcription) VALUES (%s, %s)", (filename, transcription))
        conn.commit()

        # Example: Save processed content
        # For demonstration, let's assume we save a text file with transcription in content directory
        content_file_path = os.path.join(CONTENT_DIRECTORY, f'{filename}.txt')
        with open(content_file_path, 'w') as f:
            f.write(transcription)
        print(f'Processed content saved at {content_file_path}')

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Clean up local files
        if os.path.exists(video_path):
            os.remove(video_path)
        if os.path.exists(audio_path):
            os.remove(audio_path)

    return jsonify({'filename': filename, 'transcription': transcription})

if __name__ == '__main__':
    app.run(debug=True)
