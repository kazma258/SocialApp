import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false

// 添加全局請求攔截器
axios.interceptors.request.use(
  config => {
    // 嘗試從localStorage中取出token
    const token = localStorage.getItem('token')
    // 如果有token就添加到config的headers中
    if (token) {
      config.headers.authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// 將axios添加到Vue的原型中
Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
