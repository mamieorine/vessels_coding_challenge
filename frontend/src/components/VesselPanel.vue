<script lang="ts">
	import { NCard, NButton, NSpace, NGrid, NGi, NModal, NForm, NFormItem, NInput } from 'naive-ui'
	import type {FormInst} from 'naive-ui'
	import { IVesselItem } from '../interfaces'
	import { defineComponent, ref } from "vue";
	import { api } from '../utils/api';
	import type { AxiosResponse } from 'axios';

	const formRef = ref<FormInst | null>(null)
	const showModalRef = ref(false)
	const formValue = ref({
			name: '',
			lat: '',
			lng: '',
			address: '',
		});

	export default defineComponent ({
		name: 'VesselPanel',
		data() {
			return {
				vesselsList: [] as IVesselItem[],
			}
		},
		props: {
			vessels: { type: Array<IVesselItem> },
			focused: { type: IVesselItem }
		},
		components: {
			NCard, NButton, NSpace, NGrid, NGi, NModal, NForm, NFormItem, NInput
		},
		methods: {
			async onDeleteVessel(item: IVesselItem) {
				const response: AxiosResponse = await api.delete(item.id ?? 0).then(res => res);

				if (response.status !== 200) console.log('Cannot delete the item');
				this.getVessels()
			},

			async getVessels() {
				const response: AxiosResponse = await api.get().then(res => res);

				if (response.status !== 200) console.log('Cannot fetch vessel items');
				this.vesselsList = response.data;
			},

			async addVessel(item: IVesselItem) {
				const response: AxiosResponse = await api.add(item).then(res => res);

				if (response.status !== 201) console.log('Cannot add a vessel item');
				this.getVessels();
			},

			handleValidateClick(formValue: any) {
				console.log(formRef.value)
				formRef.value?.validate(async (errors) => {
					if (!errors) {
						console.log(formValue)
						const vesselDetail: IVesselItem = {
							name: formValue.name,
							lat: parseFloat(formValue.lat),
							lng: parseFloat(formValue.lng),
							address: formValue.address,
						}

						this.addVessel(vesselDetail);
					} else {
						console.log(errors)
					}
				})
			},
			onNegativeClick () {
				showModalRef.value = false
			}
		},
		setup() {
			return {
				showModal: showModalRef,
				formRef,
				formValue: formValue,
				rules: {
					name: {
						required: true,
						message: 'Please input vessel name',
						trigger: 'blur'
					},
					lat: {
						required: true,
						message: 'Please input vessel lat',
						trigger: ['input', 'blur']
					},
					lng: {
						required: true,
						message: 'Please input vessel lng',
						trigger: ['input', 'blur']
					},
					address: {
						required: false,
						message: 'Please input address',
						trigger: ['input', 'blur']
					}
				},
			}
		}
	})
</script>

<template>
	<aside class="navbar">
		<div class="vessels-group">
			<n-grid x-gap="12" :cols="2">
				<n-gi><h4>Vessels</h4></n-gi>
				<n-gi class="addButton"><n-button type="primary" @click="showModal=true"> Add vessel </n-button></n-gi>
			</n-grid>
			<n-space vertical>
				<n-card size="medium" v-for="item of (vesselsList.length != 0 ? vesselsList : vessels)" :title="item.name" class="vessels-item">
					{{ item.name }}
					<template #header-extra>
					<n-button circle type="warning" class="card-button" @click="showModal=true"> Edit</n-button>
					<n-button circle type="error" class="card-button" @click="onDeleteVessel(item)"> Remove</n-button>
					</template>
				</n-card>
			</n-space>
		</div>
	</aside>

	<n-modal
		v-model:show="showModal">
		<n-card
			title="Add new vessel"
			:bordered="false"
			size="huge"
			role="dialog"
			aria-modal="true"
			style="width: 600px;"
			>
			<n-form
				ref="formRef"
				:label-width="80"
				:model="formValue"
				:rules="rules"
			>
				<n-form-item label="Vessel Name" path="name">
					<n-input v-model:value="formValue.name" placeholder="Name" />
				</n-form-item>
				<n-form-item label="Lat" path="lat">
					<n-input v-model:value="formValue.lat" placeholder="Lat" />
				</n-form-item>
				<n-form-item label="Lng" path="lng">
					<n-input v-model:value="formValue.lng" placeholder="Lng" />
				</n-form-item>
				<n-form-item label="Address" path="address">
					<n-input v-model:value="formValue.address" placeholder="Address" />
				</n-form-item>
			</n-form>
			<template #footer>
				<n-button @click="handleValidateClick(formValue)" type="primary" >Submit</n-button>
				<n-button @click="onNegativeClick" type="error" >Cancel</n-button>
			</template>
		</n-card>
	</n-modal>
</template>

<style>
	body {
		margin: 0;
	}

	.addButton {
		text-align: right;
	}
</style>