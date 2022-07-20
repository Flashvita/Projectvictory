<template>
  <div class="search">
    <my-input
      class="search__input"
      placeholder-text="Название статьи или имя автора"
      :model-value="this.searchQuery"
      type="text"
      @update:model-value="isSearchArticle"
    />
    <my-button
      v-if="this.searchQuery.length > 0"
      class="search__clear"
      @click="isClearSearch"
    >
      <icons-component :name="'burger-cancel'" class="search__clear__icon" />
    </my-button>
    <my-button class="search__btn">Найти</my-button>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";
import IconsComponent from "@/assets/icons/icons-component";
import { mapActions } from "vuex";

export default {
  name: "ArticleSearch",
  components: { MyInput, MyButton, IconsComponent },
  data() {
    return {
      searchQuery: "",
      timerId: null,
    };
  },
  methods: {
    ...mapActions({
      getArticlesOll: "article/getArticlesOll",
    }),
    isSearchArticle(value) {
      this.searchQuery = value;
      if (value === "") {
        this.isClearSearch();
        clearTimeout(this.timerId);
        return;
      }
      this.$router.push({ query: { search: this.searchQuery } });
      clearTimeout(this.timerId);
      this.timerId = setTimeout(() => {
        this.getArticlesOll({ search: this.searchQuery });
      }, 2000);
    },
    isClearSearch() {
      this.searchQuery = "";
      this.$router.replace("");
    },
  },
};
</script>

<style lang="scss" scoped>
.search {
  display: flex;
  position: relative;

  &__input {
    border-radius: 3px 0 0 3px;
    width: 100%;

    &:deep(.my-input) {
      border-radius: 3px 0 0 3px;
      background-color: var(--color-white);

      &:focus-visible {
        box-shadow: inset 0 0 0 2px var(--color-accent);
      }

      @media (max-width: 768px) {
        padding-right: 38px;
      }
    }

    &:deep(.my-input-placeholder) {
      @media (max-width: 500px) {
        font-size: 12px;
      }
    }

    &:deep(.my-input-placeholder_active) {
      @media (max-width: 500px) {
        font-size: 10px;
        transform: translateY(-12px);
      }
    }
  }
  &__clear {
    position: absolute;
    right: 176px;
    top: 10px;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background-color: #f0f0f0;
    padding: 3px;

    @media (max-width: 768px) {
      right: 98px;
    }

    @media (max-width: 500px) {
      right: 68px;
    }

    &__icon {
      width: 15px;
      height: 15px;
      fill: var(--color-accent);
    }
  }

  &__btn {
    border-radius: 0 3px 3px 0;
    height: 100%;

    @media (max-width: 768px) {
      width: 100px;
    }

    @media (max-width: 500px) {
      font-size: 12px;
      width: 60px;
    }
  }

  @media (max-width: 768px) {
    margin-top: 30px;
  }
}
</style>
