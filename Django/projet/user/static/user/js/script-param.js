window.addEventListener('pageshow', function() {
    var button = document.querySelector('#change-theme');
    var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

    if (storedTheme) {
        document.documentElement.setAttribute('data-theme', storedTheme);
        updateButton(storedTheme);
    }

    if (button) {
        button.addEventListener('click', function() {
            var currentTheme = document.documentElement.getAttribute("data-theme");
            var targetTheme = "light";

            if (currentTheme === "light") {
                targetTheme = "dark";
            }

            document.documentElement.setAttribute('data-theme', targetTheme);
            localStorage.setItem('theme', targetTheme);
            updateButton(targetTheme);
        });
    }

    function updateButton(theme) {
        var icon = button.querySelector('i');

        if (theme === "dark") {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
            button.textContent = ' Mode clair';
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
            button.textContent = ' Mode sombre';
        }

        button.prepend(icon);
    }
});