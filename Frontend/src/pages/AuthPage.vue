<template>
  <div class="auth">
    <div class="auth-container">
      <form @submit.prevent class="auth-form">
        <div class="auth-form-wrapper" v-if="isSignIn">
          <h1 class="auth-form-title">Вход в аккаунт</h1>
          <transition name="bounce">
            <div class="error-text" v-show="errorAuth">
              {{ messageErrorAuth }}
            </div>
          </transition>
          <my-input
            :model-value="name"
            :error="errorAuth || nameError"
            @update:model-value="setName"
            type="text"
            placeholderText="Имя"
          />
          <my-input
            :model-value="password"
            :error="errorAuth || passwordError"
            @update:model-value="setPassword"
            type="password"
            placeholderText="Пароль"
          />
          <div class="auth-form-btn">
            <my-button @click="this.signIn"> Войти </my-button>
          </div>
        </div>
        <div
          class="auth-form-wrapper auth-form-wrapper_signup"
          v-if="!isSignIn"
        >
          <h1 class="auth-form-title">Создание аккаунта</h1>
          <transition name="bounce">
            <div
              class="error-text"
              v-show="errorAuth || emailError || passwordError"
            >
              {{ messageErrorAuth }}
            </div>
          </transition>
          <my-input
            :model-value="name"
            :error="errorAuth || nameError"
            @update:model-value="setName"
            type="text"
            placeholderText="Имя"
          />
          <my-input
            :model-value="email"
            :error="errorAuth || emailError"
            @update:model-value="setEmail"
            type="text"
            placeholderText="Email"
          />
          <my-input
            :model-value="password"
            :error="errorAuth || passwordError"
            @update:model-value="setPassword"
            type="password"
            placeholderText="Пароль"
          />
          <my-input
            :model-value="confirmPassword"
            :error="errorAuth || confirmPasswordError"
            @update:model-value="setConfirmPassword"
            type="password"
            placeholderText="Подтверждение пароля"
          />
          <div class="auth-form-btn">
            <my-button @click="this.signUp" :isLoad="isLoading">
              Зарегистрироваться
            </my-button>
          </div>
        </div>
      </form>
      <my-button-link @click="changeTypeAuth">
        {{
          this.isSignIn ? "У меня ещё нет аккаунта" : "У меня уже есть аккаунта"
        }}
      </my-button-link>
      <div class="auth-circle_1"></div>
      <div class="auth-circle_2"></div>
      <div class="auth-circle_3"></div>
      <div class="auth-circle_4"></div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState, mapGetters } from "vuex";
import router from "@/router/router";
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";
import MyButtonLink from "@/components/UI/MyButton_link";

export default {
  name: "AuthPage",
  components: { MyButtonLink, MyButton, MyInput },
  data() {
    return {
      isSignIn: true,
    };
  },
  methods: {
    ...mapActions({
      signIn: "auth/signIn",
      signUp: "auth/signUp",
    }),
    ...mapMutations({
      setName: "auth/setName",
      setEmail: "auth/setEmail",
      setEmailError: "auth/setEmailError",
      setPassword: "auth/setPassword",
      setPasswordError: "auth/setPasswordError",
      setConfirmPassword: "auth/setConfirmPassword",
      setErrorAuth: "auth/setErrorAuth",
      resetError: "auth/resetError",
    }),
    changeTypeAuth() {
      this.isSignIn = !this.isSignIn;
      this.resetError();
      this.$store.state.auth.name = "";
      this.$store.state.auth.email = "";
      this.$store.state.auth.password = "";
      this.$store.state.auth.confirmPassword = "";
    },
  },
  computed: {
    ...mapState({
      name: (state) => state.auth.name,
      email: (state) => state.auth.email,
      password: (state) => state.auth.password,
      confirmPassword: (state) => state.auth.confirmPassword,
      errorConfirmPassword: (state) => state.auth.confirmPasswordError,
    }),
    ...mapGetters({
      isLoading: "auth/isLoading",
      nameError: "auth/nameError",
      emailError: "auth/emailError",
      passwordError: "auth/passwordError",
      confirmPasswordError: "auth/confirmPasswordError",
      errorAuth: "auth/errorAuth",
      messageErrorAuth: "auth/setMessageErrorAuth",
    }),
  },
  mounted() {
    if (this.$store.state.auth.isAuth) {
      router.push("/");
    }
  },
};
</script>

