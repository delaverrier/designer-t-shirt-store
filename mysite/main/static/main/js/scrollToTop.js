// Показать кнопку прокрутки при прокрутке страницы вниз
//window.onscroll = function() {
//  showScrollButton();
//};

//function showScrollButton() {
//  var scrollButton = document.getElementById("scrollButton");
//  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
//    scrollButton.style.display = "block";
//  } else {
//    scrollButton.style.display = "none";
//  }
//}

// Перемотка страницы вверх при нажатии кнопки
//function scrollToTop() {
//  document.body.scrollTop = 0; // Для Safari
//  document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE и Opera
//}
window.addEventListener('scroll', function() {
  showScrollButton();
});

function showScrollButton() {
  var scrollButton = document.getElementById("scrollButton");
  scrollButton.style.display = "block";
}

function scrollToTop() {
  document.body.scrollTop = 0; // Для Safari
  document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE и Opera
}
