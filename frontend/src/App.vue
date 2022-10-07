<script lang="ts">
  import Locations from './components/Locations.vue'
  import Map from "./components/Map.vue";
  import { NCard, NButton, NIcon } from 'naive-ui'

  export default {
    name: 'App',
    components: {
      Locations,
      Map,
      NCard, NButton, NIcon
    }
  }
</script>

<template>
    <header class="header">
      <h1>Lumico Challenge</h1>
    </header>
    <div class="grid">
      <aside class="navbar">
        <div class="vessels-group">
          <h4>Vessels</h4>
          <n-space vertical>
            <n-card title="Rathaus Galerie" size="medium" class="vessels-item">
              Kölner Str. 96-100, 41539 Dormagen, Germany
              <template #header-extra>
                <n-button circle type="warning" class="card-button"> Edit</n-button>
                <n-button circle type="error" class="card-button"> Remove</n-button>
              </template>
            </n-card>

            <n-card title="Rathaus Galerie" size="medium" class="vessels-item">
              Kölner Str. 96-100, 41539 Dormagen, Germany
              <template #header-extra>
                <n-button circle type="warning" class="card-button"> Edit</n-button>
                <n-button circle type="error" class="card-button"> Remove</n-button>
              </template>
            </n-card>

            <n-card title="Rathaus Galerie" size="medium" class="vessels-item">
              Kölner Str. 96-100, 41539 Dormagen, Germany
              <template #header-extra>
                <n-button circle type="warning" class="card-button"> Edit</n-button>
                <n-button circle type="error" class="card-button"> Remove</n-button>
              </template>
            </n-card>
          </n-space>
        </div>
      </aside>
      <main class="map"><Map /></main>
    </div>
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

.map {
  width: 100%;
  height: 100%;
  background-color: #fff;
}

</style>
