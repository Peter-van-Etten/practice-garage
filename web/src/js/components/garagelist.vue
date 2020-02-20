<template>
	<div class="container-margin-top">
		<div class="row">
			<div class="col-sm-12 text-center">
				<h1>Garages</h1>
			</div>
		</div>
		<div class="row margin-top">
			<div class="col-sm-4">
				<new-garage @change="garageList = $event"></new-garage>
			</div>
			<div class="col-sm-8">
				<transition-group name="fade" tag="ul">
					<li v-for="item in garageList" :key="item.id">
						<!-- when a garage item is deleted it will raise change event and return the new list -->
						<garage-list-item :garage="item" @change="garageList = $event"></garage-list-item>
					</li>
				</transition-group>
			</div>
		</div>
	</div>
</template>

<script>
    import GarageListItem from "./garage-list-item"
	import NewGarage from "./new-garage"

	export default {
		name: 'garage-list',
		components: {
			'new-garage': NewGarage,
			'garage-list-item': GarageListItem
		},
		data() {
			return {
				garageList: []
			}
		},
		methods: {
			load() {
				$.ajax({
					type: 'GET',
					url: `/garages/`,
					contentType: 'application/json',
					timeout: 60000
				}).then((data) => {
					console.log(data)
					this.garageList = data
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
