document.getElementById('cargar').addEventListener('click', () => {
    fetch('http://localhost:3000/peliculas')
        .then(response => {
            if (!response.ok) throw new Error("Error en el servidor");
            return response.json();
        })
        .then(data => {
            const contenedor = document.getElementById('resultados');
            if (data.error) {
                contenedor.innerHTML = `<p class="error">${data.error}</p>`;
            } else {
                contenedor.innerHTML = data.map(movie => 
                    `<p>${movie.Title} (${movie.Year})</p>`  // ¡Mayúsculas en Title y Year!
                ).join('');
            }
        })
        .catch(error => {
            document.getElementById('resultados').innerHTML = 
                `<p class="error">Error: ${error.message}</p>`;
        });
});