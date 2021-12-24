export function NavActons($parent) {
  let loggedOutTemplate = '<a class="login navbar-text actions" href="/login" style="display:flex; text-decoration: none;"><p style="margin-top: 3px; margin-right: 5px; margin-bottom: 0px; margin-left: 18px">Login with </p><div style="position:relative; height:30px; display: flex; align-items:center"><div class="logo"><div class="circle"></div><div class="bar"></div><div class="colors"></div></div></div></a>';
  let loggedInTemplate = '<span class="navbar-text actions" style="margin-left: 18px;"> <a class="login" href="#">Logout</a> </span>'
  let state = {loggedIn: localStorage.getItem('loggedIn')};

  const init = () => {
    render();
  }

  const render = () => {
    console.log(state)
    if (state.loggedIn === 'true') {
      $parent.innerHTML = loggedInTemplate;
    } else {
      $parent.innerHTML = loggedOutTemplate;
    }
  }

  return {init, render};
}