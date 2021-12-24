export function Component($parent) {
  const template = '<h1>Hello World</h1>';
  
  const init = () => {
    render();
  }

  const render = () => {
    $parent.innerHTML = template;
  }

  return {init, render};
}