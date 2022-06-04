<template>
  <HeaderComponent />
  <main>
    <router-view />
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

export default {
  components: { FooterComponent, HeaderComponent },
  data() {
    return {
      // modalVisible: false,
    };
  },
  methods: {
    // onShowModal() {
    //   this.modalVisible = true;
    // },
  },
};
</script>

<style>
html {
  box-sizing: border-box;
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
}

ul {
  list-style: none;
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
  --color-yelow: #faff00;

  --font-Thin: "Roboto-Thin", sans-serif;
  --font-light: "Roboto-Light", sans-serif;
  --font-Regular: "Roboto-Regular", sans-serif;
  --font-bold: "Roboto-Bold", sans-serif;

  --radius: 15px;
}

.container {
  width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
</style>
