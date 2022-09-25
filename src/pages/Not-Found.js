export const NotFound = () => {
  document.title = 'Not found / who is SPA';
  return `
    <section class='general-container'>
      <h1 class='general-title'>Page not found</h1>
      <p class='general-description'>Try other or <a href='/#'>go safe
      </a></p>
  </section>
  `;
};
