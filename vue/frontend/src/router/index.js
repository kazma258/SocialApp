import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ChatGroup from '@/components/Chat'
import Home from '@/views/Home'
import About from '@/views/About'
import Login from '@/views/Login'
import Chat from '@/views/Chat'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/About',
      name: 'About',
      component: About
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Chat',
      name: 'Chat',
      component: Chat
    },
    {
      path: '/Chat/:groupId',
      name: 'ChatGroup',
      component: ChatGroup
    }
    // Add more routes for other components if needed
  ]
})
