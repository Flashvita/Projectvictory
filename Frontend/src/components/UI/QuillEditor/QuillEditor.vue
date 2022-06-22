<template>
  <QuillEditor
    contentType="html"
    theme="snow"
    toolbar="full"
    @focus="onFocused"
    @blur="ofFocused"
    @update:content="setContent"
    v-model:content="content"
  />
</template>

<script>
import { QuillEditor } from "@vueup/vue-quill";
import "@vueup/vue-quill/dist/vue-quill.snow.css";
import "./style.css";
import { mapGetters, mapMutations } from "vuex";

export default {
  components: { QuillEditor },

  props: {
    onFocused: {
      type: Function,
    },
    ofFocused: {
      type: Function,
    },
  },

  methods: {
    ...mapMutations({
      setTitle: "article/setTitle",
      setContent: "article/setContent",
    }),
  },
  computed: {
    ...mapGetters({
      content: "article/content",
      loadedArticle: "article/loadedArticle",
    }),
  },
};
</script>
