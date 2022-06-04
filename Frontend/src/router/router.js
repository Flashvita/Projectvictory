import { createRouter, createWebHistory } from "vue-router";
import Main from "@/pages/MainPage";
import AuthPage from "@/pages/AuthPage";
import ArticlesPage from "@/pages/ArticlesPage";
import ArticleItemPage from "@/pages/ArticleItemPage";

const routes = [
  {
    path: "/",
    component: Main,
  },
  {
    path: "/auth",
    component: AuthPage,
  },
  {
    path: "/articles",
    component: ArticlesPage,
  },
  {
    path: "/articles/:id",
    component: ArticleItemPage,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
