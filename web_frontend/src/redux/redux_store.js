import {combineReducers, createStore} from "redux";
import searchReducer from "./searchReducer";
import docReducer from "./docReducer";

let reducers = combineReducers({
    search: searchReducer,
    doc: docReducer


});

let store = createStore(reducers);


export default store;