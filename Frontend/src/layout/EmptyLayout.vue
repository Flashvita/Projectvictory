<template>
  <div class="empty-container">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "EmptyLayout",
};
</script>

<style lang="scss" scoped>
.empty-container {
  width: 100%;
}
</style>
