<template>
  <div v-if="loadedArticle">Загрузка...</div>
  <p v-if="!loadedArticle && articleList.length === 0">Список пуст</p>
  <ul v-if="!loadedArticle && articleList.length > 0" class="article-list">
    <ArticleItem
      :key="article.id"
      :article="article"
      v-for="article in articleList"
    />
  </ul>
</template>

<script>
import ArticleItem from "@/components/Articles/ArticleItem";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ArticleList",
  components: { ArticleItem },
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

<style scoped></style>
