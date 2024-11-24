// Открытие модального окна
function showModal(title, date, location, organizer, description) {
    document.getElementById('modal-title').textContent = title;
    document.getElementById('modal-date').textContent = date;
    document.getElementById('modal-location').textContent = location;
    document.getElementById('modal-organizer').textContent = organizer;
    document.getElementById('modal-description').textContent = description;

    const modal = document.getElementById('event-modal');
    modal.style.display = 'flex';
}

// Закрытие модального окна
document.querySelector('.close').onclick = function () {
    document.getElementById('event-modal').style.display = 'none';
};

// Закрытие при клике вне модального окна
window.onclick = function (event) {
    const modal = document.getElementById('event-modal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};