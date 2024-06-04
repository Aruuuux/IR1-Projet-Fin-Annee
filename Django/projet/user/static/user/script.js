function toggleDropdown(dropdownId) {
    var dropdownContent = document.getElementById(dropdownId);
    if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
    } else {
        dropdownContent.style.display = "block";
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
    if (filtresMenu.classList.contains('open')) {
        filtresMenu.classList.remove('open');
    } else {
        filtresMenu.classList.add('open');
    }
});
