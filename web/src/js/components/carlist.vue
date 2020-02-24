<template>
	<div class="container-margin-top">
		<div class="row">
			<div class="col-sm-12 text-center">
				<h1>Cars in this garage</h1>
			</div>
		</div>
		<div class="row margin-top">
			<div class="col-sm-4">
				<!-- pve added component -->
				<new-car @change="carlist = $event"></new-car>
			</div>
			<div class="col-sm-8">
				<transition-group name="fade" tag="ul">
					<li v-for="item in carlist" :key="item.id">
						<!-- when a garage item is deleted it will raise change event and return the new list ?? pve -->
						<car-list-item :car="item" @change="carlist = $event"></car-list-item>
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
            garageId: {
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
					url: `/garages/${this.garageId}/cars`,
					contentType: 'application/json',
					timeout: 60000
				}).then((data) => {
					console.log(data)
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
