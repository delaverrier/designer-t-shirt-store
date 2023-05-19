document.getElementById('update-address-button').addEventListener('click', function() {
  var addressInput = document.getElementById('shipping-address-input');
  var addressDisplay = document.getElementById('shipping-address-display');
  var newAddress = addressInput.value;
  addressDisplay.textContent = newAddress;
});

document.addEventListener('DOMContentLoaded', function() {
  var payNowButton = document.getElementById('pay-now-button');
  payNowButton.addEventListener('click', function() {
    // Здесь ты можешь добавить код для выполнения действия при нажатии кнопки "Pay Now"
    // Например, отправку формы или закрытие модального окна
    console.log("Pay Now button clicked");
  });
});
