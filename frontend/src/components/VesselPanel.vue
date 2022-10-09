<script lang="ts">
	import { NCard, NButton, NSpace, NGrid, NGi } from 'naive-ui'
	import { IVesselItem } from '../interfaces'
	import { defineComponent } from "vue";
	import { api } from '../utils/api';
	import type { AxiosResponse } from 'axios';

	export default defineComponent ({
		name: 'VesselPanel',
		data() {
			return {
				vesselsList: [] as IVesselItem[],
			}
		},
		props: {
			vessels: {
				type: Array<IVesselItem>
			},
			focused: {
				type: IVesselItem
			}
		},
		components: {
			NCard, NButton, NSpace, NGrid, NGi
		},
		methods: {
			async onDeleteVessel(item: IVesselItem) {
				const response: AxiosResponse = await api.delete(item.id).then(res => res);

				if (response.status !== 200) {
					console.log('Cannot delete the item');
				}

				this.fetchVessels()
			},

			async fetchVessels() {
				const response: AxiosResponse = await api.get().then(res => res);

				if (response.status !== 200) {
					console.log('Cannot fetch vessel items');
				}
				this.vesselsList = response.data;
			}
		}
	})
</script>

<template>
	<aside class="navbar">
		<div class="vessels-group">
			<n-grid x-gap="12" :cols="2">
				<n-gi><h4>Vessels</h4></n-gi>
				<n-gi class="addButton"><n-button type="primary"> Add vessel </n-button></n-gi>
			</n-grid>
			<n-space vertical>
				<n-card size="medium" v-for="item of (vesselsList.length != 0 ? vesselsList : vessels)" :title="item.name" class="vessels-item">
					{{ item.name }}
					<template #header-extra>
					<n-button circle type="warning" class="card-button"> Edit</n-button>
					<n-button circle type="error" class="card-button" @click="onDeleteVessel(item)"> Remove</n-button>
					</template>
				</n-card>
			</n-space>
		</div>
	</aside>
</template>

<style>
	body {
		margin: 0;
	}

	.addButton {
		text-align: right;
	}
</style>