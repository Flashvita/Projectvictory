<template>
  <header class="header" v-if="this.$route.path !== '/auth'">
    <div class="container">
      <div class="header-wrapper">
        <div>Logo</div>
        <navbar-component />
        <div class="btn-auth">
          <my-button-link v-if="!isAuth" @click="$router.push('/auth')">
            Войти
          </my-button-link>
          <my-button-link v-else @click="this.logout"> Выйти </my-button-link>
        </div>
        <div class="navbar-mobile">
          <navbar-mobile />
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import NavbarComponent from "@/components/Navbar/Navbar";
import { mapGetters, mapActions } from "vuex";
import NavbarMobile from "@/components/Navbar/NavbarMobile";
import MyButtonLink from "@/components/UI/MyButton_link";

export default {
  name: "HeaderComponent",
  components: { MyButtonLink, NavbarMobile, NavbarComponent },
  methods: {
    ...mapActions({ logout: "auth/logout" }),
  },
  computed: {
    ...mapGetters({ isAuth: "auth/isAuth" }),
  },
};
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  width: 100%;
  height: 80px;
  background: var(--color-bacground-black);
  color: var(--color-white);
  position: fixed;
  z-index: 2;

  @media (max-width: 600px) {
    height: 50px;
  }
}

.header-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;

  button {
    font-size: 12px;

    @media (max-width: 600px) {
      display: none;
    }
  }

  .navbar-mobile {
    display: none;

    @media (max-width: 600px) {
      display: block;
    }
  }
}
</style>
