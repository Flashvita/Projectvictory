import axios from "axios";

export const articleModule = {
  state: () => ({
    title: "",
    content: "",
    article: {},
    articleError: false,
    loadedArticle: false,
    articleList: {},
    limitPagination: 4,
    offsetNext: null,
    offsetPrevious: null,
    categoryId: null,
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
    setArticle(state, article) {
      state.article = article;
    },
    setArticleError(state, articleError) {
      state.articleError = articleError;
    },
    setLoadedArticle(state, load) {
      state.loadedArticle = load;
    },
    setArticleList(state, articleList) {
      state.articleList = articleList;
    },
    setOffsetNext(state, offsetNext) {
      state.offsetNext = offsetNext;
    },
    setOffsetPrevious(state, offsetPrevious) {
      state.offsetPrevious = offsetPrevious;
    },
    setCategoryList(state, categoryList) {
      state.categoryList = categoryList;
    },
    setCategoryId(state, categoryId) {
      state.categoryId = categoryId;
    },
    setCategoryError(state, categoryError) {
      state.categoryError = categoryError;
    },
  },
  actions: {
    async createArticle({ commit }, article) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios.post(
          "server/api/v1/post/create/",
          article
        );
        return response.data;
      } catch (e) {
        console.log(e.message);
        commit("setArticleError", true);
      } finally {
        commit("setLoadedArticle", false);
      }
    },

    async patchArticle({ commit }, article) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios.patch(
          `server/api/v1/posts/detail/${article.id}/`,
          article
        );
        return response.data;
      } catch (e) {
        commit("setArticleError", true);
        console.log(e.message);
      } finally {
        commit("setLoadedArticle", false);
      }
    },

    async getArticle({ commit }, { method, article }) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios({
          method: method,
          url: `server/api/v1/posts/detail/${article.id}/`,
          data: article,
        });
        commit("setArticle", response.data);
        commit("setTitle", response.data.title);
        commit("setContent", response.data.content);
      } catch (e) {
        console.log(e.message);
      } finally {
        commit("setLoadedArticle", false);
      }
    },

    async getArticlesOll({ commit, state }, query = {}) {
      commit("setLoadedArticle", true);
      const queryParams = {
        limit: state.limitPagination,
        catalog: query.catalog,
        offset: query.offset,
      };
      try {
        const response = await axios.get("server/api/v1/posts/", {
          params: queryParams,
        });
        commit("setArticleList", response.data);
        commit("setOffsetNext", response.data.next);
        commit("setOffsetPrevious", response.data.previous);
      } catch (e) {
        console.log(e.message);
      } finally {
        commit("setLoadedArticle", false);
      }
    },

    async removeArticle({ commit }, id) {
      commit("setLoadedArticle", true);
      try {
        await axios.delete(`server/api/v1/posts/detail/${id}`);
      } catch (e) {
        console.log(e.message);
      } finally {
        commit("setLoadedArticle", false);
      }
    },

    async createCategory({ commit, dispatch }, { title, parent }) {
      commit("setLoadedArticle", true);
      try {
        const response = await axios.post(`server/api/v1/category/create/`, {
          title,
          parent,
        });
        await dispatch("getCategory");
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
        const response = await axios.get(`server/api/v1/childrens/`);
        commit("setCategoryList", response.data);
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
    article(state) {
      return state.article;
    },
    articleError(state) {
      return state.articleError;
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
    categoryId(state) {
      return state.categoryId;
    },
    categoryError(state) {
      return state.categoryError;
    },
    limitPagination(state) {
      return state.limitPagination;
    },
    offsetNext(state) {
      return state.offsetNext;
    },
    offsetPrevious(state) {
      return state.offsetPrevious;
    },
  },
  namespaced: true,
};
