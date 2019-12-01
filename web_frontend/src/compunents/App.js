import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"
import {BrowserRouter, Route} from "react-router-dom";
import MainPage from "./MainPage";
import RegistrationPanel from "./RegistrationPanel";
import LoginPanel from "./LoginPanel";
import SearchPanel from "./SearchPanel";

class App extends Component {


    render() {


        return (
            <BrowserRouter>
                <div>
                    <Route exact path='/' component={MainPage}/>
                    <Route exact path='/search' component={SearchPanel}/>
                    <Route exact path='/registration' component={RegistrationPanel}/>
                    <Route exact path='/login' component={LoginPanel}/>

                </div>
            </BrowserRouter>
        )
    }
}

export default App