<script lang="ts">
	import { IVesselList, IVesselItem } from '../interfaces'

	export default {
		name: 'Map',
		props: {
			vessels: {
				type: IVesselList
			},
			focused: {
				type: IVesselItem
			}
		}
	};
</script>

<template>
	<GMapMap
		:center="{lat: focused.lat, lng: focused.lng}"
		:zoom="16"
		ref="myMarker"
		style="width: 100%; height: 50vw"
	>
		<GMapCluster :zoomOnClick="true">
			<GMapMarker
				:key="index"
				v-for="(marker) in vessels"
				:position="{lat: marker.lat, lng: marker.lng}"
				:clickable="true"
				:draggable="true"
			/>
		</GMapCluster>
	</GMapMap>
</template>

<style>
	body {
		margin: 0;
	}
</style>