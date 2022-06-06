import axios from "axios";
import router from "@/router/router";

export const authModule = {
  state: () => ({
    isAuth: JSON.parse(localStorage.getItem("isAuth")) || false,
    token: localStorage.getItem("token") || "",
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
  },
  actions: {
    async signIn({ state, commit }) {
      if (state.email.length <= 0) commit("setEmailError", true);
      if (state.password.length <= 0) commit("setPasswordError", true);

      if (state.email.length > 0 && state.password.length > 0) {
        commit("setLoading", true);
        try {
          const response = await axios.post("/api-auth/login", {
            email: state.email,
            password: state.password,
          });
          console.log(response);
          const token = "здесь будет токен";
          if (token) {
            localStorage.setItem("isAuth", JSON.stringify(true));
            localStorage.setItem("token", JSON.stringify(token));
            commit("setIsAuth", true);
            commit("setToken", token);
            commit("setEmail", "");
            commit("setPassword", "");
            await router.push("/");
          }
        } catch (e) {
          if (e.response.status === 404) {
            commit("setErrorAuth", true);
            commit("setMessageErrorAuth", e.message);
            console.log(e);
          } else {
            commit("setErrorAuth", true);
            commit("setMessageErrorAuth", e.message);
            console.log(e);
          }
        } finally {
          commit("setLoading", false);
        }
      }
    },
    async signUp({ state, commit }) {
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
          const response = await axios.post("/auth/users", {
            user: state.name,
            email: state.email,
            password: state.password,
          });
          console.log(response);
          const token = "здесь будет токен";
          if (token) {
            localStorage.setItem("isAuth", JSON.stringify(true));
            localStorage.setItem("token", JSON.stringify(token));
            commit("setIsAuth", true);
            commit("setToken", token);
            commit("setName", "");
            commit("setEmail", "");
            commit("setPassword", "");
            commit("setConfirmPassword", "");
          }
        } catch (e) {
          if (e.response.status === 404) {
            console.log(e);
            commit("setErrorAuth", true);
            commit("setMessageErrorAuth", e.message);
          } else {
            console.log(e);
            commit("setErrorAuth", true);
            commit("setMessageErrorAuth", e.message);
          }
        } finally {
          commit("setLoading", false);
        }
      }
    },
    logout({ commit }) {
      localStorage.removeItem("isAuth");
      localStorage.removeItem("token");
      commit("setIsAuth", true);
      commit("setToken", "");
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
  },
  namespaced: true,
};
