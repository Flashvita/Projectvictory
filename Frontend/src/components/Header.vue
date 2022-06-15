<template>
  <header class="header" v-if="this.$route.path !== '/auth'">
    <div class="container">
      <div class="header-wrapper">
        <div>Logo</div>
        <NavbarComponent />
        <MyButton_link v-if="!isAuth" @click="$router.push('/auth')">
          Войти
        </MyButton_link>
        <MyButton_link v-else @click="this.logout"> Выйти </MyButton_link>
      </div>
    </div>
  </header>
</template>

<script>
import NavbarComponent from "@/components/Navbar";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "HeaderComponent",
  components: { NavbarComponent },
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
}

.header-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;

  button {
    font-size: 12px;
  }
}
</style>
