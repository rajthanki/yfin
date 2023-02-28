import React from 'react';
import styled from 'styled-components';

const NavbarContainer = styled.nav`
  background-color: #f8f9fa;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
`;

const Logo = styled.a`
  font-size: 24px;
  font-weight: bold;
  color: #000;
  text-decoration: none;
`;

const NavbarLinks = styled.ul`
  list-style: none;
  display: flex;
  align-items: center;
`;

const NavbarLink = styled.li`
  margin-right: 20px;
  font-size: 18px;
  color: #000;
  text-decoration: none;
  cursor: pointer;
  
  &:hover {
    color: #007bff;
  }
`;

const Navbar = () => {
  return (
    <NavbarContainer>
      <Logo href="#">Stock Market</Logo>
      <NavbarLinks>
        <NavbarLink>Home</NavbarLink>
        <NavbarLink>About</NavbarLink>
        <NavbarLink>Contact</NavbarLink>
      </NavbarLinks>
    </NavbarContainer>
  );
};

export default Navbar;
