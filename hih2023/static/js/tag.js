// Загружаем сохраненные выбранные теги при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    const savedTags = JSON.parse(localStorage.getItem('selectedTags')) || [];

    document.querySelectorAll('.tag').forEach(tag => {
        // Проверяем, был ли этот тег ранее выбран
        if (savedTags.includes(tag.textContent.trim())) {
            const activeBg = tag.getAttribute('data-color');
            const activeText = tag.getAttribute('data-text-color');
            tag.style.backgroundColor = activeBg;
            tag.style.color = activeText;
        }

        tag.addEventListener('click', () => {
            // Получаем цвета для активного состояния
            const activeBg = tag.getAttribute('data-color');
            const activeText = tag.getAttribute('data-text-color');

            // Проверяем, активен ли тег
            if (tag.style.backgroundColor === activeBg) {
                // Если активен, сбрасываем на серый
                tag.style.backgroundColor = '#e0e0e0';
                tag.style.color = '#666666';

                // Убираем тег из сохраненных
                const index = savedTags.indexOf(tag.textContent.trim());
                if (index > -1) {
                    savedTags.splice(index, 1);
                }
            } else {
                // Если не активен, устанавливаем активные цвета
                tag.style.backgroundColor = activeBg;
                tag.style.color = activeText;

                // Добавляем тег в сохраненные
                if (!savedTags.includes(tag.textContent.trim())) {
                    savedTags.push(tag.textContent.trim());
                }
            }

            // Сохраняем обновленный список выбранных тегов
            localStorage.setItem('selectedTags', JSON.stringify(savedTags));
        });
    });
});
