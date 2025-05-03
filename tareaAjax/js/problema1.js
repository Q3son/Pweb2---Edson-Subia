document.addEventListener('DOMContentLoaded', function() {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const regiones = data.map(region => region.region);
            const select1 = document.getElementById('region1');
            const select2 = document.getElementById('region2');

            regiones.forEach(region => {
                const option1 = document.createElement('option');
                option1.value = region;
                option1.textContent = region;
                select1.appendChild(option1);

                const option2 = document.createElement('option');
                option2.value = region;
                option2.textContent = region;
                select2.appendChild(option2);
            });

            document.getElementById('loader').style.display = 'none';
            document.getElementById('grafico').style.display = 'block';
        });
});

function compararRegiones() {
    const region1 = document.getElementById('region1').value;
    const region2 = document.getElementById('region2').value;
    const loader = document.getElementById('loader');
    const canvas = document.getElementById('grafico');

    loader.style.display = 'flex';
    canvas.style.display = 'none';

    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const datosRegion1 = data.find(r => r.region === region1).confirmed;
            const datosRegion2 = data.find(r => r.region === region2).confirmed;

            const fechas = datosRegion1.map(item => item.date);
            const valores1 = datosRegion1.map(item => parseInt(item.value));
            const valores2 = datosRegion2.map(item => parseInt(item.value));

            const ctx = canvas.getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: fechas,
                    datasets: [
                        {
                            label: region1,
                            data: valores1,
                            borderColor: 'rgba(75, 192, 192, 1)',
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            tension: 0.1
                        },
                        {
                            label: region2,
                            data: valores2,
                            borderColor: 'rgba(153, 102, 255, 1)',
                            backgroundColor: 'rgba(153, 102, 255, 0.2)',
                            tension: 0.1
                        }
                    ]
                },
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
}