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
    errorConfirmPassword: false,
    loading: false,
    errorAuth: false,
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
      state.errorConfirmPassword = false;
    },
    setEmail(state, email) {
      state.email = email;
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.errorConfirmPassword = false;
    },
    setPassword(state, password) {
      state.password = password;
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.passwordError = false;
      state.errorConfirmPassword = false;
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
      state.errorConfirmPassword = false;
    },
    setErrorAuth(state, errorAuth) {
      state.errorAuth = errorAuth;
    },
    setErrorConfirmPassword(state, errorConfirmPassword) {
      state.errorConfirmPassword = errorConfirmPassword;
    },
    resetError(state) {
      state.errorAuth = false;
      state.nameError = false;
      state.emailError = false;
      state.passwordError = false;
      state.errorConfirmPassword = false;
    },
  },
  actions: {
    async signIn({ state, commit }) {
      if (state.email.length <= 0) commit("setEmailError", true);
      if (state.password.length <= 0) commit("setPasswordError", true);

      if (state.email.length > 0 && state.password.length > 0) {
        commit("setLoading", true);
        try {
          const response = await axios.post(
            "https://jsonplaceholder.typicode.com/posts",
            {
              email: state.email,
              password: state.password,
            }
          );
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
          } else {
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
          const response = await axios.post(
            "https://jsonplaceholder.typicode.com/posts",
            {
              name: state.name,
              email: state.email,
              password: state.password,
            }
          );
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
            commit("setErrorAuth", true);
          } else {
            console.log(e);
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
  },
  namespaced: true,
};
