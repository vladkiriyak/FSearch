import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"
import "../css/main_page.css"

let MainPage = () => {


    return (
        <div>

            <input type='file'/>
            <button>Upload</button>

            <div id="logo">FSearch</div>
            <input className="search-window input-group-text float-right"/>


        </div>
    )
};

export default MainPage;