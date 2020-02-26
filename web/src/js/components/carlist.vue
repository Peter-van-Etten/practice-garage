<template>
	<div class="container-margin-top">
		<div class="row">
			<div class="col-sm-12 text-center">
				<h1>Cars in {{ garage.name }}</h1>
			</div>
		</div>
		<div class="row margin-top">
			<div class="col-sm-4">
				<new-car :garage="garage" @change="carlist = $event"></new-car>
			</div>
			<div class="col-sm-8">
				<transition-group name="fade" tag="ul">
					<li v-for="car in carlist" :key="car.id">
						<car-list-item :car="car" :garage="garage" @change="carlist = $event"></car-list-item>
					</li>
				</transition-group>
			</div>
			
		</div>
	</div>
</template>

<script>
    import CarListItem from "./car-list-item.vue"
	import NewCar from "./new-car.vue"

	export default {
		name: 'car-list',
		components: {
			'new-car': NewCar,
			'car-list-item': CarListItem
		},
        props: {
            garage: {
				type: Object,
                required: true
			}
        },
		data() {
			return {
				carlist: []
			}
		},
		methods: {
			load() {
				$.ajax({
					type: 'GET',
					url: `/cars/cars-from-garage/${this.garage.id}`,
					contentType: 'application/json',
					timeout: 60000
				}).then((data) => {
					// console.log(data)
					this.carlist = data
				}).always(() => {
					// this.loading = false
				})
			}
		},
		created() {
			this.load();
		}
	}

</script>

<style scoped></style>
