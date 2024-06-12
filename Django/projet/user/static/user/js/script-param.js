$(document).ready(function() {
    var button = $('#change-theme');
    var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

    if (storedTheme) {
        document.documentElement.setAttribute('data-theme', storedTheme);
        updateButton(storedTheme);
    }

    if (button) {
        button.click(function() {
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
        var icon = button.find('i');

        if (theme === "dark") {
            icon.removeClass('fa-moon');
            icon.addClass('fa-sun');
            button.text(' Mode clair');
        } else {
            icon.removeClass('fa-sun');
            icon.addClass('fa-moon');
            button.text(' Mode sombre');
        }

        button.prepend(icon);
    }
});