<template>
    <div id="cards-container">
        <v-card class="sensor-card">
            <v-card-title>Sensor {{name}}</v-card-title>
            <v-card-subtitle>with id {{id}}</v-card-subtitle>
            <v-card-text>
                <div v-for="stat in stats" :key="stat.name">
                    <graph-view 
                        v-if="stat.type==='graph'"
                        :name="stat.name"
                        :unit="stat.unit"
                        :value="stat.value"
                        :hueShift="stat.hueShift"
                    ></graph-view>
                </div>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
import GraphView from './stats/GraphView.vue'
export default {
  components: { GraphView },
    data:()=>({
        name:"heat",
        id:"1941561",
        stats:[
            {
                name:"Heat evolution",
                type:"graph",
                unit:"°C over time in seconds",
                value:[
                    {x:0, y:10},
                    {x:1, y:15},
                    {x:2, y:3},
                    {x:3, y:22},
                ],
                hueShift:[
                    {
                        rupturePoint:5,
                        legend:"normal",
                        color:'rgb(0, 255, 0)'
                    },
                    {
                        rupturePoint:10,
                        legend:"abnormal",
                        color:'rgb(0, 255, 255)'
                    },
                    {
                        rupturePoint:18,
                        legend:"critical",
                        color:'rgb(255, 0, 0)'
                    }
                ]                
            },
            {
                name:"Current heat",
                type:"value",
                value:15,
                unit:"°C"
            }
        ]
    })
}
</script>

<style scoped>
    .sensor-card{
        width:30%;
    }

    #cards-container{
        display:flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        margin-top:5%;
    }
</style>