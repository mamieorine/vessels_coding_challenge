import axios from 'axios';
import type {  IVesselItem } from '../interfaces';

const apiUrl = 'http://127.0.0.1:8000';

export const api = {
  async get() {
    return axios.get<IVesselItem[]>(`${apiUrl}/api/vessel/`);
  },
  async add(data: IVesselItem) {
    console.log(data)
    return axios.post<IVesselItem>(`${apiUrl}/api/vessel/`, data);
  },
  async update(vesselID: number, data: IVesselItem) {
    return axios.put<IVesselItem>(`${apiUrl}/api/vessel/${vesselID}/`, data);
  },
  async delete(vesselID: number) {
    return axios.delete(`${apiUrl}/api/vessel/${vesselID}/`);
  }
};
