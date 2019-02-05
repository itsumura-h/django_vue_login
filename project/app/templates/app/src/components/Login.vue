<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-card-text>
              <v-form>
                <v-text-field prepend-icon="person" v-model="email" name="email" label="email" type="email"></v-text-field>
                <v-text-field prepend-icon="lock" v-model="password" name="password" label="パスワード" type="password"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="login">ログイン</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

    <v-snackbar
      v-model="snackbar"
      :top="true"
      :multi-line="'multi-line'"
      :timeout="3000"
      :vertical="'vertical'"
    >
      {{ error }}
      <v-btn
        color="pink"
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-content>
</template>

<script>
import API from '../common/API';
import router from '../router';

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
      // エラーsnackbar
      snackbar: false,
      error: '',
    };
  },
  methods: {
    login() {
      API.methods.login(this.email, this.password)
        .then((response) => {
          if (response.token) {
            // ローカルストレージにトークンを保存
            localStorage.setItem('token', response.token);
            router.push(this.$route.query.redirect);
          }
        })
        .catch((err) => {
          localStorage.removeItem('token'); // トークン削除
          this.error = 'メールアドレスとパスワードが一致しません';
          this.snackbar = true; // エラーメッセージ表示
        });
    },
  },
};
</script>

<style scoped>
</style>
