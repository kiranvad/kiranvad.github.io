// Chrome-style tab controller shared by publications and talks sections

document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('.tabbed-section');

  sections.forEach((section) => {
    const tabs = Array.from(section.querySelectorAll('.chrome-tab'));
    const panels = Array.from(section.querySelectorAll('.chrome-tab-panel'));

    if (!tabs.length || !panels.length) {
      return;
    }

    // Ensure buttons behave as tabs with keyboard support
    tabs.forEach((tab) => {
      tab.setAttribute('type', 'button');
      tab.setAttribute('role', 'tab');
      tab.setAttribute('aria-selected', 'false');
      tab.setAttribute('tabindex', '-1');
    });

    panels.forEach((panel) => {
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('tabindex', '0');
      panel.hidden = true;
    });

    const defaultTarget = section.dataset.initialTab;
    const initialTab =
      tabs.find((tab) => tab.dataset.tabTarget === defaultTarget) || tabs[0];

    activateTab(initialTab);

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => {
        if (!tab.classList.contains('is-active')) {
          activateTab(tab);
        }
      });

      tab.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
          event.preventDefault();
          const offset = event.key === 'ArrowRight' ? 1 : -1;
          const nextIndex = (index + offset + tabs.length) % tabs.length;
          tabs[nextIndex].focus();
          activateTab(tabs[nextIndex]);
        }
      });
    });

    function activateTab(selectedTab) {
      tabs.forEach((tab) => {
        const isActive = tab === selectedTab;
        tab.classList.toggle('is-active', isActive);
        tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
        tab.setAttribute('tabindex', isActive ? '0' : '-1');
      });

      panels.forEach((panel) => {
        const shouldShow = panel.id === selectedTab.dataset.tabTarget;
        panel.classList.toggle('is-active', shouldShow);
        panel.hidden = !shouldShow;
      });
    }
  });
});
