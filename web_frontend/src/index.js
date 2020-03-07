import React from 'react';
import ReactDOM from 'react-dom';
import App from "./compunents/App";


import store  from "./redux/redux_store";


const renderTree = (store) => {
    ReactDOM.render(<App store={store}/>, document.getElementById('root'));
};


renderTree(store);

store.subscribe(() => renderTree(store));