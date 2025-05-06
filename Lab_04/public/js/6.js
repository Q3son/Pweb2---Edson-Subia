document.addEventListener('DOMContentLoaded', () => {
    const loader = document.getElementById('loader');
    loader.style.display = 'flex';
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const filteredData = data.filter(region => !['Lima', 'Callao'].includes(region.region));
            const chartData = [['Región', 'Crecimiento']];

            filteredData.forEach(region => {
                const crecimiento = region.confirmed.reduce((sum, day) => sum + parseInt(day.value), 0);
                chartData.push([region.region, crecimiento]);
            });

            google.charts.load('current', { packages: ['bar'] });
            google.charts.setOnLoadCallback(() => {
                const chart = new google.charts.Bar(document.getElementById('grafico-sin-lima-callao'));
                const dataTable = google.visualization.arrayToDataTable(chartData);
                chart.draw(dataTable, google.charts.Bar.convertOptions({
                    title: 'Crecimiento (Excluyendo Lima y Callao)',
                    colors: ['#34A853']
                }));
            });
        })
        .finally(() => {
            loader.style.display = 'none';
        });
});