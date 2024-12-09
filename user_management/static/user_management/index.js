function toggleRoles() {
    const isEditor = document.getElementById('is_editor').innerText === 'True';
    const isReader = document.getElementById('is_reader').innerText === 'True';

    document.getElementById('is_editor').innerText = !isEditor;
    document.getElementById('is_reader').innerText = !isReader;

    document.getElementById('toggle-form').submit();
}

function getUserArticles(userId) {
    const url = userArticlesUrl.replace('0', userId).replace('type', 'json');     
    fetch(url)
        .then(response => response.json())
        .then(articles => {
            const container = document.getElementById('articles-container');
            container.innerHTML = '<h3>Articles</h3>';
            if (articles.length > 0) {
                const list = document.createElement('ul');
                list.classList.add('list-group-item');
                articles.forEach(article => {
                    const listItem = document.createElement('li');
                    listItem.classList.add('list-group-item');

                    const link = document.createElement('a');
                    link.href = `/article/${article.id}/`;
                    link.classList.add('text-decoration-none', 'text-dark');

                    const titleParagraph = document.createElement('p');
                    titleParagraph.classList.add('mb-0');
                    titleParagraph.textContent = article.title;
                    link.appendChild(titleParagraph);

                    const dateParagraph = document.createElement('p');
                    dateParagraph.textContent = `Created at: ${article.created_at}`;
                    dateParagraph.classList.add('text-sm', 'text-muted', 'mb-0');
                    link.appendChild(dateParagraph);
                    
                    listItem.appendChild(link);
                    list.appendChild(listItem);
                });
                container.appendChild(list);
            } else {
                container.innerHTML += '<p>No articles found.</p>';
            }
        });
}