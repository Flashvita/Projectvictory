<template>
  <div class="my-input-wrapper" :class="{ 'my-input-error': error }">
    <input
      :style="[backgroundColor, padding]"
      class="my-input"
      :value="modelValue"
      :type="type"
      @input="updateInput"
      @focus="focused = true"
      @blur="focused = false"
      :ref="'input_item_' + modelValue"
    />
    <div
      class="my-input-placeholder"
      :class="{
        'my-input-placeholder_active': focused || modelValue.length > 0,
      }"
      @click="this.focusInput(this.$refs, modelValue)"
    >
      {{ placeholderText }}
    </div>
  </div>
</template>
<script>
export default {
  name: "MyInput",
  props: {
    type: [String],
    modelValue: [String, Number],
    placeholderText: String,
    error: Boolean,
    backgroundColor: Object,
    padding: Object,
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
    focusInput(ref, input) {
      ref["input_item_" + input].focus();
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

.my-input-wrapper {
  position: relative;
}

.my-input {
  width: 100%;
  height: 46px;
  padding: 8px 14px 0;
  border-radius: var(--radius);
  border: 2px solid transparent;
  background-color: rgba(255, 255, 255, 0.62);
  font-size: 19px;
  color: var(--color-text-black);

  &:focus-visible {
    outline: none;
    box-shadow: 0 0 0 2px var(--color-accent);
  }
}

.my-input-error {
  animation: errors 500ms;
  box-shadow: 0 0 0 2px var(--color-error);
  border-radius: var(--radius);
}

.my-input-placeholder {
  position: absolute;
  top: 14px;
  left: 14px;
  transition: all 0.3s;
  color: var(--color-text-black);
  cursor: pointer;
}

.my-input-placeholder_active {
  color: var(--color-accent);
  font-size: 10px;
  transform: translateY(-8px);
}
</style>
