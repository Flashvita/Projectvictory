import { createRouter, createWebHistory } from "vue-router";
import Main from "@/pages/MainPage";
import AuthPage from "@/pages/AuthPage";
// import ArticlesPage from "@/pages/ArticlesPage";
import ArticleItemPage from "@/components/Articles/ArticleItemPage";
import ArticleCreate from "@/components/Articles/ArticleCreate";
import ArticleList from "@/components/Articles/ArticleList";

const routes = [
  {
    path: "/",
    meta: { layout: "EmptyLayout" },
    component: Main,
  },
  {
    path: "/auth",
    meta: { layout: "EmptyLayout" },
    component: AuthPage,
  },
  {
    path: "/articles",
    name: "articles",
    meta: { layout: "LayoutArticles" },
    component: ArticleList,
  },
  {
    path: "/articles/create",
    name: "ArticleCreate",
    meta: { layout: "LayoutArticles" },
    component: ArticleCreate,
  },
  {
    path: "/articles/:id",
    name: "ArticleItemPage",
    meta: { layout: "LayoutArticles" },
    component: ArticleItemPage,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
