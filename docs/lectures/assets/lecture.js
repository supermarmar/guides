/* ============================================================
   Lecture bootstrap
   Initialises KaTeX auto-render, Mermaid, and exposes a small
   helper for Chart.js so individual lectures stay concise.
   ============================================================ */

(function () {
  'use strict';

  function onReady(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  // ---------- KaTeX auto-render ----------
  function renderMaths() {
    if (typeof renderMathInElement === 'undefined') return;
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\[', right: '\\]', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false,
      strict: 'ignore'
    });
  }

  // ---------- Mermaid ----------
  function initMermaid() {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize({
      startOnLoad: true,
      theme: 'base',
      themeVariables: {
        primaryColor: '#f0fdfa',
        primaryTextColor: '#18181b',
        primaryBorderColor: '#0d9488',
        lineColor: '#71717a',
        secondaryColor: '#f4f4f5',
        tertiaryColor: '#ffffff',
        background: '#ffffff',
        fontFamily: 'Inter, system-ui, sans-serif',
        fontSize: '13px'
      },
      flowchart: { curve: 'basis', htmlLabels: true },
      sequence: { useMaxWidth: true }
    });
  }

  // ---------- Chart.js helper ----------
  // Lectures use:  Lecture.chart('canvasId', { type, data, options })
  window.Lecture = window.Lecture || {};
  window.Lecture.chart = function (id, config) {
    onReady(function () {
      if (typeof Chart === 'undefined') return;
      var el = document.getElementById(id);
      if (!el) return;
      Chart.defaults.font.family = "'Inter', system-ui, sans-serif";
      Chart.defaults.font.size = 12;
      Chart.defaults.color = '#71717a';
      Chart.defaults.borderColor = '#e4e4e7';
      config.options = config.options || {};
      config.options.responsive = true;
      config.options.maintainAspectRatio = false;
      new Chart(el.getContext('2d'), config);
    });
  };

  onReady(function () {
    renderMaths();
    initMermaid();
  });
})();
