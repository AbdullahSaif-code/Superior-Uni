const movieId = window.MOVIE_ID;
let movieData = null;
let streamingData = null;

// Load movie data on page load
window.addEventListener('DOMContentLoaded', () => {
    loadMovieData();
});

async function loadMovieData() {
    try {
        // Fetch movie details
        const movieResponse = await fetch(`/api/movie/${movieId}`);
        movieData = await movieResponse.json();

        if (movieData.error) {
            alert('Failed to load movie details');
            window.location.href = '/';
            return;
        }

        // Fetch streaming URLs
        const streamResponse = await fetch(`/api/movie/${movieId}/stream-url`);
        streamingData = await streamResponse.json();

        displayMovieInfo();
        displayStreamingOptions();

        document.getElementById('loadingSpinner').classList.add('hidden');
        document.getElementById('playerSection').classList.remove('hidden');
    } catch (error) {
        console.error('Error loading movie data:', error);
        alert('Failed to load movie. Please try again.');
        window.location.href = '/';
    }
}

function displayMovieInfo() {
    document.getElementById('movieTitle').textContent = movieData.title;
    document.getElementById('moviePoster').src = movieData.poster_path || 'https://via.placeholder.com/500x750?text=No+Poster';
    document.getElementById('moviePoster').alt = movieData.title;
    
    const year = movieData.release_date || 'N/A';
    document.getElementById('movieYear').innerHTML = `<i class="fas fa-calendar mr-2"></i>${year}`;
    
    const rating = movieData.vote_average ? movieData.vote_average.toFixed(1) : 'N/A';
    document.getElementById('movieRating').innerHTML = `<i class="fas fa-star mr-2"></i>${rating}`;
    
    const runtime = movieData.runtime ? `${movieData.runtime} min` : 'N/A';
    document.getElementById('movieRuntime').innerHTML = `<i class="fas fa-clock mr-2"></i>${runtime}`;
    
    document.getElementById('movieTagline').textContent = movieData.tagline || '';
    document.getElementById('movieOverview').textContent = movieData.overview || 'No overview available.';
    
    const genresContainer = document.getElementById('movieGenres');
    if (movieData.genres && movieData.genres.length > 0) {
        genresContainer.innerHTML = movieData.genres.map(genre => 
            `<span class="bg-purple-600 px-3 py-1 rounded-full text-sm">${genre.name}</span>`
        ).join('');
    }

    document.title = `Watch ${movieData.title} - Movie Stream`;
}

function displayStreamingOptions() {
    const optionsContainer = document.getElementById('streamingOptions');
    const manualLinksContainer = document.getElementById('manualLinks');

    if (!streamingData.streaming_urls || streamingData.streaming_urls.length === 0) {
        optionsContainer.innerHTML = '<p class="text-gray-400">No streaming sources available. Try the custom embed option below.</p>';
        return;
    }

    // Display streaming buttons with quality badges
    optionsContainer.innerHTML = streamingData.streaming_urls.map((source, index) => {
        const qualityBadge = source.quality ? 
            `<span class="ml-2 bg-green-500 text-white text-xs px-2 py-1 rounded">${source.quality}</span>` : '';
        
        return `
            <button 
                onclick="loadStream('${source.iframe_url}')" 
                class="streaming-option w-full bg-purple-600 hover:bg-purple-700 px-4 py-3 rounded-lg text-left flex items-center justify-between transition"
            >
                <span class="flex items-center">
                    <i class="fas fa-play-circle mr-3 text-xl"></i>
                    <span class="font-semibold">${source.site}</span>
                    ${qualityBadge}
                </span>
                <i class="fas fa-chevron-right"></i>
            </button>
        `;
    }).join('');

    // Display manual links
    manualLinksContainer.innerHTML = streamingData.streaming_urls.map(source => {
        const linkText = source.url.length > 80 ? source.url.substring(0, 80) + '...' : source.url;
        return `
            <a 
                href="${source.url}" 
                target="_blank" 
                class="block text-blue-400 hover:text-blue-300 transition mb-2"
            >
                <i class="fas fa-external-link-alt mr-2"></i>${source.site}<br>
                <span class="text-xs text-gray-400 ml-6">${linkText}</span>
            </a>
        `;
    }).join('');
}

function loadStream(videoUrl) {
    const videoPlayer = document.getElementById('videoPlayer');
    const videoIframe = document.getElementById('videoIframe');

    videoIframe.src = videoUrl;
    videoPlayer.classList.remove('hidden');
    
    // Scroll to video player
    videoPlayer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function loadCustomEmbed() {
    const customUrl = document.getElementById('customEmbedUrl').value.trim();
    
    if (!customUrl) {
        alert('Please enter a valid URL');
        return;
    }

    if (!customUrl.startsWith('http://') && !customUrl.startsWith('https://')) {
        alert('URL must start with http:// or https://');
        return;
    }

    loadStream(customUrl);
}
