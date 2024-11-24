//   <!-- JavaScript điều khiển khung chat -->

function toggleChat() {
  const chatContainer = document.getElementById("chat-container");
  chatContainer.style.display =
    chatContainer.style.display === "none" ? "flex" : "none";
}

function sendMessage() {
  const userMessage = document.getElementById("user-input").value;
  document.getElementById("user-input").value = "";

  if (userMessage.trim() === "") {
    return;
  }

  const chatMessages = document.getElementById("chat-messages");

  // Hiển thị tin nhắn của người dùng
  chatMessages.innerHTML += `<div class="message user"><b>You:</b> ${userMessage}</div>`;
  chatMessages.scrollTop = chatMessages.scrollHeight;

  // Hiển thị hiệu ứng bot typing
  const typingIndicator = document.createElement("div");
  typingIndicator.id = "typing-indicator";
  typingIndicator.className = "message bot";
  typingIndicator.innerHTML = "<b>Bot:</b> ...";
  chatMessages.appendChild(typingIndicator);
  chatMessages.scrollTop = chatMessages.scrollHeight;

  // Giả lập thời gian bot gõ trong 3 giây
  setTimeout(() => {
    typingIndicator.remove();

    // Fetch câu trả lời từ server (hoặc câu trả lời giả lập nếu không có server)
    fetch("http://localhost:5005/webhooks/rest/webhook", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userMessage }),
    })
      .then((response) => response.json())
      .then((data) => {
        data.forEach((message) => {
          chatMessages.innerHTML += `<div class="message bot"><b>Bot:</b> ${message.text}</div>`;
          chatMessages.scrollTop = chatMessages.scrollHeight;
        });
      })
      .catch(() => {
        // Trường hợp không kết nối được server, trả lời mặc định
        chatMessages.innerHTML += `<div class="message bot"><b>Bot:</b> Xin lỗi, hiện tại tôi không thể trả lời yêu cầu của bạn.</div>`;
        chatMessages.scrollTop = chatMessages.scrollHeight;
      });
  }, 3000); // Thời gian bot gõ là 3 giây
}

// Gán sự kiện gửi tin nhắn cho nút gửi và phím Enter
document.getElementById("send-button").onclick = sendMessage;
document
  .getElementById("user-input")
  .addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });
