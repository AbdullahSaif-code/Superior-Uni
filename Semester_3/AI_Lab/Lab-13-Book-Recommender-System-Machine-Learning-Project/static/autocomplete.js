document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('bookInput');
    const suggestionsBox = document.getElementById('suggestions');

    input.addEventListener('input', function() {
        const query = input.value;
        if (query.length < 2) {
            suggestionsBox.innerHTML = '';
            return;
        }
        fetch(`/autocomplete?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(suggestions => {
                suggestionsBox.innerHTML = '';
                suggestions.forEach(suggestion => {
                    const item = document.createElement('a');
                    item.classList.add('list-group-item', 'list-group-item-action');
                    item.textContent = suggestion;
                    item.onclick = function() {
                        input.value = suggestion;
                        suggestionsBox.innerHTML = '';
                    };
                    suggestionsBox.appendChild(item);
                });
            });
    });

    document.addEventListener('click', function(e) {
        if (e.target !== input) {
            suggestionsBox.innerHTML = '';
        }
    });
});