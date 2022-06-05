<template>
  <a v-scroll-to="to" class="my-link" href="#">
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: "MyLink",
  props: {
    to: {
      type: String,
      default() {
        return "";
      },
    },
  },
};
</script>

<style scoped>
.my-link {
  padding: 10px;
  text-decoration: none;
  color: black;
}
</style>
