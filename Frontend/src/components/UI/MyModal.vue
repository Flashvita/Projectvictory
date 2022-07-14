<template>
  <div class="modal" v-if="show">
    <div class="modal__content">
      <icons-component
        :name="'burger-cancel'"
        class="modal__content__icon"
        @click="closeModal"
      />
      <slot></slot>
    </div>
    <div class="modal__background" @click="closeModal"></div>
  </div>
</template>

<script>
import IconsComponent from "@/assets/icons/icons-component";

export default {
  name: "MyModal",
  components: { IconsComponent },

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
  z-index: 999;

  &__content {
    z-index: 1;
    margin: auto;
    padding: 20px;
    min-width: 400px;
    //min-height: 100px;
    background: #fff;
    border-radius: var(--radius);

    &__icon {
      display: none;
      position: absolute;
      width: 16px;
      height: 16px;
      top: 20px;
      right: 20px;
      fill: var(--color-accent);

      @media (max-width: 600px) {
        display: block;
      }
    }

    @media (max-width: 600px) {
      width: 100%;
      height: 100%;
      border-radius: 0;
      min-width: 100%;
    }
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
