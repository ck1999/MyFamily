import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/info',
    name: 'Info',
    component: () => import('../views/Info.vue') 
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue') 
  }, 
  {
    path: '/account',
    name: 'Account',
    component: () => import('../views/Account.vue') 
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/Admin.vue') 
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router