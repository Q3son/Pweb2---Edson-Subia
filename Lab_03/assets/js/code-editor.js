// Configuración del editor de código (para los ejercicios)
document.addEventListener('DOMContentLoaded', function() {
    // Resaltado de sintaxis
    if (document.querySelector('pre code')) {
      // Usar Highlight.js si está disponible
      if (typeof hljs !== 'undefined') {
        hljs.highlightAll();
      } else {
        // Fallback básico
        document.querySelectorAll('pre code').forEach(block => {
          const code = block.textContent;
          const highlighted = code
            .replace(/(\/\/.*$)/gm, '<span class="comment">$1</span>')
            .replace(/\b(function|return|const|let|var|if|else|for|while)\b/g, '<span class="keyword">$1</span>')
            .replace(/\b(true|false|null|undefined)\b/g, '<span class="value">$1</span>')
            .replace(/\b(\d+)\b/g, '<span class="number">$1</span>');
          block.innerHTML = highlighted;
        });
      }
    }
  
    // Hacer el código editable en los ejercicios
    const codeBlocks = document.querySelectorAll('.editable-code');
    codeBlocks.forEach(block => {
      block.setAttribute('contenteditable', 'true');
      block.addEventListener('input', function() {
        // Actualizar resaltado al editar
        if (typeof hljs !== 'undefined') {
          hljs.highlightElement(this);
        }
      });
    });
  
    // Botones de ejecución
    document.querySelectorAll('.run-button').forEach(button => {
      button.addEventListener('click', function() {
        const code = this.parentElement.nextElementSibling.textContent;
        try {
          // Ejecutar el código (usando Function para evitar eval directo)
          new Function(code)();
        } catch (error) {
          console.error('Error al ejecutar:', error);
        }
      });
    });
  });