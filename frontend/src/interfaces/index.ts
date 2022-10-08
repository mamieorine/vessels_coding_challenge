export class IVesselList {
    list: IVesselItem[];

    constructor(list: IVesselItem[]) {
      this.list = list
    }
}

export class IVesselItem {
    name: string;
    lat: number;
    lng: number;
    address: string;

    constructor(name: string, lat: number, lng: number, address: string) {
      this.name = name
      this.lat = lat
      this.lng = lng
      this.address = address
    }
}
