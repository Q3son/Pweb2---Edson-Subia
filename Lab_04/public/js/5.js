document.addEventListener('DOMContentLoaded', () => {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const regiones = ['Lima', 'Arequipa', 'Cusco', 'Piura']; // Ejemplo
            const chartData = [['Fecha', ...regiones]];

            // Obtener fechas comunes (ejemplo simplificado)
            const fechas = data[0].confirmed.map(day => day.date);

            fechas.forEach((fecha, i) => {
                const row = [fecha];
                regiones.forEach(region => {
                    const regionData = data.find(r => r.region === region);
                    row.push(parseInt(regionData.confirmed[i].value));
                });
                chartData.push(row);
            });

            google.charts.load('current', { packages: ['line'] });
            google.charts.setOnLoadCallback(() => {
                const chart = new google.charts.Line(document.getElementById('grafico-comparativo'));
                const dataTable = google.visualization.arrayToDataTable(chartData);
                chart.draw(dataTable, google.charts.Line.convertOptions({
                    title: 'Comparativo entre Regiones',
                    curveType: 'function',
                    legend: { position: 'bottom' },
                    colors: ['#4285F4', '#EA4335', '#FBBC05', '#34A853']
                }));
            });
        });
});