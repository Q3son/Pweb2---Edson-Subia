document.addEventListener('DOMContentLoaded', () => {
    const loader = document.getElementById('loader');
    loader.style.display = 'flex';
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const totales = data.map(region => ({
                nombre: region.region,
                total: region.confirmed.reduce((sum, day) => sum + parseInt(day.value), 0)
            }));

            google.charts.load('current', { packages: ['table'] });
            google.charts.setOnLoadCallback(() => {
                const table = new google.visualization.Table(document.getElementById('total-confirmados'));
                const dataTable = new google.visualization.DataTable();
                dataTable.addColumn('string', 'Región');
                dataTable.addColumn('number', 'Total Confirmados');
                dataTable.addRows(totales.map(region => [region.nombre, region.total]));
                table.draw(dataTable, { title: 'Total Confirmados por Región', width: '100%' });
            });
        })
        .finally(() => {
            loader.style.display = 'none';
        });
});