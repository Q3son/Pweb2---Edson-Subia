document.addEventListener('DOMContentLoaded', () => {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const top10 = data.map(region => ({
                nombre: region.region,
                total: region.confirmed.reduce((sum, day) => sum + parseInt(day.value), 0)
            })).sort((a, b) => b.total - a.total).slice(0, 10);

            google.charts.load('current', { packages: ['bar'] });
            google.charts.setOnLoadCallback(() => {
                const chart = new google.charts.Bar(document.getElementById('top10-regiones'));
                const dataTable = new google.visualization.DataTable();
                dataTable.addColumn('string', 'Región');
                dataTable.addColumn('number', 'Casos Confirmados');
                dataTable.addRows(top10.map(region => [region.nombre, region.total]));
                chart.draw(dataTable, google.charts.Bar.convertOptions({
                    title: 'Top 10 Regiones con Más Casos Confirmados',
                    colors: ['#e6693e'],
                    chartArea: { width: '60%' }
                }));
            });
        });
});