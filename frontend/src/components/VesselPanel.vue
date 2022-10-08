<script lang="ts">
	import { NCard, NButton, NSpace } from 'naive-ui'
	import { IVesselItem } from '../interfaces'
	import { defineComponent } from "vue";

	export default defineComponent ({
		name: 'VesselPanel',
		props: {
			vessels: {
				type: Array<IVesselItem>
			},
			focused: {
				type: IVesselItem
			}
		},
		components: {
			NCard, NButton, NSpace
		},
		method() {
			return function openModal(vessel: IVesselItem) {
				console.log(vessel.name);
				// this.$emit('changeTitle', 'Awesome ')
			}
		}
	})
</script>

<template>
	<aside class="navbar">
		<div class="vessels-group">
			<h4>Vessels</h4>
			<n-space vertical>
			<div v-for="item of vessels">
				<n-card size="medium" :title="item.name" :focused="focused" class="vessels-item" @click="$emit('update:focused', item)">
					{{ item.name }}
					<template #header-extra>
					<n-button circle type="warning" class="card-button"> Edit</n-button>
					<n-button circle type="error" class="card-button"> Remove</n-button>
					</template>
				</n-card>
			</div>
			</n-space>
		</div>
	</aside>
</template>

<style>
	body {
		margin: 0;
	}
</style>