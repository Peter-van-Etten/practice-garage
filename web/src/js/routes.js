import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './components/Home'
import Garages from './components/garagelist'

Vue.use(VueRouter)


const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/garages', name: 'garages', component: Garages }
]


export default new VueRouter({ routes })