<script lang="ts">
  import Map from "./components/Map.vue";
  import VesselPanel from "./components/VesselPanel.vue";

  export default {
    name: 'App',
    components: {
      Map,
      VesselPanel,
    },
    data() {
      return { vessels: [{
        id: '1',
        name: 'string',
        lat: 50.9344,
        lng: -1.39595,
        address: 'address 1'
      },{
        id: '2',
        name: 'string 2',
        lat: 51.0714,
        lng: -1.2202,
        address: 'address 2'
      }],
      focused: {
        id: '1',
        name: 'string',
        lat: 50.9344,
        lng: -1.39595,
        address: 'address 1'
      } }
    }
  }
</script>

<template>
    <header class="header">
      <h1>Lumico Challenge</h1>
    </header>
    <main class="grid">
      <VesselPanel :vessels="vessels"></VesselPanel>
      <Map :vessels="vessels" :focused="focused" />
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
