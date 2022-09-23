import { onRouteChanged } from './routes/index.js';

window.addEventListener('load', onRouteChanged);
window.addEventListener('hashchange', onRouteChanged);
