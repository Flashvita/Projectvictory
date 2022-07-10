<template>
  <div class="pagination" v-if="countComputed > 1">
    <my-button
      v-if="1 <= offsetChange - range - 1"
      @click="onChooseOffset(1)"
      class="offset"
      :class="{ offset_active: offsetChange === 1 }"
    >
      {{ 1 }}
    </my-button>
    <div class="offset_dot" v-if="1 <= offsetChange - range - 2">...</div>
    <template :key="offset" v-for="offset in countComputed">
      <my-button
        v-if="offset <= offsetChange + range && offset >= offsetChange - range"
        @click="onChooseOffset(offset)"
        class="offset"
        :class="{ offset_active: offsetChange === offset }"
      >
        {{ offset }}
      </my-button>
    </template>
    <div class="offset_dot" v-if="countComputed >= offsetChange + range + 2">
      ...
    </div>
    <my-button
      v-if="countComputed >= offsetChange + range + 1"
      @click="onChooseOffset(countComputed)"
      class="offset"
      :class="{ offset_active: offsetChange === countComputed }"
    >
      {{ countComputed }}
    </my-button>
    <my-button
      v-if="countComputed !== offsetChange"
      @click="onChooseOffset(offsetChange + 1)"
      class="offset offset_next"
    >
      Далее
    </my-button>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
export default {
  name: "MyPagination",
  components: { MyButton },
  props: {
    count: {
      type: Number,
      required: true,
    },
    limit: {
      type: Number,
      required: true,
    },
    handlerClick: {
      type: Function,
      required: true,
    },
  },
  computed: {
    countComputed: function () {
      return Math.ceil(this.count / this.limit);
    },
  },
  methods: {
    onChooseOffset(offset) {
      if (offset > 2) this.range = 1;
      if (offset > this.countComputed - 2) this.range = 2;
      if (offset > this.countComputed - 1) this.range = 3;
      if (offset < 3) this.range = 2;
      if (offset < 2) this.range = 3;
      this.handlerClick({ offset: offset - 1 });
      this.offsetChange = offset;
    },
  },
  data() {
    return {
      offsetChange: 1,
      range: 3,
    };
  },
};
</script>

<style lang="scss" scoped>
.pagination {
  display: flex;
  align-items: center;

  & .offset {
    width: 40px;
    height: 40px;
    margin-right: 20px;
    background-color: var(--color-white);
    border-radius: 3px;
    color: var(--color-text-black);

    &_dot {
      margin-right: 20px;
    }

    &_next {
      width: auto;
    }
  }

  & .offset_active {
    color: var(--color-accent);
  }
}
</style>
