document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.getElementById('change-theme');

    var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    if (storedTheme)
        document.documentElement.setAttribute('data-theme', storedTheme)

    if (button) {
        const icon = button.querySelector('i');

        button.addEventListener('click', function() {
            var currentTheme = document.documentElement.getAttribute("data-theme");
            var targetTheme = "light";

            if (currentTheme === "light") {
                targetTheme = "dark";
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
                button.textContent = ' Mode clair';
            } else {
                targetTheme = "light";
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
                button.textContent = ' Mode sombre';
            }

            document.documentElement.setAttribute('data-theme', targetTheme)
            localStorage.setItem('theme', targetTheme);
            button.prepend(icon);
        });
    }
});