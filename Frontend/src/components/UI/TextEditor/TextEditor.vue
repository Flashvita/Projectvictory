<template>
  <div class="editor-wrapper" :class="{ 'editor-active': active }">
    <ckeditor
      @blur="ofFocused"
      @focus="onFocused"
      :editor="editor"
      :value="modelValue"
      :config="editorConfig"
      :ref="'text-editor'"
      @input="onChangeData"
    ></ckeditor>
  </div>
</template>

<script>
import ClassicEditor from "@ckeditor/ckeditor5-editor-classic/src/classiceditor";
import Autoformat from "@ckeditor/ckeditor5-autoformat/src/autoformat.js";
import AutoImage from "@ckeditor/ckeditor5-image/src/autoimage.js";
import AutoLink from "@ckeditor/ckeditor5-link/src/autolink.js";
import Base64UploadAdapter from "@ckeditor/ckeditor5-upload/src/adapters/base64uploadadapter.js";
import BlockQuote from "@ckeditor/ckeditor5-block-quote/src/blockquote.js";
import Bold from "@ckeditor/ckeditor5-basic-styles/src/bold.js";
import Code from "@ckeditor/ckeditor5-basic-styles/src/code.js";
import Essentials from "@ckeditor/ckeditor5-essentials/src/essentials.js";
import FontBackgroundColor from "@ckeditor/ckeditor5-font/src/fontbackgroundcolor.js";
import FontColor from "@ckeditor/ckeditor5-font/src/fontcolor.js";
import FontSize from "@ckeditor/ckeditor5-font/src/fontsize.js";
import Heading from "@ckeditor/ckeditor5-heading/src/heading.js";
import HorizontalLine from "@ckeditor/ckeditor5-horizontal-line/src/horizontalline.js";
import Image from "@ckeditor/ckeditor5-image/src/image.js";
import ImageCaption from "@ckeditor/ckeditor5-image/src/imagecaption.js";
import ImageStyle from "@ckeditor/ckeditor5-image/src/imagestyle.js";
import ImageToolbar from "@ckeditor/ckeditor5-image/src/imagetoolbar.js";
import ImageUpload from "@ckeditor/ckeditor5-image/src/imageupload.js";
import Indent from "@ckeditor/ckeditor5-indent/src/indent.js";
import Italic from "@ckeditor/ckeditor5-basic-styles/src/italic.js";
import Link from "@ckeditor/ckeditor5-link/src/link.js";
import List from "@ckeditor/ckeditor5-list/src/list.js";
import MediaEmbed from "@ckeditor/ckeditor5-media-embed/src/mediaembed.js";
import Paragraph from "@ckeditor/ckeditor5-paragraph/src/paragraph.js";
import PasteFromOffice from "@ckeditor/ckeditor5-paste-from-office/src/pastefromoffice.js";
import Table from "@ckeditor/ckeditor5-table/src/table.js";
import TableToolbar from "@ckeditor/ckeditor5-table/src/tabletoolbar.js";
import TextTransformation from "@ckeditor/ckeditor5-typing/src/texttransformation.js";
import "./style.css";

export default {
  name: "TextEditor",
  props: {
    modelValue: {
      type: String,
      default() {
        return "";
      },
    },
  },
  methods: {
    onChangeData(data) {
      this.$emit("update:modelValue", data);
    },
    onFocused() {
      this.active = true;
    },
    ofFocused() {
      this.active = false;
    },
  },
  data() {
    return {
      active: false,
      editor: ClassicEditor,
      editorData: "",
      editorConfig: {
        plugins: [
          Autoformat,
          AutoImage,
          AutoLink,
          Base64UploadAdapter,
          BlockQuote,
          Bold,
          Code,
          Essentials,
          FontBackgroundColor,
          FontColor,
          FontSize,
          Heading,
          HorizontalLine,
          Image,
          ImageCaption,
          ImageStyle,
          ImageToolbar,
          ImageUpload,
          Indent,
          Italic,
          Link,
          List,
          MediaEmbed,
          Paragraph,
          PasteFromOffice,
          Table,
          TableToolbar,
          TextTransformation,
        ],
        toolbar: {
          items: [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "fontBackgroundColor",
            "fontColor",
            "fontSize",
            "bulletedList",
            "numberedList",
            "horizontalLine",
            "|",
            "outdent",
            "indent",
            "|",
            "code",
            "imageUpload",
            "blockQuote",
            "insertTable",
            "mediaEmbed",
            "undo",
            "redo",
          ],
        },
        language: "ru",
        image: {
          toolbar: [
            "imageTextAlternative",
            "imageStyle:inline",
            "imageStyle:block",
            "imageStyle:side",
          ],
        },
        table: {
          contentToolbar: ["tableColumn", "tableRow", "mergeTableCells"],
        },
      },
    };
  },
};
</script>
<style lang="scss" scoped>
.editor-wrapper {
  margin: 30px 0;
  padding: 16px;
  background-color: var(--color-white);
  border-radius: var(--radius);
}

.editor-active {
  box-shadow: 0 0 0 2px var(--color-accent);
}
</style>
