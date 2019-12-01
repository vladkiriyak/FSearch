import React, {Component} from "react"

import Article from "./Acrticle";


class ArticleList extends Component {
    state = {
        articles: []
    };

    constructor(props) {
        super(props);
        let {articles} = props;
        this.state.articles = articles;


    }

    componentWillReceiveProps(nextProps, nextContext) {
        let {articles} = nextProps;
        this.setState({articles: articles});
    }


    render() {

        const articleElements = this.state.articles.map(
            article => <Article article={article}/>
        );


        return (

            <div>
                {articleElements}
            </div>

        )


    }


}


export default ArticleList








