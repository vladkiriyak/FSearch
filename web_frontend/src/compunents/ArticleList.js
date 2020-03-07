import React, {Component} from "react"

import Article from "./Acrticle";


let ArticleList = ({articles}) => {

    const articleElements = articles.map(
        article => <Article article={article}/>
    );

    return (

        <div>
            {articleElements}
        </div>
    )

};


export default ArticleList








