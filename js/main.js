document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contact-form');
  const status = document.getElementById('form-status');

  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const formData = new FormData(form);
      // Mock async submission
      setTimeout(() => {
        status.textContent = 'Message sent successfully!';
        form.reset();
      }, 1000);
    });
  }
});
