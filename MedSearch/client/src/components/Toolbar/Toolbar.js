import React, {useState} from "react";
import {Link} from "react-router-dom";
import logo from './Logo1.png';
import "./Toolbar.css";
import {
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  InputGroup,
  InputGroupAddon,
  InputGroupText,
  FormInput,
  Collapse
} from "shards-react";

export default function Toolbar(props) {

  // const [dropdownOpen, setDropdownOpen] = useState(false)
  const [collapseOpen, setCollapseOpen] = useState(false)

  // const toggleDropdown = () => {
  //   setDropdownOpen(!dropdownOpen)
  // }

  const toggleNavbar = () => {
    setCollapseOpen(!collapseOpen)
  }
  
  return (
    <div className="fixed">
      <Navbar type="dark" className="bg-fourth w-screen" expand="md">

        <Link to="/"><img src={logo} alt="logo" /></Link>
        
        <NavbarToggler onClick={toggleNavbar} />

        <Collapse open={collapseOpen} navbar>
          <Nav navbar className=" text-purple-900" >

            <NavItem className="items-center justify-center" >
              <Link className="p-2 text-gray-600 hover:text-black transition hover:no-underline" to="/appointments">
                Appointments
              </Link>
            </NavItem>

            <NavItem>
              <Link className="p-2 text-gray-600 hover:text-black transition hover:no-underline" to="/offices">
                Offices
              </Link>
            </NavItem>

            <NavItem>
              <Link className="p-2 text-gray-600 hover:text-black transition hover:no-underline" to="/">
                Placeholder
              </Link>
            </NavItem>

            <NavItem>
              <img className=" h-6" src="https://img.icons8.com/android/50/000000/calendar.png"/>
            </NavItem>


            {/* AN OPTINAL DROPDOWN FOR THE NAVBAR   to enable, uncomment dropDown state and handler function*/}
            {/* <Dropdown               
              open={dropdownOpen}
              toggle={toggleDropdown}
            >
              <DropdownToggle nav caret>
                Dropdown
              </DropdownToggle>
              <DropdownMenu>
                <DropdownItem>Action</DropdownItem>
                <DropdownItem>Another action</DropdownItem>
                <DropdownItem>Something else here</DropdownItem>
              </DropdownMenu>
            </Dropdown> */}


          </Nav>

          <Nav navbar className="ml-auto">
            <InputGroup size="sm" seamless>
              <InputGroupAddon className="" type="prepend">
                <InputGroupText>
                <img src="https://img.icons8.com/material-sharp/24/000000/search.png"/>
                </InputGroupText>
              </InputGroupAddon>
              <FormInput className="border-0" placeholder="Search..." />
            </InputGroup>
          </Nav>

        </Collapse>
      </Navbar>
    </div>
  )
  }
