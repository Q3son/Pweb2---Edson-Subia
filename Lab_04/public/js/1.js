document.addEventListener('DOMContentLoaded', () => {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const regiones = data.map(region => region.region);
            const listHTML = `<ul class="region-list">${regiones.map(region => `<li>${region}</li>`).join('')}</ul>`;
            document.getElementById('regiones-list').innerHTML = listHTML;
        });
});