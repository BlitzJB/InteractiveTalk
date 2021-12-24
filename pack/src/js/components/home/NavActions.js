import { getCookie } from "../../helpers.js";

export function NavActons($parent) {
  const cookieFieldName = 'google_id';
  const cookie = getCookie(cookieFieldName);
  const pfpFieldName = 'profile_picture';
  const pfp = getCookie(pfpFieldName);
  const nameFieldName = 'name';
  const name = getCookie(nameFieldName);
  
  let loggedOutTemplate = '<a class="login navbar-text actions" href="/login" style="display:flex; text-decoration: none;"><p style="margin-top: 3px; margin-right: 5px; margin-bottom: 0px; margin-left: 18px">Login with </p><div style="position:relative; height:30px; display: flex; align-items:center"><div class="logo"><div class="circle"></div><div class="bar"></div><div class="colors"></div></div></div></a>';
  let loggedInTemplate = `
    <div class="profile">   
      <div class="profile__img">
        <a href="/profile" style="display: flex; text-decoration: none;">
          <p class="navbar-text actions profile__name" style="margin-top: auto; margin-bottom: auto; margin-right: 10px;">${name}</p>
          <img src="${pfp}" style="border-radius: 50%; height:50px; border:2px solid lightgreen"/>
        </a>
      </div>
    </div> 
  `
  let state = {
    loggedIn: cookie ? true : false,
    pfp: pfp ? pfp : null
  };
  
  const init = () => {
    render();
  }
  
  const render = () => {
    console.log('NavCTAstate', state);
    if (state.loggedIn === true) {
      $parent.innerHTML = loggedInTemplate;
    } else {
      $parent.innerHTML = loggedOutTemplate;
    }
  }

  return {init, render};
}