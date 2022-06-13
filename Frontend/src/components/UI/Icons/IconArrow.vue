<template>
  <div :class="{ 'arrow-down': isRotate }" class="arrow" />
</template>

<script>
export default {
  name: "IconArrow",
  props: {
    isRotate: {
      type: Boolean,
      default() {
        return false;
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.arrow {
  width: 100%;
  height: 100%;
  transition: all 0.1s;
  transform: rotate(0deg);
  cursor: pointer;

  &:before {
    content: "";
    position: absolute;
    top: 10px;
    left: 3px;
    width: 50%;
    height: 2px;
    background-color: var(--color-text-black);
    transform: rotate(45deg);
  }
  &:after {
    content: "";
    position: absolute;
    top: 10px;
    right: 2px;
    width: 50%;
    height: 2px;
    background-color: var(--color-text-black);
    transform: rotate(-45deg);
  }
}

.arrow-down {
  transform: rotate(90deg);
}
</style>
