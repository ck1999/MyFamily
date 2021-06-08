<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p>{{ errors[0] }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log in</button>
                        </div>
                    </div>

                    <hr>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            const formData = {
                username: this.username,
                password: this.password
            }
            await axios.post("/api/v1/token/login/", formData).then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)

                    this.$router.go(-1)

                }).catch(error => {
                    this.errors.push('Неверный логин или пароль')
                })
            await axios
                .get('/api/v1/profile')
                .then(response => {
                    this.$store.commit('setInfo', response.data.staff, response.data.full_name)
                })
                .catch(error => {
                    console.log(error)
                })  
        }
    }
}
</script>