import { reactive } from 'vue'
import type { IVesselItem } from './interfaces'

export const store = reactive({
  vessels: [] as IVesselItem[],
  focusedVessel: {} as IVesselItem
})