document.addEventListener('DOMContentLoaded', function() {
    const weekLabel = document.getElementById('weekLabel');
    let currentWeekStart = new Date('2024-01-01');

    function updateWeekLabel() {
        weekLabel.textContent = `Semaine du ${currentWeekStart.toLocaleDateString('fr-FR')}`;
    }

    function changeWeek(weekDelta) {
        currentWeekStart.setDate(currentWeekStart.getDate() + (weekDelta * 7));
        updateWeekLabel();
    }

    function toggleDropdown(dropdownId) {
        const dropdown = document.getElementById(dropdownId);
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    }

    function filterSchedule() {
        const searchInput = document.getElementById('searchInput').value.toLowerCase();
        const timeSlots = document.querySelectorAll('.time-slot');

        timeSlots.forEach(slot => {
            if (slot.textContent.toLowerCase().includes(searchInput)) {
                slot.style.display = '';
            } else {
                slot.style.display = 'none';
            }
        });
    }

    function toggleFiltres() {
        const filtresMenu = document.getElementById('filtres-menu');
        filtresMenu.style.display = filtresMenu.style.display === 'block' ? 'none' : 'block';
    }

    // Ajout de la classe de mode sombre au chargement de la page
    document.body.classList.add('dark-mode');

    window.toggleDropdown = toggleDropdown;
    window.filterSchedule = filterSchedule;
    window.toggleFiltres = toggleFiltres;
    window.changeWeek = changeWeek;

    updateWeekLabel();
});
