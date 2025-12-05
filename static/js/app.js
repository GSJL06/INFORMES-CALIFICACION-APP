/**
 * app.js - JavaScript para el Generador de Informes de Calificación
 * NETUX SAS - Sistema de Telemetría
 */

// Inicialización cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('Generador de Informes de Calificación - Inicializado');
    
    // Establecer fecha actual en campos de fecha vacíos
    setDefaultDates();
    
    // Inicializar validación de formulario
    initFormValidation();
});

/**
 * Establecer fechas por defecto
 */
function setDefaultDates() {
    const today = new Date().toISOString().split('T')[0];
    const dateInputs = document.querySelectorAll('input[type="date"]');
    
    dateInputs.forEach(input => {
        if (!input.value) {
            input.value = today;
        }
    });
}

/**
 * Inicializar validación de formulario
 */
function initFormValidation() {
    const form = document.getElementById('informeForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            // Validar que hay al menos un dispositivo
            const dispositivos = document.querySelectorAll('input[name="dispositivo_nombre[]"]');
            let hasDevice = false;
            dispositivos.forEach(input => {
                if (input.value.trim()) hasDevice = true;
            });
            
            if (!hasDevice) {
                e.preventDefault();
                alert('Debe agregar al menos un dispositivo');
                return false;
            }
            
            // Validar que hay al menos un contacto
            const contactos = document.querySelectorAll('input[name="contacto_nombre[]"]');
            let hasContact = false;
            contactos.forEach(input => {
                if (input.value.trim()) hasContact = true;
            });
            
            if (!hasContact) {
                e.preventDefault();
                alert('Debe agregar al menos un contacto de notificación');
                return false;
            }
            
            return true;
        });
    }
}

/**
 * Previsualizar imagen antes de subir
 */
function previewImage(input, previewId) {
    const preview = document.getElementById(previewId);
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(input.files[0]);
    }
}

/**
 * Confirmar antes de limpiar formulario
 */
function confirmReset() {
    return confirm('¿Está seguro de que desea limpiar todos los datos del formulario?');
}

/**
 * Formatear fecha para mostrar
 */
function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('es-CO', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

/**
 * Auto-cerrar mensajes flash después de 5 segundos
 */
setTimeout(function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(msg => {
        msg.style.opacity = '0';
        setTimeout(() => msg.remove(), 300);
    });
}, 5000);

