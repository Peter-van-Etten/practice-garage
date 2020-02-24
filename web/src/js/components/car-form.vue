<template>
    <div class="col">
        <form>
            <div class="form-group">
                <input type="text" id="garage" class="form-control form-control-sm" placeholder="garage" v-model="car.garage">
            </div>
            <div class="form-group">
                <input type="text" id="brand" class="form-control form-control-sm" placeholder="brand" v-model="car.brand">
            </div>
            <div class="form-group">
                <input type="text" id="licence_plate" class="form-control form-control-sm" placeholder="license plate" v-model="car.license_plate">
            </div>
            <div class="form-group">
                <button class="btn btn-success" @click.prevent="save">Save</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "car-form",
        props: {
            car: {
                type: Object,
                required: false,
                default: ''
            }
        },
        computed: {
            title() {
                return this.car.license_plate ? 'Edit car': 'Add new car'
            },
            name: {
                set(val) {
                    this.car.brand = val
                },
                get() {
                    return this.car.brand
                }
            }
        },
        data() {
            return {
                myCar: {}
            }
        },
        mounted() {
            console.log(JSON.stringify(this.car))
            Object.assign(this.myCar, this.car)
        },
        methods:{
            save() {
                if (this.car.license_plate) {
                    Object.assign(this.myCar, this.car)
                }
                $.ajax({
					type: this.myCar.id ? 'PUT':'POST',
					url: `/garages/carlist/`,
					contentType: 'application/json',
                    data: JSON.stringify(this.myCar),
					timeout: 2000
				}).then((data) => {
                    this.$emit('change', data)
                    if (this.car.id === undefined){
                        this.resetForm()
                    }
				}).always(() => {
					// this.loading = false
                })
            },
            nothing() {
                pass
            },
            resetForm() {
                if (this.car.license_plate) {
                    Object.assign(this.myCar, this.car)
                } else {
                    this.myCar = {
                        garage: '',
                        brand: '',
                        license_plate: ''
                    }
                    Object.assign(this.car, this.myCar)
                }
            }
        }
    }
</script>

<style scoped></style>