<template>
  <div class="auth">
    <div class="auth-container">
      <form @submit.prevent class="auth-form">
        <div class="auth-form-wrapper" v-if="isSignIn">
          <h1>Вход в аккаунт</h1>
          <div class="error-text" v-if="errorAuth">{{ messageErrorAuth }}</div>
          <MyInput
            :model-value="name"
            :error="errorAuth || nameError"
            @update:model-value="setName"
            type="text"
            placeholderText="Имя"
          />
          <MyInput
            :model-value="password"
            :error="errorAuth || passwordError"
            @update:model-value="setPassword"
            type="password"
            placeholderText="Пароль"
          />
          <div class="auth-form-btn">
            <MyButton @click="this.signIn"> Войти </MyButton>
          </div>
        </div>
        <div
          class="auth-form-wrapper auth-form-wrapper_signup"
          v-if="!isSignIn"
        >
          <h1>Создание аккаунта</h1>
          <div class="error-text" v-if="errorAuth">{{ messageErrorAuth }}</div>
          <MyInput
            :model-value="name"
            :error="errorAuth || nameError"
            @update:model-value="setName"
            type="text"
            placeholderText="Имя"
          />
          <MyInput
            :model-value="email"
            :error="errorAuth || emailError"
            @update:model-value="setEmail"
            type="text"
            placeholderText="Email"
          />
          <MyInput
            :model-value="password"
            :error="errorAuth || passwordError"
            @update:model-value="setPassword"
            type="password"
            placeholderText="Пароль"
          />
          <MyInput
            :model-value="confirmPassword"
            :error="errorAuth || confirmPasswordError"
            @update:model-value="setConfirmPassword"
            type="password"
            placeholderText="Подтверждение пароля"
          />
          <div class="auth-form-btn">
            <MyButton @click="this.signUp" :isLoad="isLoading">
              Зарегистрироваться
            </MyButton>
          </div>
        </div>
      </form>
      <MyButton_link @click="changeTypeAuth">
        {{
          this.isSignIn ? "У меня ещё нет аккаунта" : "У меня уже есть аккаунта"
        }}
      </MyButton_link>
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

export default {
  name: "AuthPage",
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
  width: 1026px;
  height: 512px;
  margin: auto;
  background: rgba(217, 217, 217, 0.48);
  border-radius: 47px;
}

.auth-form {
  margin-top: 37px;
  margin-bottom: 14px;
  width: 407px;

  h1 {
    text-align: center;
    font-size: 38px;
    font-family: var(--font-bold);
    color: var(--color-white);
  }

  .error-text {
    position: absolute;
    top: 53px;
    width: 100%;
    text-align: center;
    color: var(--color-error);
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
</style>
