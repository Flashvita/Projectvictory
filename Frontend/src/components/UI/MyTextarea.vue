<template>
  <div class="textarea-wrapper" :class="{ error: error }">
    <textarea
      class="textarea"
      :value="modelValue"
      @input="updateInput"
      @focus="focused = true"
      @blur="focused = false"
      :ref="'select_' + modelValue"
    />
    <div
      class="placeholder"
      :class="{
        placeholder_active: focused || modelValue.length > 0,
      }"
      @click="this.$refs['select_' + modelValue].focus()"
    >
      {{ placeholderText }}
    </div>
  </div>
</template>

<script>
export default {
  name: "MyTextarea",
  props: {
    type: [String],
    modelValue: [String, Number],
    placeholderText: String,
    error: Boolean,
  },
  data() {
    return {
      focused: false,
    };
  },
  methods: {
    updateInput(event) {
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
@keyframes errors {
  0% {
    transform: translateX(-2px);
  }
  10% {
    transform: translateX(3px);
  }
  20% {
    transform: translateX(-3px);
  }
  30% {
    transform: translateX(4px);
  }
  40% {
    transform: translateX(-4px);
  }
  50% {
    transform: translateX(4px);
  }
  60% {
    transform: translateX(-4px);
  }
  70% {
    transform: translateX(4px);
  }
  80% {
    transform: translateX(-3px);
  }
  90% {
    transform: translateX(3px);
  }
  100% {
    transform: translateX(0px);
  }
}

.textarea-wrapper {
  height: 100%;
  position: relative;

  .textarea {
    width: 100%;
    height: 100%;
    padding: 16px 14px 0;
    border-radius: var(--radius);
    border: 2px solid transparent;
    background-color: rgba(255, 255, 255, 0.62);
    font-size: 19px;
    color: var(--color-text-black);

    &:focus-visible {
      outline: 2px solid var(--color-accent);
    }
  }

  .placeholder {
    position: absolute;
    top: 11px;
    left: 14px;
    transition: all 0.3s;
    color: var(--color-text-black);
  }

  .placeholder_active {
    color: var(--color-accent);
    font-size: 10px;
    transform: translateY(-8px);
  }
}

.error {
  animation: errors 500ms;
  box-shadow: 0 0 0 2px var(--color-error);
  border-radius: var(--radius);
}
</style>
