<template>
  <div>
    <p v-if='isLoggedIn'>聊天画面</p>
    <p v-else>
      您尚未登入，請登入。
      <router-link to='/login'>登录</router-link>
    </p>
    <div>
      <h2>創建新的群組</h2>
      <input type='text' v-model='newGroupName' placeholder='輸入群組名稱' />
      <button @click='createGroup'>創建</button>
    </div>

    <div>
      <h2>我創建的群組</h2>
      <ul>
        <li v-for="group in groups" :key="group[0]">
          {{ group[1] }}
          <!-- 添加一个跳转按钮 -->
          <button @click="goToChat(group[0])">進入聊天</button>
        </li>
</ul>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ChatView',
  data () {
    return {
      // 初始设定用户状态为未登录
      isLoggedIn: false,
      // 新建群组的名称
      newGroupName: '',
      groups: []
    }
  },
  created () {
    // 獲取當前用戶加入的所有群組

    this.checkLoginStatus()
    console.log('獲取當前用戶加入的所有群組')
    console.log(localStorage.getItem('uid'))
    axios
      .post('http://localhost:5000/api/groups', {
        uid: localStorage.getItem('uid')
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        this.groups = response.data
        console.log(this.groups)
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    checkLoginStatus () {
      // 检查localStorage中是否存在token
      this.isLoggedIn = !!localStorage.getItem('uid')
    },
    createGroup () {
      // 創建新的群組
      this.$http
        .post('http://localhost:5000/api/groups', { name: this.newGroupName })
        .then(response => {
          this.groups.push(response.data)
          this.newGroupName = ''
        })
    },
    goToChat (groupId) {
      // 使用 JavaScript 的 window.location.href 进行跳转
      window.location.href = `http://localhost:8080/#/Chat/${groupId}`
    }
  }
}
</script>
