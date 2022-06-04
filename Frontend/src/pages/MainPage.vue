<template>
  <section id="about" class="main-about">
    <div class="main-about-center">
      <h1>Тут пару строк или строчка о том, что мы делаем</h1>
      <MyButton>Заказать сайт</MyButton>
    </div>
    <div class="main-about-arrow">
      <img src="@/assets/icons/arrow.svg" alt="arrow" />
    </div>
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
  <section id="cases" class="main-cases">
    <h2>Кейсы</h2>
    <div class="carousel">
      <div class="main-cases-carousel">
        <div class="main-cases-carousel-item">
          <div class="main-cases-item">
            <img src="@/assets/img.png" alt="img" />
            <div class="main-case-description">
              <h3>Название</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem error excepturi fugiat incidunt mollitia neque nisi
                optio soluta! Doloremque est libero mollitia nam nobis quibusdam
                voluptas. Aut fugit laudantium sed.
              </p>
            </div>
          </div>
        </div>
        <div class="main-cases-carousel-item">
          <div class="main-cases-item">
            <img src="@/assets/img.png" alt="img" />
            <div class="main-case-description">
              <h3>Название</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem error excepturi fugiat incidunt mollitia neque nisi
                optio soluta! Doloremque est libero mollitia nam nobis quibusdam
                voluptas. Aut fugit laudantium sed.
              </p>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-btn carousel-btn-prev">
        <img src="@/assets/icons/next.svg" alt="prev" />
      </button>
      <button class="carousel-btn carousel-btn-next">
        <img src="@/assets/icons/next.svg" alt="next" />
      </button>
    </div>
  </section>
  <FeedbackComponent />
</template>

<script>
import ServicesItem from "@/components/ServicesItem";
import FeedbackComponent from "@/components/Main/Feedback";

export default {
  buildModules: ["vue-ssr-carousel/nuxt"],
  name: "MainPage",
  components: { FeedbackComponent, ServicesItem },
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
}

.main-about-center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;

  h1 {
    font-size: 19px;
    font-weight: 400;
    margin-bottom: 40px;
  }
}

.circle-main-about {
  position: absolute;
  width: 274px;
  height: 274px;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  background: #ff0a7f;
  filter: blur(200px);
}

.main-about-arrow {
  margin-bottom: 10px;
  cursor: pointer;
}

.main-services {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 20px;

  h2 {
    font-size: 43px;
    font-weight: 600;
  }

  .main-services-list {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    row-gap: 55px;
    column-gap: 75px;
    max-width: 930px;
    list-style: none;
    margin-top: 50px;
  }
}

.main-cases {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 20px;
  width: 913px;
  margin: 0 auto;

  h2 {
    font-size: 43px;
    font-weight: 600;
    margin-bottom: 64px;
  }

  .carousel {
    width: 930px;
    position: relative;

    .carousel-btn {
      position: absolute;
      top: 0;
      bottom: 0;
      margin: auto 0;
      width: 50px;
      height: 50px;
      background-color: transparent;
      border: none;
      border-radius: 50%;
      cursor: pointer;
    }

    .carousel-btn-prev {
      left: -53px;
    }

    .carousel-btn-next {
      right: -53px;
      transform: rotate(180deg);
    }
  }

  .main-cases-carousel {
    position: relative;
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    width: 100%;

    .main-cases-carousel-item {
      position: relative;
      display: inline-block;
      min-width: 913px;
      margin-right: 34px;
      scroll-snap-align: start;
      scroll-snap-stop: always;
    }
  }
  .main-cases-item {
    display: grid;
    grid-template-columns: 50% 50%;
    width: 100%;
    background-color: var(--color-bacground-black);
    border-radius: 33px;
    color: var(--color-white);

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 10px;
    }

    .main-case-description {
      padding: 28px 40px 28px 35px;

      h3 {
        font-size: 41px;
        font-weight: 600;
      }

      p {
        margin-top: 20px;
        font-size: 19px;
      }
    }
  }
}
</style>
