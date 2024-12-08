function toggleRoles() {
    const isEditor = document.getElementById('is_editor').innerText === 'True';
    const isReader = document.getElementById('is_reader').innerText === 'True';

    document.getElementById('is_editor').innerText = !isEditor;
    document.getElementById('is_reader').innerText = !isReader;

    document.getElementById('toggle-form').submit();
}

function getUserArticles(userId) {
    const userId = document.getElementById('user_id').innerText;
    const url = "{% url 'user_articles' 0 %}".replace('0', userId);
    fetch(`/user/${userId}/articles/`)
        .then(response => response.json())
        .then(articles => {
            const container = document.getElementById('articles-container');
            container.innerHTML = '<h3>Articles</h3>';
            if (articles.length > 0) {
                const list = document.createElement('ul');
                articles.forEach(article => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${article.title} (Created at: ${article.created_at})`;
                    list.appendChild(listItem);
                });
                container.appendChild(list);
            } else {
                container.innerHTML += '<p>No articles found.</p>';
            }
        });
}
// document.getElementById('username').addEventListener('click', function() {
//     const userId = {{ user.id }};
//     fetch(`/user/${userId}/articles/`)
//         .then(response => response.json())
//         .then(articles => {
//             const container = document.getElementById('articles-container');
//             container.innerHTML = '<h3>Articles</h3>';
//             if (articles.length > 0) {
//                 const list = document.createElement('ul');
//                 articles.forEach(article => {
//                     const listItem = document.createElement('li');
//                     listItem.textContent = `${article.title} (Created at: ${article.created_at})`;
//                     list.appendChild(listItem);
//                 });
//                 container.appendChild(list);
//             } else {
//                 container.innerHTML += '<p>No articles found.</p>';
//             }
//         });
// });