<script lang="ts">
	import { store } from '@/store'

	export default {
		name: 'Map',
		data() {
			return {
				store,
				defaultFocused: {
					lat: 50.9346,
					lng: -1.3960
				}
			}
		},
	};
</script>

<template>
	<GMapMap
		:center="{lat: store.focusedVessel.lat ?? defaultFocused.lat, lng: store.focusedVessel.lng ?? defaultFocused.lng}"
		:zoom="16"
		map-type-id="terrain"
		style="width: 100%; height: 50vw">
		<GMapMarker
			v-for="(marker, index) in store.vessels"
			:key="index"
			:position="{lat: marker.lat, lng: marker.lng}"
			:clickable="true"
			:draggable="true"/>
	</GMapMap>
</template>

<style>
	Map {
		width: 100%;
		height: 100%;
		background-color: #fff;
	}
</style>