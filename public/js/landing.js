/*
================================================================================
FILE: public/js/landing.js
PURPOSE: Landing page interactions — knowledge modals, FAQ accordions, help drawer
================================================================================
*/
document.addEventListener('DOMContentLoaded', function () {
  // ==================== KNOWLEDGE MODAL (Task 3) ====================
  const knowledgeData = {
    hazards: {icon:'⚠️', title:'Hazards', text:'A hazard is any condition, event, or circumstance that could lead to an incident or contribute to unsafe operations. Identifying and reporting hazards early allows risk controls to be applied before events occur.'},
    reportTypes: {icon:'📋', title:'Report Types', text:'Reports include mandatory occurrences, voluntary safety reports, hazard reports, and confidential reports. Each type is classified and routed to specialists for assessment.'},
    justCulture: {icon:'⚖️', title:'Just Culture', text:'A Just Culture balances accountability with learning. Honest mistakes are treated fairly to encourage reporting, while willful violations remain accountable.'},
    confidentiality: {icon:'🔒', title:'Confidentiality', text:'Reporter identity is protected and reports are de-identified where possible. Confidential channels ensure trust and sustained reporting culture.'},
    whoCanReport: {icon:'👤', title:'Who Can Report', text:'Anyone in the aviation system — flight crew, maintenance, ATC, ground handling, and management — can and should submit reports.'},
    whatHappens: {icon:'🔄', title:'What Happens Next', text:'Reports are assessed, risk-rated, and tracked. Mitigations are implemented, effectiveness is monitored, and lessons are shared to drive continuous improvement.'}
  };
  const modal = document.getElementById('knowledgeModal');
  if (modal) {
    const iconEl = document.getElementById('modalIcon');
    const titleEl = document.getElementById('modalTitle');
    const textEl = document.getElementById('modalText');
    const closeBtn = modal.querySelector('.modal-close');
    function openModal(key) {
      const item = knowledgeData[key];
      if (!item) return;
      iconEl.textContent = item.icon;
      titleEl.textContent = item.title;
      textEl.textContent = item.text;
      modal.style.display = 'flex';
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
    function closeModal() {
      modal.style.display = 'none';
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
    document.querySelectorAll('.knowledge-card').forEach(card => {
      card.addEventListener('click', () => openModal(card.dataset.knowledge));
    });
    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && modal.style.display === 'flex') closeModal(); });
  }

  // ==================== FAQ ACCORDION (Task 4) — only one open at a time ====================
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(btn => {
    btn.addEventListener('click', () => {
      const isOpen = btn.getAttribute('aria-expanded') === 'true';
      // Close all
      faqQuestions.forEach(b => {
        b.setAttribute('aria-expanded', 'false');
        const ans = b.nextElementSibling;
        if (ans) ans.hidden = true;
      });
      // Open clicked if was closed
      if (!isOpen) {
        btn.setAttribute('aria-expanded', 'true');
        const ans = btn.nextElementSibling;
        if (ans) ans.hidden = false;
      }
    });
  });

  // ==================== HELP DRAWER (Task 5) ====================
  const helpBtn = document.getElementById('helpWidgetBtn');
  const helpDrawer = document.getElementById('helpDrawer');
  const helpOverlay = document.getElementById('helpDrawerOverlay');
  const helpClose = helpDrawer ? helpDrawer.querySelector('.help-drawer-close') : null;

  function openDrawer() {
    if (!helpDrawer || !helpOverlay) return;
    helpDrawer.classList.add('open');
    helpDrawer.setAttribute('aria-hidden', 'false');
    helpOverlay.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
  function closeDrawer() {
    if (!helpDrawer || !helpOverlay) return;
    helpDrawer.classList.remove('open');
    helpDrawer.setAttribute('aria-hidden', 'true');
    helpOverlay.style.display = 'none';
    document.body.style.overflow = '';
  }
  if (helpBtn) helpBtn.addEventListener('click', openDrawer);
  if (helpClose) helpClose.addEventListener('click', closeDrawer);
  if (helpOverlay) helpOverlay.addEventListener('click', closeDrawer);
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && helpDrawer && helpDrawer.classList.contains('open')) closeDrawer(); });
  // Close drawer when clicking a link (smooth scroll)
  document.querySelectorAll('.help-drawer-link').forEach(link => {
    link.addEventListener('click', () => closeDrawer());
  });
});
