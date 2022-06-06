<template>
  <button class="my-button">
    <slot v-if="!isLoad"></slot>
    <MySpinner v-if="isLoad" />
  </button>
</template>

<script>
export default {
  name: "MyButton",
  props: {
    isLoad: {
      type: Boolean,
      default() {
        return false;
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.my-button {
  width: 200px;
  padding: 0 20px;
  height: 39px;
  border-radius: var(--radius);
  border: none;
  background-color: var(--color-accent-70);
  color: var(--color-white);
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;

  &:hover {
    //transform: scale(1.1);
  }
}
</style>
