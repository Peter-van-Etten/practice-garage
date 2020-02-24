<template>
    <form>
        <div class="form-group">
                <!-- pve should this be change-able in the new-car form? -->
                <p>Garage: {{ car.id }}</p>

        </div>
        <div class="form-group">
            <div class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">Brand</span>
                </div>
                <input type="text" id="carbrand" class="form-control" v-model="car.brand">
            </div>
        </div>
        <div class="form-group">
            <div class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">License Plate</span>
                </div>
                <input type="text" id="license-plate" class="form-control" v-model="car.license_plate">
            </div>
        </div>
        <div class="form-group">
            <button class="btn btn-success btn-block" @click.prevent="save">Save</button>
        </div>
        <div class="form-group">
            <button class="btn btn-success btn-block" @click.prevent="resetForm">Reset</button>
        </div>
    </form>
</template>

<script>
    export default {
        name: "new-car",
        data() {
            return {
                car: {
                    garage: '',
                    brand: '',
                    license_plate: ''
                }
            }
        },
        methods: {
            save() {
                console.log(this.garage)
                $.ajax({
                    type: 'POST',
                    url: `/garages/carlist/`,
                    contentType: 'application/json',
                    data: JSON.stringify(this.car),
                    timeout: 2000
                }).then((data) => {
                    this.$emit('change', data)
                    this.resetForm()
                }).always(() => {
                    // this.loading = false
                })
            },
            resetForm() {
                if (this.car.id) {
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