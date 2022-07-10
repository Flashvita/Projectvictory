<template>
  <li class="article">
    <div class="article-owner">
      <div class="article-avatar">
        <div v-if="!article.avatar" class="article-avatar-placeholder"></div>
        <img
          v-else
          :src="'http://45.8.248.219/media/' + article.avatar"
          alt="avatar"
        />
      </div>
      <div>{{ article.owner }}</div>
    </div>
    <h2 class="article-title">{{ article.title }}</h2>
    <div class="article-body" v-html="article.content"></div>
    <div class="article-button-block">
      <MyButton
        class="article-btn"
        @click="$router.push(`/articles/${article.id}`)"
      >
        Читать далее
      </MyButton>
      <div
        class="icon-remove"
        @click="this.onRemove(article.id, this.$route.query)"
      >
        <IconBase
          iconName="remove-icon"
          width="20"
          heigth="20"
          view-box="0 0 448 512"
        >
          <remove-basket />
        </IconBase>
      </div>
    </div>
  </li>
</template>

<script>
import RemoveBasket from "@/assets/icons/remove-basket";
import IconBase from "@/components/UI/IconBase";
import { mapActions } from "vuex";
import axios from "axios";

export default {
  name: "ArticleItem",
  components: { IconBase, RemoveBasket },

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
};
</script>

<style lang="scss" scoped>
.article {
  width: 100%;
  margin-bottom: 32px;
  padding: 20px 25px;
  background-color: var(--color-white);
  border-radius: 3px;

  .article-button-block {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;

    .article-btn {
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
  }

  .icon-remove {
    color: var(--color-bacground-grey);
    cursor: pointer;
    transition: all 0.3s;
    &:hover {
      color: var(--color-accent);
    }
  }
}
.article-owner {
  display: flex;
  border-radius: 3px;
  margin-bottom: 10px;
  align-items: flex-end;
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
