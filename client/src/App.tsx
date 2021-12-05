/** @jsxImportSource @emotion/react */

import { Provider } from "react-redux";
import { configureStore, combineReducers } from "@reduxjs/toolkit";
import Router from "./Router";
import hideHeaderSlice from "./modules/hideHeaderSlice";
import recipeSlice from "./modules/recipeSlice";
import rankingSlice from "./modules/rankingSlice";
import searchedImageSlice from "./components/Result/searchedImageSlice";
import searchText from "./redux/search";
import getSearchList from "./redux/searchList";
import getUserInfo from "./redux/userLogin";
import getMyInfoList from "./redux/myInfo";
import getNewAccessList from './redux/newToken'
import "./App.css";

function App() {
    const rootReducer = combineReducers({
        hideHeaderSlice: hideHeaderSlice,
        searchedImageSlice: searchedImageSlice,
        recipeSlice: recipeSlice,
        rankingSlice: rankingSlice,
        searchText : searchText,
        getSearchList : getSearchList,
        getUserInfo : getUserInfo,
        getMyInfoList : getMyInfoList,
        getNewAccessList:getNewAccessList
    });

    const store = configureStore({
        reducer: rootReducer
    });

    return (
        <Provider store={store}>
            <div>
                <Router />
            </div>
        </Provider>
    );
}

export default App;
