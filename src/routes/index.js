import { About } from '../pages/About';
import { Framework } from '../pages/Framework.js';
import { Frameworks } from '../pages/Frameworks';
import { Home } from '../pages/Home';
import { NotFound } from '../pages/Not-Found';

const ROUTES = {
  '/not-found': NotFound,
  '/': Home,
  '/about': About,
  '/frameworks': Frameworks,
  '/frameworks/:id': Framework,
};

const getPath = () => {
  // Case '/topic without #'
  if (window.location.pathname.length > 1) return `/not-found`;

  const path = window.location.hash.slice(1).split('/');

  // Case: '/#topic/id'
  if (path.length >= 2) {
    return `/${path[0]}/:id`;
  }

  // Case: '/#topic'
  if (path.length == 1) {
    return `/${path[0]}`;
  }

  // Case: '/ or /#'
  return '/';
};

export const onRouteChanged = async () => {
  const toRender = ROUTES[getPath()] ?? ROUTES['/not-found'];
  document.getElementById('main').innerHTML = await toRender();
};
