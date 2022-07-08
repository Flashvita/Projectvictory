<template>
  <div v-if="loadedArticle" class="spinner">
    <my-spinner></my-spinner>
  </div>
  <p
    class="article_list_zero"
    v-if="!loadedArticle && articleList.length === 0"
  >
    Список пуст
  </p>
  <ul class="article_list" v-if="!loadedArticle && articleList.length > 0">
    <ArticleItem
      :key="article.id"
      :article="article"
      v-for="article in articleList"
    />
  </ul>
</template>

<script>
import ArticleItem from "@/components/Articles/ArticleItem";
import MySpinner from "@/components/UI/Spinner";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ArticleList",
  components: { ArticleItem, MySpinner },
  data() {
    return {
      articles: [],
      load: false,
    };
  },
  methods: {
    ...mapActions({
      getArticlesOll: "article/getArticlesOll",
    }),
  },
  computed: {
    ...mapGetters({
      articleList: "article/articleList",
      loadedArticle: "article/loadedArticle",
    }),
  },
  mounted() {
    this.getArticlesOll();
  },
};
</script>

<style lang="scss" scoped>
.article_list {
  width: 100%;
  margin-top: 40px;
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
