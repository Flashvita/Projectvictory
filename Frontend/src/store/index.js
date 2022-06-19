import { createStore } from "vuex";
import { authModule } from "@/store/authModule";
import { articleModule } from "@/store/articleModule";

export default createStore({
  modules: {
    auth: authModule,
    article: articleModule,
  },
});
