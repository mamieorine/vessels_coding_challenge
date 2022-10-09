<script lang="ts">
	import { store } from '../store'

	export default {
		name: 'Map',
		data() {
			return {
				store
			}
		},
	};
</script>

<template>
	<GMapMap
		:center="{lat: store.focusedVessel?.lat ?? -1.39595, lng: store.focusedVessel?.lng ?? 50.9474}"
		:zoom="16"
		ref="myMarker"
		style="width: 100%; height: 50vw"
	>
		<GMapCluster :zoomOnClick="true">
			<GMapMarker
				:key="index"
				v-for="(marker, index) in store.vessels"
				:position="{lat: marker.lat, lng: marker.lng}"
				:clickable="true"
				:draggable="true"
			/>
		</GMapCluster>
	</GMapMap>
</template>

<style>
	Map {
		width: 100%;
		height: 100%;
		background-color: #fff;
	}
</style>