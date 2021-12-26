import firebase from 'firebase/app'
import 'firebase/auth'
import { setCurrentUser, getCurrentUser } from '../../utils'
import {api } from '../../constants/config'
import router from '../../router'
import axios from "axios";

export default {
  state: {
    currentUser: getCurrentUser(),
    loginError: null,
    processing: false,
    forgotMailSuccess: null,
    registerSuccess: null,
    resetPasswordSuccess: null
  },
  getters: {
    currentUser: state => state.currentUser,
    processing: state => state.processing,
    loginError: state => state.loginError,
    registerSuccess: state => state.registerSuccess,
    forgotMailSuccess: state => state.forgotMailSuccess,
    resetPasswordSuccess: state => state.resetPasswordSuccess,
  },
  mutations: {
    setUser(state, payload) {
      state.currentUser = payload
      state.processing = false
      state.loginError = null
    },
    setLogout(state) {
      state.currentUser = null
      state.processing = false
      state.loginError = null
    },
    setProcessing(state, payload) {
      state.processing = payload
      state.loginError = null
    },
    setError(state, payload) {
      state.loginError = payload
      state.currentUser = null
      state.processing = false
    },
    setForgotMailSuccess(state) {
      state.loginError = null
      state.currentUser = null
      state.processing = false
      state.forgotMailSuccess = true
    },
    setResetPasswordSuccess(state) {
      state.loginError = null
      state.currentUser = null
      state.processing = false
      state.resetPasswordSuccess = true
    },
    setRegisterSuccess(state) {
      state.registerSuccess = true;
      state.processing = false;
    },
    clearError(state) {
      state.loginError = null
    }
  },
  actions: {
    login({ commit }, payload) {
      commit('clearError');
      commit('setProcessing', true);

      console.log()
      const data={
        username: payload.username,
        password: payload.password,    
      };

      axios
        .post(api+"login/",data)
        .then(response => {
          console.log(response);
          return response.data;
        })
        .then(res => {
          console.log(res.status);
          if (res.status==200){
            console.log()
            var userData = res;
            setCurrentUser(userData);
            commit('setUser', userData);
            router.replace("/");
          }
          else {
            alert(res.msg);
          }

        });


    },
    register({ commit }, payload) {
      commit('clearError');
      commit('setProcessing', true);

      console.log()
      const data={
        username: payload.username,
        password: payload.password,
        email: payload.email,
        role: payload.role      
      };

      axios
        .post(api+"signup/",data)
        .then(response => {
          console.log("register res");
          console.log(response.data);
          return response.data;
        })
        .then(res => {
          console.log(res.status);
          if (res.status==200){
            console.log()
            var userData = res;
            setCurrentUser(userData);
            commit('setUser', userData);
            router.replace("/");
          }
          else {
            alert(res.msg);
          }

        });


    },

    forgotPassword({ commit }, payload) {
      commit('clearError')
      commit('setProcessing', true)
      firebase
        .auth()
        .sendPasswordResetEmail(payload.email)
        .then(
          user => {
            commit('clearError')
            commit('setForgotMailSuccess')
          },
          err => {
            commit('setError', err.message)
            setTimeout(() => {
              commit('clearError')
            }, 3000)
          }
        )
    },
    resetPassword({ commit }, payload) {
      commit('clearError')
      commit('setProcessing', true)
      firebase
        .auth()
        .confirmPasswordReset(payload.resetPasswordCode, payload.newPassword)
        .then(
          user => {
            commit('clearError')
            commit('setResetPasswordSuccess')
          },
          err => {
            commit('setError', err.message)
            setTimeout(() => {
              commit('clearError')
            }, 3000)
          }
        )
    },


    signOut({ commit }) {
      setCurrentUser(null);
      commit('setLogout');
}
  }
}
