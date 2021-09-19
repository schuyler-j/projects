
const app = Vue.createApp({
    data(){

        return{
            firstName: 'Wellford',
            logo: 'logo2021 copy.png'
        }

    },
    methods: {
        async getUser() {
            const res = await fetch('https://randomuser.me/api')
            const { results } = await res.json()


            this.firstName = results[0].name.first

        },

    }
})



app.mount('#app')