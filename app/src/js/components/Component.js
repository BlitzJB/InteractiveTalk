export function Component(parentQuerySelector) {
  const template = '<h1>Hello World</h1>';
  const parent = document.querySelector(parentQuerySelector);
  
  const init = () => {
    render();
  }

  const render = () => {
    parent.innerHTML = template;
  }

  return {init, render};
}