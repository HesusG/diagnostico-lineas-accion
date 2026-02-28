const fs = require('fs');
const path = require('path');

const htmlContent = `<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slides Semana 3 - Diagnóstico</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.5; }
        h1 { color: #2563eb; }
        .card { border: 1px solid #e5e7eb; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; transition: transform 0.2s; }
        .card:hover { transform: translateY(-2px); box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
        a { text-decoration: none; color: inherit; display: block; }
        .tag { background: #dbeafe; color: #1e40af; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem; display: inline-block; margin-bottom: 0.5rem; }
    </style>
</head>
<body>
    <h1>📚 Slides Semana 3: Administración Estratégica</h1>
    <p>Material para el curso CD2001B - Diagnóstico para Líneas de Acción (Caso Teletón)</p>
    
    <a href="./slide1/" class="card">
        <span class="tag">Parte 1</span>
        <h2>🔭 Estrategia y Análisis del Entorno</h2>
        <p>Fundamentos, Misión/Visión, PESTEL, FODA y Controversia ONU.</p>
    </a>

    <a href="./slide2/" class="card">
        <span class="tag">Parte 2</span>
        <h2>🛠️ Herramientas de Medición</h2>
        <p>Objetivos SMART, KPIs, 5 Fuerzas de Porter y Matriz BCG.</p>
    </a>
    
    <footer style="margin-top: 3rem; font-size: 0.875rem; color: #6b7280;">
        Generado automáticamente con Slidev y GitHub Actions.
    </footer>
</body>
</html>`;

const distDir = path.join(__dirname, '../dist');
if (!fs.existsSync(distDir)) {
    fs.mkdirSync(distDir, { recursive: true });
}

fs.writeFileSync(path.join(distDir, 'index.html'), htmlContent);
console.log('Generated dist/index.html');
