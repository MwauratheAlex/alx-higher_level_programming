$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (data) => {
      data.results.map((movie) => $('#list_movies').append(`<li>${movie.title}</li>`));
    }
  });
});
