// Load top movies on page load
window.addEventListener('DOMContentLoaded', () => {
    loadTopMovies();
});

function handleSearchKeyPress(event) {
    if (event.key === 'Enter') {
        searchMovies();
    }
}

function showLoading() {
    document.getElementById('loadingSpinner').classList.remove('hidden');
    document.getElementById('moviesGrid').classList.add('hidden');
    document.getElementById('noResults').classList.add('hidden');
    document.getElementById('errorMessage').classList.add('hidden');
}

function hideLoading() {
    document.getElementById('loadingSpinner').classList.add('hidden');
    document.getElementById('moviesGrid').classList.remove('hidden');
}

function showError(message) {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.querySelector('p').textContent = message;
    errorDiv.classList.remove('hidden');
    hideLoading();
}

function loadTopMovies() {
    showLoading();
    document.getElementById('sectionTitle').innerHTML = '<i class="fas fa-fire text-orange-500 mr-3"></i>Top 10 Popular Movies';
    document.getElementById('searchInput').value = '';

    fetch('/api/movies/top50')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                showError(data.error);
                return;
            }
            displayMovies(data.movies);
        })
        .catch(error => {
            showError('Failed to load movies. Please try again.');
            console.error('Error:', error);
        });
}

function searchMovies() {
    const query = document.getElementById('searchInput').value.trim();
    
    if (!query) {
        showError('Please enter a search query');
        return;
    }

    showLoading();
    document.getElementById('sectionTitle').innerHTML = `<i class="fas fa-search text-purple-500 mr-3"></i>Search Results for "${query}"`;

    fetch(`/api/movies/search?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                showError(data.error);
                return;
            }
            displayMovies(data.movies);
        })
        .catch(error => {
            showError('Failed to search movies. Please try again.');
            console.error('Error:', error);
        });
}

function displayMovies(movies) {
    hideLoading();
    const grid = document.getElementById('moviesGrid');
    const noResults = document.getElementById('noResults');

    if (!movies || movies.length === 0) {
        grid.innerHTML = '';
        noResults.classList.remove('hidden');
        return;
    }

    noResults.classList.add('hidden');
    grid.innerHTML = movies.map(movie => createMovieCard(movie)).join('');
}

function createMovieCard(movie) {
    const posterUrl = movie.poster_path || 'https://via.placeholder.com/500x750?text=No+Poster';
    const rating = movie.vote_average ? movie.vote_average.toFixed(1) : 'N/A';
    const year = movie.release_date || 'N/A';

    return `
        <div class="movie-card bg-gray-800 rounded-lg overflow-hidden shadow-lg cursor-pointer" onclick="openMovie('${movie.id}')">
            <div class="relative">
                <img src="${posterUrl}" alt="${movie.title}" class="w-full h-80 object-cover">
                <div class="absolute top-2 right-2 bg-yellow-500 text-gray-900 px-2 py-1 rounded-full font-bold text-sm flex items-center">
                    <i class="fas fa-star mr-1"></i>${rating}
                </div>
            </div>
            <div class="p-4">
                <h3 class="font-bold text-lg mb-2 line-clamp-2" title="${movie.title}">${movie.title}</h3>
                <div class="flex items-center justify-between text-sm text-gray-400">
                    <span><i class="fas fa-calendar mr-1"></i>${year}</span>
                    <button class="bg-purple-600 hover:bg-purple-700 px-3 py-1 rounded text-white transition">
                        <i class="fas fa-info-circle mr-1"></i>View Info
                    </button>
                </div>
            </div>
        </div>
    `;
}

function openMovie(movieId) {
    window.location.href = `/info/${movieId}`;
}
