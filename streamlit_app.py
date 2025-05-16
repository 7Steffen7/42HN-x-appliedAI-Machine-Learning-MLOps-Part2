import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title('Spotify Track Popularity')


danceability = st.slider('Danceability', 0.0, 1.0, 0.726)
energy = st.slider('Energy', 0.0, 1.0, 0.698)
loudness = st.slider('Loudness', -60.0, 6.2, -4.087)
speechiness = st.slider('Speechiness', 0.0, 1.0, 0.0431)
acousticness = st.slider('Acousticness', 0.0, 1.0, 0.049)
instrumentalness = st.slider('Instrumentalness', 0.0, 1.0)
liveness = st.slider('Liveness', 0.0, 1.0, 0.309)
valence = st.slider('Valence', 0.0, 1.0, 0.867)
tempo = st.slider('Tempo', 0.0, 250.0, 143.994)
duration_ms = st.slider('Duration (ms)', 0, 6000500, 233478)
year = st.slider('Year', 2000, 2023, 2012)
key = st.slider('Key', 0, 11, 5)
mode = st.slider('Mode', 0, 1, 1)
time_signature = st.slider('Time Signature', 0, 5, 4)
genre = st.selectbox(
    'Genre',
    options = ['acoustic', 'afrobeat', 'alt-rock', 'ambient', 'black-metal',
       'blues', 'breakbeat', 'cantopop', 'chicago-house', 'chill',
       'classical', 'club', 'comedy', 'country', 'dance', 'dancehall',
       'death-metal', 'deep-house', 'detroit-techno', 'disco',
       'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic',
       'emo', 'folk', 'forro', 'french', 'funk', 'garage', 'german',
       'gospel', 'goth', 'grindcore', 'groove', 'guitar', 'hard-rock',
       'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'house',
       'indian', 'indie-pop', 'industrial', 'jazz', 'k-pop', 'metal',
       'metalcore', 'minimal-techno', 'new-age', 'opera', 'party',
       'piano', 'pop', 'pop-film', 'power-pop', 'progressive-house',
       'psych-rock', 'punk', 'punk-rock', 'rock', 'rock-n-roll',
       'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes',
       'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul',
       'spanish', 'swedish', 'tango', 'techno', 'trance', 'trip-hop'],
    index=14
)

if st.button('Predict'):
    input_data = {
        'danceability': danceability,
        'energy': energy,
        'loudness': loudness,
        'speechiness': speechiness,
        'acousticness': acousticness,
        'instrumentalness': instrumentalness,
        'liveness': liveness,
        'valence': valence,
        'tempo': tempo,
        'duration_ms': duration_ms,
        'year': year,
        'key': key,
        'mode': mode,
        'time_signature': time_signature,
        'genre': genre
    }
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        result = response.json()
        # st.success(f'Predicted Popularity: {result}')
        if result['prediction'][0] == 0:
            st.error('Song is a miss')
        else:
            st.success('Song is a hit')
    else:
        st.error('Prediction failed.')