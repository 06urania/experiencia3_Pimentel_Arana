document.addEventListener('DOMContentLoaded', function () {
  alert('Para reservar debes registrarte primero')

  var opcion = confirm('¿Quieres registrarte ahora?')

  if (opcion) {
    window.location.href = 'registro.html'
  } else {
  }
})
