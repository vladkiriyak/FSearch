import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"
import "../css/main_page.css"

class MainPage extends Component {


    render() {


        return (
            <div>
                <div id="logo">FSearch</div>
                <input className="search-window input-group-text float-right"/>


            </div>
        )
    }
}

export default MainPage