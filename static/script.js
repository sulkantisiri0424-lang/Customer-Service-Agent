
function sendMessage() {
    let input = document.getElementById("user-input");
    let chatBox = document.getElementById("chat-box");

    let message = input.value.trim();

    if (message === "") return;

    chatBox.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot"><b>Bot:</b> ${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    input.value = "";
}

document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});