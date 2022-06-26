<template>
  <div>
    <button class="navbar-btn-menu" @click="openMenu">Menu</button>
    <transition name="fade" key="menu">
      <div v-if="menuActive" class="navbar-mobile_wrapper">
        <div class="close-btn-wrapper">
          <button class="close-btn" @click="closeMenu">
            <icon-base
              iconName="close-icon"
              width="20"
              heigth="20"
              view-box="0 0 17 17"
            >
              <close-icon />
            </icon-base>
          </button>
        </div>
        <nav class="navbar__mobile" @click="closeMenu">
          <router-link class="link" to="/" v-scroll-to="'#about'">
            Главная
          </router-link>
          <router-link class="link" to="/" v-scroll-to="'#services'">
            Услуги
          </router-link>
          <router-link class="link" to="/" v-scroll-to="'#cases'">
            Кейсы
          </router-link>
          <router-link v-if="isAuth" class="link" to="/articles">
            Статьи
          </router-link>
          <router-link class="link" to="/" v-scroll-to="'#feedback'">
            Контакты
          </router-link>
        </nav>
      </div>
    </transition>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import IconBase from "@/components/UI/IconBase";
import CloseIcon from "@/assets/icons/close-icon";

export default {
  name: "NavbarMobile",
  components: {
    CloseIcon,
    IconBase,
  },

  data() {
    return {
      menuActive: false,
    };
  },
  methods: {
    openMenu() {
      this.menuActive = true;
    },
    closeMenu() {
      this.menuActive = false;
    },
  },
  computed: {
    ...mapGetters({ isAuth: "auth/isAuth" }),
  },
};
</script>

<style lang="scss" scoped>
.navbar-btn-menu {
  background-color: transparent;
  outline: none;
  border: none;
  color: var(--color-white);
}

.navbar-mobile_wrapper {
  display: none;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  background-color: var(--color-bacground-black);

  .navbar__mobile {
    display: flex;
    flex-direction: column;
  }

  .link {
    padding: 13px;
    text-decoration: none;
    color: var(--color-white);
    text-align: center;
    font-size: 29px;
  }

  .close-btn-wrapper {
    display: flex;
    width: 100%;
    padding: 20px;
    justify-content: right;
  }

  .close-btn {
    background-color: transparent;
    width: 30px;
    height: 30px;
    outline: none;
    cursor: pointer;
    border: none;
  }
}

@media (max-width: 600px) {
  .navbar-mobile_wrapper {
    display: block;
  }
}
</style>
