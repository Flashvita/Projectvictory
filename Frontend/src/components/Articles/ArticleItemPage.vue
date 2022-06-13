<template>
  <div v-if="this.load">Загрузка...</div>
  <div v-if="!this.load">
    <h1>{{ this.articleItem.title }}</h1>
    <div>{{ this.articleItem.content }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ArticleItemPage",
  components: {},
  data() {
    return {
      articleItem: {},
      load: false,
    };
  },
  methods: {
    async fetchArticleItem() {
      this.load = true;
      try {
        const response = await axios
          .get(`/api/v1/posts/detail/${this.$route.params.id}`)
          .finally(() => {
            this.load = false;
          });
        this.articleItem = response.data;
        await this.$router.push({
          query: { catalog: "Разработка/Backend/Docker" },
        });
        console.log(this.articleItem);
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
