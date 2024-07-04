from fastapi import FastAPI, HTTPException
import httpx
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv('Client_ID')
CLIENT_SECRET = os.getenv('Client_secret')

async def get_access_token():
    auth_url = "https://accounts.spotify.com/api/token"
    async with httpx.AsyncClient() as client:
        auth_response = await client.post(auth_url, data={
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })
        if auth_response.status_code == 200:
            auth_response_data = auth_response.json()
            return auth_response_data['access_token']
        else:
            raise HTTPException(status_code=auth_response.status_code, detail="Error fetching access token")

async def fetch_spotify_data(url, headers):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from Spotify")

async def get_artist_genres(artist_id, headers):
    artist_data = await fetch_spotify_data(f'https://api.spotify.com/v1/artists/{artist_id}', headers)
    return artist_data.get('genres', [])

async def get_tracks(playlist_id):
    try:
        access_token = await get_access_token()
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    headers = {'Authorization': f'Bearer {access_token}'}
    tracks_data = await fetch_spotify_data(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers)
    
    tracks = []
    for item in tracks_data['items']:
        track = item['track']
        artist_id = track['artists'][0]['id']
        genres = await get_artist_genres(artist_id, headers)
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'preview_url': track['preview_url'],
            'genres': genres
        })
    return tracks

@app.get("/top-tracks")
async def get_top_tracks():
    return await get_tracks('37i9dQZEVXbMDoHDwVN2tF')

@app.get("/indonesia-top-tracks")
async def get_indonesia_top_tracks():
    return await get_tracks('37i9dQZEVXbObFQZ3JLcXt')

@app.get("/us-top-tracks")
async def get_us_top_tracks():
    return await get_tracks('37i9dQZEVXbLRQDuF5jeBp')

@app.get("/pop-rising-tracks")
async def get_pop_rising_tracks():
    return await get_tracks('37i9dQZF1DWUa8ZRTfalHk')

@app.get("/popular-indonesia-artist-tracks")
async def get_popular_indonesia_artist_tracks():
    return await get_tracks('37i9dQZF1DWZxM58TRkuqg')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)