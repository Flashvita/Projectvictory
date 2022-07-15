import axios from "axios";

export const feedbackModule = {
  state: () => ({
    name: "",
    nameError: false,
    email: "",
    emailError: false,
    phone: "",
    phoneError: false,
    service: "",
    serviceError: false,
    message: "",
    messageError: false,
    errorAPI: false,
    errorTextAPI: "",
    isLoad: false,
  }),
  mutations: {
    setName(state, name) {
      state.name = name;
      state.nameError = false;
      state.errorAPI = false;
    },
    setNameError(state, nameError) {
      state.nameError = nameError;
    },
    setEmail(state, email) {
      state.email = email;
      state.emailError = false;
      state.errorAPI = false;
    },
    setEmailError(state, emailError) {
      state.emailError = emailError;
    },
    setPhone(state, phone) {
      state.phone = phone;
      state.phoneError = false;
      state.errorAPI = false;
    },
    setPhoneError(state, phoneError) {
      state.phoneError = phoneError;
    },
    setService(state, service) {
      state.service = service;
      state.serviceError = false;
      state.errorAPI = false;
    },
    setServiceError(state, serviceError) {
      state.serviceError = serviceError;
    },
    setMessage(state, message) {
      state.message = message;
      state.messageError = false;
      state.errorAPI = false;
    },
    setMessageError(state, messageError) {
      state.messageError = messageError;
    },
    setErrorAPI(state, errorAPI) {
      state.errorAPI = errorAPI;
    },
    setErrorTextAPI(state, errorTextAPI) {
      state.errorTextAPI = errorTextAPI;
    },
    setIsLoad(state, isLoad) {
      state.isLoad = isLoad;
    },
  },
  getters: {
    name(state) {
      return state.name;
    },
    nameError(state) {
      return state.nameError;
    },
    email(state) {
      return state.email;
    },
    emailError(state) {
      return state.emailError;
    },
    phone(state) {
      return state.phone;
    },
    phoneError(state) {
      return state.phoneError;
    },
    service(state) {
      return state.service;
    },
    serviceError(state) {
      return state.serviceError;
    },
    message(state) {
      return state.message;
    },
    messageError(state) {
      return state.messageError;
    },
    errorAPI(state) {
      return state.errorAPI;
    },
    errorTextAPI(state) {
      return state.errorTextAPI;
    },
    isLoad(state) {
      return state.isLoad;
    },
  },
  actions: {
    async sendFeedbackForm({ commit }, data) {
      try {
        commit("setIsLoad", true);
        return await axios.post("server/api/v1/", data);
      } catch (e) {
        console.log(e);
        commit("setErrorAPI", true);
        commit("setErrorTextAPI", "Ошибка!!!");
      } finally {
        commit("setIsLoad", false);
      }
    },
  },
  namespaced: true,
};