<style lang="scss" scoped>
.auth {
  display: flex;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--color-bacground-black);
}

.auth-circle_1 {
  position: absolute;
  width: 0;
  height: 0;
  left: 60px;
  top: 476px;
  -webkit-box-shadow: 0 0 143px 129px var(--color-accent);
  -moz-box-shadow: 0 0 143px 129px var(--color-accent);
  box-shadow: 0 0 143px 129px var(--color-accent);
  border-radius: 50%;
  opacity: 0.6;
}

.auth-circle_2 {
  position: absolute;
  width: 0;
  height: 0;
  left: 285px;
  top: 93px;
  -webkit-box-shadow: 0 0 143px 92px rgba(10, 255, 137, 0.7);
  -moz-box-shadow: 0 0 143px 92px rgba(10, 255, 137, 0.7);
  box-shadow: 0 0 143px 92px rgba(10, 255, 137, 0.7);
  border-radius: 50%;
  opacity: 0.3;
}

.auth-circle_3 {
  position: absolute;
  width: 0;
  height: 0;
  left: 1023px;
  top: 493px;
  -webkit-box-shadow: 0 0 143px 92px rgba(10, 255, 137, 0.7);
  -moz-box-shadow: 0 0 143px 92px rgba(10, 255, 137, 0.7);
  box-shadow: 0 0 143px 92px rgba(10, 255, 137, 0.7);
  border-radius: 50%;
  opacity: 0.5;
}

.auth-circle_4 {
  position: absolute;
  width: 0;
  height: 0;
  left: 1016px;
  top: 38px;
  -webkit-box-shadow: 0 0 143px 92px var(--color-accent);
  -moz-box-shadow: 0 0 143px 92px var(--color-accent);
  box-shadow: 0 0 143px 92px var(--color-accent);
  border-radius: 50%;
  opacity: 0.3;
}

.auth-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 600px;
  width: 100%;
  margin: auto;
  background: rgba(217, 217, 217, 0.48);
  border-radius: 47px;
  padding-bottom: 30px;
  padding-left: 60px;
  padding-right: 60px;

  @media (max-width: 600px) {
    height: 100%;
    width: 100%;
    border-radius: 0;
  }

  @media (max-width: 425px) {
    padding-left: 16px;
    padding-right: 16px;
  }
}

.auth-form {
  margin-top: 37px;
  margin-bottom: 14px;
  width: 100%;

  .auth-form-title {
    text-align: center;
    font-size: 38px;
    font-family: var(--font-bold);
    color: var(--color-white);
    margin-bottom: 10px;

    @media (max-width: 425px) {
      font-size: 26px;
    }
  }

  .error-text {
    position: absolute;
    top: 53px;
    width: 100%;
    text-align: center;
    color: #c00052;
  }
}

.auth-form-wrapper {
  display: grid;
  grid-template-columns: 1fr;
  gap: 37px;
  position: relative;

  .auth-form-btn {
    display: flex;
    justify-content: center;
  }
}

.auth-form-wrapper_signup {
  gap: 30px;
}

.register-form-wrapper {
  position: relative;

  .my-input-wrapper {
    margin-bottom: 30px;
  }

  .auth-form-btn {
    display: flex;
    justify-content: center;
  }
}

.bounce-enter-active {
  animation: bounce-in 0.3s;
}
.bounce-leave-active {
  animation: bounce-in 0.3s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}
</style>
