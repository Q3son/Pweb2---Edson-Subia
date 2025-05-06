const express = require('express');
const app = express();
const path = require('path');

// Middleware para archivos estáticos
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

// Ruta para data.json
app.get('/data', (req, res) => {
    res.sendFile(path.join(__dirname, 'data.json'));
});

// Ruta principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// Iniciar servidor
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});