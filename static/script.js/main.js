function filterEvents(category, event) {
  const allSections = document.querySelectorAll('.event-section');
  const buttons = document.querySelectorAll('.filter-buttons button');

  // Update active button style
  buttons.forEach(btn => btn.classList.remove('active'));
  if (event) event.target.classList.add('active');

  // Show/hide event sections
  allSections.forEach(section => {
    if (category === 'all' || section.classList.contains(category)) {
      section.style.display = 'block';
    } else {
      section.style.display = 'none';
    }
  });

  // Scroll to the relevant section smoothly
  if (category !== 'all') {
    setTimeout(() => {
      const scrollTarget = document.getElementById(category);
      if (scrollTarget) {
        scrollTarget.scrollIntoView({ behavior: 'smooth' });
      }
    }, 100);
  } else {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function goToBookingPage() {
  window.location.href = '/booking/';
}

function goToIndexPage() {
  window.location.href = '/index/';
}

console.log("main.js loaded ✅");
