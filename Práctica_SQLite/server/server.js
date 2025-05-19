const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const app = express();

app.use(cors());

// Simulamos un error de conexión a la BD (ruta incorrecta)
const db = new sqlite3.Database('./ruta/incorrecta/imdb.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
        console.error("🔥 Error de conexión a la BD:", err.message); // Log en servidor
    }
});

app.get('/peliculas', (req, res) => {
    // Si la BD no está conectada, devolvemos un error controlado
    if (!db) {
        return res.status(500).json({ 
            error: "Base de datos no disponible. Revisa la conexión." 
        });
    }

    db.all("SELECT title, year FROM movies LIMIT 5", [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.json(rows || []); // Devuelve array vacío si no hay datos
        }
    });
});

app.listen(3000, () => console.log('Servidor en http://localhost:3000'));