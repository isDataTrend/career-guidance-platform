import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  careerRecommendations: [],
};

const dataSlice = createSlice({
  name: "data",
  initialState,
  reducers: {
    setCareerRecommendations: (state, action) => {
      state.careerRecommendations = action.payload;
    },
  },
});

export const { setCareerRecommendations } = dataSlice.actions;

export default dataSlice.reducer;
