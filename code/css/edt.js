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
        const icon = dropdown.previousElementSibling.querySelector('i');
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
        icon.className = dropdown.style.display === 'block' ? 'fas fa-caret-down' : 'fas fa-caret-right';
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
        const filtresMenu = document.getElementById('menu-filter');
        filtresMenu.style.display = filtresMenu.style.display === 'block' ? 'none' : 'block';
        const icon = document.getElementById('title-filter-icon');
        icon.className = filtresMenu.style.display === 'block' ? 'fas fa-caret-down' : 'fas fa-caret-right';
    }

    function resetFilters() {
        document.querySelectorAll('#menu-filter input[type="checkbox"]').forEach(checkbox => {
            checkbox.checked = false;
        });
        filterSchedule();
    }

    function applyFilters() {
        // Placeholder function for applying filters
        // Implement filter logic based on checked checkboxes
        console.log('Filters applied');
    }

    // Event listeners for filter buttons
    document.getElementById('reset-button').addEventListener('click', resetFilters);
    document.getElementById('applied-button').addEventListener('click', applyFilters);

    // Event listener for the main filter button
    document.getElementById('menu-filter-button').addEventListener('click', toggleFiltres);

    window.toggleDropdown = toggleDropdown;
    window.filterSchedule = filterSchedule;
    window.toggleFiltres = toggleFiltres;
    window.changeWeek = changeWeek;

    updateWeekLabel();
});


