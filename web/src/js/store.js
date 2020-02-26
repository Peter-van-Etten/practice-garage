import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        msg: 'Welcome to the Garage-Application',
        garageList: [],
        garage: {
            name: '',
            brand: '',
            postal_country: ''
        },
        updated_garage: {},
        editing: false,
        myGarage: {}
    },
    mutations: {},
    actions: {
        load() {},
        save() {},
        resetForm() {},
        deleteGarage() {},
        refresh() {},
        garage() {},
        saveEdit() {}
    },
    getters: {}
})