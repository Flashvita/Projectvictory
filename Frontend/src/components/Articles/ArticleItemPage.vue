<template>
  <div v-if="loadedArticle">Загрузка...</div>
  <div v-else class="article">
    <div class="article__body">
      <div class="article-owner">
        <div class="article-avatar">
          <div
            v-if="!article.owner_avatar"
            class="article-avatar-placeholder"
          />
          <img
            v-else
            :src="baseURL + 'media/' + article.owner_avatar"
            alt="avatar"
          />
        </div>
        <div>{{ article.owner }}</div>
        <router-link
          :to="{
            path: '/articles/create',
            query: {
              catalog: 'Разработка/Backend/Docker', // this.articleItem.path !!!!!!!!!!!!!!!!!!!!!!
              id: this.$route.params.id,
            },
          }"
          class="article-owner-button"
        >
          Редактировать
        </router-link>
      </div>
      <h2 class="article-title">{{ article.title }}</h2>
      <div class="article-body" v-html="article.content"></div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import axios from "axios";

export default {
  name: "ArticleItemPage",
  data() {
    return {
      baseURL: axios.defaults.baseURL,
    };
  },
  methods: {
    ...mapActions({
      getArticle: "article/getArticle",
    }),
  },
  computed: {
    ...mapGetters({
      article: "article/article",
      loadedArticle: "article/loadedArticle",
    }),
  },
  mounted() {
    this.getArticle({
      method: "GET",
      article: { id: this.$route.params.id },
    });
  },
};
</script>

<style lang="scss" scoped>
.article {
  width: 100%;

  &__body {
    width: 100%;
    margin-bottom: 32px;
    padding: 20px 25px;
    background-color: var(--color-white);
    border-radius: 3px;
  }
}

.article-owner {
  display: flex;
  border-radius: 3px;
  margin-bottom: 10px;
  align-items: flex-end;

  .article-owner-button {
    padding: 0;
    width: auto;
    margin-left: auto;
    border: none;
    color: var(--color-bacground-grey);
    text-decoration: none;
    transition: color 0.3s;

    &:hover {
      color: var(--color-accent);
    }
  }
}

.article-avatar {
  width: 30px;
  margin-right: 10px;
  border-radius: 3px;
}

.article-avatar-placeholder {
  width: 100%;
  height: 100%;
  background-color: var(--color-bacground-grey);
  border-radius: 3px;
}

.article-body {
  margin: 20px 0;
}
</style>
