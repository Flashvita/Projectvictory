<template>
  <button class="my-button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "MyButton",
};
</script>

<style lang="scss" scoped>
.my-button {
  width: auto;
  padding: 0 20px;
  height: 39px;
  border-radius: var(--radius);
  border: none;
  background-color: var(--color-accent-70);
  color: var(--color-white);
  cursor: pointer;
  //transition: all 0.3s;

  &:hover {
    //transform: scale(1.1);
  }
}
</style>
