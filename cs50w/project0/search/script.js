const form = document.getElementById('advanced-search-form');

form.addEventListener('submit', function(e) {
  e.preventDefault();

  const allWords = form.allWords.value.trim();
  const exactPhrase = form.exactPhrase.value.trim();
  const anyWords = form.anyWords.value.trim();
  const noneWords = form.noneWords.value.trim();

  let query = '';

  if (allWords) query += allWords + ' ';
  if (exactPhrase) query += `"${exactPhrase}" `;
  if (anyWords) query += anyWords.split(/\s+/).join(' OR ') + ' ';
  if (noneWords) query += noneWords.split(/\s+/).map(word => `-${word}`).join(' ') + ' ';

  query = query.trim();

  if (!query) {
    alert('Please enter at least one search term.');
    return;
  }

  const url = 'https://www.google.com/search?q=' + encodeURIComponent(query);
  window.location.href = url;
});
