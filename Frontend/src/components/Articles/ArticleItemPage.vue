<template>
  <div v-if="loadedArticle">Загрузка...</div>
  <div v-else class="article">
    <div class="article__body">
      <div class="article__owner">
        <div class="avatar">
          <div v-if="!article.owner_avatar" class="avatar__placeholder" />
          <img
            v-else
            :src="baseURL + 'media/' + article.owner_avatar"
            alt="avatar"
          />
        </div>
        <div>{{ article.owner }}</div>
        <div v-if="isAuth" class="article__active">
          <router-link
            v-if="profile.is_admin || article.owner === profile.username"
            :to="{
              path: '/articles/create',
              query: {
                catalog: this.article.category_title, // this.article.road !!!!!!!!!!!!!!!!!!!!!!
                id: this.$route.params.id,
              },
            }"
            class="article__active__edit"
          >
            Редактировать
          </router-link>
          <MyButtonLink
            v-if="!article.is_active && profile.is_admin"
            class="article__active__publish"
            @click="onPublishArticle(article.id)"
          >
            Опубликовать
          </MyButtonLink>
          <MyButtonLink
            v-if="article.is_active && profile.is_admin"
            class="article__active__publish"
            @click="onPrivateArticle(article.id)"
          >
            Сделать
            {{ article.is_private ? "доступной для всех" : "приватной" }}
          </MyButtonLink>
        </div>
      </div>
      <h2 class="article__title">{{ article.title }}</h2>
      <div class="article__content" v-html="article.content" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import axios from "axios";
import MyButtonLink from "@/components/UI/MyButton_link";

export default {
  name: "ArticleItemPage",
  components: { MyButtonLink },
  data() {
    return {
      baseURL: axios.defaults.baseURL,
    };
  },
  methods: {
    ...mapActions({
      getArticle: "article/getArticle",
      patchArticle: "article/patchArticle",
    }),
    onPublishArticle(id) {
      this.patchArticle({
        id: id,
        is_active: true,
      });
    },
    onPrivateArticle(id) {
      this.patchArticle({
        id: id,
        is_private: !this.article.is_private,
      });
    },
  },
  computed: {
    ...mapGetters({
      article: "article/article",
      loadedArticle: "article/loadedArticle",
      isAuth: "auth/isAuth",
      profile: "auth/profile",
    }),
  },
  mounted() {
    this.getArticle({
      // method: "GET",
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

  &__owner {
    display: flex;
    border-radius: 3px;
    margin-bottom: 10px;
    align-items: flex-end;
  }

  &__active {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-left: auto;

    &__edit {
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

    &__publish {
      color: var(--color-bacground-grey);
      font-size: 16px;
      transition: color 0.3s;
      margin-top: 5px;

      &:hover {
        color: var(--color-accent);
      }
    }
  }

  &__title {
    margin-top: 40px;
  }

  &__content {
    margin: 20px 0;
  }
}

.avatar {
  width: 30px;
  height: 30px;
  margin-right: 10px;
  border-radius: 3px;

  &__placeholder {
    width: 100%;
    height: 100%;
    background-color: var(--color-bacground-grey);
    border-radius: 3px;
  }
}
</style>
