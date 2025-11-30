// main.js — small UI enhancements: typing effect, counters, scroll reveal

document.addEventListener('DOMContentLoaded', () => {
  // Typing effect on elements with .typing and data-words
  document.querySelectorAll('.typing').forEach(el => {
    const words = (el.dataset.words || '').split('|').filter(Boolean);
    if (!words.length) return;
    let idx = 0, pos = 0, forward = true;
    el.classList.add('animate');
    const tick = () => {
      const word = words[idx];
      if (forward) {
        pos++;
        el.textContent = word.slice(0, pos);
        if (pos === word.length) { forward = false; setTimeout(tick, 900); return; }
      } else {
        pos--;
        el.textContent = word.slice(0, pos);
        if (pos === 0) { forward = true; idx = (idx+1) % words.length; }
      }
      setTimeout(tick, forward ? 80 : 40);
    };
    tick();
  });

  // Simple counter animation for elements with data-target
  const animateCounters = () => {
    document.querySelectorAll('.counter .num').forEach(el => {
      if (el.dataset.animated) return;
      const target = parseInt(el.dataset.target || el.textContent || '0', 10);
      if (!target) return;
      el.dataset.animated = 'true';
      let cur = 0;
      const step = Math.max(1, Math.floor(target / 60));
      const timer = setInterval(() => {
        cur += step;
        if (cur >= target) { el.textContent = target; clearInterval(timer); }
        else el.textContent = cur;
      }, 16);
    });
  };

  // Reveal on scroll using IntersectionObserver
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        if (entry.target.matches('.counters')) animateCounters();
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal, .counters').forEach(el => observer.observe(el));

  // Smooth in-page anchor scrolling
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const href = a.getAttribute('href');
      const target = document.querySelector(href);
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });
});
