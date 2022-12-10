<template>
  <v-app>
    <v-main>
      <v-app-bar color="primary">
        <p style="margin-left:10px;">MQTT Sensor simulator</p>
      </v-app-bar>
      <StatsDashboardVue/>
      <v-bottom-navigation 
      v-model="menu"
      :bg-color="color"
      mandatory>
        <v-btn value="stats">
          <span>Stats</span>
          <v-icon>mdi-chart-bar</v-icon>
        </v-btn>
        <v-btn value="sensor">
          <span>Sensor</span>
          <v-icon>mdi-leak</v-icon>
        </v-btn>
      </v-bottom-navigation>
    </v-main>
  </v-app>
</template>

<script>
import StatsDashboardVue from './components/StatsDashboard.vue'

export default {
  name: 'App',

  components: {
    StatsDashboardVue
  },
  computed: {
    color () {
      switch (this.menu) {
        case "stats": return 'blue-grey'
        case "sensor": return 'teal'
        default: return 'blue-grey'
      }
    },
  },

  data: () => ({
    menu:"stats"
  }),
}
</script>
