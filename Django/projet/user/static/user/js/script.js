function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    var button = dropdown.previousElementSibling;
    var iconId = dropdownId.replace('dropdown', 'filter-icon');
    var icon = document.getElementById(iconId);
    if (dropdown.style.display === "" || dropdown.style.display === "none") {
        dropdown.style.display = "block";
        icon.className = "fas fa-caret-down";
        button.classList.add('open');
    } else {
        dropdown.style.display = "none";
        icon.className = "fas fa-caret-right";
        button.classList.remove('open');
    }
}

document.getElementById('profil-utilisateur').addEventListener('click', function (event) {
    event.stopPropagation();
    var dropdownMenu = document.getElementById('dropdown-menu');
    if (dropdownMenu.classList.contains('show')) {
        dropdownMenu.classList.remove('show');
    } else {
        dropdownMenu.classList.add('show');
    }
});


window.addEventListener('DOMContentLoaded', (event) => {
    var filtresMenu = document.getElementById('menu-filter');
    var menuIcon = document.getElementById('menu-filter-icon');
    var rightSrc = menuIcon.getAttribute('data-right-src');
    var downSrc = menuIcon.getAttribute('data-down-src');

    // Set initial icon state based on menu state
    if (filtresMenu.classList.contains('open')) {
        menuIcon.src = downSrc;
    } else {
        menuIcon.src = rightSrc;
    }

    document.getElementById('menu-filter-button').addEventListener('click', function () {
        var uniqueParam = '?v=' + new Date().getTime();
        if (filtresMenu.classList.contains('open')) {
            filtresMenu.classList.remove('open');
            this.classList.remove('open');
            menuIcon.src = rightSrc + uniqueParam;
        } else {
            filtresMenu.classList.add('open');
            this.classList.add('open');
            menuIcon.src = downSrc + uniqueParam;
        }
    });
});
document.getElementById('reset-button').addEventListener('click', function() {
    var checkboxes = document.querySelectorAll('#menu-filter input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
    });
});
