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
        <label for="username">使用者名稱</label>
        <input type="text" id="username" placeholder="請輸入使用者" />
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
      axios
        .post('http://localhost:5000/api/register', {
          email: document.getElementById('email').value,
          account: document.getElementById('account').value,
          password: document.getElementById('password').value,
          username: document.getElementById('username').value
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(res => {
          if (res.data.success) {
            console.log(res.data)
            alert('註冊成功')
            this.showRegister = false
          } else {
            console.log(res.data)
            alert('註冊失敗')
          }
        })
        .catch(err => {
          console.log('Error: ', err)
        })
    },
    submitSigninForm () {
      // 登入表單送出
      axios
        .post('http://localhost:5000/api/login', {
          account: document.getElementById('account').value,
          password: document.getElementById('password').value
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(res => {
          if (res.data.success) {
            console.log(res.data.success)
            alert('登入成功')

            // 保存登入狀態
            localStorage.setItem('uid', res.data.success.uid)
            // Redirecting to the URL sent from the backend
            this.$router.push('/Chat')
            this.showLogin = false
          } else {
            console.log(res.data)
            alert('登入失敗')
          }
        })
        .catch(err => {
          console.log('Error: ', err)
        })
    }
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
