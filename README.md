# Spotify Data Fetcher API

This API uses **FastAPI** to fetch data from Spotify, including top tracks, trending tracks, and popular artist tracks in Indonesia.

## Deployment

[link] (https://spotify-data-fetcher-api.vercel.app/)

## Features

- **Top Tracks**: Fetches the top tracks from various playlists.
- **Indonesia Top Tracks**: Fetches the top tracks in Indonesia.
- **US Top Tracks**: Fetches the top tracks in the United States.
- **Pop Rising Tracks**: Fetches the trending tracks.
- **Popular Indonesia Artist Tracks**: Fetches tracks from popular artists in Indonesia.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- Spotify Developer Account

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/username/repo-name.git
    cd repo-name
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your Spotify `Client_ID` and `Client_secret`:

    ```env
    Client_ID=your_spotify_client_id
    Client_secret=your_spotify_client_secret
    ```

## Running the Application

Run the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
