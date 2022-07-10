<template>
  <li class="article">
    <div class="article__owner">
      <div class="avatar">
        <div v-if="!article.avatar" class="avatar__placeholder" />
        <img v-else :src="baseURL + 'media/' + article.avatar" alt="avatar" />
      </div>
      <div>{{ article.owner }}</div>
    </div>
    <h2 class="article__title">{{ article.title }}</h2>
    <div class="article__body" v-html="article.content"></div>
    <div class="article__buttons">
      <my-button
        class="btn__next"
        @click="$router.push(`/articles/${article.id}`)"
      >
        Читать далее
      </my-button>
      <my-button
        v-if="profile.is_admin"
        class="btn__basket"
        @click="this.onRemove(article.id, this.$route.query)"
      >
        <icons-component name="basket" class="btn__basket_icon" />
      </my-button>
    </div>
  </li>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import axios from "axios";
import MyButton from "@/components/UI/MyButton";
import IconsComponent from "@/assets/icons/icons-component";

export default {
  name: "ArticleItem",
  components: { MyButton, IconsComponent },

  props: {
    article: Object,
  },

  data() {
    return {
      baseURL: axios.defaults.baseURL,
    };
  },

  methods: {
    ...mapActions({
      getArticleOll: "article/getArticlesOll",
      removeArticle: "article/removeArticle",
    }),
    async onRemove(id, query) {
      await this.removeArticle(id);
      await this.getArticleOll(query);
    },
  },
  computed: {
    ...mapGetters({
      profile: "auth/profile",
    }),
  },
};
</script>

<style lang="scss" scoped>
.article {
  width: 100%;
  margin-bottom: 32px;
  padding: 20px 25px;
  background-color: var(--color-white);
  border-radius: 3px;

  &__owner {
    display: flex;
    border-radius: 3px;
    margin-bottom: 10px;
    align-items: flex-end;

    & .avatar {
      width: 30px;
      margin-right: 10px;
      border-radius: 3px;

      &__placeholder {
        width: 100%;
        height: 100%;
        background-color: var(--color-bacground-grey);
        border-radius: 3px;
      }
    }
  }

  &__title {
    margin-top: 20px;
  }

  &__body {
    margin: 20px 0;
  }

  &__buttons {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;

    & .btn__next {
      border-radius: 3px;
      background-color: transparent;
      border: 1px solid var(--color-accent);
      color: var(--color-accent);
      transition: all 0.5s;

      &:hover {
        background-color: var(--color-accent);
        color: var(--color-white);
      }
    }

    & .btn__basket {
      width: 30px;
      height: 30px;
      padding: 0;
      border-radius: 50%;
      background-color: transparent;

      &:hover .btn__basket_icon {
        fill: var(--color-accent);
      }

      &_icon {
        width: 20px;
        height: 20px;
        fill: var(--color-bacground-grey);
        transition: all 0.2s;
      }
    }
  }
}
</style>
