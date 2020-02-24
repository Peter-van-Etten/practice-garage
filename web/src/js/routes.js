import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './components/Home'
import Garages from './components/garagelist'
import Cars from './components/carlist.vue'

Vue.use(VueRouter)


const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/garages', name: 'garages', component: Garages },
    { path: '/garages/:garageId/carlist', name: 'cars', props: true, component: Cars} 
]


export default new VueRouter({ routes })