import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import login from '../components/login'
import register from '../components/register'
import index from '../components/index'
import test from '../components/test'
import upload from '../components/upload'
import uptest from '../components/choujiang'

Vue.use(Router)

export default new Router({
  base: '/',
  mode:'history',
  routes: [
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/register/',
      name: 'register',
      component: register
    },
    {
      path: '/test/',
      name: 'test',
      component: test
    },
    {
      path: '/upload/',
      name: 'upload',
      component: upload
    },
    {
      path: '/uptest/',
      name: 'uptest',
      component: uptest
    },
  ]
})
