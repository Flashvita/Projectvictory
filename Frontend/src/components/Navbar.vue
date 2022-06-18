<template>
  <nav class="navbar">
    <router-link class="link" to="/">Главная</router-link>
    <router-link class="link" to="/" v-scroll-to="'#services'">
      Услуги
    </router-link>
    <router-link class="link" to="/" v-scroll-to="'#cases'">Кейсы</router-link>
    <router-link v-if="isAuth" class="link" to="/articles">Статьи</router-link>
    <router-link class="link" to="/" v-scroll-to="'#feedback'">
      Контакты
    </router-link>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "NavbarComponent",
  computed: {
    ...mapGetters({ isAuth: "auth/isAuth" }),
  },
};
</script>

<style lang="scss" scoped>
.navbar {
  display: flex;
  flex-wrap: nowrap;

  .link {
    padding: 10px;
    text-decoration: none;
    color: var(--color-white);
  }
}
</style>
