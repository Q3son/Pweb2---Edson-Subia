document.addEventListener('DOMContentLoaded', function() {
  // 1. Configuración de satélites
  const exercises = [
      { 
          name: "Invertir Texto", 
          icon: "invertir.svg", 
          link: "ejercicios/texto_invertido.html",
          color: "#3498db"
      },
      { 
          name: "Día de la Semana", 
          icon: "calendario.svg", 
          link: "ejercicios/día_Semana.html",
          color: "#e74c3c" 
      },
      { 
          name: "Días Arequipa", 
          icon: "arequipa.svg", 
          link: "ejercicios/días_Arequipa.html",
          color: "#2ecc71"
      },
      { 
          name: "Código Meet", 
          icon: "meet.svg", 
          link: "ejercicios/código_de_meet.html",
          color: "#9b59b6"
      },
      { 
          name: "Suma Tabla", 
          icon: "tabla.svg", 
          link: "ejercicios/suma_tabla.html",
          color: "#f39c12"
      },
      { 
          name: "Editor Texto", 
          icon: "editor.svg", 
          link: "ejercicios/Página1.html",
          color: "#1abc9c"
      },
      { 
          name: "Calculadora", 
          icon: "calculadora.svg", 
          link: "ejercicios/Página2.html",
          color: "#d35400"
      }
  ];

  // 2. Creación del sistema orbital
  const orbitalSystem = document.getElementById('orbitalSystem');
  const orbit = document.createElement('div');
  orbit.className = 'orbit';
  orbitalSystem.appendChild(orbit);

  // 3. Posicionamiento de satélites
  exercises.forEach((exercise, index) => {
      const angle = (index * (360 / exercises.length)) * (Math.PI / 180);
      const radius = 180;
      const x = radius * Math.cos(angle);
      const y = radius * Math.sin(angle);

      const satellite = document.createElement('a');
      satellite.href = exercise.link;
      satellite.className = 'satellite';
      satellite.dataset.tooltip = exercise.name;
      satellite.style.setProperty('--satellite-color', exercise.color);
      satellite.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;

      const icon = document.createElement('img');
      icon.src = `assets/img/icons/${exercise.icon}`;
      icon.alt = exercise.name;
      icon.loading = "lazy"; // Optimización de carga
      
      satellite.appendChild(icon);
      orbit.appendChild(satellite);
  });

  // 4. Animación de rotación
  let angle = 0;
  let lastTime = 0;
  const rotationSpeed = 0.3; // Grados por frame

  function animate(currentTime) {
      const deltaTime = currentTime - lastTime;
      lastTime = currentTime;
      
      angle += rotationSpeed * (deltaTime / 16); // Ajuste para 60fps
      orbit.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`;
      
      requestAnimationFrame(animate);
  }

  // 5. Control de animación
  orbitalSystem.addEventListener('mouseenter', () => {
      orbitalSystem.style.animationPlayState = 'paused';
  });

  orbitalSystem.addEventListener('mouseleave', () => {
      orbitalSystem.style.animationPlayState = 'running';
  });

  // Iniciar animación
  requestAnimationFrame(animate);
});