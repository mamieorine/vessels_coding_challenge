import { createApp } from 'vue';
import VueGoogleMaps from "@fawmi/vue-google-maps";

import '@/assets/main.css'
import App from '@/App.vue'

const APIKEY = 'AIzaSyBmGmH6S8KlukMJrFMkpjL9cCtHz-dem88';

createApp(App).use(VueGoogleMaps, {
    load: {
      key: APIKEY
    }
}).mount('#app')
