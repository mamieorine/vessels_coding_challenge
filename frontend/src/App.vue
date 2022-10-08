<script lang="ts">
  import Map from "@/components/Map.vue";
  import VesselPanel from "@/components/VesselPanel.vue";
  import { defineComponent } from "vue";
	import type { IVesselItem } from './interfaces';

  export default defineComponent ({
    name: 'App',
    components: {
      Map,
      VesselPanel,
    },
    data() {
      return {
        vessels: [] as IVesselItem[],
        focused: {} as IVesselItem
      }
    },
    method: {
			fetchData: function fetchData() {
        return [{
          name: 'string',
          lat: 50.9344,
          lng: -1.39595,
          address: 'address 1'
        }]
      }
		},
		mounted() {
      const response = [{
          name: 'string',
          lat: 50.9344,
          lng: -1.39595,
          address: 'address 1'
        },{
          name: 'string 2',
          lat: 51.0714,
          lng: -1.2202,
          address: 'address 2'
      }]

      this.vessels = response
      this.focused = response[0]
		}
    //   .get('https://api.coindesk.com/v1/bpi/currentprice.json')
    //   .then(response => (this.info = response))

  })
</script>

<template>
    <header class="header">
      <h1>Lumico Challenge</h1>
    </header>
    <!-- <p :focused.sync="focused"
    {{ focused }}
    ></p> -->
    <main class="grid">
      <p>{{ focused }}</p>
      <VesselPanel :vessels="vessels" :focused.sync="focused"></VesselPanel>
      <Map v-if="vessels.length > 0" :vessels="vessels" :focused="focused" />
    </main>
</template>

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #333;
}

.header {
  width: 100%;
  height: 80px;
  padding-top: 20px;
  border-bottom: 1px solid #ddd;
  text-align: center;
}

.header h1 {
  font-size: 30px !important;
}

h4 {
  font-size: 22px !important;
  margin-bottom: 20px !important;
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

Map {
  width: 100%;
  height: 100%;
  background-color: #fff;
}

</style>

    function fetchData() {
      throw new Error('Function not implemented.');
    }
