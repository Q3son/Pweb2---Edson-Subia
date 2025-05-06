document.addEventListener('DOMContentLoaded', () => {
    const loader = document.getElementById('loader');
    loader.style.display = 'flex';
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const filteredData = data.filter(region => !['Lima', 'Callao'].includes(region.region));
            const chartData = [['Fecha', 'Total Confirmados']];
            const fechas = filteredData[0].confirmed.map(day => day.date);

            fechas.forEach((fecha, i) => {
                let total = 0;
                filteredData.forEach(region => {
                    total += parseInt(region.confirmed[i].value);
                });
                chartData.push([fecha, total]);
            });

            google.charts.load('current', { packages: ['line'] });
            google.charts.setOnLoadCallback(() => {
                const chart = new google.charts.Line(document.getElementById('grafico-crecimiento-diario'));
                const dataTable = google.visualization.arrayToDataTable(chartData);
                chart.draw(dataTable, google.charts.Line.convertOptions({
                    title: 'Crecimiento Diario (Sin Lima y Callao)',
                    curveType: 'function',
                    legend: { position: 'none' },
                    colors: ['#EA4335']
                }));
            });
        })
        .finally(() => {
            loader.style.display = 'none';
        });
});