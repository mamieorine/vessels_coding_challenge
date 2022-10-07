<template>
	<GMapMap
		:center="center"
		:zoom="15"
		ref="myMarker"
		style="width: 100%; height: 50vw"
	>
		<!-- <GMapCluster :zoomOnClick="true"> -->
			<GMapMarker
				:key="index"
				v-for="(marker, index) in markers"
				:position="marker.position"
				:clickable="true"
				:draggable="true"
			/>
		<!-- </GMapCluster> -->
	</GMapMap>
</template>

<script>
	export default {
		data() {
			return {
			center: { lat: 50.9344, lng: -1.39595 },
			markers: [
				{
					position: {
						lat: 50.9344,
						lng: -1.39595,
					},
				},
				{
					position: {
						lat: 51.0714,
						lng: -1.2202,
					},
				}
			],
			};
		},
	};
</script>

<style>
	body {
		margin: 0;
	}
</style>