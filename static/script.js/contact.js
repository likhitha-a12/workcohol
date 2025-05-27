document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('.contact-form');
  const nameInput = document.querySelector('#name');
  const emailInput = document.querySelector('#email');
  const messageInput = document.querySelector('#message');
  const thankYouMessage = document.getElementById('thank-you-message');
  const errorMessage = document.getElementById('error-message');

  if (!form || !nameInput || !emailInput || !messageInput) {
    console.error('One or more form elements not found.');
    return;
  }

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const message = messageInput.value.trim();

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
      body: JSON.stringify({ name, email, message })
    })
    .then(response => {
      if (response.ok) {
        if (thankYouMessage) thankYouMessage.style.display = 'block';
        form.reset();
      } else {
        if (errorMessage) {
          errorMessage.textContent = 'Failed to send message.';
          errorMessage.style.display = 'block';
        }
      }
    })
    .catch(error => {
      console.error('Error:', error);
      if (errorMessage) {
        errorMessage.textContent = 'An error occurred. Please try again.';
        errorMessage.style.display = 'block';
      }
    });
  });
});
