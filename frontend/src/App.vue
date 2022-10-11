<script lang="ts">
  import Map from "@/components/Map.vue";
  import VesselPanel from "@/components/VesselPanel.vue";
  import { defineComponent } from "vue";

  export default defineComponent ({
    name: 'App',
    components: {
      Map,
      VesselPanel,
    }
  })
</script>

<template>
    <header class="header">
      <h1>Lumico Challenge</h1>
    </header>

    <main class="grid">
      <VesselPanel></VesselPanel>
      <Map />
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
  font-weight: 600;
}

.grid {
  display: grid;
  grid-template-columns: 1.2fr 3fr;
  padding: 0;
  margin: auto;
  align-items: start;
}

</style>
