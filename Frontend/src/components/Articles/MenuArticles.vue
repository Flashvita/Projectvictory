<template>
  <div :key="category.id" v-for="category in listCategories" class="category">
    <div
      class="category-title"
      :class="{
        'category-title-selected': this.$route.query.catalog === category.road,
      }"
    >
      <div class="category-title-wrapper">
        <span
          class="category-title-arrow"
          :class="{
            'category-title-arrow-rotate': this.changedCategory.includes(
              category.title
            ),
          }"
        >
          <icon-base
            v-if="category.listCategories && category.listCategories.length > 0"
            iconName="arrow-icon"
            width="10"
            heigth="10"
            view-box="0 0 284.929 284.929"
          >
            <arrow-icon />
          </icon-base>
        </span>
        <span
          class="category-title-name"
          @click="onChangeCategory(category.title, category.road)"
        >
          {{ category.title }}
        </span>
        <span
          class="add-btn-block"
          v-if="
            this.$route.query.catalog === category.road &&
            this.$route.path === '/articles'
          "
        >
          <my-button
            class="add-btn"
            @click="addArticle(category.road, category.id)"
          >
            +
            <icons-component name="document" class="icon__folder" />
          </my-button>
          <my-button @click="onShowModal(category.id)" class="add-btn">
            +
            <icons-component name="folder" class="icon__folder" />
          </my-button>
        </span>
      </div>
    </div>
    <div
      class="subcategory"
      :class="{
        'subcategory-active': this.changedCategory.includes(category.title),
      }"
    >
      <menu-articles
        v-if="category.listCategories && category.listCategories.length > 0"
        :list-categories="category.listCategories"
      />
    </div>
  </div>
</template>

<script>
import IconBase from "@/components/UI/IconBase";
import ArrowIcon from "@/assets/icons/arrow-icon";
import IconsComponent from "@/assets/icons/icons-component";
import { mapActions, mapMutations } from "vuex";
import MyButton from "@/components/UI/MyButton";

export default {
  name: "MenuArticles",
  components: { ArrowIcon, IconBase, MyButton, IconsComponent },

  data() {
    return {
      openingCategory: false,
      changedCategory: [],
    };
  },
  props: {
    openBurgerMenu: {
      type: Function,
    },
    onShowModal: {
      type: Function,
    },
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
    ...mapMutations({
      setCategoryId: "article/setCategoryId",
      setContent: "article/setContent",
      setTitle: "article/setTitle",
    }),
    addArticle(address, categoryId) {
      this.setCategoryId(categoryId);
      this.setContent("");
      this.setTitle("");
      this.$router.push({
        path: "/articles/create",
        query: { catalog: address },
      });
    },
    onChangeCategory(name, address) {
      if (window.innerWidth < 600) {
        this.openBurgerMenu();
      }
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

  @media (min-width: 600px) {
    margin-left: 20px;
  }
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
  display: flex;
  margin-left: 10px;
  transition: all 0.2s;

  .add-btn {
    margin-left: 3px;
    padding: 7px;
    height: 18px;
    width: auto;
    color: var(--color-text-black);
    background-color: #d9d9d9;

    &:hover {
      background-color: var(--color-accent);
      color: var(--color-white);

      .icon__folder {
        stroke: var(--color-white);
      }
    }
  }

  .icon__folder {
    width: 10px;
    height: 10px;
    margin-left: 4px;
    stroke: var(--color-text-black);
    transition: all 0.2s;
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
