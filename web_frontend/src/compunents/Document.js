import React from "react";

let Document = ({store}) => {

    return (


        <div>
            <h1>{store.getState().doc.doc.file_name}</h1>
            <h2>{store.getState().doc.doc.file_content}</h2>

        </div>


    )


};

export default Document
