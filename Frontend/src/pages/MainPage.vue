<template>
  <section id="about" class="main-about">
    <div class="main-about-center">
      <h1 class="about_title">
        Тут пару строк или строчка о том, что мы делаем
      </h1>
      <MyButton>Заказать сайт</MyButton>
    </div>
    <a href="#" v-scroll-to="'#services'" class="main-about-arrow">
      <img src="@/assets/icons/arrow.svg" alt="arrow" />
    </a>
    <div class="circle-main-about"></div>
  </section>
  <section id="services" class="main-services">
    <h2>Услуги</h2>
    <ul class="main-services-list">
      <ServicesItem
        v-for="service in this.services"
        :service="service"
        :key="service.name"
      />
    </ul>
  </section>
  <cases-component />
  <feedback-component />
</template>

<script>
import ServicesItem from "@/components/ServicesItem";
import FeedbackComponent from "@/components/Main/Feedback";
import CasesComponent from "@/components/Main/Cases";

export default {
  buildModules: ["vue-ssr-carousel/nuxt"],
  name: "MainPage",
  components: { CasesComponent, FeedbackComponent, ServicesItem },
  data() {
    return {
      services: [
        {
          name: "Название 1",
          price: 5000,
          description:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus architecto autem dolore earum eos eum ex excepturi fugiat inventore, iure maiores nam officia praesentium qui repellendus sed tempore ullam veniam!",
        },
        {
          name: "Название 2",
          price: 6000,
          description:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus architecto autem dolore earum eos eum ex excepturi fugiat inventore, iure maiores nam officia praesentium qui repellendus sed tempore ullam veniam!",
        },
        {
          name: "Название 3",
          price: 10000,
          description:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus architecto autem dolore earum eos eum ex excepturi fugiat inventore, iure maiores nam officia praesentium qui repellendus sed tempore ullam veniam!",
        },
        {
          name: "Название 4",
          price: 8000,
          description:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus architecto autem dolore earum eos eum ex excepturi fugiat inventore, iure maiores nam officia praesentium qui repellendus sed tempore ullam veniam!",
        },
        {
          name: "Название 5",
          price: 2000,
          description:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus architecto autem dolore earum eos eum ex excepturi fugiat inventore, iure maiores nam officia praesentium qui repellendus sed tempore ullam veniam!",
        },
        {
          name: "Название 6",
          price: 5000,
          description:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus architecto autem dolore earum eos eum ex excepturi fugiat inventore, iure maiores nam officia praesentium qui repellendus sed tempore ullam veniam!",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.main-about {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: calc(668px - 80px);
  background: var(--color-bacground-black);
  color: var(--color-white);
  margin-top: -80px;
  padding-top: 80px;

  @media (max-width: 600px) {
    margin-top: -50px;
    padding-top: 50px;
  }

  @media (max-width: 425px) {
    height: 100vh;
  }
}

.main-about-center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  margin: 0 30px;
  z-index: 1;

  .about_title {
    text-align: center;
    font-size: 19px;
    font-weight: 400;
    margin-bottom: 40px;
  }
}

.circle-main-about {
  position: absolute;
  max-width: 500px;
  height: 500px;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  background-color: var(--color-accent);
  -webkit-box-shadow: 0 0 180px 124px var(--color-bacground-black) inset;
  -moz-box-shadow: 0 0 180px 124px var(--color-bacground-black) inset;
  box-shadow: 0 0 180px 124px var(--color-bacground-black) inset;
  opacity: 0.3;
  border-radius: 50%;
}

.main-about-arrow {
  margin-bottom: 10px;
  cursor: pointer;
}

.main-services {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: -80px;
  padding: 110px 50px 30px 50px;
  background-color: var(--color-white);

  @media (max-width: 600px) {
    margin-top: -50px;
    padding: 90px 50px 30px 50px;
  }

  h2 {
    font-size: 43px;
    font-weight: 600;
  }

  .main-services-list {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    row-gap: 55px;
    column-gap: 5%;
    max-width: 930px;
    list-style: none;
    margin-top: 50px;
  }

  @media (max-width: 900px) {
    .main-services-list {
      grid-template-columns: 1fr 1fr;
    }
  }

  @media (max-width: 600px) {
    .main-services-list {
      grid-template-columns: 1fr;
    }
  }
}
</style>
