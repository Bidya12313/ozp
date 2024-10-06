document.addEventListener('DOMContentLoaded', function() {
    // Знаходимо таблицю та всі рядки
    const table = document.getElementById('taxesTable');
    if (table) {  // Перевіряємо, чи існує таблиця
        const rows = table.getElementsByTagName('tr');

        // Додаємо обробник подій на кожен рядок таблиці
        for (let i = 1; i < rows.length; i++) { // Починаємо з 1, щоб пропустити заголовок
            rows[i].addEventListener('click', function() {
                // Видаляємо клас виділення з усіх рядків
                for (let j = 1; j < rows.length; j++) {
                    rows[j].classList.remove('highlight');
                }

                // Додаємо клас виділення до натиснутого рядка
                rows[i].classList.add('highlight');

                // Отримуємо всі клітинки поточного рядка
                const cells = rows[i].getElementsByTagName('td');

                // Заповнюємо відповідні поля форм
                document.getElementById('applicant').value = cells[0].innerText; // Заявник
                document.getElementById('payer').value = cells[1].innerText; // Платник
                document.getElementById('manager').value = cells[2].innerText; // Керівник
                document.getElementById('recipient').value = cells[3].innerText; // Отримувач
                document.getElementById('amount').value = cells[4].innerText; // Сума
                document.getElementById('category').value = cells[5].innerText; // Категорія
                document.getElementById('comment').value = cells[7].innerText; // Коментар
            });
        }
    }
});
