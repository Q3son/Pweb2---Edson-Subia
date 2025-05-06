document.addEventListener('DOMContentLoaded', () => {
    const loader = document.getElementById('loader');
    loader.style.display = 'flex';
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const arequipa = data.find(region => region.region === 'Arequipa');
            const fechas = arequipa.confirmed.map(day => day.date);
            const valores = arequipa.confirmed.map(day => parseInt(day.value));

            google.charts.load('current', { packages: ['line'] });
            google.charts.setOnLoadCallback(() => {
                const chart = new google.charts.Line(document.getElementById('grafico-arequipa'));
                const dataTable = new google.visualization.DataTable();
                dataTable.addColumn('string', 'Fecha');
                dataTable.addColumn('number', 'Casos Confirmados');
                arequipa.confirmed.forEach(day => {
                    dataTable.addRow([day.date, parseInt(day.value)]);
                });
                chart.draw(dataTable, google.charts.Line.convertOptions({
                    title: 'Evolución de Casos en Arequipa',
                    curveType: 'function',
                    legend: { position: 'bottom' },
                    colors: ['#4285F4']
                }));
            });
        })
        .finally(() => {
            loader.style.display = 'none';
        });
});