import axios from "axios";

window.axios = axios;
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://45.8.248.219:5000";
axios.interceptors.request.use(function (config) {
  config.headers.common = {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
    "Content-type": "application/json",
    Accept: "application/json",
  };
  return config;
});
