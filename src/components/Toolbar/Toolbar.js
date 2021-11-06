import React from "react";

import "./Toolbar.css";

const toolbar = (props) => (
  <header className="toolbar">
    <nav className="toolbar_navigation">
      {/*First we're going to add the "hambuger", on the top left.*/}
      <div></div>
      {/*Clickable logo back to the main menu.*/}
      <div className="toolbar_logo">
        <a href="/">The Logo</a>
      </div>
      {/*This div is for any extra elements in the tool bar.*/}
      <div className="toolbar_navigation-items">
        {/*Unumbered list.*/}
        <ul>
          {/*List*/}
          <li>
            <a href="/">Products</a>
          </li>
          <li>
            <a href="/">Users </a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
);

export default toolbar;
