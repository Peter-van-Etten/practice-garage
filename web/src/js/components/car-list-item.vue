<template>
    <div>
        <div class="card">
            <div class="card-body">
                <!-- pve here the right key-field for a car should be entered... -->
                <h5 class="card-title">{{ garage.name }}</h5>
                <p class="card-subtitle text-muted">{{ car.brand }}</p>
                <p class="card-subtitle text-muted text-uppercase">{{ car.licence_plate }}</p>
                <span></span>
                <a href="#" class="card-link" @click.prevent="refresh">Refresh</a>
                <template v-if="!editing">
                    <a href="#" class="card-link" @click.prevent="editing = !editing">Edit</a>
                    <a href="#" class="card-link" @click.prevent="listCars">List Cars</a> <!-- pve -->
                    <a href="#" class="card-link text-danger" @click.prevent="deleteCar">Delete Car</a>
                </template>
                <template v-else>
                    <!-- <a href="#" class="card-link disabled" @click.prevent="save">Save</a> -->
                    <a href="#" class="card-link text-danger" @click.prevent="editing = !editing; Object.assign(car, updated_car)">Cancel</a>
                </template>
            </div>
            <transition name="fade" mode="out-in">
                <car-form v-if="editing" :car="car" @change="editing = false; Object.assign(updated_car, car)"></car-form>
            </transition>
        </div>
    </div>
</template>

<script>
    import CarForm from "./car-form.vue";
    export default {
        name: "car-list-item",
        components: {
            'car-form': CarForm
        },
        props: {
            car: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                updated_car: {},
                editing: false
            }
        },
        mounted() {
            this.updated_car = Object.assign({}, this.car)
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
            deleteCar() {
                $.ajax({
                    type: 'DELETE',
                    contentType: 'application/json',
                    url: `/garages/carlist`,
                    data: JSON.stringify({'car': this.car.id})
                }).then((data) => {
                    this.$emit('change', data)
                }).always(() => {
                })
            },
            // pve
            listCars () {
                $.ajax({
                    type: 'LIST',
                    contentType: 'application/json',
                    url: `/garages/carlist`,
                    data: JSON.stringify({'car': this.car.id})
                }).then((data) => {
                    this.$emit('change', data)
                }).always(() => {
                })
            },
            // pve
            refresh() {
                $.ajax({
                    type: 'GET',
                    contentType: 'application/json',
                    url: `/garages/?car=${this.car.id}`,
                }).then((data) => {
                    console.log(data)
                    Object.assign(this.car, data) // watch does not work this way then we need to use deep watch
                    Object.assign(this.updated_car, this.car)
                }).always(() => {
                })
            }
        },
        watch: {
            garage(g) {
                console.log('car update:' + g)
                Object.assign(this.updated_car, g)
            }
        }
    }
</script>

<style scoped></style>