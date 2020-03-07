import React from 'react';
import "bootstrap/dist/css/bootstrap.css"

import ArticleList from "./ArticleList";
import {Route} from "react-router-dom";
import Document from "./Document";

let SearchPanel = ({store}) => {

    let searchElementRef = React.createRef();

    const search = () => {
        let query = searchElementRef.current.value;
        store.dispatch({type: 'SEARCH', query: query})

    };



    return (
        <div className="container">
            <br/>
            <h2 className="d-inline">FSearch</h2>
            <button onClick={search} className="d-inline  btn btn-success float-right">click</button>
            <input ref={searchElementRef} className="input-group-text float-right"/>
            <br/>
            <br/>
            <br/>
            <ArticleList articles={store.getState().search.articles}/>
        </div>

    )


};

export default SearchPanel