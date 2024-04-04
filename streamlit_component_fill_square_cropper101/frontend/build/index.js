// frontend/index.js

import React from "react";
import ReactDOM from "react-dom";

const Streamlit_component_fill_square_cropper101 = ({ image_url }) => {
  return (
    <div>
      <img src={image_url} alt="Image" />
    </div>
  );
};

ReactDOM.render(<Streamlit_component_fill_square_cropper101 />, document.getElementById("image-cropped"));