const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const app = express();

app.use(cors());

// Conexión a la BD con manejo real de errores
let db;
try {
    db = new sqlite3.Database('../imdb.db', sqlite3.OPEN_READWRITE, (err) => {
        if (err) {
            console.error("🔥 Error de conexión a la BD:", err.message);
            db = null; // Forzamos db a null si hay error
        }
    });
} catch (err) {
    console.error("🚨 Error al crear conexión a BD:", err);
    db = null;
}

app.get('/peliculas', (req, res) => {
    if (!db) {
        return res.status(500).json({ 
            error: "Base de datos no disponible. Revisa la conexión." 
        });
    }

    db.all("SELECT title, year FROM movie LIMIT 5", [], (err, rows) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json(rows || []);
    });
});

app.get('/', (req, res) => {
    res.send(`
        <h1>Servidor IMDB funcionando</h1>
        <p>Usa la ruta <a href="/peliculas">/peliculas</a> para ver los datos.</p>
    `);
});

app.listen(3000, () => console.log('Servidor en http://localhost:3000'));