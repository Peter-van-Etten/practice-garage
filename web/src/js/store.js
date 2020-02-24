import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        msg: 'Welcome to The Best Garage-Application in Town',
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
    // hier zou ik een aanvulling verwachten:
    // - list van car-objecten  sleutel is garage-key en licenceplate?
    // - lokaal car-object,
    // - list van bijbehorende actions.
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