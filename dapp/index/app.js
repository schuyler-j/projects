
const app = Vue.createApp({
    data(){

        return{
            firstName: 'Wellford',
            upload: 'uploading your personality to the web, one bit at a time...',
            logo: 'logo2021 copy.png'
        }

    },
    methods: {
        async getUser() {

            this.upload = 'uploading...';
            for (var i = 0; i < 10; i++){
                this.upload = this.upload + 'uploading...';
            }
        },

    }
})



app.mount('#app')