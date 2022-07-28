import React, {useState} from 'react';
import '../navbar.css'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

function Navbar() {
    const [active, setActive] = useState('nav__menu')
    const [toggleIcon, setToggleIcon] = useState('nav__toggler')
    const navToggle = () => {
        active === 'nav__menu' ? setActive('nav__menu nav__active') : setActive('nav__menu');

        toggleIcon === 'nav__toggler' ? setToggleIcon('nav__toggler toggle') : setToggleIcon('nav__toggler')
    }
    return (
        <Router>
        <nav className='nav'>
            <Link to='/' className='nav__brand'>Все услуги</Link>
            <ul className={active}>
                <li className='nav__item'>
                    <Link to='/' className='nav__link'>Личный кабинет</Link>
                </li>
                <li className='nav__item'>
                    <Link to='/' className='nav__link'>Услуги</Link>
                </li>
                <li className='nav__item'>
                    <Link to='/' className='nav__link'>Главная</Link>
                </li>
                <li className='nav__item'>
                    <Link to='/' className='nav__link'>Уведомления</Link>
                </li>
                <li className='nav__item'>
                    <Link to='/' className='nav__link'>Настройки</Link>
                </li>
            </ul>
            <div onClick={navToggle} className={toggleIcon}>
                <div className="line1"></div>
                <div className="line2"></div>
                <div className="line3"></div>
            </div>
        </nav>
        </Router>
    );
}

export default Navbar;