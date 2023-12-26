<template>
  <div>
    <p v-if="isLoggedIn">聊天画面</p>
    <p v-else>您未登录，请登录。
      <router-link to="/login">登录</router-link>
    </p>
    <div>
      <h2>創建新的群組</h2>
      <input type="text" v-model="newGroupName" placeholder="輸入群組名稱">
      <button @click="createGroup">創建</button>
    </div>

    <div>
      <h2>我加入的群組</h2>
      <ul>
        <li v-for="group in groups" :key="group.id">{{ group.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
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
    this.checkLoginStatus()
  },
  methods: {
    checkLoginStatus () {
      // 检查localStorage中是否存在token
      this.isLoggedIn = !!localStorage.getItem('token')
    },
    createGroup () {
      // 創建新的群組
      this.$http.post('http://localhost:5000/api/groups', { name: this.newGroupName })
        .then(response => {
          this.groups.push(response.data)
          this.newGroupName = ''
        })
    },
    created () {
      // 獲取當前用戶加入的所有群組
      this.$http.get('http://localhost:5000/api/groups')
        .then(response => {
          this.groups = response.data
        })
    }
  }
}
</script>
