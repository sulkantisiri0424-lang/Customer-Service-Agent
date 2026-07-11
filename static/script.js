function sendMessage() {
    const message = document.getElementById("message").value;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById("chat-box");
        chatBox.innerHTML += "<p><b>You:</b> " + message + "</p>";
        chatBox.innerHTML += "<p><b>Bot:</b> " + data.response + "</p>";
        document.getElementById("message").value = "";
    });
}
