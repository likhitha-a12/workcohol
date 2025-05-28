"use strict";

document.addEventListener('DOMContentLoaded', function () {
  var form = document.querySelector('.contact-form');
  var nameInput = document.querySelector('#name');
  var emailInput = document.querySelector('#email');
  var messageInput = document.querySelector('#message');
  var thankYouMessage = document.getElementById('thank-you-message');
  var errorMessage = document.getElementById('error-message');

  if (!form || !nameInput || !emailInput || !messageInput) {
    console.error('One or more form elements not found.');
    return;
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    var name = nameInput.value.trim();
    var email = emailInput.value.trim();
    var message = messageInput.value.trim();
    if (thankYouMessage) thankYouMessage.style.display = 'none';
    if (errorMessage) errorMessage.style.display = 'none';

    if (!name || !email || !message) {
      if (errorMessage) errorMessage.style.display = 'block';
      return;
    }

    fetch('/api/contact/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body: JSON.stringify({
        name: name,
        email: email,
        message: message
      })
    }).then(function (response) {
      if (response.ok) {
        if (thankYouMessage) thankYouMessage.style.display = 'block';
        form.reset();
      } else {
        if (errorMessage) {
          errorMessage.textContent = 'Failed to send message.';
          errorMessage.style.display = 'block';
        }
      }
    })["catch"](function (error) {
      console.error('Error:', error);

      if (errorMessage) {
        errorMessage.textContent = 'An error occurred. Please try again.';
        errorMessage.style.display = 'block';
      }
    });
  });
});
//# sourceMappingURL=contact.dev.js.map
