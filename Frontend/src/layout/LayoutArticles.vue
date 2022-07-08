<template>
  <div class="container">
    <div class="article">
      <div class="article__breadcrumbs">
        <my-button @click="openBurgerMenu" class="article__burger">
          <icons-component
            :name="burger ? 'burger-cancel' : 'burger'"
            class="article__burger__icon"
          />
        </my-button>
        <p>Разработка / Frontend / Разработка</p>
      </div>
      <transition name="fade">
        <div v-show="burger" class="article__menu">
          <menu-articles
            :list-categories="categoryList"
            :onShowModal="onShowModal"
            :openBurgerMenu="openBurgerMenu"
          />
          <my-button @click="onShowModal" class="article__menu_button">
            + добавить категорию
          </my-button>
        </div>
      </transition>
      <div class="article__layout">
        <router-view />
      </div>
    </div>
  </div>
  <my-modal v-model:show="modalVisible">
    <category-create :parent="this.parent" :ofShowModal="ofShowModal" />
  </my-modal>
</template>

<script>
import MenuArticles from "@/components/Articles/MenuArticles";
import { mapActions, mapGetters } from "vuex";
import MyModal from "@/components/UI/MyModal";
import MyButton from "@/components/UI/MyButton";
import CategoryCreate from "@/components/Articles/CategoryCreate";
import IconsComponent from "@/assets/icons/icons-component";

export default {
  computed: {
    ...mapGetters({
      isAuth: "auth/isAuth",
      categoryList: "article/categoryList",
    }),
  },
  name: "LayoutArticles",
  components: {
    CategoryCreate,
    MyButton,
    MyModal,
    MenuArticles,
    IconsComponent,
  },
  data() {
    return {
      burger: false,
      parent: null,
      modalVisible: false,
      articles: [],
      load: false,
      // listCategories: [
      //   {
      //     id: "1",
      //     name: "Разработка",
      //     path: "Разработка",
      //     listCategories: [
      //       {
      //         id: "11",
      //         name: "Backend",
      //         path: "Разработка/Backend",
      //         listCategories: [
      //           { id: "23", name: "Docker", path: "Разработка/Backend/Docker" },
      //         ],
      //       },
      //       { id: "12", name: "Frontend", path: "Разработка/Frontend" },
      //     ],
      //   },
      //   {
      //     id: "2",
      //     name: "Дизайн",
      //     path: "Дизайн",
      //     listCategories: [
      //       {
      //         id: "21",
      //         name: "Figma",
      //         path: "Дизайн/Figma",
      //       },
      //     ],
      //   },
      //   { id: "3", name: "Тестирование", path: "Тестирование" },
      // ],
    };
  },
  methods: {
    ...mapActions({
      getCategory: "article/getCategory",
    }),
    openBurgerMenu() {
      this.burger = !this.burger;
    },
    onShowModal(id) {
      this.modalVisible = true;
      if (typeof id === "object") return;
      this.parent = id;
    },
    ofShowModal() {
      this.modalVisible = false;
    },
  },
  mounted() {
    this.getCategory();
    if (window.innerWidth > 768) this.burger = true;
    addEventListener("resize", () => {
      this.burger = window.innerWidth > 768;
    });
  },
};
</script>

<style lang="scss" scoped>
.article {
  display: flex;
  padding: 30px 0;

  &__breadcrumbs {
    display: flex;
    font-size: 12px;
    align-items: center;
    position: fixed;
    top: 80px;
    left: 0;
    width: 100%;
    //min-height: 40px;
    padding: 16px 10px 8px;
    background-color: var(--color-bacground-grey);
    z-index: 1;

    @media (max-width: 600px) {
      top: 50px;
    }

    @media (min-width: 768px) {
      display: none;
    }
  }

  &__menu {
    margin: 40px 0 20px -20px;
    width: 450px;

    @media (max-width: 768px) {
      position: fixed;
      width: 100vw;
      height: 100vh;
      background-color: var(--color-bacground-grey);
      overflow-y: auto;
      top: 70px;
      //padding-top: 80px;
      z-index: 2;
    }

    &_button {
      background: transparent;
      width: auto;
      color: var(--color-bacground-black);
      padding: 0;
      margin-left: 32px;

      &:hover {
        color: var(--color-accent);
      }
    }
  }

  &__layout {
    display: flex;
    width: 100%;
    margin-left: 30px;
    //margin-top: 50px;
    //padding-top: 50px;

    @media (max-width: 768px) {
      margin-left: 0;
      //padding-top: 0;
    }
  }

  &__burger {
    width: auto;
    height: auto;
    background-color: transparent;
    padding: 0;
    border-radius: 50%;
    margin-right: 10px;

    &__icon {
      width: 20px;
      height: 20px;
      fill: var(--color-text-black);
    }
  }
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
