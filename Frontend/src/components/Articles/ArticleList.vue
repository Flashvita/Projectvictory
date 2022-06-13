<template>
  <div v-if="load">Загрузка...</div>
  <p v-if="!load && articles.length === 0">Список пуст</p>
  <ul v-if="!load && articles.length > 0" class="article-list">
    <ArticleItem
      :key="article.id"
      :article="article"
      v-for="article in articles"
      :remove="removeArticle"
    />
  </ul>
</template>

<script>
import axios from "axios";
import ArticleItem from "@/components/ArticleItem";

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
    async fetchArticles() {
      this.load = true;
      try {
        const response = await axios.get("/api/v1/posts/").finally(() => {
          this.load = false;
        });
        this.articles = response.data;
      } catch (e) {
        console.log(e.message);
      }
    },
    async removeArticle(id) {
      this.load = true;
      try {
        await axios.delete(`/api/v1/posts/detail/${id}`).finally(() => {
          this.load = false;
        });
        await this.fetchArticles();
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

<style scoped></style>
