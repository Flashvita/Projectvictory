<template>
  <div :key="category.id" v-for="category in listCategories" class="category">
    <div
      class="category-title"
      :class="{
        'category-title-selected': this.$route.query.catalog === category.path,
      }"
    >
      <div @click="onChangeCategory(category.name, category.path)">
        <span class="category-title-arrow">
          <icon-arrow
            v-if="category.listCategories && category.listCategories.length > 0"
            :is-rotate="this.changedCategory.includes(category.name)"
          />
        </span>
        {{ category.name }}
      </div>
    </div>
    <div v-show="this.changedCategory.includes(category.name)">
      <MenuArticles
        v-if="category.listCategories && category.listCategories.length > 0"
        :list-categories="category.listCategories"
      />
    </div>
  </div>
</template>

<script>
import IconArrow from "@/components/UI/Icons/IconArrow";

export default {
  name: "MenuArticles",
  components: { IconArrow },
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
    onChangeCategory(name, adress) {
      const path =
        this.$route.name === "ArticleCreate" ? "/articles/create" : "/articles";
      this.$router.push({ path: path, query: { catalog: adress } });
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
  cursor: pointer;
}

.category-title-arrow {
  display: inline-block;
  width: 20px;
  height: 16px;
  transform: rotate(-90deg);
}
.category-title-selected {
  font-weight: bold;
  color: var(--color-accent);
}
</style>
