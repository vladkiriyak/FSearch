import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"
import {BrowserRouter, Route} from "react-router-dom";
import MainPage from "./MainPage";
import RegistrationPanel from "./RegistrationPanel";
import LoginPanel from "./LoginPanel";
import SearchPanel from "./SearchPanel";
import Document from "./Document";

let App = ({store}) => {



    return (
        <BrowserRouter>
            <div>
                <Route exact path='/' component={MainPage}/>
                <Route exact path='/search' render={() => <SearchPanel store={store}/>}/>
                <Route exact path='/doc' render={() => <Document store={store}/>}/>
                <Route exact path='/registration' render={() => <RegistrationPanel store={store}/>}/>
                <Route exact path='/authentication' render={() => <LoginPanel store={store}/>}/>

            </div>
        </BrowserRouter>
    )
};

export default App