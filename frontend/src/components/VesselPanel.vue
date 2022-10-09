<script lang="ts">
	import { NCard, NButton, NSpace, NGrid, NScrollbar,
		NGi, NModal, NForm, NFormItem, NInput } from 'naive-ui'
	import type {FormInst} from 'naive-ui'
	import type { IVesselItem } from '../interfaces'
	import { defineComponent, ref } from "vue";
	import { api } from '../utils/api';
	import type { AxiosResponse } from 'axios';
	import { store } from '../store'

	const formRef = ref<FormInst | null>(null)
	const showModalRef = ref(false)
	const formValue = ref({id: '', name: '', lat: '', lng: '', address: ''});

	export default defineComponent ({
		name: 'VesselPanel',
		data() {
			return {
				store,
				isEdit: false,
			}
		},
		components: {
			NCard, NButton, NSpace, NGrid, NGi, NModal, NForm, NFormItem, NInput, NScrollbar
		},
		async mounted() {
			await this.getVessels().then(() => {
				store.focusedVessel = store.vessels[0]
			});
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
				store.vessels = response.data;
			},

			async addVessel(item: IVesselItem) {
				const response: AxiosResponse = await api.add(item).then(res => res);

				if (response.status !== 201) console.log('Cannot add a vessel item');
				this.getVessels();
			},

			async updateVessel(item: IVesselItem, vesselID: number) {
				const response: AxiosResponse = await api.update(vesselID, item).then(res => res);

				if (response.status !== 200) console.log('Cannot update a vessel item');
				this.getVessels();
			},

			handleValidateClick(item: any) {
				formRef.value?.validate(async (errors) => {
					if (!errors) {
						const vesselDetail: IVesselItem = {
							name: item.name,
							lat: parseFloat(item.lat),
							lng: parseFloat(item.lng),
							address: item.address,
						}

						this.isEdit ? this.updateVessel(vesselDetail, item.id) : this.addVessel(vesselDetail);
						this.getVessels();
						this.isEdit = false;
						showModalRef.value = false;

					} else {
						console.log(errors)
					}
				})
			},
			onAddVesselButtonClick() {
				this.formValue.id = this.formValue.name = this.formValue.address = this.formValue.lat = this.formValue.lng = '';
				showModalRef.value = true;
			},
			onEditVesselButtonClick(item: IVesselItem) {
				this.formValue.id = item.id?.toString() || ''
				this.formValue.name = item.name
				this.formValue.address = item.address
				this.formValue.lat = item.lng.toString()
				this.formValue.lng = item.lat.toString()

				showModalRef.value = true;
				this.isEdit = true;
			},
			onNegativeClick() {
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
		<n-scrollbar style="max-height: 90%" class="vessels-group">
			{{ store.focusedVessel }}
			<n-grid x-gap="12" :cols="2">
				<n-gi><h4>Vessels {{store.vessels[0]?.name }}</h4></n-gi>
				<n-gi class="addButton"><n-button type="primary" @click="onAddVesselButtonClick()"> Add vessel </n-button></n-gi>
			</n-grid>
			<n-space vertical>
				<n-card size="medium" v-for="item of (store.vessels)" :title="item.name" class="vessels-item" @click="store.focusedVessel = item">
					{{ item.name }}
					<template #header-extra>
					<n-button circle type="warning" class="card-button" @click="onEditVesselButtonClick(item)"> Edit</n-button>
					<n-button circle type="error" class="card-button" @click="onDeleteVessel(item)"> Remove</n-button>
					</template>
				</n-card>
			</n-space>
		</n-scrollbar>
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
	h4 {
		font-size: 22px !important;
		margin-bottom: 20px !important;
	}

	.addButton {
		text-align: right;
	}

	.card-button {
		margin-left: 5px;
	}

	.grid {
		display: grid;
		grid-template-columns: 1fr 3fr;
		padding: 0;
		margin: auto;
		align-items: start;
	}

	.navbar {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: flex-start !important;
	}

	.vessels-group {
		width: 100%;
		padding-right: 40px;
		padding: 40px;
	}
	.vessels-item {
		margin-bottom: 10px;
	}
</style>