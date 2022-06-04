<template>
  <nav class="navbar">
    <MyLink to="/">Главная</MyLink>
    <MyLink to="#services">Услуги</MyLink>
    <MyLink to="#cases">Кейсы</MyLink>
    <MyLink to="#feedback">Контакты</MyLink>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>

<style lang="scss" scoped>
.navbar {
  display: flex;
  flex-wrap: nowrap;

  a {
    color: var(--color-white);
  }
}
</style>
