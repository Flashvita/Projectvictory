import axios from "axios";

export const articleModule = {
  state: () => ({
    title: "",
    content: "",
    loadedArticle: false,
    articleList: [],
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
    setArticleList(state, articleList) {
      state.articleList = articleList;
    },
  },
  actions: {
    async getArticle({ commit }, article) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios.get(`/api/v1/posts/detail/${article.id}`);
        console.log(response);
        commit("setTitle", response.data.title);
        commit("setContent", response.data.content);
      } catch (e) {
        console.log(e.message);
      } finally {
        commit("setLoadedArticle", false);
      }
    },
    async getArticlesOll({ commit }, query = "") {
      commit("setLoadedArticle", true);
      const queryParams = {
        limit: 10,
        catalog: query,
      };
      try {
        const response = await axios.get("/api/v1/posts/", {
          params: queryParams,
        });
        commit("setArticleList", response.data);
      } catch (e) {
        console.log(e.message);
      } finally {
        commit("setLoadedArticle", false);
      }
    },
    async removeArticle({ commit }, id) {
      commit("setLoadedArticle", true);
      try {
        await axios.delete(`/api/v1/posts/detail/${id}`);
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
    articleList(state) {
      return state.articleList;
    },
  },
  namespaced: true,
};
