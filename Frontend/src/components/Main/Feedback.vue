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
              <div v-if="errorAPI" class="feedback__error_text">
                {{ errorTextAPI }}
              </div>
              <div class="form-left">
                <my-input
                  class="input"
                  type="text"
                  placeholderText="Имя"
                  :model-value="name"
                  :error="nameError"
                  @update:model-value="setName"
                />
                <my-input
                  class="input"
                  type="text"
                  placeholderText="Email"
                  :model-value="email"
                  :error="emailError"
                  @update:model-value="setEmail"
                />
                <my-input
                  class="input"
                  type="text"
                  placeholderText="Телефон"
                  :model-value="phone"
                  :error="phoneError"
                  @update:model-value="setPhone"
                />
                <my-select
                  :error="serviceError"
                  :options="servicesList"
                  :value="service"
                  placeholderText="Услуга"
                  @select="serviceHandler"
                />
              </div>
              <div class="form-right">
                <my-textarea
                  :model-value="message"
                  placeholderText="Комментарий"
                  :error="messageError"
                  @update:model-value="setMessage"
                />
              </div>
            </div>
            <my-button @click="this.sendRequest" :is-load="isLoad">
              Отправить заявку
            </my-button>
          </form>
        </div>
      </div>
    </div>
  </section>
  <my-modal v-model:show="isReady">
    <div class="feedback__modal">
      <p class="feedback__modal__text">Сообщение отправлено!</p>
      <my-button @click="isReady = false">Закрыть</my-button>
    </div>
  </my-modal>
</template>

<script>
import MyTextarea from "@/components/UI/MyTextarea";
import MyInput from "@/components/UI/MyInput";
import MySelect from "@/components/UI/MySelect";
import MyButton from "@/components/UI/MyButton";
import { mapActions, mapGetters, mapMutations } from "vuex";
import MyModal from "@/components/UI/MyModal";

export default {
  name: "FeedbackComponent",
  components: { MyButton, MySelect, MyInput, MyTextarea, MyModal },
  data() {
    return {
      isReady: false,
      servicesList: [
        { name: "Интернет-магазин", value: "1" },
        { name: "Лендинг", value: "2" },
        { name: "Телеграмм-бот", value: "3" },
      ],
    };
  },
  methods: {
    ...mapActions({
      sendFeedbackForm: "feedback/sendFeedbackForm",
    }),
    ...mapMutations({
      setName: "feedback/setName",
      setNameError: "feedback/setNameError",
      setEmail: "feedback/setEmail",
      setEmailError: "feedback/setEmailError",
      setPhone: "feedback/setPhone",
      setPhoneError: "feedback/setPhoneError",
      setService: "feedback/setService",
      setServiceError: "feedback/setServiceError",
      setMessage: "feedback/setMessage",
      setMessageError: "feedback/setMessageError",
    }),
    resetForm() {
      this.setName("");
      this.setEmail("");
      this.setPhone("");
      this.setService("");
      this.setMessage("");
    },
    resetError() {
      this.setNameError(false);
      this.setEmailError(false);
      this.setPhoneError(false);
      this.setServiceError(false);
      this.setMessageError(false);
    },
    serviceHandler(serviceSelected) {
      this.setServiceError(false);
      this.setService(serviceSelected.name);
    },
    async sendRequest(e) {
      e.preventDefault();
      if (this.name.length <= 0) this.setNameError(true);
      if (this.email.length <= 0) this.setEmailError(true);
      if (this.phone.length <= 0) this.setPhoneError(true);
      if (this.service.length <= 0) this.setServiceError(true);
      if (this.message.length <= 0) this.setMessageError(true);

      if (
        this.name.length > 0 &&
        this.email.length > 0 &&
        this.phone.length > 0 &&
        this.service.length > 0 &&
        this.message.length > 0
      ) {
        const response = await this.sendFeedbackForm({
          name: this.name,
          email: this.email,
          phone: this.phone,
          service: this.service,
          message: this.message,
        });
        this.resetForm();
        console.log(response);
        if (response.status === 200) {
          console.log(response.status);
          this.isReady = true;
        }
      }
    },
  },
  computed: {
    ...mapGetters({
      name: "feedback/name",
      nameError: "feedback/nameError",
      email: "feedback/email",
      emailError: "feedback/emailError",
      phone: "feedback/phone",
      phoneError: "feedback/phoneError",
      service: "feedback/service",
      serviceError: "feedback/serviceError",
      message: "feedback/message",
      messageError: "feedback/messageError",
      errorAPI: "feedback/errorAPI",
      errorTextAPI: "feedback/errorTextAPI",
      isLoad: "feedback/isLoad",
    }),
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

  &__modal {
    display: flex;
    flex-direction: column;
    align-items: center;

    &__text {
      margin-bottom: 20px;
    }
  }

  &__error_text {
    position: absolute;
    top: -30px;
    width: 100%;
    color: var(--color-accent);
    text-align: center;
  }
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
      position: relative;

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
