import React from 'react';
import {Link, Route} from "react-router-dom";
import Document from "./Document";


let Article = ({article}) => {

    let openDoc = () => {
        store.dispatch({type: 'DOC', uuid: uuid})


    };

    return (
        <a href={'/doc/' + article.uuid} onClick={openDoc}>
            <div className="card">
                <section>
                    <div className="card-header">
                        {article.title}
                    </div>
                    <div className="card-body">
                        {article.body}
                    </div>
                </section>
            </div>

        </a>


    )


};

export default Article





























