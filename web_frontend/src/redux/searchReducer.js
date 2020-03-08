const SEARCH = 'SEARCH';


let initialState = {articles: []};


const searchReducer = (state = initialState, action) => {
    if (action.type === SEARCH) {


        let xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://localhost:8000/searcher/search?q=' + action.query, false);

        xhr.send();
        state.articles = JSON.parse(xhr.responseText)['docs'];

        return state
    } else {

        return state
    }


};


export default searchReducer;