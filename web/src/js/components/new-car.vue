<template>
    <form>
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
        <!-- <div class="form-group">
            <button class="btn btn-success btn-block" @click.prevent="resetForm">Reset</button>
        </div> -->
    </form>
</template>

<script>
    export default {
        name: "new-car",
        data() {
            return {
                car: {
                    garage_id: this.garage.id,
                    brand: '',
                    license_plate: ''
                }
            }
        },
        props: {
            garage: {
                required: true
            }
        },
        methods: {
            save() {
                // console.log('in new-car.save')
                // console.log('this.garage.id', this.garage.id)                
                // console.log('this.car.brand', this.car.brand)
                $.ajax({
                    type: 'POST',
                    url: `/cars/`,
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
                // console.log('in new-car/resetForm')
                if (this.car.id) {
                    // console.log('in new-car/resetForm, this.car.id:', this.car.id)
                    Object.assign(this.myCar, this.car)
                } else {
                    // console.log('in new-car/resetForm, else')
                    this.myCar = {
                        garage_id: this.garage.id,
                        brand: '',
                        license_plate: ''
                    }
                    // console.log('in new-car/resetForm, this.mycar:', this.mycar)
                    Object.assign(this.car, this.myCar)
                }
            }
        }
    }
</script>

<style scoped></style>