document.addEventListener('DOMContentLoaded', function() {
    // Configuración de los satélites orbitales
    const exercises = [
      { 
        name: "Invertir Texto", 
        icon: "invertir.svg", 
        link: "Lab_03/ejercicios/texto_invertido.html",
        color: "#3498db"
      },
      { 
        name: "Día de la Semana", 
        icon: "calendario.svg", 
        link: "Lab_03/ejercicios/día_Semana.html",
        color: "#e74c3c"
      },
      { 
        name: "Días Arequipa", 
        icon: "arequipa.svg", 
        link: "Lab_03/ejercicios/días_Arequipa.html",
        color: "#2ecc71"
      },
      { 
        name: "Código Meet", 
        icon: "meet.svg", 
        link: "Lab_03/ejercicios/código_de_meet.html",
        color: "#9b59b6"
      },
      { 
        name: "Suma Tabla", 
        icon: "tabla.svg", 
        link: "Lab_03/ejercicios/suma_tabla.html",
        color: "#f39c12"
      },
      { 
        name: "Editor Texto", 
        icon: "editor.svg", 
        link: "Lab_03/ejercicios/Página1.html",
        color: "#1abc9c"
      },
      { 
        name: "Calculadora", 
        icon: "calculadora.svg", 
        link: "Lab_03/ejercicios/Página2.html",
        color: "#d35400"
      }
    ];
  
    const orbit = document.createElement('div');
    orbit.className = 'orbit';
    document.querySelector('.orbital-system').appendChild(orbit);
  
    // Crear satélites para cada ejercicio
    exercises.forEach((exercise, index) => {
      const satellite = document.createElement('a');
      satellite.href = exercise.link;
      satellite.className = 'satellite';
      satellite.dataset.tooltip = exercise.name;
      satellite.style.setProperty('--satellite-color', exercise.color);
  
      const icon = document.createElement('img');
      icon.src = `assets/img/icons/${exercise.icon}`;
      icon.alt = exercise.name;
      
      satellite.appendChild(icon);
      orbit.appendChild(satellite);
    });
  
    // Efecto de rotación al pasar el mouse
    const orbitElement = document.querySelector('.orbit');
    let isPaused = false;
  
    orbitElement.addEventListener('mouseenter', () => {
      isPaused = true;
      orbitElement.style.animationPlayState = 'paused';
    });
  
    orbitElement.addEventListener('mouseleave', () => {
      isPaused = false;
      orbitElement.style.animationPlayState = 'running';
    });
  
    // Rotación manual al arrastrar
    let isDragging = false;
    let startAngle = 0;
    let currentAngle = 0;
  
    orbitElement.addEventListener('mousedown', (e) => {
      isDragging = true;
      startAngle = getAngle(e.clientX, e.clientY);
      orbitElement.style.animation = 'none';
      e.preventDefault();
    });
  
    document.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      const angle = getAngle(e.clientX, e.clientY);
      currentAngle = angle - startAngle;
      orbitElement.style.transform = `translate(-50%, -50%) rotateZ(${currentAngle}deg)`;
    });
  
    document.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        if (!isPaused) {
          orbitElement.style.animation = 'orbit-rotate 30s linear infinite';
        }
      }
    });
  
    function getAngle(x, y) {
      const rect = orbitElement.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      return Math.atan2(y - centerY, x - centerX) * 180 / Math.PI;
    }
  });