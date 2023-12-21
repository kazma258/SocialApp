<template>
  <div>
    <h1>登入頁面</h1>
    <button @click="showRegisterForm">註冊</button>
    <button @click="showLoginForm">登入</button>

    <div v-if="showRegister">
      <!-- 註冊表單 -->
      <h2>註冊</h2>
      <div>
        <label for="email">Email:</label>
        <input type="text" id="email" placeholder="請輸入Email" />
      </div>
      <div>
        <label for="account">帳號:</label>
        <input type="text" id="account" placeholder="請輸入帳號" />
      </div>
      <div>
        <label for="password">密碼:</label>
        <input type="password" id="password" placeholder="請輸入密碼" />
      </div>
      <div>
        <label for="confirmPassword">確認密碼:</label>
        <input
          type="password"
          id="confirmPassword"
          placeholder="請再次輸入密碼"
        />
      </div>
      <div>
        <button @click="submitSignupForm">註冊</button>
      </div>
    </div>

    <div v-if="showLogin">
      <!-- 登入表單 -->
      <h2>登入</h2>
      <div>
        <label for="account">帳號:</label>
        <input type="text" id="account" placeholder="請輸入帳號" />
      </div>
      <div>
        <label for="password">密碼:</label>
        <input type="password" id="password" placeholder="請輸入密碼" />
      </div>
      <div>
        <button @click="submitSigninForm">登入</button>
      </div>
      <!-- 登入表單的內容 -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      showRegister: false,
      showLogin: false
    }
  },
  methods: {
    showRegisterForm () {
      this.showRegister = true
      this.showLogin = false
    },
    showLoginForm () {
      this.showRegister = false
      this.showLogin = true
    },
    submitSignupForm () {
      // 註冊表單送出
      
    },
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
