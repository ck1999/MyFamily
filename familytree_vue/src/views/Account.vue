<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Account info</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>

            <hr>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Account',
    components: {
    },
    data() {

    },
    mounted() {
        document.title = 'Account Info'
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeInfo')
            this.$router.push(this.$route.query.redirect || '/')
        },
    }
}
</script>