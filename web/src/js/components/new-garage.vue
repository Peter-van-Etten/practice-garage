<template>
    <form>
        <div class="form-group">
            <div class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">Name</span>
                </div>
                <input type="text" id="name" class="form-control" v-model="garage.name">
            </div>
        </div>
        <div class="form-group">
            <div class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">Brand</span>
                </div>
                <input type="text" id="brand" class="form-control" v-model="garage.brand">
            </div>
        </div>
        <div class="form-group">
            <div class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">Country</span>
                </div>
                <input type="text" id="country" class="form-control" v-model="garage.postal_country">
            </div>
        </div>
        <div class="form-group">
            <button class="btn btn-success btn-block" @click.prevent="save">Save</button>
        </div>
    </form>
</template>

<script>
    export default {
        name: "new-garage",
        data() {
            return {
                garage: {
                    name: '',
                    brand: '',
                    postal_country: ''
                }
            }
        },
        methods: {
            save() {
                // console.log('in new-garage - load, garage: ', this.garage.id)
                $.ajax({
                    type: 'POST',
                    url: `/garages/`,
                    contentType: 'application/json',
                    data: JSON.stringify(this.garage),
                    timeout: 2000
                }).then((data) => {
                    this.$emit('change', data)
                    this.resetForm()
                }).always(() => {
                    // this.loading = false
                })
            },
            resetForm() {
                if (this.garage.id) {
                    Object.assign(this.myGarage, this.garage)
                } else {
                    this.myGarage = {
                        name: '',
                        brand: '',
                        postal_country: ''
                    }
                    Object.assign(this.garage, this.myGarage)
                }
            }
        }
    }
</script>

<style scoped></style>