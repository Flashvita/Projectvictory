<template>
  <button class="my-button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "MyButtonLink",
};
</script>

<style scoped>
.my-button {
  width: auto;
  /*padding: 0 20px;*/
  border: none;
  background-color: transparent;
  color: var(--color-white);
  cursor: pointer;
  font-size: 9px;
}
</style>
