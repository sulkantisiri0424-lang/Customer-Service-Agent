document.addEventListener("DOMContentLoaded", function () {

    fetch("/analytics")
        .then(response => response.json())
        .then(data => {

            document.getElementById("totalChats").textContent = data.total_chats;
            document.getElementById("feedback").textContent = data.total_feedback;

        })
        .catch(error => {
            console.log("Analytics Error:", error);
        });

});