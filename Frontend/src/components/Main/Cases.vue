<template>
  <section id="cases" class="main-cases">
    <div class="container">
      <h2 class="cases-title">Кейсы</h2>
      <carousel :autoplay="3000" :wrap-around="true" :items-to-show="1">
        <slide v-for="slide in 3" :key="slide">
          <div class="cases-item">
            <img class="cases-item-img" src="@/assets/img.png" alt="img" />
            <div class="description">
              <h3 class="description-title">Название</h3>
              <p class="description-paragraph">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem error excepturi fugiat incidunt mollitia neque nisi
                optio soluta! Doloremque est libero mollitia nam nobs quicksand
                voluptas. Aut fugit laudantium sed.
              </p>
            </div>
          </div>
        </slide>
        <template #addons>
          <navigation />
        </template>
      </carousel>
    </div>
  </section>
</template>

<script>
import { Carousel, Slide, Navigation } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";

export default {
  name: "CasesComponent",
  components: {
    Carousel,
    Slide,
    Navigation,
  },
};
</script>

<style lang="scss" scoped>
.main-cases {
  background-color: var(--color-white);
  margin-top: -80px;
  padding-top: 80px;
  padding-bottom: 80px;

  @media (max-width: 600px) {
    margin-top: -50px;
    padding-top: 50px;
  }

  .container {
    padding: 0 50px;

    @media (max-width: 768px) {
      padding: 0 20%;
    }

    @media (max-width: 500px) {
      padding: 0 10%;
    }
  }
}

.cases-title {
  text-align: center;
  font-size: 43px;
  font-weight: 600;
  margin-bottom: 64px;
  margin-top: 50px;
}

.cases-item {
  display: grid;
  grid-template-columns: 50% 50%;
  width: 100%;
  background-color: var(--color-bacground-black);
  border-radius: 40px;
  color: var(--color-white);

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
    border-radius: 48px;
  }

  .cases-item-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
  }

  .description {
    padding: 28px 40px 28px 35px;
    text-align: left;

    .description-title {
      font-size: 41px;
      font-weight: 600;

      @media (max-width: 768px) {
        font-size: 30px;
      }
    }

    .description-paragraph {
      margin-top: 20px;
      font-size: 19px;

      @media (max-width: 768px) {
        font-size: 16px;
      }
    }
  }
}
</style>
