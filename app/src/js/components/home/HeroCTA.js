export function HeroCTA($parent) {
  let state = {loggedIn: localStorage.getItem('loggedIn')};
  if (state.loggedIn === 'true') {
    state.text = 'Open Dashboard'
    state.link = '/dashboard'
  } else {
    state.text = 'Get Started'
    state.link = '/login'
  };
  let template = `<a href="${state.link}"><button class="btn btn-primary btn-lg px-4 gap-3" type="button"><strong>${state.text}</strong></button></a>`;

  const init = (params) => {
    render();
  }

  const render = () => {
    $parent.innerHTML = template;
  }

  return {init, render};
}