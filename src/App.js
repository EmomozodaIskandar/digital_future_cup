import React from 'react';
import Navbar from "./components/Navbar";
import Cards from "./components/cards/Cards";
// import {
//     BrowserRouter as Router,
//     Routes,
//     Route,
// } from "react-router-dom";
// import Home from "./components/Home";
// import Privat from "./components/Privat";
// import Services from "./components/Services";
// import Notifications from "./components/Notifications";
// import Settings from "./components/Settings";

function App() {
    return (
        <>
            {/*<Router>*/}
            <Navbar/>
            <div className='wrapper'>
            <Cards img='3366ef083868d63a4dd4afb318808883.png' text='Водительское удостоверение'/>
            <Cards img='b67ee3462bcd830686436331c1206880.png' text='Заграничный паспорт'/>
            <Cards img='d1ef3d0b2f504f56245b178dde31597f.png' text='Общегражданский паспорт'/>
            <Cards img='8735572b3ff3e561f5174a06cd8a5cb9.png' text='Справка об отсутствии судимости'/>
            <Cards img='0456c0d279b484bafdf973ed87f1ab98.png' text='Электронная медицинская
карта'/>
            <Cards img='e7a89d2948227579b93ce5d4f4e87f88.png' text='Электронная трудовая книжка'/>
            </div>
                {/*<Routes>*/}
                {/*    <Route path='/' element={<Home/>} exact><Home/></Route>*/}
                {/*    <Route path='/' element={<Privat/>} exact><Privat/></Route>*/}
                {/*    <Route path='/' element={<Services/>} exact><Services/></Route>*/}
                {/*    <Route path='/' element={<Notifications/>} exact><Notifications/></Route>*/}
                {/*    <Route path='/' element={<Settings/>} exact><Settings/></Route>*/}
                {/*</Routes>*/}
            {/*</Router>*/}
        </>
    );
}

export default App;
