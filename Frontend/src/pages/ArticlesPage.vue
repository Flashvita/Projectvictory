<template>
  <h1>Страница с постами</h1>
  <div v-if="load">Загрузка...</div>
  <p v-if="!load && articles.length === 0">Список пуст</p>
  <ul v-if="!load && articles.length > 0" class="article-list">
    <ArticleItem
      :key="article.id"
      :article="article"
      v-for="article in articles"
    />
  </ul>
</template>

<script>
import axios from "axios";
import ArticleItem from "@/components/ArticleItem";

export default {
  name: "ArticlesPage",
  components: { ArticleItem },
  data() {
    return {
      articles: [],
      load: false,
    };
  },
  methods: {
    async fetchArticles() {
      this.load = true;
      try {
        const response = await axios
          .get("https://jsonplaceholder.typicode.com/posts?_limit=10")
          .finally(() => {
            this.load = false;
          });
        this.articles = response.data;
      } catch (e) {
        console.log(e.message);
      }
    },
  },
  mounted() {
    this.fetchArticles();
  },
};
</script>

<style scoped>
.article {
  margin: 20px 0;
}
</style>
