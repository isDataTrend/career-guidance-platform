import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  name: "",
  email: "",
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    setUser: (state, action) => {
      state.name = action.payload.name;
      state.email = action.payload.email;
    },
    logout: (state) => {
      state.name = "";
      state.email = "";
    },
  },
});

export const { setUser, logout } = userSlice.actions;

export default userSlice.reducer;
