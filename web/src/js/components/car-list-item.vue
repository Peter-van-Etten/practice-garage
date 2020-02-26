<template>
    <div>
        <div class="card">
            <div class="card-body">
                <h5 class="card-title"></h5>
                <p class="card-subtitle text-muted">Brand: {{ car.brand }}</p>
                <p class="card-subtitle text-muted">License plate: {{ car.license_plate }}</p>
                <span></span>
                <a href="#" class="card-link" @click.prevent="refresh">Refresh</a>
                <template v-if="!editing">
                    <a href="#" class="card-link" @click.prevent="editing = !editing">Edit</a>
                    <a href="#" class="card-link text-danger" @click.prevent="deleteCar">Delete Car</a>
                </template>
                <template v-else>
                    <a href="#" class="card-link text-danger" @click.prevent="editing = !editing; Object.assign(car, updated_car)">Cancel</a>
                </template>
            </div>
            <transition name="fade" mode="out-in">
                <car-form v-if="editing" :car="car" :garage="garage" @change="editing = false; Object.assign(updated_car, car)"></car-form>
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
            },
            garage: {
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
            deleteCar() {
                $.ajax({
                    type: 'DELETE',
                    contentType: 'application/json',
                    url: `/cars/`,
                    data: JSON.stringify({'car': this.car.id})
                }).then((data) => {
                    this.$emit('change', data)
                }).always(() => {
                })
            },
            refresh() {
                $.ajax({
                    type: 'GET',
                    contentType: 'application/json',
                    url: `/cars/cars-from-garage/${this.car.id}`,
                }).then((data) => {
                    // console.log(data)
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