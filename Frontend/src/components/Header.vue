<template>
  <header class="header" v-if="this.$route.path !== '/auth'">
    <div class="container">
      <div class="header-wrapper">
        <div>Logo</div>
        <NavbarComponent />
        <MyButton_link @click="$router.push('/auth')">Войти</MyButton_link>
      </div>
    </div>
  </header>
</template>

<script>
import NavbarComponent from "@/components/Navbar";

export default {
  name: "HeaderComponent",
  components: { NavbarComponent },
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
