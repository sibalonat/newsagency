function toggleRoles() {
    const isEditor = document.getElementById('is_editor').innerText === 'True';
    const isReader = document.getElementById('is_reader').innerText === 'True';

    document.getElementById('is_editor').innerText = !isEditor;
    document.getElementById('is_reader').innerText = !isReader;

    document.getElementById('toggle-form').submit();
}