export function NavActons($parent) {
  let loggedOutTemplate = '<span class="navbar-text actions" style="margin-left: 18px;"> <a class="login" href="#">Log In</a><a class="btn btn-light action-button" role="button" href="#">Sign Up</a></span>';
  let loggedInTemplate = '<span class="navbar-text actions" style="margin-left: 18px;"> <a class="login" href="#">Log Out</a> </span>'
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