<template>
    <div>
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ garage.name }}</h5>
                <p class="card-subtitle text-muted">{{ garage.brand }}</p>
                <p class="card-subtitle text-muted text-uppercase">{{ garage.postal_country }}</p>
                <span></span>
                <a href="#" class="card-link" @click.prevent="refresh">Refresh</a>
                <template v-if="!editing">
                    <a href="#" class="card-link" @click.prevent="editing = !editing">Edit</a>                    
                    <!-- pve aanpassing voor clickable 'list-cars' tekst -->
                    <!-- <a href="#" class="card-link text-muted text-uppercase" @click.prevent="listCars">List of Cars</a> -->
                    <router-link :to="{ name: 'cars', params: { garageId:garage.id } }" tag="a" class="card-link">List of Cars</router-link>
                    <a href="#" class="card-link text-danger" @click.prevent="deleteGarage">Delete Garage</a>
                </template>
                <template v-else>
                    <!-- <a href="#" class="card-link disabled" @click.prevent="save">Save</a> -->
                    <a href="#" class="card-link text-danger" @click.prevent="editing = !editing; Object.assign(garage, updated_garage)">Cancel</a>
                </template>
            </div>
            <transition name="fade" mode="out-in">
                <garage-form v-if="editing" :garage="garage" @change="editing = false; Object.assign(updated_garage, garage)"></garage-form>
            </transition>
        </div>
    </div>
</template>

<script>
    import GarageForm from "./garage-form";
    export default {
        name: "garage-list-item",
        components: {
            'garage-form': GarageForm
        },
        props: {
            garage: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                updated_garage: {},
                editing: false
            }
        },
        mounted() {
            this.updated_garage = Object.assign({}, this.garage)
        },
        methods: {
            // save() {
            //     this.editing = false
            //     $.ajax({
            //         type: 'PUT',
            //         contentType: 'application/json',
            //         url: `/garages/`,
            //         data: JSON.stringify(this.garage)
            //     }).then((data) => {
            //         // this.$emit('change', data)
            //         Object.assign(this.updated_garage, this.garage)
            //     }).always(() => {
            //     })
            // },
            deleteGarage() {
                $.ajax({
                    type: 'DELETE',
                    contentType: 'application/json',
                    url: `/garages/`,
                    data: JSON.stringify({'garage': this.garage.id})
                }).then((data) => {
                    this.$emit('change', data)
                }).always(() => {
                })
            },
            // pve hier zou een lijst met CARS moeten worden 'opgebouwd'
            // pve geeft een change-event
            // listCars() {
            //     $.ajax({
            //         type: 'LIST',
            //         contentType: 'application/json',
            //         url: `/${this.garage.id}/carlist/`,
            //         data: JSON.stringify({'garage': this.garage.id})
            //     }).then((data) => {
            //         this.$emit('change', data)
            //     }).always(() => {
            //     })
            // },
            refresh() {
                $.ajax({
                    type: 'GET',
                    contentType: 'application/json',
                    url: `/garages/?garage=${this.garage.id}`,
                }).then((data) => {
                    console.log(data)
                    Object.assign(this.garage, data) // watch does not work this way then we need to use deep watch
                    Object.assign(this.updated_garage, this.garage)
                }).always(() => {
                })
            }
        },
        watch: {
            garage(g) {
                console.log('garage update:' + g)
                Object.assign(this.updated_garage, g)
            }
        }
    }
</script>

<style scoped></style>