import React, {Component} from "react"

import Article from "./Acrticle";


let ArticleList = ({store}) => {


    const articleElements = store.getState().search.articles.map(
        article => <Article store={store} article={article}/>
    );

    return (

        <div>
            {articleElements}
        </div>
    )

};


export default ArticleList








