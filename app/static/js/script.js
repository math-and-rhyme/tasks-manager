document.getElementById('add_task').onsubmit = async function(event) {
    event.preventDefault(); // Prevent default form submission

    const title_added = document.getElementById("task_title").value;
    const info_added = document.getElementById("task_info").value;

    const task_data = {
        title: title_added,
        info: info_added,
    };

    const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task_data })
    });

    const result = await response.json();
    const responseDiv = document.getElementById('response');
    if (result.success) {
        responseDiv.innerHTML += `<p>${result.message}</p>`;
    } else {
        responseDiv.innerHTML += `<p>Error: ${result.message}</p>`;
    }
};