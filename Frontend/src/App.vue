<template>
  <HeaderComponent />
  <main class="app-main">
    <component :is="layout">
      <router-view />
    </component>
  </main>
  <FooterComponent />
  <!--  <MyButton @click="onShowModal">Открыть модальное окно</MyButton>-->
  <!--  <MyModal v-model:show="modalVisible">-->
  <!--    <div>text</div>-->
  <!--  </MyModal>-->
</template>

<script>
import HeaderComponent from "@/components/Header";
import FooterComponent from "@/components/Footer";
import LayoutArticles from "@/layout/LayoutArticles";
import EmptyLayout from "@/layout/EmptyLayout";
// import axios from "axios";
import { mapActions } from "vuex";

export default {
  components: { FooterComponent, HeaderComponent, LayoutArticles, EmptyLayout },
  computed: {
    layout() {
      return this.$route.meta.layout || "EmptyLayout";
    },
  },
  methods: {
    ...mapActions({
      getMe: "auth/getMe",
    }),
  },
  mounted() {
    if (this.$store.state.auth.isAuth) {
      this.getMe();
    }
  },
};
</script>

<style lang="scss">
html {
  box-sizing: border-box;
  height: 100%;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  overflow-anchor: none;
  scroll-behavior: smooth;
  font-family: "Roboto-Regular", sans-serif;
  color: var(--color-text-black);
  height: 100%;
}

ul {
  list-style: none;
}

li {
  margin: 0;
  padding: 0;
}

img {
  max-width: 100%;
  vertical-align: bottom;
}

:root {
  --color-white: #ffffff;
  --color-accent: #ff0a7f;
  --color-error: #ff0062;
  --color-accent-70: rgba(255, 10, 127, 0.7);
  --color-text-black: rgba(23, 9, 47, 0.7);
  --color-bacground-black: #17092f;
  --color-bacground-grey: #b8b5c1;
  --color-yelow: #faff00;

  --font-Thin: "Roboto-Thin", sans-serif;
  --font-light: "Roboto-Light", sans-serif;
  --font-Regular: "Roboto-Regular", sans-serif;
  --font-bold: "Roboto-Bold", sans-serif;

  --radius: 15px;
}

.app {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}

.app-main {
  background-color: var(--color-bacground-grey);
  flex: 1 1 auto;
  display: flex;
  margin-top: 80px;
}

.container {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 0 20px;
}

.carousel {
  .carousel__prev,
  .carousel__next {
    background-color: transparent;
    width: 60px;

    @media (max-width: 500px) {
      display: none;
    }
  }

  .carousel__next {
    right: -20px;
  }

  .carousel__prev {
    left: -20px;
  }

  .carousel__prev--in-active,
  .carousel__next--in-active {
    display: none;
  }

  .carousel__icon {
    fill: var(--color-bacground-black);
  }
}
</style>
