// JavaScript code for the Music Recommendation App

// Example data for recommendations and genres
const recommendations = [
    { title: "Song 1", artist: "Artist 1" },
    { title: "Song 2", artist: "Artist 2" },
    { title: "Song 3", artist: "Artist 3" }
  ];
  
  const genres = [
    "Pop", "Rock", "Hip Hop", "Electronic", "Jazz"
  ];
  
  // Function to generate recommendation cards dynamically
  function generateRecommendationCards() {
    const recommendationList = document.querySelector('.recommendation-list');
  
    recommendations.forEach(recommendation => {
      const card = document.createElement('div');
      card.classList.add('recommendation-card');
      card.innerHTML = `
        <h3>${recommendation.title}</h3>
        <p>${recommendation.artist}</p>
      `;
      recommendationList.appendChild(card);
    });
  }
  
  // Function to generate genre list dynamically
  function generateGenreList() {
    const genreList = document.querySelector('.genre-list');
  
    genres.forEach(genre => {
      const listItem = document.createElement('li');
      listItem.textContent = genre;
      genreList.appendChild(listItem);
    });
  }
  
  // Call the functions to generate the dynamic content
  generateRecommendationCards();
  generateGenreList();
  