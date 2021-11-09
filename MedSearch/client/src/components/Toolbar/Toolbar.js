import React from "react";
import SearchBar from "../Searchbar/search";
import logo from './Logo.png';
import "./Toolbar.css";

const Toolbar = (props) => (
  <div className=" w-screen bg-fifth h-14 top-0 left-0">
    <nav className="flex h-full items-center px-0 py-1">
      {/*First we're going to add the "hambuger", on the top left.*/}
      
      <img src={logo} className="App-logo" alt="logo" />
      {/*Clickable logo back to the main menu.*/}
      <SearchBar/>
      {/*This div is for any extra elements in the tool bar.*/}
      <div className=" text-white ">
        {/*Unumbered list.*/}
        <ul className="container flex flex-row mx-4 px-4 ">
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
  </div>
);

export default Toolbar;
