function deleteAppointment(element){
    var apptId = element.getAttribute('data-id');
    var url = '/doctors/delete_appointment/' + apptId;
    var listItems = element.closest('.u-list-item'); // Найти ближайший родительский элемент записи
    var csrfToken = getCookie('csrftoken');
    
    // Ajax запрос
    var postData = {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json'
        }
    };

    fetch(url, postData)
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка сети');  // Вызываем ошибку для неправильного HTTP-статуса
        }
        return response.json(); // если всё хорошо, обрабатываем ответ как JSON
    })
    .then(result => {
        listItems.remove(); // удаление элемента со страницы
        updateNoAppointmentsMessage(); // Проверка, остались ли еще записи
    })
    .catch(error => {
        alert("Ошибка удаления: " + error.message);
    });
}

function updateNoAppointmentsMessage(){
    var appointmentsList = document.querySelector('.u-repeater-1');
    if (!appointmentsList.children.length){
        // Если записей больше нет, обновляем сообщение
        document.querySelector('.u-text-1').textContent = "Пока записей нет! :)";
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
