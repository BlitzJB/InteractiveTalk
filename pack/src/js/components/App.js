import { Component } from "./Component.js";

export function App(parentQuerySelector = 'body') {
  let appNode = document.createElement('div');
  appNode.classList.add('app');
  
  const init = () => {
    const parent = document.querySelector(parentQuerySelector);
    parent.appendChild(appNode);
    mount();
  }

  const mount = () => {
    const component = new Component(appNode);
    component.init();
  }

  return {init}
}