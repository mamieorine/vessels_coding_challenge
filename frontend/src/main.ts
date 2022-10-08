import { createApp } from 'vue'
import App from './App.vue'

import VueGoogleMaps from "@fawmi/vue-google-maps";
import './assets/main.css'

createApp(App).use(VueGoogleMaps, {
    load: {
      key: "AIzaSyBmGmH6S8KlukMJrFMkpjL9cCtHz-dem88"
    }
}).mount('#app')
