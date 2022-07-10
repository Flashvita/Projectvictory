<template>
  <div class="category-create" :class="{ 'my-input-error': categoryError }">
    <my-input
      :model-value="category"
      :error="categoryError"
      type="text"
      placeholderText="категория"
      @update:model-value="changeCategory"
    />
    <my-button :isLoad="loadedArticle" @click="onCreateCategory">
      Сохранить
    </my-button>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";
import { mapActions, mapGetters, mapMutations } from "vuex";

export default {
  name: "CategoryCreate",
  components: { MyInput, MyButton },
  props: {
    parent: [Number],
    ofShowModal: [Function],
  },
  data() {
    return {
      category: "",
    };
  },
  methods: {
    ...mapActions({
      createCategory: "article/createCategory",
    }),
    ...mapMutations({
      setCategoryError: "article/setCategoryError",
    }),
    changeCategory(value) {
      this.setCategoryError(false);
      this.category = value;
    },
    async onCreateCategory() {
      this.setCategoryError(false);
      if (this.category.length <= 0) {
        this.setCategoryError(true);
        return;
      }
      const category = await this.createCategory({
        title: this.category,
        parent: this.parent,
      });
      if (category.status === 201) {
        this.ofShowModal();
      }
    },
  },
  computed: {
    ...mapGetters({
      loadedArticle: "article/loadedArticle",
      categoryError: "article/categoryError",
    }),
  },
};
</script>

<style lang="scss" scoped>
.category-create {
  display: flex;

  & .my-input-wrapper {
    width: 350px;
    //box-shadow: 0 0 0 1px var(--color-bacground-black);
    border: 1px solid var(--color-bacground-black);
    border-radius: var(--radius);
    margin-right: 16px;
  }

  & .my-input-error {
    border: none;
  }

  & .my-button {
    width: 100px;
    height: auto;
  }
}
</style>
