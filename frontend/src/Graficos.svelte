<script>
    import { onMount } from 'svelte';
    import * as echarts from 'echarts';

    let pieChart;
    let barChart;

    let pieData = { labels: [], values: [] };
    let barData = { categories: [], values: [] };

    const fetchData = async () => {
        try {
            const response = await fetch('http://localhost:8000/data');
            //const response = await fetch('http://app:8001/data');
            const data = await response.json();

            
            pieData = data.piechart;
            barData = data.barplot;  

            renderCharts();
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    const renderCharts = () => {
        if (!document.getElementById('pie-chart') || !document.getElementById('bar-chart')) {
            console.error("Los div de los gráficos no están en el DOM todavía.");
            return;
        }

        if (!pieChart) {
            pieChart = echarts.init(document.getElementById('pie-chart'));
        }
        pieChart.setOption({
            title: { text: 'Porcentaje de productos vendidos', left: 'center' },
            tooltip: { trigger: 'item', formatter: '{a} <br/>{b}: {c} ({d}%)' },
            series: [{
                name: 'Productos',
                type: 'pie',
                radius: '50%',
                data: pieData.labels.map((label, index) => ({
                    name: label,
                    value: pieData.values[index]
                }))
            }]
        });

        if (!barChart) {
            barChart = echarts.init(document.getElementById('bar-chart'));
        }
        barChart.setOption({
            title: { text: 'Ventas Mensuales', left: 'center' },
            tooltip: {},
            xAxis: { type: 'category', data: barData.categories },
            yAxis: { type: 'value' },
            series: [{ data: barData.values, type: 'bar' }]
        });
    };

    onMount(() => {
        fetchData();
    });
</script>

<div style="display:flex">

    <div id="pie-chart" style="width: 100%; height: 600px;"></div>
    <div id="bar-chart" style="width: 100%; height: 500px;"></div>

</div>