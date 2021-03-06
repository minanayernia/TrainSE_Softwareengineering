import Vue from "vue";
import Vuex from "vuex";

import app from "../main";
import user from "./modules/user";
import survey from "./modules/survey";
import menu from "./modules/menu";
import { setCurrentLanguage } from "../utils";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {
    changeLang(state, payload) {
      app.$i18n.locale = payload;
      setCurrentLanguage(payload);
    }
  },
  actions: {
    setLang({ commit }, payload) {
      commit("changeLang", payload);
    }
  },
  modules: {
    menu,
    user,
    survey
  }
});
