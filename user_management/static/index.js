document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.onsubmit = function(event) {
        event.preventDefault();
        const request = new XMLHttpRequest();
        request.open('POST', form.action);
        request.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
        request.onload = function() {
            if (request.status === 200) {
                const comment = JSON.parse(request.responseText);
                const li = document.createElement('li');
                li.innerHTML = `${comment.content} - ${comment.author}`;
                document.querySelector('ul').append(li);
                form.reset();
            }
        };
        const data = new FormData(form);
        request.send(data);
    };
});