<template>
  <div v-if="!articleItem">Загрузка...</div>
  <div v-else>
    <h1>{{ articleItem.title }}</h1>
    <p>{{ articleItem.body }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ArticleItemPage",
  data() {
    return {
      articleItem: null,
    };
  },
  methods: {
    async fetchArticleItem() {
      this.load = true;
      try {
        const response = await axios
          .get(
            `https://jsonplaceholder.typicode.com/posts/${this.$route.params.id}`
          )
          .finally(() => {
            this.load = false;
          });
        this.articleItem = response.data;
      } catch (e) {
        console.log(e.message);
      }
    },
  },
  mounted() {
    this.fetchArticleItem();
  },
};
</script>

<style scoped></style>
