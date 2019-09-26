$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  const char = data.name;
  $('DIV#character').text(char);
});
