document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.getElementById('change-theme');
    const icon = button.querySelector('i');

    button.addEventListener('click', function() {
        if (icon.classList.contains('fa-moon')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
            button.textContent = ' Mode clair';
            button.prepend(icon);
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
            button.textContent = ' Mode sombre';
            button.prepend(icon);
        }
    });
});