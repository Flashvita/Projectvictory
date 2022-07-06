<template>
  <div class="modal" v-if="show">
    <div class="modal__content">
      <slot></slot>
    </div>
    <div class="modal__background" @click="closeModal"></div>
  </div>
</template>

<script>
export default {
  name: "MyModal",
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    closeModal() {
      this.$emit("update:show", false);
    },
  },
};
</script>

<style lang="scss" scoped>
.modal {
  display: flex;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;

  &__content {
    z-index: 1;
    margin: auto;
    padding: 20px;
    min-width: 400px;
    //min-height: 100px;
    background: #fff;
    border-radius: var(--radius);
  }

  &__background {
    display: flex;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0, 0, 0, 0.5);
  }
}
</style>
