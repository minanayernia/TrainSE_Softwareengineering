<template>
  <div id="app-container" :class="getMenuType">
    <topnav />
    <main>
      <div class="container-fluid">
        <slot></slot>
      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from "../containers/Sidebar";
import Topnav from "../containers/Topnav";
import Footer from "../containers/Footer";
import { mapGetters } from "vuex";

export default {
  components: {
    topnav: Topnav,
    sidebar: Sidebar,
    "footer-component": Footer
  },
  data() {
    return {
      show: false
    };
  },
  computed: {
    ...mapGetters(["getMenuType"])
  },
  mounted() {
    setTimeout(() => {
      document.body.classList.add("default-transition");
    }, 100);
  }
};
</script>
