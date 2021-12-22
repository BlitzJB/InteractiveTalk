import { NavActons } from "./components/NavActions.js";
import { HeroCTA } from "./components/HeroCTA.js";

document.addEventListener('DOMContentLoaded', () => {
  const navActions_parent = document.querySelector('#nav_actions') 
  const navActions = new NavActons(navActions_parent);
  navActions.init();

  const heroCTA_parent = document.querySelector('#hero_cta')
  const heroCTA = new HeroCTA(heroCTA_parent);
  heroCTA.init();

})

const currentYear=document.querySelector(".current-year");currentYear.innerText=(new Date).getFullYear();