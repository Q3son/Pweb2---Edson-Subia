// Funcionalidades generales del sitio
document.addEventListener('DOMContentLoaded', function() {
    // Actualizar el año en el footer
    document.querySelector('footer p').innerHTML += ` - ${new Date().getFullYear()}`;
    
    // Efecto de carga inicial
    const loadAnimation = () => {
      const elements = document.querySelectorAll('.exercise-card, .orbit');
      elements.forEach((el, i) => {
        setTimeout(() => {
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        }, i * 150);
      });
    };
  
    // Inicializar elementos
    document.querySelectorAll('.exercise-card').forEach(card => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = 'all 0.5s ease';
    });
  
    document.querySelector('.orbit').style.opacity = '0';
    document.querySelector('.orbit').style.transition = 'opacity 1s ease';
  
    // Ejecutar animación después de cargar todo
    window.addEventListener('load', () => {
      setTimeout(loadAnimation, 300);
    });
  
    // Smooth scroll para anclas
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
  });