<template>
    <div>
        <ul :id="'legend-'+name"></ul>
        <div style="position:relative; width:100%; height:100%;">
            <canvas :id="('chart-'+name)"></canvas>
        </div>
    </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables)

export default {
    props:{
        name:String,
        unit:String,
        value:Array,
        hueShift:Array
    },
    mounted(){
        const self = this;
        const htmlLegendPlugin = {
            id: 'htmlLegend',
            afterUpdate(chart, args, options) {
                chart;
                args;
                const ul = document.getElementById(options.containerID)
                while (ul.firstChild) {
                    ul.firstChild.remove();
                }
                ul.style.display="flex"
                ul.style.width="100%"
                ul.style.justifyContent="center"
                ul.style.flexWrap="wrap"
                let shifts = new Array(...self.hueShift)
                shifts.sort((a, b)=>{
                    if(a.rupturePoint < b.rupturePoint) return -1
                    if(a.rupturePoint > b.rupturePoint) return 1
                    return 0
                })
                console.log(shifts)
                for(const shift of shifts)
                {
                    let li = document.createElement("li")
                    li.innerHTML=shift.legend
                    li.style.color = shift.color
                    li.style.listStyleType="none"
                    li.style.width="33%"
                    li.style.textAlign="center"
                    ul.appendChild(li)
                }
            }
        }

        this.chart = new Chart(document.getElementById("chart-"+this.name), {
            type:"line",
            data:this.lineChartData(),
            options:{
                responsive: true,
                maintainAspectRatio:false,
                plugins:{
                    htmlLegend: {
                        // ID of the container to put the legend in
                        containerID: 'legend-'+this.name,
                    },
                    legend: {
                        display: false,
                    }
                }
            },
            plugins: [htmlLegendPlugin],
        });
        window.addEventListener('beforeprint', () => {
            console.log("key")
            this.chart.resize(600, 600);
        });
        window.addEventListener('afterprint', () => {
            this.chart.resize();
        });
    },    
    data:()=>({
        chart:null
    }),
    methods:{
        lineChartData(){
            let labels = this.value.map((v)=>{
                return v.x
            });
            const self = this;
            return{
                labels,
                datasets:[{
                    label:this.name+"(in "+this.unit+")",
                    data:this.value.map((v)=>v.y),
                    fill: false,
                    tension: 0.1,
                    borderColor: function(context) {
                        const chart = context.chart;
                        const {ctx, chartArea} = chart;
                        const max = chart.scales.y.max

                        if (!chartArea) {
                        // This case happens on initial chart load
                        return;
                        }
                        return self.getGradient(ctx, chartArea, max);
                    }
                }]
            }
        },
        getGradient(ctx, chartArea, max) {
            let gradient;
            gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);

            for(const shift of this.hueShift)
            {             
                gradient.addColorStop(shift.rupturePoint/max, shift.color)
            }

            return gradient;
        }
    }
}
</script>