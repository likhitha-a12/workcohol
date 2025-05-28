"use strict";

function filterEvents(category, event) {
  var allSections = document.querySelectorAll('.event-section');
  var buttons = document.querySelectorAll('.filter-buttons button'); // Update active button style

  buttons.forEach(function (btn) {
    return btn.classList.remove('active');
  });
  if (event) event.target.classList.add('active'); // Show/hide event sections

  allSections.forEach(function (section) {
    if (category === 'all' || section.classList.contains(category)) {
      section.style.display = 'block';
    } else {
      section.style.display = 'none';
    }
  }); // Scroll to the relevant section smoothly

  if (category !== 'all') {
    setTimeout(function () {
      var scrollTarget = document.getElementById(category);

      if (scrollTarget) {
        scrollTarget.scrollIntoView({
          behavior: 'smooth'
        });
      }
    }, 100);
  } else {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
}

function goToBookingPage() {
  window.location.href = '/booking/';
}

function goToIndexPage() {
  window.location.href = '/index/';
}

console.log("main.js loaded ✅");
//# sourceMappingURL=main.dev.js.map
