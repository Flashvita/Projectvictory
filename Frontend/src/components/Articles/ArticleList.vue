<template>
  <div v-if="loadedArticle" class="spinner">
    <my-spinner></my-spinner>
  </div>
  <p
    class="article_list_zero"
    v-if="!loadedArticle && articleList.results?.length === 0"
  >
    Список пуст
  </p>
  <ul
    class="article_list"
    v-if="!loadedArticle && articleList.results?.length > 0"
  >
    <ArticleItem
      :key="article.id"
      :article="article"
      v-for="article in articleList.results"
    />
  </ul>
  <my-pagination
    v-if="articleList.results"
    :count="articleList.count"
    :limit="limitPagination"
    :handlerClick="handlerPagination"
  />
</template>

<script>
import ArticleItem from "@/components/Articles/ArticleItem";
import MySpinner from "@/components/UI/Spinner";
import MyPagination from "@/components/UI/MyPagination";
import { mapActions, mapGetters, mapMutations } from "vuex";

export default {
  name: "ArticleList",
  components: { ArticleItem, MySpinner, MyPagination },
  methods: {
    ...mapActions({
      getArticlesOll: "article/getArticlesOll",
    }),
    ...mapMutations({
      setCategoryId: "article/setCategoryId",
    }),
    handlerPagination({ offset }) {
      const catalog = this.$route.query;
      if (offset <= 0) {
        this.getArticlesOll({ ...catalog, offset });
      } else {
        this.getArticlesOll({
          ...catalog,
          offset: offset * this.limitPagination,
        });
      }
    },
  },
  computed: {
    ...mapGetters({
      articleList: "article/articleList",
      loadedArticle: "article/loadedArticle",
      limitPagination: "article/limitPagination",
    }),
  },
  mounted() {
    console.log(this.$route.query);
    if (!this.$route.query) this.setCategoryId(null);
    this.getArticlesOll({ category: this.$route.query.catalog });
  },
};
</script>

<style lang="scss" scoped>
.article_list {
  width: 100%;
  margin-top: 40px;
  flex: 1 1 auto;
}

.article_list_zero {
  text-align: center;
  margin-top: 40px;
  width: 100%;
}

.spinner {
  width: 30px;
  height: 30px;
  margin: auto;
}
</style>
