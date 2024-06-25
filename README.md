# Video Management System for a task

## Overview
This project is a comprehensive video management system designed for an online education platform. It includes functionalities for video uploading, audio extraction, transcription, and metadata storage. The system utilizes Flask for the backend, PostgreSQL for database management, Whisper for transcription, MoviePy for video processing, and Streamlit for the frontend interface.

## Directory Structure
```
FLASK-API-MAIN
 ┣ backend
 ┃  ┣ audio
 ┃  ┃  ┗ audio.mp3
 ┃  ┣ models
 ┃  ┃  ┣ database.py
 ┃  ┃  ┗ video.py
 ┃  ┣ utils
 ┃  ┃  ┣ audio_extraction.py
 ┃  ┃  ┗ transcription.py
 ┃  ┣ app.py
 ┃  ┣ config.py
 ┃  ┗ requirements.txt
 ┣ db
 ┃  ┣ init_db.py
 ┃  ┗ schema.sql
 ┣ frontend
 ┃  ┣ requirements.txt
 ┃  ┗ streamlit_app.py
 ┗ .gitignore
```

## Setup Instructions

### Backend Setup

1. **Clone the Repository**
   ```sh
   git clone <repository-link>
   cd FLASK-API-MAIN
   ```

2. **Create and Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Backend Dependencies**
   ```sh
   cd backend
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**
   - Ensure PostgreSQL is installed and running.
   - Create a new database named `tahadb`.
   - Update the database connection details in `config.py`.

5. **Initialize the Database**
   ```sh
   python init_db.py
   ```

6. **Run the Flask Application**
   ```sh
   python app.py
   ```

### Frontend Setup

1. **Install Frontend Dependencies**
   ```sh
   cd ../frontend
   pip install -r requirements.txt
   ```

2. **Run the Streamlit Application**
   ```sh
   streamlit run streamlit_app.py
   ```

## Usage

1. **Upload a Video**
   - Navigate to the Streamlit application.
   - Upload a video file (supported formats: mp4, avi, mov).
   - Enter tags for the video.
   - Click "Upload and Transcribe" to upload the video and get the transcription.

2. **View Transcription**
   - The transcription of the uploaded video will be displayed on the Streamlit application.

## Libraries and Tools Used

- **Flask**: Web framework for the backend API.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **psycopg2**: PostgreSQL database adapter.
- **ffmpeg-python**: Library for audio extraction from video files.
- **google-cloud-speech**: Google Cloud's Speech-to-Text API for audio transcription.
- **transformers (Whisper)**: Whisper model for transcription.
- **MoviePy**: Video processing library.
- **Streamlit**: Framework for building the frontend interface.
- **Requests**: HTTP library for making requests from the Streamlit app to the Flask API.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or inquiries, please contact Taha at [your-email@example.com].
