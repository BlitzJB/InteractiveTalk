import { NavActons } from "./components/NavActions.js";

document.addEventListener('DOMContentLoaded', () => {
  const navActions = new NavActons();
  const parent = document.querySelector('#nav_actions')
  console.log(parent)
  navActions.init(parent);
})

const currentYear=document.querySelector(".current-year");currentYear.innerText=(new Date).getFullYear();