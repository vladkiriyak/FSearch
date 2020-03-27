import React from "react";

let Document = ({store}) => {

    let file_id = window.location.href.split('/')[window.location.href.split('/').length - 1];
    store.dispatch({type: 'DOC', file_id: file_id});



    return(

        <div className="card">
            <div className="card-header">
                {store.getState().doc.doc.file_name}
            </div>
            <div className="card-body">
                <p className="card-text">{store.getState().doc.doc.file_content}.
                </p>
                <a className="btn btn-primary">Download</a>
            </div>
        </div>


    )

};

export default Document
