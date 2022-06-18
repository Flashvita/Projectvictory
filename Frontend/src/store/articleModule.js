import axios from "axios";
// import router from "@/router/router";

export const articleModule = {
  state: () => ({
    title: "",
    content: "",
    loadedArticle: false,
  }),
  mutations: {
    setTitle(state, title) {
      state.title = title;
    },
    setContent(state, content) {
      state.content = content;
    },
    setLoadedArticle(state, load) {
      state.loadedArticle = load;
    },
  },
  actions: {
    async getArticle({ commit }, article) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios.get(`/api/v1/posts/detail/${article.id}`);
        commit("setTitle", response.data.title);
        commit("setContent", response.data.content);
      } catch (e) {
        console.log(e.message);
      } finally {
        commit("setLoadedArticle", false);
      }
    },
  },
  getters: {
    title(state) {
      return state.title;
    },
    content(state) {
      return state.content;
    },
    loadedArticle(state) {
      return state.loadedArticle;
    },
  },
  namespaced: true,
};
