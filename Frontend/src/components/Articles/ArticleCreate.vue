<template>
  <div v-if="loadedArticle">Загрузка...</div>
  <div v-else class="main">
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
          :model-value="title"
          :error="false"
          type="text"
          @update:model-value="setTitle"
        />
      </div>
      <div class="article-wrapper" :class="{ 'quill-active': activeQuill }">
        <QuillEditor :onFocused="onFocused" :ofFocused="ofFocused" />
      </div>
      <MyButton @click="this.createArticle">Создать статью</MyButton>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions, mapMutations, mapGetters } from "vuex";
import QuillEditor from "@/components/UI/QuillEditor/QuillEditor";

export default {
  name: "ArticleCreate",
  components: { QuillEditor },

  data() {
    return {
      activeQuill: false,
      backgroundColor: {
        backgroundColor: "#ffffff",
      },
      padding: {
        padding: "0px 16px",
      },
      theme: "",
      load: false,
    };
  },

  methods: {
    ...mapActions({
      getArticle: "article/getArticle",
    }),
    ...mapMutations({
      setTitle: "article/setTitle",
      setContent: "article/setContent",
    }),
    onFocused() {
      this.activeQuill = true;
    },
    ofFocused() {
      this.activeQuill = false;
    },
    async createArticle(e) {
      e.preventDefault();
      console.log({
        category: this.$route.query.catalog,
        theme: this.theme,
        title: this.title,
        content: this.content,
      });
      try {
        const response = await axios.post("/api/v1/post/create/", {
          subcategory: this.$route.query.catalog,
          theme: this.theme,
          title: this.title,
          content: this.content,
          category: 1,
        });
        console.log(response);
      } catch (e) {
        console.log(e);
      }
    },
  },

  computed: {
    ...mapGetters({
      title: "article/title",
      content: "article/content",
      loadedArticle: "article/loadedArticle",
    }),
  },

  async mounted() {
    if (this.$route.query.id) {
      await this.getArticle({ id: this.$route.query.id });
    } else {
      this.setTitle("");
      this.setContent("");
    }
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

    @media (max-width: 600px) {
      font-size: 26px;
    }
  }

  .form-wrapper {
    //width: 740px;

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

    .article-wrapper {
      margin: 30px 0;
      position: relative;
      border: 2px solid transparent;
      border-radius: var(--radius);
    }

    .quill-active {
      border: 2px solid var(--color-accent);
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
