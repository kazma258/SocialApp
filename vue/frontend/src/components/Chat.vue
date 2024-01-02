<template>
  <div class="app-container">
    <h1>群組列表</h1>
    <ul>
      <li v-for="group in groups" :key="group[0]">
        <span>{{ group[1] }}(ID:{{ group[0] }})</span>
        <button @click="goToChat(group[0])">進入聊天</button>
      </li>
    </ul>

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
      messages: [] // 頻道的歷史訊息
    }
  },
  methods: {
    goToChat (groupId) {
      window.location.href = `http://localhost:8080/#/Chat/${groupId}`
    },
    fetchHistory () {
      // 假設有一個方法可以根據 selectedChannel 從後端獲取歷史訊息
      // this.messages = ...
    }
  }
}
</script>

<!-- <style>
.app-container {
  /* 添加您的樣式 */
}
</style> -->
