import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    isLoading: false,
    isStaff: false,
    full: '',
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    setInfo(state, staff, full) {
      state.isStaff = staff
      state.full = full
    },  
    removeInfo(state) {
      state.token = ''
      state.isAuthenticated = false
      state.isStaff = false
      state.full = ''
    }
  },
  actions: {
  },
  modules: {
  }
})