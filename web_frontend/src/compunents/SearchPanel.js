import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"
import articles from "../content"

import ArticleList from "./ArticleList";

class SearchPanel extends Component {

    state = {
        articles: []
    };


    constructor(props){
        super(props);

        let xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://localhost:8000/getContent', false);
        xhr.send();
        this.state.articles = JSON.parse(xhr.responseText)['articles'];
        this.search = this.search.bind(this);
    }

    render() {

        return (
            <div className="container">
                <br/>
                <h2 className="d-inline">FSearch</h2>
                <button onClick={this.search} className="d-inline  btn btn-success float-right">click</button>
                <input id='searchInput' className="input-group-text float-right"/>
                <br/>
                <br/>
                <br/>
                <ArticleList articles={this.state.articles}/>
            </div>

        )
    }




    search = function() {

        let xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://localhost:8000/getContenttt', false);
        xhr.send();
        let articles = JSON.parse(xhr.responseText)['articles'];

        this.setState({articles: articles});

        let searchInput = document.getElementById('searchInput');

        console.log(searchInput.value)


    };



}

export default SearchPanel