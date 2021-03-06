import { createSlice, PayloadAction } from "@reduxjs/toolkit";

type SliceState = { hide: Boolean }

const initialState: SliceState = {
    hide: false
};

export const hideHeaderSlice = createSlice({
    name: "hideHeaderSlice",
    initialState,
    reducers: {
        setHideTrue: (state, action: PayloadAction<Boolean>) => {
            state.hide = action.payload;
        },
        setHideFalse: (state, action: PayloadAction<Boolean>) => {
            state.hide = action.payload;
        }
    }
});

export const { setHideTrue, setHideFalse } = hideHeaderSlice.actions;
export default hideHeaderSlice.reducer;
