<script lang="ts">
	import { NCard, NButton, NSpace } from 'naive-ui'
	import { IVesselList } from '../interfaces'

	export default {
		name: 'VesselPanel',
		props: {
			vessels: {
				type: IVesselList
			}
		},
		components: {
			NCard, NButton, NSpace
		},
  }
</script>

<template>
	<aside class="navbar">
		<div class="vessels-group">
			<h4>Vessels</h4>
			<n-space vertical>
			<div v-for="item of vessels">
				<n-card size="medium" :title="item.name" class="vessels-item">
					{{ item }}
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