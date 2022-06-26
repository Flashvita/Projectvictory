<template>
  <li class="main-services-item">
    <h3>{{ service.name }}</h3>
    <div class="main-services-item_price">от {{ service.price }} ₽</div>
    <div class="main-services-item_description">{{ service.description }}</div>
    <MyButton>Заказать</MyButton>
  </li>
</template>

<script>
export default {
  name: "ServicesItem",
  props: {
    service: {
      name: {
        type: String,
      },
      price: {
        type: Number,
      },
      description: {
        type: String,
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.main-services-item {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: 290px;
  background: radial-gradient(
    88.49% 88.49% at 11.89% 3.95%,
    var(--color-accent) 0%,
    var(--color-bacground-black) 100%
  );
  padding: 18px 27px;
  border-radius: 30px;

  h3 {
    font-weight: 600;
    font-size: 20px;
    color: var(--color-white);
  }

  .main-services-item_price {
    margin-top: 10px;
    font-weight: 600;
    font-size: 20px;
    color: var(--color-yelow);
  }

  .main-services-item_description {
    margin-top: 10px;
    margin-bottom: 20px;
    font-size: 12px;
    color: var(--color-white);
  }

  button {
    width: 100%;
    margin-top: auto;
    background-color: transparent;
    border: 1px solid var(--color-yelow);
    color: var(--color-yelow);
  }
}

@media (max-width: 600px) {
  //.main-services-item {
  //  height: auto;
  //}
}
</style>
