document.addEventListener('DOMContentLoaded', () => {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('region-select');
            data.forEach(region => {
                const option = document.createElement('option');
                option.value = region.region;
                option.textContent = region.region;
                select.appendChild(option);
            });

            select.addEventListener('change', () => {
                const selected = Array.from(select.selectedOptions).map(opt => opt.value);
                if (selected.length === 0) return;

                const chartData = [['Fecha', ...selected]];
                const fechas = data[0].confirmed.map(day => day.date);

                fechas.forEach((fecha, i) => {
                    const row = [fecha];
                    selected.forEach(regionName => {
                        const region = data.find(r => r.region === regionName);
                        row.push(parseInt(region.confirmed[i].value));
                    });
                    chartData.push(row);
                });

                google.charts.load('current', { packages: ['line'] });
                google.charts.setOnLoadCallback(() => {
                    const chart = new google.charts.Line(document.getElementById('grafico-regiones-seleccionadas'));
                    const dataTable = google.visualization.arrayToDataTable(chartData);
                    chart.draw(dataTable, google.charts.Line.convertOptions({
                        title: 'Comparativo de Regiones Seleccionadas',
                        curveType: 'function',
                        legend: { position: 'bottom' }
                    }));
                });
            });
        });
});