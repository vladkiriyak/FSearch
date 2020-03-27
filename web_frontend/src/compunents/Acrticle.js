import React from 'react';
import {Link, Route} from "react-router-dom";
import Document from "./Document";


let Article = ({article, store}) => {

    let openDoc = () => {
        window.location.href = "http://localhost:3000/doc/" + article.file_id;
    };

    return (
        <a onClick={openDoc}>
            <div className="card" onClick={openDoc}>
                <section>
                    <div className="card-header">
                        {article.file_name}
                    </div>
                    <div className="card-body">
                        {article.file_content}
                    </div>
                </section>
            </div>

        </a>


    )


};

export default Article





























