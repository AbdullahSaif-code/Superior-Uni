from flask import Flask, render_template, request, jsonify
import requests
import os
from urllib.parse import quote

app = Flask(__name__)

OMDB_API_KEY = os.environ.get('OMDB_API_KEY', '11dc5e9b')
OMDB_BASE_URL = 'http://www.omdbapi.com/'

STREAMING_SITES = {
    'aboutmovies': 'https://aboutmovies.info',
    'watchmovies': 'https://www.watch-movies.com.pk'
}

POPULAR_MOVIE_IDS = [
    'tt0111161',  # The Shawshank Redemption
    'tt0068646',  # The Godfather
    'tt0468569',  # The Dark Knight
    'tt0071562',  # The Godfather Part II
    'tt0050083',  # 12 Angry Men
    'tt0108052',  # Schindler's List
    'tt0167260',  # The Lord of the Rings: The Return of the King
    'tt0110912',  # Pulp Fiction
    'tt0060196',  # The Good, the Bad and the Ugly
    'tt0137523',  # Fight Club
]


@app.route('/')
def home():
    """Home page showing top 10 popular movies"""
    return render_template('index.html')


@app.route('/api/movies/top50')
def get_top_movies():
    """Fetch top 10 popular movies from OMDb"""
    try:
        formatted_movies = []
        
        for imdb_id in POPULAR_MOVIE_IDS:
            response = requests.get(
                OMDB_BASE_URL,
                params={
                    'apikey': OMDB_API_KEY,
                    'i': imdb_id,
                    'plot': 'short'
                }
            )
            
            if response.status_code == 200:
                movie = response.json()
                if movie.get('Response') == 'True':
                    formatted_movies.append({
                        'id': movie.get('imdbID'),
                        'imdb_id': movie.get('imdbID'),
                        'title': movie.get('Title'),
                        'overview': movie.get('Plot'),
                        'poster_path': movie.get('Poster') if movie.get('Poster') != 'N/A' else None,
                        'backdrop_path': movie.get('Poster') if movie.get('Poster') != 'N/A' else None,
                        'release_date': movie.get('Year'),
                        'vote_average': float(movie.get('imdbRating', 0)) if movie.get('imdbRating') != 'N/A' else 0,
                        'popularity': float(movie.get('imdbVotes', '0').replace(',', '')) if movie.get('imdbVotes') != 'N/A' else 0
                    })
        
        return jsonify({'movies': formatted_movies, 'total': len(formatted_movies)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/movies/search')
def search_movies():
    """Search movies by query"""
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    try:
        response = requests.get(
            OMDB_BASE_URL,
            params={
                'apikey': OMDB_API_KEY,
                's': query,
                'type': 'movie'
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('Response') == 'False':
                return jsonify({'movies': [], 'total': 0})
            
            movies = data.get('Search', [])
            formatted_movies = []
            
            for movie in movies[:10]:
                formatted_movies.append({
                    'id': movie.get('imdbID'),
                    'imdb_id': movie.get('imdbID'),
                    'title': movie.get('Title'),
                    'overview': f"{movie.get('Title')} ({movie.get('Year')})",
                    'poster_path': movie.get('Poster') if movie.get('Poster') != 'N/A' else None,
                    'backdrop_path': movie.get('Poster') if movie.get('Poster') != 'N/A' else None,
                    'release_date': movie.get('Year'),
                    'vote_average': 0,
                    'popularity': 0
                })
            
            return jsonify({'movies': formatted_movies, 'total': len(formatted_movies)})
        else:
            return jsonify({'error': 'Failed to search movies'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/movie/<movie_id>')
def get_movie_details(movie_id):
    """Get detailed information about a specific movie by IMDb ID"""
    try:
        response = requests.get(
            OMDB_BASE_URL,
            params={
                'apikey': OMDB_API_KEY,
                'i': movie_id,
                'plot': 'full'
            }
        )
        
        if response.status_code == 200:
            movie = response.json()
            
            if movie.get('Response') == 'False':
                return jsonify({'error': 'Movie not found'}), 404
            
            genres = []
            if movie.get('Genre') and movie.get('Genre') != 'N/A':
                genre_list = movie.get('Genre').split(', ')
                genres = [{'name': g} for g in genre_list]
            
            runtime = movie.get('Runtime', 'N/A')
            if runtime and runtime != 'N/A':
                runtime = runtime.replace(' min', '')
            
            formatted_movie = {
                'id': movie.get('imdbID'),
                'imdb_id': movie.get('imdbID'),
                'title': movie.get('Title'),
                'overview': movie.get('Plot'),
                'poster_path': movie.get('Poster') if movie.get('Poster') != 'N/A' else None,
                'backdrop_path': movie.get('Poster') if movie.get('Poster') != 'N/A' else None,
                'release_date': movie.get('Year'),
                'vote_average': float(movie.get('imdbRating', 0)) if movie.get('imdbRating') != 'N/A' else 0,
                'runtime': runtime,
                'genres': genres,
                'tagline': movie.get('Awards', ''),
                'director': movie.get('Director'),
                'actors': movie.get('Actors'),
                'rated': movie.get('Rated')
            }
            
            return jsonify(formatted_movie)
        else:
            return jsonify({'error': 'Movie not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/info/<movie_id>')
def movie_info(movie_id):
    """Movie info page - display only, no video"""
    return render_template('info.html', movie_id=movie_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
