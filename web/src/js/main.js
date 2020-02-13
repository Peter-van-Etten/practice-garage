// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './routes'
import store from './store'

// import stylesheets
// import './assets/css/main.css'
import './assets/css/garage.css'

// Bootstrap with custom-colors scss
import 'bootstrap'
import './assets/css/bootstrap-overwrite.scss'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
})
