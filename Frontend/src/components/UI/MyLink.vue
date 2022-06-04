<template>
  <router-link class="my-link" to="to">
    <slot></slot>
  </router-link>
</template>

<script>
export default {
  name: "MyLink",
};
</script>

<style scoped>
.my-link {
  padding: 10px;
  text-decoration: none;
  color: black;
}
</style>
