import axios from "axios";

export const articleModule = {
  state: () => ({
    title: "",
    content: "",
    loadedArticle: false,
    articleList: [],
    categoryList: [],
    categoryError: false,
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
    setCategoryList(state, categoryList) {
      state.categoryList = categoryList;
    },
    setCategoryError(state, categoryError) {
      state.categoryError = categoryError;
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
      console.log(query);
      const queryParams = {
        limit: 10,
        catalog: query,
      };
      try {
        const response = await axios.get("/api/v1/posts/", {
          params: queryParams,
        });
        console.log(response.data);
        commit("setArticleList", response.data.results);
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
    async createCategory({ commit, dispatch }, title, parent) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios.post(`/api/v1/category/create/`, {
          title,
          parent,
        });
        await dispatch("getCategory");
        console.log(response);
        return response;
      } catch (e) {
        console.log(e.message);
        commit("setCategoryError", true);
      } finally {
        commit("setLoadedArticle", false);
      }
    },
    async getCategory({ commit }) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios.get(`/api/v1/categories/`);
        commit("setCategoryList", response.data.results);
        console.log(response.data.results);
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
    categoryList(state) {
      return state.categoryList;
    },
    categoryError(state) {
      return state.categoryError;
    },
  },
  namespaced: true,
};
