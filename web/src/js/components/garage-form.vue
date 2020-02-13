<template>
    <div class="col">
        <form>
            <div class="form-group">
                <input type="text" id="name" class="form-control form-control-sm" placeholder="name" v-model="name">
            </div>
            <div class="form-group">
                <input type="text" id="brand" class="form-control form-control-sm" placeholder="brand" v-model="garage.brand">
            </div>
            <div class="form-group">
                <input type="text" id="country" class="form-control form-control-sm" placeholder="country" v-model="garage.postal_country">
            </div>
            <div class="form-group">
                <button class="btn btn-success" @click.prevent="save">Save</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "garage-form",
        props: {
            garage: {
                type: Object,
                required: false,
                default: ''
            }
        },
        computed: {
            title() {
                return this.garage.id ? 'Edit garage': 'Add new garage'
            },
            name: {
                set(val) {
                    this.garage.name = val
                },
                get() {
                    return this.garage.name
                }
            }
        },
        data() {
            return {
                myGarage: {}
            }
        },
        mounted() {
            console.log(JSON.stringify(this.garage))
            Object.assign(this.myGarage, this.garage)
        },
        methods:{
            save() {
                if (this.garage.id) {
                    Object.assign(this.myGarage, this.garage)
                }
                $.ajax({
					type: this.myGarage.id ? 'PUT':'POST',
					url: `/garages/`,
					contentType: 'application/json',
                    data: JSON.stringify(this.myGarage),
					timeout: 2000
				}).then((data) => {
                    this.$emit('change', data)
                    if (this.garage.id === undefined){
                        this.resetForm()
                    }
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