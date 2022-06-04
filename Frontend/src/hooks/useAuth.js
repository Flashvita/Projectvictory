import axios from "axios";
import { ref } from "vue";

export function useAuth(name, email, password) {
  const loading = ref(false);
  const isAuth = ref(false);
  const isAuthError = ref(false);
  const token = ref("");

  // if (state.password !== state.confirmPassword) {
  //   commit("setErrorConfirmPassword", true);
  //   return;
  // }
  loading.value = true;
  const fetching = async () => {
    try {
      const response = await axios.post(
        "https://jsonplaceholder.typicode.com/user",
        {
          name,
          email,
          password,
        }
      );
      console.log(response);
      const token_res = "здесь будет токен";
      if (token_res) {
        localStorage.setItem("isAuth", JSON.stringify(true));
        localStorage.setItem("token", JSON.stringify(token_res));
        token.value = token_res;
        isAuth.value = true;
      }
    } catch (e) {
      if (e.response.status === 404) {
        isAuthError.value = true;
      } else {
        console.log(e);
      }
    } finally {
      loading.value = false;
    }
  };

  // onMounted(fetching);

  return {
    fetching,
    loading,
    isAuth,
    isAuthError,
  };
}
