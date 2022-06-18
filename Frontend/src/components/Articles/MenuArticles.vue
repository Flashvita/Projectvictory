<template>
  <div :key="category.id" v-for="category in listCategories" class="category">
    <div
      class="category-title"
      :class="{
        'category-title-selected': this.$route.query.catalog === category.path,
      }"
    >
      <div class="category-title-wrapper">
        <span
          class="category-title-arrow"
          :class="{
            'category-title-arrow-rotate': this.changedCategory.includes(
              category.name
            ),
          }"
        >
          <IconBase
            v-if="category.listCategories && category.listCategories.length > 0"
            iconName="arrow-icon"
            width="10"
            heigth="10"
            view-box="0 0 284.929 284.929"
          >
            <arrow-icon />
          </IconBase>
        </span>
        <span
          class="category-title-name"
          @click="onChangeCategory(category.name, category.path)"
        >
          {{ category.name }}
        </span>
        <span
          class="add-btn-block"
          v-if="
            this.$route.query.catalog === category.path &&
            this.$route.path === '/articles'
          "
        >
          <MyButton class="add-btn" @click="addArticle(category.path)">
            + статья
          </MyButton>
          <MyButton class="add-btn"> + раздел</MyButton>
        </span>
      </div>
    </div>
    <div
      class="subcategory"
      :class="{
        'subcategory-active': this.changedCategory.includes(category.name),
      }"
    >
      <MenuArticles
        v-if="category.listCategories && category.listCategories.length > 0"
        :list-categories="category.listCategories"
      />
    </div>
  </div>
</template>

<script>
import IconBase from "@/components/UI/IconBase";
import ArrowIcon from "@/assets/icons/arrow-icon";
import { mapActions } from "vuex";

export default {
  name: "MenuArticles",
  components: { ArrowIcon, IconBase },
  data() {
    return {
      openingCategory: false,
      changedCategory: [],
    };
  },
  props: {
    listCategories: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  methods: {
    ...mapActions({
      getArticlesOll: "article/getArticlesOll",
    }),
    addArticle(address) {
      this.$router.push({
        path: "/articles/create",
        query: { catalog: address },
      });
    },
    onChangeCategory(name, address) {
      const path =
        this.$route.name === "ArticleCreate" ? "/articles/create" : "/articles";
      this.$router.push({ path: path, query: { catalog: address } });
      this.getArticlesOll(address);
      if (this.changedCategory.includes(name)) {
        const indexElement = this.changedCategory.findIndex(
          (element) => element === name
        );
        this.changedCategory.splice(indexElement, 1);
      } else {
        this.changedCategory = [...this.changedCategory, name];
      }
    },
  },
  mounted() {
    if (this.$route.query.catalog) {
      const lastElement = this.$route.query.catalog.split("/").length - 1;
      this.changedCategory = this.$route.query.catalog.split("/");
      this.onChangeCategory(
        this.$route.query.catalog.split("/")[lastElement],
        this.$route.query.catalog
      );
    }
  },
};
</script>

<style lang="scss" scoped>
.category {
  margin-left: 10px;
}

.category-title {
  position: relative;
  font-size: 18px;
  margin: 8px 0;
  //cursor: pointer;

  //&:hover .add-btn-block {
  //  opacity: 1;
  //}
}

.category-title-wrapper {
  display: flex;
  align-items: center;

  .category-title-name {
    cursor: pointer;
  }
}

.add-btn-block {
  //opacity: 0;
  display: flex;
  transition: all 0.6s;

  .add-btn {
    margin-left: 10px;
    padding: 7px;
    height: 18px;
    width: auto;
    color: var(--color-text-black);
    background-color: #d9d9d9;

    &:hover {
      background-color: var(--color-accent);
      color: var(--color-white);
    }
  }
}

.category-title-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 16px;
  transform: rotate(-90deg);
  transition: all 0.2s;
}

.category-title-arrow-rotate {
  transform: rotate(0deg);
}

.category-title-selected {
  font-weight: bold;
  color: var(--color-accent);
}

.subcategory {
  overflow: hidden;
  max-height: 1000px;
  transition: max-height 0.3s cubic-bezier(1, 0, 1, 0);
}

.subcategory-active {
  max-height: 0;
  transition: max-height 0.3s cubic-bezier(0, 1, 0, 1);
}
</style>
