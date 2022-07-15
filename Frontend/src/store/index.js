import { createStore } from "vuex";
import { authModule } from "@/store/authModule";
import { articleModule } from "@/store/articleModule";
import { feedbackModule } from "@/store/feedbackModule";

export default createStore({
  modules: {
    auth: authModule,
    article: articleModule,
    feedback: feedbackModule,
  },
});
