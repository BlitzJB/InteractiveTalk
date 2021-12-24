import { getCookie } from "../../helpers.js";

export function HeroCTA($parent) {
  const cookieFieldName = 'google_id';
  const cookie = getCookie(cookieFieldName);
  
  let state = {loggedIn: cookie ? true : false};
  
  if (state.loggedIn === true) {
    state.text = 'Open Dashboard'
    state.link = '/dashboard'
  } else {
    state.text = 'Get Started'
    state.link = '/signup'
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