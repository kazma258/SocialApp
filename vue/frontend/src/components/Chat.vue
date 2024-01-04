<template>
  <div class="app-container">
    <h1>群組列表</h1>
    <ul>
      <li v-for="group in groups" :key="group[0]">
        <span>{{ group[1] }}(ID:{{ group[0] }})</span>
        <button @click="goToChat(group[0])">進入聊天</button>
      </li>
    </ul>

    <div class="create-channel">
      <h2>創建頻道</h2>
      <form @submit.prevent="createChannel">
        <input v-model="channelName" type="text" placeholder="輸入頻道名稱" required>
        <button type="submit">創建</button>
      </form>
    </div>

    <div class="channel-selector">
      <h2>選擇頻道</h2>
      <select v-model="selectedChannel">
        <option v-for="channel in channels" :key="channel.id">{{
          channel.name
        }}</option>
      </select>
      <button @click="fetchHistory">查詢歷史訊息</button>
    </div>

    <div class="message-history">
      <h2>歷史訊息</h2>
      <ul>
        <li v-for="message in messages" :key="message.id">
          {{ message.content }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    console.log('跳轉到聊天室')
    return {
      groups: [], // 群組數據
      channels: [], // 頻道數據
      selectedChannel: '', // 選中的頻道
      messages: [], // 頻道的歷史訊息
      channelName: '' // 創建頻道的名稱
    }
  },
  created () {
    // 獲取當前用戶加入的所有群組

    this.checkLoginStatus()
    console.log('獲取當前用戶加入的所有群組')
    console.log(localStorage.getItem('uid'))
    this.$http
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
    goToChat (groupId) {
      window.location.href = `http://localhost:8080/#/Chat/${groupId}`
    },
    fetchHistory () {
      // 假設有一個方法可以根據 selectedChannel 從後端獲取歷史訊息
      // this.messages = ...
    },
    createChannel () {
      // 創建新頻道
      let currentHash = window.location.hash
      let hashSegments = currentHash.split('/')
      let groupId = hashSegments[hashSegments.length - 1]
      console.log('當前所在頻道:', groupId)
      this.$http
        .post(`http://localhost:5000/api/createchannel`,
          {channelname: this.channelName, gid: groupId})
        .then(response => {
          alert('Channel created successfully')
          console.log(response)
        })
        .catch(error => {
          alert('Error creating channel')
          console.log(error)
        })
      console.log('創建頻道, 名稱:', this.channelName)
    }
  }
}
</script>

<!-- <style>
.app-container {
  /* 添加您的樣式 */
}
</style> -->
