function updateMedicine(element) {
    const medId = element.getAttribute('data-id'); 
    const action = element.getAttribute('data-action');
    const url = `/medicine/update_medicine/${medId}/${action}/`;
    const postData = {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    };

    fetch(url, postData).then(response => response.json())
      .then(data => {
          if (data.success) {
              // Обновление элемента на странице
              const todayElement = document.getElementById(`today-${medId}`);
              if (todayElement) {
                  todayElement.textContent = `${data.new_today}/${data.amount_per_day}`;
              }
          }
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
