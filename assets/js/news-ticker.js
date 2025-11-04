document.addEventListener('DOMContentLoaded', function () {
  const tickerContent = document.querySelector('.news-ticker-content');
  if (!tickerContent) {
    return;
  }

  const newsItems = Array.from(tickerContent.querySelectorAll('.news-item'));
  if (newsItems.length <= 1) {
    return;
  }

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (prefersReducedMotion.matches) {
    return;
  }

  const rotationClass = 'news-ticker-content--rotating';
  const activeClass = 'is-active';

  tickerContent.setAttribute('aria-live', 'polite');
  tickerContent.setAttribute('aria-atomic', 'true');

  newsItems.forEach((item) => item.classList.remove(activeClass));
  tickerContent.classList.add(rotationClass);

  let currentIndex = 0;
  newsItems[currentIndex].classList.add(activeClass);

  const displayDuration = 5000;

  window.setInterval(() => {
    const previousIndex = currentIndex;
    currentIndex = (currentIndex + 1) % newsItems.length;

    newsItems[previousIndex].classList.remove(activeClass);
    newsItems[currentIndex].classList.add(activeClass);
  }, displayDuration);
});
