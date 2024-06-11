function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    var iconId = dropdownId.replace('dropdown', 'filter-icon');
    var icon = document.getElementById(iconId);
    if (dropdown.style.display === "" || dropdown.style.display === "none") {
        dropdown.style.display = "block";
        icon.className = "fas fa-caret-down";
    } else {
        dropdown.style.display = "none";
        icon.className = "fas fa-caret-right";
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

window.addEventListener('click', function() {
    document.getElementById('dropdown-menu').classList.remove('show');
});


document.getElementById('menu-filter-button').addEventListener('click', function () {
    var filtresMenu = document.getElementById('menu-filter');
    var icon = document.getElementById('menu-filter-icon');
    if (filtresMenu.classList.contains('open')) {
        filtresMenu.classList.remove('open');
        icon.className = "fas fa-caret-right";
    } else {
        filtresMenu.classList.add('open');
        icon.className = "fas fa-caret-down";
    }
});