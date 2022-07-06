<template>
  <div v-if="this.load">Загрузка...</div>
  <div v-else class="article">
    <div class="article__body">
      <div class="article-owner">
        <div class="article-avatar">
          <div
            v-if="!this.articleItem.avatar"
            class="article-avatar-placeholder"
          />
          <img v-else src="#" alt="avatar" />
        </div>
        <div>{{ this.articleItem.owner }}</div>
        <router-link
          :to="{
            path: '/articles/create',
            query: {
              catalog: 'Разработка/Backend/Docker', // this.articleItem.path !!!!!!!!!!!!!!!!!!!!!!
              id: this.articleItem.id,
            },
          }"
          class="article-owner-button"
        >
          Редактировать
        </router-link>
      </div>
      <h2 class="article-title">{{ this.articleItem.title }}</h2>
      <div class="article-body" v-html="this.articleItem.content"></div>
    </div>
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
  height: 30px;
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
