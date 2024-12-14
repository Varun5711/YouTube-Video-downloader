# YouTube Video Downloader

A simple YouTube video downloader built using Flask. This project allows users to download YouTube videos by providing a URL.

![Screenshot](screenshot.png)

## Features

- Download YouTube videos in the highest resolution available.
- User-friendly interface with a modern design.
- Cross-Origin Resource Sharing (CORS) enabled for flexibility.

## Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate  # On Windows
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

    Make sure your `requirements.txt` includes the following packages:

    ```text
    Flask
    flask-cors
    pytube
    ```

## Usage

1. **Run the Flask app:**

    ```sh
    python app.py
    ```

2. **Open your browser and navigate to:**

    ```
    http://localhost:8000
    ```

3. **Enter a YouTube video URL and click "Download" to start downloading the video.**

## Project Structure

```plaintext
your-repo-name/
│
├── app.py             # Main Flask application
├── requirements.txt   # List of required packages
├── templates/
│   └── index.html     # HTML file for the web interface
├── static/
│   └── style.css      # CSS file for styling
└── downloads/         # Directory where downloaded videos will be saved
