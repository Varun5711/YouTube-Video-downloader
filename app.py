from flask import Flask, request, jsonify
from flask_cors import CORS
from pytube import YouTube
import pytube
import os

app = Flask(__name__)

CORS(app, resources={r"/download": {"origins": "*"}})

download_dir = "downloads"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

@app.route('/')
def home():
    return "YouTube Downloader Backend is Running!"

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.json
        if not data or 'url' not in data:
            raise KeyError("No URL provided")
        
        video_url = data['url']
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        file_name = f"{yt.title}.mp4".replace('/', '_')
        download_path = os.path.join(download_dir, file_name)
        stream.download(output_path=download_dir, filename=file_name)

        return jsonify({"message": "Download successful!", "filename": file_name, "path": download_path})

    except KeyError:
        return jsonify({"error": "No URL provided"}), 400
    except pytube.exceptions.PytubeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
