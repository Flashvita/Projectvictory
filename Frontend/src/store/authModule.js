import axios from "axios";
import router from "@/router/router";

export const authModule = {
  state: () => ({
    isAuth: JSON.parse(localStorage.getItem("isAuth")) || false,
    token: localStorage.getItem("token") || "",
    profile: {},
    name: "",
    nameError: false,
    email: "",
    emailError: false,
    password: "",
    passwordError: false,
    confirmPassword: "",
    confirmPasswordError: false,
    loading: false,
    errorAuth: false,
    messageErrorAuth: "",
  }),
  mutations: {
    setLoading(state, loading) {
      state.loading = loading;
    },
    setIsAuth(state, isAuth) {
      state.isAuth = isAuth;
    },
    setToken(state, token) {
      state.token = token;
    },
    setName(state, name) {
      state.name = name;
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.confirmPasswordError = false;
    },
    setEmail(state, email) {
      state.email = email;
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.confirmPasswordError = false;
    },
    setPassword(state, password) {
      state.password = password;
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.passwordError = false;
      state.confirmPasswordError = false;
    },
    setNameError(state, nameError) {
      state.nameError = nameError;
    },
    setEmailError(state, emailError) {
      state.emailError = emailError;
    },
    setPasswordError(state, passwordError) {
      state.passwordError = passwordError;
    },
    setConfirmPassword(state, confirmPassword) {
      state.confirmPassword = confirmPassword;
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.passwordError = false;
      state.confirmPasswordError = false;
    },
    setErrorAuth(state, errorAuth) {
      state.errorAuth = errorAuth;
    },
    setErrorConfirmPassword(state, errorConfirmPassword) {
      state.confirmPasswordError = errorConfirmPassword;
    },
    resetError(state) {
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.confirmPasswordError = false;
      state.messageErrorAuth = "";
    },
    setMessageErrorAuth(state, message) {
      state.messageErrorAuth = message;
    },
    setProfile(state, profile) {
      state.profile = profile;
    },
  },
  actions: {
    async signIn({ state, commit, dispatch }) {
      if (state.name.length <= 0) commit("setNameError", true);
      if (state.password.length <= 0) commit("setPasswordError", true);

      if (state.name.length > 0 && state.password.length > 0) {
        commit("setLoading", true);
        try {
          const response = await axios.post("server/auth/token/login/", {
            username: state.name,
            password: state.password,
          });
          const token = response.data.auth_token;
          if (token) {
            localStorage.setItem("isAuth", JSON.stringify(true));
            localStorage.setItem("token", JSON.stringify(token));
            commit("setIsAuth", true);
            commit("setToken", token);
            commit("setName", "");
            commit("setPassword", "");
            await dispatch("getMe");
            await router.push("/");
          }
        } catch (e) {
          commit("setErrorAuth", true);
          if (e.message === "Network Error") {
            commit(
              "setMessageErrorAuth",
              "Хьюстон, у нас проблема! Мы работаем над этим."
            );
          } else {
            commit("setMessageErrorAuth", e.response.data.non_field_errors[0]);
          }
        } finally {
          commit("setLoading", false);
        }
      }
    },
    async signUp({ state, commit, dispatch }) {
      if (state.name.length <= 0) commit("setNameError", true);
      if (state.email.length <= 0) commit("setEmailError", true);
      if (state.password.length <= 0) commit("setPasswordError", true);
      if (state.confirmPassword.length <= 0)
        commit("setErrorConfirmPassword", true);
      if (state.password !== state.confirmPassword) {
        commit("setErrorConfirmPassword", true);
        commit("setPasswordError", true);
      }
      if (
        state.name.length > 0 &&
        state.email.length > 0 &&
        state.password.length > 0 &&
        state.password === state.confirmPassword
      ) {
        commit("setLoading", true);
        try {
          const response = await axios.post("server/auth/users/", {
            username: state.name,
            email: state.email,
            password: state.password,
          });
          console.log(response);
          if (response.status === 201) {
            await dispatch("signIn");
            commit("setName", "");
            commit("setEmail", "");
            commit("setPassword", "");
            commit("setConfirmPassword", "");
          }
        } catch (e) {
          console.log(e);
          if (e.message === "Network Error") {
            commit("setErrorAuth", true);
            commit(
              "setMessageErrorAuth",
              "Хьюстон, у нас проблема! Мы работаем над этим."
            );
          } else if (e.response.data.email) {
            commit("setMessageErrorAuth", e.response.data.password.join(" "));
            commit("setEmailError", true);
          } else if (e.response.data.password) {
            commit("setMessageErrorAuth", e.response.data.password.join(" "));
            commit("setPasswordError", true);
            commit("setErrorConfirmPassword", true);
          } else {
            commit("setErrorAuth", true);
            commit(
              "setMessageErrorAuth",
              "Хьюстон, у нас проблема! Мы работаем над этим."
            );
          }
        } finally {
          commit("setLoading", false);
        }
      }
    },
    async logout({ commit }) {
      localStorage.removeItem("isAuth");
      localStorage.removeItem("token");
      commit("setIsAuth", false);
      commit("setToken", "");
      await router.push("/");
    },
    async getMe({ commit, dispatch }) {
      try {
        const response = await axios.get("server/auth/users/me/");
        commit("setProfile", response.data);
      } catch (e) {
        await dispatch("logout");
        console.log(e);
      }
    },
  },
  getters: {
    isAuth(state) {
      return state.isAuth;
    },
    isLoading(state) {
      return state.loading;
    },
    nameError(state) {
      return state.nameError;
    },
    emailError(state) {
      return state.emailError;
    },
    passwordError(state) {
      return state.passwordError;
    },
    confirmPasswordError(state) {
      return state.confirmPasswordError;
    },
    errorAuth(state) {
      return state.errorAuth;
    },
    setMessageErrorAuth(state) {
      return state.messageErrorAuth;
    },
    profile(state) {
      return state.profile;
    },
  },
  namespaced: true,
};
