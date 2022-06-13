<template>
  <div class="container">
    <div class="article-wrapper">
      <div class="article-menu">
        <MenuArticles :list-categories="this.listCategories" />
      </div>
      <div class="articleLayout-container">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import MenuArticles from "@/components/Articles/MenuArticles";

export default {
  name: "LayoutArticles",
  components: { MenuArticles },
  data() {
    return {
      articles: [],
      load: false,
      listCategories: [
        {
          id: "1",
          name: "Разработка",
          path: "Разработка",
          listCategories: [
            {
              id: "11",
              name: "Backend",
              path: "Разработка/Backend",
              listCategories: [
                { id: "23", name: "Docker", path: "Разработка/Backend/Docker" },
              ],
            },
            { id: "12", name: "Frontend", path: "Разработка/Frontend" },
          ],
        },
        {
          id: "2",
          name: "Дизайн",
          path: "Дизайн",
          listCategories: [
            {
              id: "21",
              name: "Figma",
              path: "Дизайн/Figma",
            },
          ],
        },
        { id: "3", name: "Тестирование", path: "Тестирование" },
      ],
    };
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.article-wrapper {
  display: flex;
  padding: 30px 0;
}

.article-menu {
  margin: 40px 0 20px -20px;
  width: 200px;
}

.articleLayout-container {
  width: 100%;
  margin-left: 30px;
}
</style>
