window.addEventListener('load', function() {
    var button = document.querySelector('#change-theme');
    var storedTheme = sessionStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

    document.documentElement.setAttribute('data-theme', storedTheme);
    updateButton(storedTheme);

    if (button) {
        button.addEventListener('click', function() {
            var currentTheme = document.documentElement.getAttribute("data-theme");
            var targetTheme = "light";

            if (currentTheme === "light") {
                targetTheme = "dark";
            }

            document.documentElement.setAttribute('data-theme', targetTheme);
            sessionStorage.setItem('theme', targetTheme);
            updateButton(targetTheme);
        });
    }

    function updateButton(theme) {
        var button = document.querySelector('#change-theme');
        var icon = button.querySelector('img');
        
        if (theme === "dark") {
            icon.src = button.dataset.moonIcon;
            button.textContent = ' Mode sombre';
        } else {
            icon.src = button.dataset.sunIcon;
            button.textContent = ' Mode clair';
        }
        
        button.prepend(icon);
    }
});