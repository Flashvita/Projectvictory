<template>
  <div class="select-wrapper" :class="{ 'select-error': error }">
    <div class="select">
      <div
        :style="backgroundColor"
        class="select-textTitle"
        :class="{ 'select-textTitle-error': error || this.isOpen }"
        @click="() => this.setOpenSelect(true)"
      >
        {{ value }}
      </div>
      <div class="select-arrow" @click="() => this.setOpenSelect(true)">
        <IconArrow :is-rotate="this.isOpen" />
      </div>
      <div
        class="select-placeholder"
        :class="{ 'select-placeholder_active': value.length > 0 }"
        @click="() => this.setOpenSelect(true)"
      >
        {{ placeholderText }}
      </div>
    </div>
    <div
      v-show="this.isOpen"
      class="backgroundSelect"
      @click="() => this.setOpenSelect(false)"
    />
    <div
      :style="backgroundColor"
      class="select-optionsBlock"
      :class="{ 'select-optionsBlock_active': this.isOpen }"
    >
      <ul class="select-options">
        <li
          v-for="option in options"
          :key="option.value"
          class="elementSelect"
          @click="this.selectedHandler(option)"
        >
          {{ option.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import IconArrow from "@/components/UI/Icons/IconArrow";
export default {
  name: "MySelect",
  components: { IconArrow },
  data() {
    return {
      isOpen: false,
    };
  },
  props: {
    backgroundColor: {
      type: Object,
      default() {
        return {};
      },
    },
    options: {
      type: Array,
      default() {
        return [];
      },
    },
    value: {
      type: String,
      default() {
        return "";
      },
    },
    placeholderText: {
      type: String,
      default() {
        return "";
      },
    },
    error: {
      type: Boolean,
      default() {
        return false;
      },
    },
  },
  methods: {
    setOpenSelect(isOpen) {
      this.isOpen = isOpen;
    },

    selectedHandler(option) {
      this.$emit("select", option);
      this.isOpen = false;
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

.select-wrapper {
  position: relative;
  color: var(--color-text-black);
}

.select-textTitle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 46px;
  border-radius: var(--radius);
  background-color: #a7a2b0;
  padding-left: 16px;
  padding-top: 8px;
  border: 1px solid var(--color-black);
  cursor: pointer;
  font-size: 19px;
  color: var(--color-text-black);
}

.select-textTitle-error {
  box-shadow: 0 0 0 2px var(--color-accent);
}

.select {
  position: relative;
}

.select-arrow {
  width: 26px;
  height: 20px;
  position: absolute;
  margin-left: auto;
  top: 14px;
  right: 16px;
  transform: rotate(-90deg);
  cursor: pointer;
}

.elementSelect {
  padding: 8px 16px;
  cursor: pointer;
  font-size: 19px;
  &:hover {
    background-color: var(--color-accent-70);
  }
}

.select-optionsBlock {
  position: absolute;
  width: 100%;
  top: 30px;
  background-color: #a7a2b0;
  border-radius: var(--radius);
  border: 1px solid var(--color-black);
  box-shadow: 0 4px 8px 3px rgba(0, 0, 0, 0.2);
  z-index: 1;
  padding: 16px 0;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s;
}

.select-optionsBlock_active {
  top: 51px;
  opacity: 1;
  visibility: visible;
}

.select-text-error {
  position: absolute;
  bottom: -16px;
  left: 0;
  color: red;
}

.backgroundSelect {
  position: fixed;
  content: "";
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: var(--color-bacdrop);
}

.select-placeholder {
  position: absolute;
  top: 14px;
  left: 14px;
  transition: all 0.3s;
  cursor: pointer;
}

.select-placeholder_active {
  color: var(--color-accent);
  font-size: 10px;
  transform: translateY(-8px);
}

.select-error {
  animation: errors 500ms;
  box-shadow: 0 0 0 2px var(--color-error);
  border-radius: var(--radius);
}
</style>
