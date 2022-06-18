import { createApp } from "vue";
import App from "./App.vue";
import components from "@/components/UI";
import router from "@/router/router";
import store from "@/store";
import VueScrollTo from "vue-scrollto";
import "@/axios";
import CKEditor from "@ckeditor/ckeditor5-vue";

const app = createApp(App);

components.forEach((component) => {
  app.component(component.name, component);
});

app
  .use(router)
  .use(store)
  .use(VueScrollTo, {
    container: "body",
    duration: 500,
    easing: "ease",
    offset: 0,
    force: true,
    cancelable: true,
    onStart: false,
    onDone: false,
    onCancel: false,
    x: false,
    y: true,
  })
  .use(CKEditor)
  .mount("#app");
