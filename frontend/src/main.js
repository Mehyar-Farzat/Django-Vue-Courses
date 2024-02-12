import { createApp } from 'vue'
import PrimeVue from 'primevue/config';
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap-grid.min.css'
//import 'bootstrap'
//import 'bootstrap-icons/font/bootstrap-icons.css'

//import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primevue/resources/themes/aura-dark-indigo/theme.css'
//import 'primevue/resources/themes/lara-dark-pink/theme.css'
//import 'primevue/resources/themes/lara-light-cyan/theme.css'

import 'primeicons/primeicons.css'


import Button from "primevue/button"
import Menubar from 'primevue/menubar';
import Card from 'primevue/card';

const app = createApp(App)

app.use(PrimeVue);
app.use(router)

app.component('Button', Button);
app.component('Menubar', Menubar);
app.component('Card', Card);



app.mount('#app')
