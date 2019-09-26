$.get('https://swapi.co/api/films/?format=json', function (data) {
  const res = data.results;
  for (const film of res) {
    const item = $('<li></li>').text(film.title);
    $('UL#list_movies').append(item);
  }
});
