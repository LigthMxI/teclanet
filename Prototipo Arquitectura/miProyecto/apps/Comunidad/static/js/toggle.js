var toggle = document.getElementById('container');
var body = document.querySelector('body');

// Recuperar el estado almacenado del localStorage
var isToggleActive = localStorage.getItem('toggleActive');
var isBodyActive = localStorage.getItem('bodyActive');

// Establecer los estados iniciales
if (isToggleActive === 'true') {
  toggle.classList.add('active');
}

if (isBodyActive === 'true') {
  body.classList.add('active');
}

toggle.onclick = function() {
  toggle.classList.toggle('active');
  body.classList.toggle('active');

  // Guardar el estado actual en el localStorage
  var isToggleActive = toggle.classList.contains('active');
  var isBodyActive = body.classList.contains('active');

  localStorage.setItem('toggleActive', isToggleActive);
  localStorage.setItem('bodyActive', isBodyActive);
};

