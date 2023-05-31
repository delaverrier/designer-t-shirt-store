function openChat() {
  var chatWindow = document.getElementById("chat-window");
  chatWindow.style.display = "block";
  var messageButton = document.getElementsByClassName("message-button")[0];
  messageButton.style.display = "none";
}

function closeChat() {
  var chatWindow = document.getElementById("chat-window");
  chatWindow.style.display = "none";
  var messageButton = document.getElementsByClassName("message-button")[0];
  messageButton.style.display = "block";
}

var closeButton = document.getElementById("close-chat");
closeButton.addEventListener("click", closeChat);

function toggleChatWindow() {
  var chatWindow = document.getElementById('chat-window');
  if (chatWindow.style.display === 'none') {
    chatWindow.style.display = 'block';
    var messageButton = document.getElementsByClassName("message-button")[0];
    messageButton.style.display = "none";
  } else {
    chatWindow.style.display = 'none';
    var messageButton = document.getElementsByClassName("message-button")[0];
    messageButton.style.display = "block";
  }
}

function startDrag(event) {
  event.stopPropagation();

  var chatWindow = document.getElementById('chat-window');
  var startX = event.clientX;
  var startY = event.clientY;
  var initialLeft = chatWindow.offsetLeft;
  var initialTop = chatWindow.offsetTop;

  // Изменение иконки курсора
  chatWindow.style.cursor = 'move';

  function moveWindow(event) {
    event.preventDefault();

    var deltaX = event.clientX - startX;
    var deltaY = event.clientY - startY;
    chatWindow.style.left = initialLeft + deltaX + 'px';
    chatWindow.style.top = initialTop + deltaY + 'px';
  }

  function stopMoving() {
    document.removeEventListener('mousemove', moveWindow);
    document.removeEventListener('mouseup', stopMoving);

    // Возвращаем исходную иконку курсора
    chatWindow.style.cursor = 'default';
  }

  document.addEventListener('mousemove', moveWindow);
  document.addEventListener('mouseup', stopMoving);
}

var chatInput = document.getElementById('chat-input');

chatInput.addEventListener('keydown', function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    sendMessage();
  }
});

function sendMessage() {
  var message = chatInput.value;
  var messageElement = document.createElement('div');
  var timeElement = document.createElement('span');
  var currentTime = new Date().toLocaleTimeString();
  timeElement.textContent = currentTime;
  timeElement.className = 'message-time';
  var textElement = document.createElement('span');
  textElement.textContent = message;
  messageElement.appendChild(timeElement);
  messageElement.appendChild(textElement);
  var chatBody = document.querySelector('.chat-body');
  chatBody.appendChild(messageElement);
  chatInput.value = '';
}



