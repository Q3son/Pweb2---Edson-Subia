document.addEventListener('DOMContentLoaded', function() {
    const loader = document.getElementById('loader');
    const canvas = document.getElementById('grafico');

    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const regionesFiltradas = data.filter(region => 
                region.region !== 'Lima' && region.region !== 'Callao'
            );

            const fechas = data[0].confirmed.map(item => item.date);
            const datasets = regionesFiltradas.map(region => {
                const color = `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 1)`;
                return {
                    label: region.region,
                    data: region.confirmed.map(item => parseInt(item.value)),
                    borderColor: color,
                    backgroundColor: color.replace('1)', '0.2)'),
                    tension: 0.1
                };
            });

            const ctx = canvas.getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: { labels: fechas, datasets: datasets },
                options: {
                    responsive: true,
                    scales: {
                        y: { beginAtZero: true },
                        x: { ticks: { maxRotation: 45, minRotation: 45 } }
                    }
                }
            });

            loader.style.display = 'none';
            canvas.style.display = 'block';
        });
});