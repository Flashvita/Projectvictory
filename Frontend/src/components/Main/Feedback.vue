<template>
  <section id="feedback" class="feedback-section">
    <div class="feedback">
      <div class="container">
        <div class="wrapper">
          <h2 class="feedback-title">Заказать сайт</h2>
          <p class="feedback-description">
            Выберите вид работ и оставьте свои контакты — с вами свяжется наш
            менеджер
          </p>
          <form class="form">
            <div class="wrapper-form">
              <div class="form-left">
                <MyInput
                  class="input"
                  v-model="this.name"
                  type="text"
                  placeholderText="Имя"
                  :error="this.nameError"
                  @update:model-value="this.nameError = false"
                />
                <MyInput
                  class="input"
                  v-model="this.email"
                  type="text"
                  placeholderText="Email"
                  :error="this.emailError"
                  @update:model-value="this.emailError = false"
                />
                <MySelect
                  :error="this.serviceError"
                  :options="servicesList"
                  :value="this.service"
                  placeholderText="Услуга"
                  @select="serviceHandler"
                  @update:model-value="this.serviceError = false"
                />
              </div>
              <div class="form-right">
                <MyTextarea
                  v-model="this.comments"
                  placeholderText="Комментарий"
                  :error="this.commentsError"
                  @update:model-value="this.commentsError = false"
                />
              </div>
            </div>
            <MyButton @click="this.sendRequest">Отправить заявку</MyButton>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "FeedbackComponent",
  data() {
    return {
      name: "",
      nameError: false,
      email: "",
      emailError: false,
      service: "",
      serviceError: false,
      servicesList: [
        { name: "Интернет-магазин", value: "1" },
        { name: "Лендинг", value: "2" },
        { name: "Телеграмм-бот", value: "3" },
      ],
      comments: "",
      commentsError: false,
    };
  },
  methods: {
    resetForm() {
      this.name = "";
      this.email = "";
      this.service = "";
      this.comments = "";
    },
    resetError() {
      this.nameError = false;
      this.emailError = false;
      this.serviceError = false;
      this.commentsError = false;
    },
    serviceHandler(serviceSelected) {
      this.serviceError = false;
      this.service = serviceSelected.name;
    },
    sendRequest(e) {
      e.preventDefault();
      if (this.name.length <= 0) this.nameError = true;
      if (this.email.length <= 0) this.emailError = true;
      if (this.service.length <= 0) this.serviceError = true;
      if (this.comments.length <= 0) this.commentsError = true;

      if (
        this.name.length > 0 &&
        this.email.length > 0 &&
        this.service.length > 0 &&
        this.comments.length > 0
      ) {
        console.log({
          name: this.name,
          email: this.email,
          service: this.service,
          comments: this.comments,
        });
        this.resetForm();
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.feedback-section {
  margin-top: -50px;
  padding-top: 50px;
}

.feedback {
  background-color: var(--color-bacground-black);
}

.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: var(--color-white);
  padding-bottom: 63px;

  .feedback-title {
    text-align: center;
    font-size: 43px;
    margin-top: 30px;
    margin-bottom: 20px;
  }

  .feedback-description {
    text-align: center;
  }

  .form {
    display: flex;
    flex-direction: column;
    align-items: center;

    @media (max-width: 768px) {
      width: 100%;
    }

    .wrapper-form {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 23px;
      margin-top: 60px;
      margin-bottom: 64px;

      .form-right {
        color: var(--color-bacground-black);
      }

      @media (max-width: 768px) {
        grid-template-columns: 1fr;
        width: 100%;
        padding: 0 10%;
      }

      @media (max-width: 425px) {
        padding: 0;
      }
    }

    .input {
      width: 300px;
      color: var(--color-bacground-black);
      margin-bottom: 23px;

      @media (max-width: 768px) {
        width: 100%;
      }
    }

    button:hover {
      background-color: var(--color-accent);
    }
  }
}
</style>
