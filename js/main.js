// script.js

// Smooth scrolling for internal links
const navLinks = document.querySelectorAll('a[href^="#"], a[href$=".html"]');

navLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    const targetId = link.getAttribute('href');
    if (targetId.startsWith('#')) {
      e.preventDefault();
      document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Toggle visibility for sections (if needed)
document.addEventListener('DOMContentLoaded', () => {
  const toggleButtons = document.querySelectorAll('.toggle-section');

  toggleButtons.forEach(button => {
    button.addEventListener('click', () => {
      const target = document.querySelector(button.dataset.target);
      if (target) {
        target.classList.toggle('hidden');
      }
    });
  });
});
