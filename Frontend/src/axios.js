import axios from "axios";

window.axios = axios;
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "https://45.8.248.219/";
axios.interceptors.request.use(function (config) {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.common = {
      Authorization: `Token ${JSON.parse(token)}`,
    };
  }
  return config;
});
