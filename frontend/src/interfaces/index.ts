export class IVesselItem {
    id: number;
    name: string;
    lat: number;
    lng: number;
    address: string;

    constructor(id:number, name: string, lat: number, lng: number, address: string) {
      this.id = id
      this.name = name
      this.lat = lat
      this.lng = lng
      this.address = address
    }
}
