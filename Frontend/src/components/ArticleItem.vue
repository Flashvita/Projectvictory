<template>
  <li class="article" @click="$router.push(`/articles/${article.id}`)">
    <h2 class="article-title">{{ article.title }}</h2>
    <p class="article-body">{{ article.body }}</p>
  </li>
</template>

<script>
export default {
  name: "ArticleItem",
  props: {
    article: {
      id: {
        type: String,
        required: true,
      },
      title: {
        type: String,
        required: true,
      },
      body: {
        type: String,
        required: true,
      },
    },
  },
  methods: {},
};
</script>

<style scoped></style>
