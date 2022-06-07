import "./assets/css/vendor/dropzone.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "./assets/css/vendor/bootstrap.min.css";
import "./assets/css/vendor/bootstrap.rtl.only.min.css";
import "video.js/dist/video-js.css";

import { getThemeColor } from "./utils";

var color = getThemeColor();
let render = () => {
  import("./assets/css/sass/themes/piaf." + color + ".scss").then(() =>
    require("./main")
  );
};

render();
