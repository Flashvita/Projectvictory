import { createRouter, createWebHistory } from "vue-router";
import Main from "@/pages/MainPage";
import AuthPage from "@/pages/AuthPage";
import ArticleItemPage from "@/components/Articles/ArticleItemPage";
import ArticleCreate from "@/components/Articles/ArticleCreate";
import ArticleList from "@/components/Articles/ArticleList";
import NotFound from "@/pages/404";
import store from "@/store";

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
    meta: { layout: "LayoutArticles" }, // для приватной странички добавить requiresAuth: true
    component: ArticleList,
  },
  {
    path: "/articles/create",
    name: "articleCreate",
    meta: { layout: "LayoutArticles" },
    component: ArticleCreate,
  },
  {
    path: "/articles/:id",
    name: "articleItemPage",
    meta: { layout: "LayoutArticles" },
    component: ArticleItemPage,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "notFound",
    component: NotFound,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((route) => route.meta?.requiresAuth)) {
    if (store.state.auth.isAuth) {
      next();
    } else {
      next("/auth");
    }
  } else {
    next();
  }
});

export default router;
