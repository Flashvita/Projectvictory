<template>
  <div class="main">
    <h1 class="title">Создание статьи</h1>
    <form class="form-wrapper">
      <div class="theme-wrapper">
        <div>Тема</div>
        <div class="theme-input-wrapper">
          <div class="theme-input-radio-item">
            <input
              class="theme-input"
              type="radio"
              id="red"
              value="red"
              v-model="this.theme"
            />
            <label
              class="theme-label"
              style="background-color: #ff0a7f"
              for="red"
            ></label>
          </div>
          <div class="theme-input-radio-item">
            <input
              class="theme-input"
              type="radio"
              id="yellow"
              value="yellow"
              v-model="this.theme"
            />
            <label
              style="background-color: #faff00"
              class="theme-label"
              for="yellow"
            ></label>
          </div>
          <div class="theme-input-radio-item">
            <input
              class="theme-input"
              type="radio"
              id="grin"
              value="grin"
              v-model="this.theme"
            />
            <label
              style="background-color: #0aff89"
              class="theme-label"
              for="grin"
            ></label>
          </div>
          <div class="theme-input-radio-item">
            <input
              class="theme-input"
              type="radio"
              id="white"
              value="white"
              v-model="this.theme"
            />
            <label
              style="background-color: #ffffff"
              class="theme-label"
              for="white"
            ></label>
          </div>
        </div>
      </div>
      <div class="name-wrapper">
        <div class="name-wrapper-title">Название</div>
        <MyInput
          :padding="padding"
          :backgroundColor="backgroundColor"
          :model-value="this.name"
          :error="false"
          type="text"
          @update:model-value="changeName"
        />
      </div>
      <div class="article-wrapper">
        <TextEditor
          @update:model-value="changeBodyArticle"
          :model-value="this.bodyArticle"
        />
      </div>
      <MyButton @click="createArticle">Создать статью</MyButton>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import TextEditor from "@/components/UI/TextEditor/TextEditor";

export default {
  name: "ArticleCreate",
  components: { TextEditor },
  methods: {
    changeName(e) {
      this.name = e;
    },
    changeBodyArticle(body) {
      this.bodyArticle = body;
    },
    async createArticle(e) {
      e.preventDefault();
      try {
        const response = await axios.post("/api/v1/post/create/", {
          category: this.$route.query.catalog,
          // subcategory: this.subcategory,
          // theme: this.theme,
          title: this.name,
          content: this.bodyArticle,
        });
        console.log(response);
      } catch (e) {
        console.log(e);
      }
      console.log({
        category: this.$route.query.catalog,
        subcategory: this.subcategory,
        theme: this.theme,
        name: this.name,
        bodyArticle: this.bodyArticle,
      });
    },
    changeCategory(selected) {
      this.categoryError = false;
      this.category = selected.name;
    },
    changeSubcategory(selected) {
      this.subcategoryError = false;
      this.subcategory = selected.name;
    },
  },
  data() {
    return {
      backgroundColor: {
        backgroundColor: "#ffffff",
      },
      padding: {
        padding: "0px 16px",
      },
      categoryError: false,
      category: "",
      categories: [
        { name: "Категория-1", id: "1" },
        { name: "Категория-2", id: "2" },
        { name: "Категория-3", id: "3" },
        { name: "Категория-4", id: "4" },
      ],
      subcategoryError: false,
      subcategory: "",
      subcategories: [
        { name: "Подкатегория-1", id: "1" },
        { name: "Подкатегория-2", id: "2" },
        { name: "Подкатегория-3", id: "3" },
        { name: "Подкатегория-4", id: "4" },
      ],
      theme: "",
      name: "",
      bodyArticle: "",
    };
  },
};
</script>

<style lang="scss" scoped>
.main {
  background-color: var(--color-bacground-grey);
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;

  .title {
    margin-top: 38px;
    font-size: 38px;
    font-weight: 700;
  }

  .form-wrapper {
    width: 740px;

    .category-wrapper {
      display: flex;
      flex-wrap: nowrap;
      justify-content: flex-start;

      .category-item {
        width: 237px;
        margin-right: 28px;
      }
    }

    .theme-wrapper {
      margin: 20px 0;

      .theme-input-wrapper {
        display: flex;
        margin-top: 10px;
      }
    }

    .name-wrapper-title {
      margin-bottom: 10px;
    }
  }
  .theme-input-radio-item {
    position: relative;
    width: 45px;
    height: 45px;
    margin-right: 18px;

    .theme-input {
      position: absolute;
      opacity: 0;
      z-index: -1;
    }

    .theme-input:checked + .theme-label {
      border: 2px solid white;
      box-shadow: 0 0 2px 2px var(--color-accent);
    }

    .theme-label {
      position: absolute;
      top: 0;
      left: 0;
      width: 45px;
      height: 45px;
      border-radius: 50px;
    }
  }
}
</style>
