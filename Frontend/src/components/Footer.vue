<template>
  <footer v-if="this.$route.path !== '/auth'" class="footer">
    <div class="container">
      <div class="footer-wrapper">
        <div>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores et
          id nobis quisquam quo quos, saepe. Ab, cumque, dignissimos dolor
          facere facilis fugit natus odio officia praesentium quia sapiente,
          voluptate.
        </div>
        <small>projectvictory © 2022 v.1.0.4</small>
        <div>
          <div>
            --------------------------------------------------------------------
          </div>
          <div>
            --------------------------------------------------------------------
          </div>
          <div>
            --------------------------------------------------------------------
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterComponent",
};
</script>

<style lang="scss" scoped>
.footer {
  padding-top: 60px;
  padding-bottom: 60px;
  background-color: var(--color-bacground-black);
  border-top: 2px solid #000000;
}

.footer-wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 30px;
  align-items: end;
  justify-items: center;
  color: var(--color-white);

  @media (max-width: 600px) {
    grid-template-columns: 1fr;
  }

  small {
    font-size: 10px;
  }
}
</style>
