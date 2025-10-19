#!/usr/bin/env python3
"""Test script to verify OMDb API is working"""

import requests

OMDB_API_KEY = '11dc5e9b'
OMDB_BASE_URL = 'http://www.omdbapi.com/'

print("Testing OMDb API...\n")

# Test 1: Get a specific movie
print("Test 1: Fetching 'The Shawshank Redemption' (tt0111161)")
response = requests.get(
    OMDB_BASE_URL,
    params={
        'apikey': OMDB_API_KEY,
        'i': 'tt0111161',
        'plot': 'full'
    }
)

if response.status_code == 200:
    data = response.json()
    if data.get('Response') == 'True':
        print(f"✅ Success!")
        print(f"   Title: {data.get('Title')}")
        print(f"   Year: {data.get('Year')}")
        print(f"   Rating: {data.get('imdbRating')}")
        print(f"   Plot: {data.get('Plot')[:100]}...")
    else:
        print(f"❌ Error: {data.get('Error')}")
else:
    print(f"❌ HTTP Error: {response.status_code}")

print("\n" + "="*50 + "\n")

# Test 2: Search for movies
print("Test 2: Searching for 'Matrix'")
response = requests.get(
    OMDB_BASE_URL,
    params={
        'apikey': OMDB_API_KEY,
        's': 'Matrix',
        'type': 'movie'
    }
)

if response.status_code == 200:
    data = response.json()
    if data.get('Response') == 'True':
        movies = data.get('Search', [])
        print(f"✅ Found {len(movies)} movies")
        for i, movie in enumerate(movies[:5], 1):
            print(f"   {i}. {movie.get('Title')} ({movie.get('Year')}) - {movie.get('imdbID')}")
    else:
        print(f"❌ Error: {data.get('Error')}")
else:
    print(f"❌ HTTP Error: {response.status_code}")

print("\n" + "="*50 + "\n")
print("API tests complete!")
