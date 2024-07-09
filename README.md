[Uploading im@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Roboto', sans-serif;
    scroll-behavior: smooth;
    background-color: #d3d3d3;
    margin: 0;
    padding: 0;
}

.texto-redondeado {
    font-family: 'Roboto', sans-serif;
}

.contenido-header {
    background-color: rgba(0, 0, 0, 0.8);
    position: fixed;
    width: 100vw;
    z-index: 100;
    top: 0;
    left: 0;
    margin: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 20px 30px;
    flex-grow: 2;
}

#logo img {
    border-radius: 25%;
    width: 50px;
    height: 50px;
}

.nav-main {
    flex-grow: 1;
    display: flex;
    justify-content: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-menu li a:hover {
    color: #1ad5ee;
}

.redes {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-right: 20px;
    flex-shrink: 0;
}

.redes a {
    text-decoration: none;
    color: #fff;
    margin-left: 10px;
    transition: color 0.3s ease;
}

.redes a:hover {
    color: #12ddef;
}

.presentacion-container {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(imagenes/_22eedba3-5180-4087-a579-cda14da58dc2.jpeg) center center / cover;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-align: center;
    position: relative;
}

.presentacion {
    max-width: 1100px;
    margin: auto;
    color: #fff;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
}

.presentacion .bienvenida {
    font-size: 16px;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 5px;
}

.presentacion h2 {
    font-size: 20px;
    margin-bottom: 25px;
    text-align: left;
}

.presentacion h2 span {
    font-size: 25px;
    color: red;
}

.presentacion .descripcion {
    max-width: 100%;
    margin: 25px 50px;
    font-size: 18px;
    text-align: center;
}

.presentacion a {
    text-decoration: none;
    display: inline-block;
    margin: 25px 0;
    padding: 20px 25px;
    border: 2px solid #fff;
    border-radius: 50px;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: 0.5s;
}

.presentacion a:hover {
    background-color: aqua;
}

#icono-nav {
    color: #fff;
    display: none;
    cursor: pointer;
}

/* Estilos para la sección de alojamiento */

#alojamiento {
    padding: 50px 0;
    background-color: #f2f2f2;
    text-align: center;
}

#alojamiento .titulo-seccion {
    margin-top: 20px;
    margin-bottom: 50px;
    font-size: 28px;
    text-transform: capitalize;
    color: #111135;
}

#alojamiento .fila {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
}

#alojamiento .servicio {
    width: 300px;
    background-color: #fff;
    padding: 20px;
    margin: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease;
}

#alojamiento .servicio:hover {
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}

#alojamiento .servicio h4 {
    font-size: 20px;
    margin-bottom: 15px;
}

#alojamiento .servicio hr {
    width: 50%;
    margin: auto;
    margin-bottom: 15px;
    border-color: #ddd;
}

#alojamiento .servicio p {
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 15px;
}

#alojamiento .servicio .caracteristicas {
    list-style-type: none;
    padding: 0;
    text-align: left;
}

#alojamiento .servicio .caracteristicas li {
    margin-bottom: 8px;
}

#alojamiento .servicio .caracteristicas li i {
    margin-right: 8px;
    color: #5cb85c; /* Verde para características disponibles */
}

#alojamiento .servicio .caracteristicas li .fa-xmark {
    color: #d9534f; /* Rojo para características no disponibles */
}

.btn-contacto {
    display: inline-block;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.btn-contacto:hover {
    background-color: #0056b3;
}

/* Estilos para la sección de conclusión */

#conclusion {
    background-image: url('imagenes/_f27c292f-e342-4251-9b79-cc718d4384c9.jpeg');
    background-size: cover;
    background-position: center;
    padding: 50px 0;
    text-align: center;
}

#conclusion .container {
    max-width: 800px;
    margin: 0 auto;
}

#conclusion .contenido {
    background-color: rgba(255, 255, 255, 0.8); /* Fondo semitransparente blanco */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1); /* Sombra ligera */
}

#conclusion .titulo-seccion {
    font-size: 24px;
    color: #111135;
    text-transform: capitalize;
    margin-bottom: 20px;
}

#conclusion p {
    font-size: 16px;
    line-height: 1.6;
    color: #333;
}


@media (max-width: 768px) {
    #nav.responsive {
        display: block;
        background-color: rgba(0, 0, 0, 0.8);
        width: 100%;
        height: calc(100vh - 60px);
        position: absolute;
        top: 60px;
        left: 0;
        padding: 10px 0;
        margin: 0;
    }

    #nav.responsive ul {
        display: block;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    #nav.responsive ul li {
        margin: 10px 0;
        text-align: left;
    }
}

@media (max-width: 480px) {
    .nav-main {
        display: none;
    }

    #icono-nav {
        display: block;
    }

    .redes {
        display: none;
    }

    .presentacion h2 {
        font-size: 18px;
    }

    .presentacion .descripcion {
        font-size: 16px;
    }

    #alojamiento .servicio {
        width: 100%;
        margin: 10px 0;
    }
}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <link rel="stylesheet" href="alojamiento.css"/>
    <script src="alojamiento.js" defer></script>
    <title>Alojamiento de Sitios Web</title>
</head>
<body>
    <div class="contenido-header">
        <div id="logo">
            <img src="imagenes/_78881fc4-1efe-4915-bb51-8f76768ae06b.jpeg" alt="Logo">
        </div>
        <div id="icono-nav" class="menu-btn">
            <i class="fas fa-bars fa-2x"></i>
        </div>
        <nav id="nav" class="nav-main">
            <ul class="nav-menu">
                <li><a href="Inicio.html">Inicio</a></li>
                <li><a href="Sobre-nosotros.html">Sobre Nosotros</a></li>
                <li><a href="Servicio.html">Servicios</a></li>
                <li><a href="Cursos.html">Cursos</a></li>
                <li><a href="alojamiento.html">Alojamiento web</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
            <div class="redes">
                <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            </div>
        </nav>
    </div>

    <div class="presentacion-container">
        <div class="presentacion">
            <h1 class="texto-redondeado">Alojamiento de Sitios Web</h1>
            <br>
            <p class="descripcion texto-redondeado">
                En "WebTech Financial Mastery", ofrecemos servicios completos de alojamiento web para que tu sitio esté siempre accesible y seguro. Según el plan que elijas, incluimos diferentes niveles de soporte y características para satisfacer tus necesidades.
            </p>
            <a href="https://www.facebook.com/profile.php?id=61558466327819" target="_blank">Síguenos en Facebook</a>
        </div>
    </div>

    <br>
    <br>

    <!--Alojamiento-->
    <section id="alojamiento">
        <h3 class="titulo-seccion">Planes de Alojamiento</h3>
        <div class="fila">
            <div class="servicio">
                <span class="icono"><i class="fa-solid fa-server"></i></span>
                <h4>Plan Básico de Alojamiento</h4>
                <hr>
                <ul class="caracteristicas">
                    <li><i class="fa-solid fa-check"></i> Hosting confiable</li>
                    <li><i class="fa-solid fa-check"></i> Dominio incluido</li>
                    <li><i class="fa-solid fa-check"></i> Soporte técnico básico</li>
                    <li><i class="fa-solid fa-xmark"></i> Certificado SSL</li>
                    <li><i class="fa-solid fa-xmark"></i> Soporte técnico prioritario</li>
                    <li><i class="fa-solid fa-xmark"></i> Soporte técnico 24/7</li>
                    <li><i class="fa-solid fa-xmark"></i> Backups automáticos</li>
                </ul>
                <a href="Contacto.html" class="btn-contacto" target="_blank">Contactar</a>
            </div>
            <div class="servicio">
                <span class="icono"><i class="fa-solid fa-server"></i></span>
                <h4>Plan Intermedio de Alojamiento</h4>
                <hr>
                <ul class="caracteristicas">
                    <li><i class="fa-solid fa-check"></i> Hosting avanzado</li>
                    <li><i class="fa-solid fa-check"></i> Dominio incluido</li>
                    <li><i class="fa-solid fa-check"></i> Certificado SSL</li>
                    <li><i class="fa-solid fa-check"></i> Soporte técnico prioritario</li>
                    <li><i class="fa-solid fa-xmark"></i> Soporte técnico 24/7</li>
                    <li><i class="fa-solid fa-xmark"></i> Backups automáticos</li>
                </ul>
                <a href="Contacto.html" class="btn-contacto" target="_blank">Contactar</a>
            </div>
            <div class="servicio">
                <span class="icono"><i class="fa-solid fa-server"></i></span>
                <h4>Plan Avanzado de Alojamiento</h4>
                <hr>
                <ul class="caracteristicas">
                    <li><i class="fa-solid fa-check"></i> Hosting premium</li>
                    <li><i class="fa-solid fa-check"></i> Dominio incluido</li>
                    <li><i class="fa-solid fa-check"></i> Certificado SSL</li>
                    <li><i class="fa-solid fa-check"></i> Soporte técnico 24/7</li>
                    <li><i class="fa-solid fa-check"></i> Backups automáticos</li>
                </ul>
                <a href="Contacto.html" class="btn-contacto" target="_blank">Contactar</a>
            </div>
        </div>
    </section>

    <br>
    <br>

    <!--Conclusion-->
    <section id="conclusion">
        <div class="container">
            <div class="contenido">
                <h3 class="titulo-seccion">Conclusión</h3>
                <p>En "WebTech Financial Mastery", nos comprometemos a proporcionar servicios de alojamiento web que no solo cumplan con tus expectativas, sino que también aseguren que tu sitio esté siempre accesible y seguro. Cada plan está diseñado para ofrecer valor agregado y resultados tangibles que te ayuden a alcanzar tus objetivos empresariales.</p>
            </div>
        </div>
    </section>
</body>
</html>

// Función para manejar el menú responsivo
function toggleResponsiveMenu() {
    var nav = document.getElementById('nav');
    nav.classList.toggle('nav-main');
    nav.classList.toggle('responsive');
}

// Event listener para el icono de navegación responsivo
document.getElementById('icono-nav').addEventListener('click', function() {
    toggleResponsiveMenu();
});

/* Estilos del cuerpo del documento */
body {
    font-family: 'Roboto', sans-serif;
    background-color: #d3d3d3;
    margin: 0;
    padding: 0;
}

/* Estilos del contenido del encabezado */
.contenido-header {
    background-color: rgba(0, 0, 0, 0.8);
    position: fixed;
    width: 100%;
    z-index: 100;
    top: 0;
    left: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 0 30px;
}

#logo img {
    border-radius: 25%;
    width: 50px;
    height: 50px;
}

.nav-main {
    flex-grow: 1;
    display: flex;
    justify-content: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-menu li a:hover {
    color: #1ad5ee;
}

.redes {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-right: 20px;
    flex-shrink: 0;
}

.redes a {
    text-decoration: none;
    color: #fff;
    margin-left: 10px;
    transition: color 0.3s ease;
}

.redes a:hover {
    color: #12ddef;
}

#icono-nav {
    color: #fff;
    display: none;
    cursor: pointer;
}

/* Estilos del formulario de contacto */
.contacto {
    padding: 100px 0;
    text-align: center;
}

.titulo-seccion {
    font-size: 2rem;
    margin-bottom: 30px;
    color: #333;
}

.formulario-contacto {
    max-width: 600px;
    margin: 0 auto;
    background-color: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.formulario-contacto .campo {
    margin-bottom: 20px;
}

.formulario-contacto label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

.formulario-contacto input[type="text"],
.formulario-contacto input[type="email"],
.formulario-contacto input[type="tel"],
.formulario-contacto textarea {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

.formulario-contacto textarea {
    resize: vertical;
}

.formulario-contacto button {
    display: block;
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    background-color: #1ad5ee;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.formulario-contacto button:hover {
    background-color: #12ddef;
}

/* Estilos para el footer */
footer {
    background-color: rgba(0, 0, 0, 0.8);
    color: #fff;
    text-align: center;
    padding: 10px 0;
    position: fixed;
    bottom: 0;
    width: 100%;
}

footer p {
    margin: 0;
    font-size: 0.9rem;
}

/* Media queries para dispositivos móviles */
@media (max-width: 768px) {
    .contenido-header {
        padding: 10px 20px;
        height: auto;
    }

    .nav-main {
        display: none;
    }

    #icono-nav {
        display: block;
    }

    .redes {
        display: none;
    }

    #nav.responsive {
        display: block;
        background-color: rgba(0, 0, 0, 0.8);
        width: 100%;
        height: calc(100vh - 60px);
        position: absolute;
        top: 60px;
        left: 0;
        padding: 10px 0;
        margin: 0;
    }

    #nav.responsive ul {
        display: block;
        text-align: center;
    }

    #nav.responsive ul li {
        margin: 10px 0;
        text-align: left;
    }
}

@media (max-width: 480px) {
    .formulario-contacto {
        padding: 20px;
    }

    .titulo-seccion {
        font-size: 1.5rem;
    }

    .formulario-contacto input[type="text"],
    .formulario-contacto input[type="email"],
    .formulario-contacto input[type="tel"],
    .formulario-contacto textarea {
        padding: 8px;
    }
}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacto</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <link rel="stylesheet" href="Contacto.css">
    <script src="Contacto.js" defer></script>
</head>
<body>
    <div class="contenido-header">
        <div id="logo">
            <img src="imagenes/_78881fc4-1efe-4915-bb51-8f76768ae06b.jpeg" alt="Logo">
        </div>
        <div id="icono-nav" class="menu-btn">
            <i class="fas fa-bars fa-2x"></i>
        </div>
        <nav id="nav" class="nav-main">
            <ul class="nav-menu">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="Sobre-nosotros.html">Sobre Nosotros</a></li>
                <li><a href="Servicio.html">Servicios</a></li>
                <li><a href="Cursos.html">Cursos</a></li>
                <li><a href="alojamiento.html">Alojamiento web</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
            <div class="redes">
                <a href="https://www.facebook.com/profile.php?id=61558466327819/" target="_blank"><i class="fab fa-facebook"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
            </div>
        </nav>
    </div>

    <form id="contactForm" class="formulario-contacto" action="https://formspree.io/f/mwpekdpo" method="POST">
        <section id="contacto" class="contacto">
            <div class="container">
                <h2 class="titulo-seccion">Contáctanos</h2>
                <div class="campo">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" name="nombre" required>
                </div>
                <div class="campo">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="campo">
                    <label for="telefono">Teléfono:</label>
                    <input type="tel" id="telefono" name="telefono">
                </div>
                <div class="campo">
                    <label for="mensaje">Mensaje:</label>
                    <textarea id="mensaje" name="message" rows="4" required></textarea>
                </div>
                <button type="submit" class="btn-contacto">Enviar</button>
            </div>
        </section>
    </form>

    <footer>
        <div class="container">
            <p>&copy; 2024 WebTech Financial Mastery. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>

// Función para manejar el menú responsivo
function toggleResponsiveMenu() {
    var nav = document.getElementById('nav');
    nav.classList.toggle('nav-main');
    nav.classList.toggle('responsive');
}

// Event listener para el icono de navegación responsivo
document.getElementById('icono-nav').addEventListener('click', function() {
    toggleResponsiveMenu();
});


// Función para validar y enviar el formulario
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que se envíe el formulario por defecto

    // Validación de campos (puedes agregar más validaciones según necesites)
    var nombre = document.getElementById('nombre').value.trim();
    var email = document.getElementById('email').value.trim();
    var mensaje = document.getElementById('mensaje').value.trim();

    if (nombre === '' || email === '' || mensaje === '') {
        alert('Por favor, completa todos los campos.');
        return;
    }

    // Aquí puedes agregar código para enviar el formulario (por ejemplo, mediante AJAX)
    // En este ejemplo, simplemente mostramos una alerta de éxito
    alert('¡Formulario enviado con éxito!');
    document.getElementById('contactForm').reset(); // Reinicia el formulario después de enviarlo
});

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}

/* Estilos del cuerpo del documento */
body {
    font-family: 'Roboto', sans-serif;
    scroll-behavior: smooth;
    background-color: #d3d3d3;
    margin: 0px;
    padding: 0px;
}

.texto-redondeado {
    font-family: 'Roboto', sans-serif;
}

.contenido-header {
    background-color: rgba(0, 0, 0, 0.8);
    position: fixed;
    width: 100vw;
    z-index: 100;
    top: 0;
    left: 0px;
    margin: 0px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 20px 30px;
    flex-grow: 2;
}

#logo img {
    border-radius: 25%;
    width: 50px;
    height: 50px;
}

.nav-main {
    flex-grow: 1;
    display: flex;
    justify-content: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-menu li a:hover {
    color: #1ad5ee;
}

.redes {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* Alineación a la derecha */
  margin-right: 20px; /* Espacio a la derecha */
  flex-shrink: 0; /* Evita que las redes sociales se encogan */
}

.redes a {
  text-decoration: none;
  color: #fff;
  margin-left: 10px; /* Espacio entre íconos */
  transition: color 0.3s ease;
}

.redes a:hover {
  color: #12ddef;
}

.presentacion-container {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(imagenes/_22eedba3-5180-4087-a579-cda14da58dc2.jpeg) center center / cover;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-align: center;
    position: relative;
}

.presentacion {
    max-width: 1100px;
    margin: auto;
    color: #fff;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
}

.presentacion .bienvenida {
    font-size: 16px;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 5px;
}

.presentacion h2 {
    font-size: 20px;
    margin-bottom: 25px;
    text-align: left;
}

.presentacion h2 span {
    font-size: 25px;
    color: red;
}

.presentacion .descripcion {
    max-width: 100%;
    margin: 25px 50px;
    font-size: 18px;
    text-align: center;
}

.presentacion a {
    text-decoration: none;
    display: inline-block;
    margin: 25px 0;
    padding: 20px 25px;
    border: 2px solid #fff;
    border-radius: 50px;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: 0.5s;
}

.presentacion a:hover {
    background-color: aqua;
}

#icono-nav {
    color: #fff;
    display: none;
    cursor: pointer;
}

/* Estilos para la sección de cursos */
#cursos {
    padding: 50px 0;
    
}

#cursos .titulo-seccion {
    font-size: 24px;
    text-align: center;
    margin-bottom: 30px;
    text-transform: uppercase;
}

#cursos .fila {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    max-width: 1200px;
    margin: 0 auto;
}

#cursos .curso {
    width: calc(50% - 20px);
    background-color: #fff;
    padding: 20px;
    margin: 20px 0;
    border-radius: 5px;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
}

#cursos .curso h4 {
    font-size: 20px;
    margin-bottom: 10px;
    color: #333;
}

#cursos .curso p {
    margin-bottom: 10px;
}

#cursos .curso ul {
    margin-bottom: 10px;
    padding-left: 20px;
}

#cursos .curso ul li {
    margin-bottom: 5px;
}

#cursos .curso strong {
    font-weight: bold;
}

#cursos .curso .ejemplo {
    font-style: italic;
    color: #666;
}

/* Estilos para la sección de conclusión */
#conclusion {
    padding: 50px 0;
    text-align: center;
}

#conclusion .titulo-seccion {
    font-size: 24px;
    text-transform: uppercase;
    margin-bottom: 30px;
}

#conclusion p {
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 20px;
}

#conclusion .boton-contacto {
    display: inline-block;
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s;
}

#conclusion .boton-contacto:hover {
    background-color: #45a049;
}

/**/
/* Media queries para dispositivos móviles */
@media (max-width: 768px) {
    /* Estilos para el menú responsivo */
    #nav.responsive {
        display: block;
        background-color: rgba(0, 0, 0, 0.8);
        width: 100%; /* Ocupa todo el ancho disponible */
        height: calc(100vh - 60px); /* Calcula el alto del viewport menos la altura del header */
        position: absolute;
        top: 60px; /* Posiciona debajo del header */
        left: 0;
        padding: 10px 0;
        margin: 0;
    }
  
    #nav.responsive ul {
        display: block;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
  
    #nav.responsive ul li {
        margin: 10px 0;
        text-align: left; /* Alinea los elementos del menú a la izquierda */
    }
  }
  
  
    #nav.responsive ul {
        display: block !important;
        text-align: center;
    }
  
    #nav.responsive ul li {
        margin: 5px 0;
        text-align: left; /* Alinea los elementos del menú a la izquierda */
    }
  
    @media screen and (max-width: 800px) {
      nav.responsive ul {
          display: block !important;
          text-align: center;
      }
  
      nav.responsive ul li {
          margin-bottom: 10px; /* Ajusta el margen inferior entre elementos */
      }
  }
  
  
  /* Media queries para tabletas y dispositivos móviles */
  @media (max-width: 768px) {
      .nav-main {
          display: none; /* Oculta la barra de navegación en tamaños pequeños */
      }
  
      #icono-nav {
          display: block; /* Muestra el icono de navegación en tamaños pequeños */
      }
  
      .redes {
          display: none; /* Oculta las redes sociales en tamaños pequeños */
      }
  
      .presentacion h2 {
          font-size: 18px; /* Ajusta el tamaño del título en tamaños pequeños */
      }
  
      .presentacion .descripcion {
          font-size: 16px; /* Ajusta el tamaño del texto de descripción en tamaños pequeños */
      }
  }
  
  /* Media queries para dispositivos móviles */
  @media (max-width: 480px) {
      .nav-main {
          display: none; /* Oculta la barra de navegación en tamaños muy pequeños */
      }
  
      #icono-nav {
          display: block; /* Muestra el icono de navegación en tamaños muy pequeños */
      }
  
      .redes {
          display: none; /* Oculta las redes sociales en tamaños muy pequeños */
      }
  
      .presentacion h2 {
          font-size: 16px; /* Ajusta el tamaño del título en tamaños muy pequeños */
      }
  
      .presentacion .descripcion {
          font-size: 14px; /* Ajusta el tamaño del texto de descripción en tamaños muy pequeños */
      }
  }
  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <link rel="stylesheet" href="Cursos.css"/>
    <script src="Cursos.js" defer></script>
    <title>Cursos</title>
</head>
<body>
    <div class="contenido-header">
        <div id="logo">
            <img src="imagenes/_78881fc4-1efe-4915-bb51-8f76768ae06b.jpeg" alt="Logo">
        </div>
        <div id="icono-nav" class="menu-btn">
            <i class="fas fa-bars fa-2x"></i>
        </div>
        <nav id="nav" class="nav-main">
            <ul class="nav-menu">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="Sobre-nosotros.html">Sobre Nosotros</a></li>
                <li><a href="Servicio.html">Servicios</a></li>
                <li><a href="Cursos.html">Cursos</a></li>
                <li><a href="alojamiento.html">Alojamiento web</a></li>
                <li><a href="Contacto.html">Contacto</a></li>
            </ul>
            <div class="redes">
                <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            </div>
        </nav>
    </div>
    
    <div class="presentacion-container">
        <div class="presentacion">
            <h1 class="texto-redondeado">"Descubre Cómo Aumentar Tus Ingresos con Nuestros Cursos de Finanzas y Trading"</strong></h2>
            <p class="descripcion texto-redondeado">
                Bienvenido a "WebTech Financial Mastery", donde puedes explorar cursos diseñados para potenciar tus habilidades financieras y de trading. Nuestros programas están diseñados para proporcionarte las herramientas necesarias para gestionar tus finanzas personales de manera efectiva y explorar el mundo del trading con confianza y conocimiento.
            </p>
            <a href="https://www.facebook.com/profile.php?id=61558466327819" target="_blank">Síguenos en Facebook</a>
        </div>
    </div>

    <br>
    <br>

    <section id="cursos">
        <h3 class="titulo-seccion">Cursos de Educación Financiera</h3>
        <div class="fila">
            <div class="curso">
                <h4>Curso Básico de Fundamentos Financieros ($25)</h4>
                <p><strong>Contenido:</strong></p>
                <ul>
                    <li>Cómo manejar tu dinero.</li>
                    <li>Hacer un presupuesto.</li>
                    <li>Estrategias simples de ahorro.</li>
                    <li>Conceptos iniciales de inversión.</li>
                    <li>Herramientas básicas para analizar tus finanzas.</li>
                </ul>
                <p><strong>Beneficios:</strong></p>
                <ul>
                    <li>Introducción práctica a la gestión financiera.</li>
                    <li>Fundamentos para construir una base financiera sólida.</li>
                </ul>
                <p><strong>Desventajas:</strong></p>
                <ul>
                    <li>Limitado a conceptos básicos.</li>
                </ul>
                <p><strong>Ejemplo:</strong> Mejora de habilidades financieras personales.</p>
            </div>
            
            <div class="curso">
                <h4>Curso Intermedio de Planificación Financiera ($50)</h4>
                <p><strong>Contenido:</strong></p>
                <ul>
                    <li>Planificación financiera a medio y largo plazo.</li>
                    <li>Cómo manejar deudas y créditos.</li>
                    <li>Estrategias de inversión intermedias.</li>
                    <li>Optimización de tu presupuesto.</li>
                    <li>Herramientas avanzadas para analizar tus finanzas.</li>
                </ul>
                <p><strong>Beneficios:</strong></p>
                <ul>
                    <li>Profundización en la planificación financiera estratégica.</li>
                    <li>Herramientas avanzadas para análisis financiero.</li>
                </ul>
                <p><strong>Desventajas:</strong></p>
                <ul>
                    <li>Requiere un entendimiento previo de conceptos básicos.</li>
                </ul>
                <p><strong>Ejemplo:</strong> Planificación financiera efectiva para objetivos a largo plazo.</p>
            </div>
            
            <div class="curso">
                <h4>Curso Avanzado de Estrategias Financieras ($75)</h4>
                <p><strong>Contenido:</strong></p>
                <ul>
                    <li>Cómo optimizar tus inversiones.</li>
                    <li>Técnicas avanzadas de planificación financiera.</li>
                    <li>Gestión avanzada de riesgos financieros.</li>
                    <li>Estrategias de inversión diversificadas.</li>
                    <li>Análisis y previsión de tendencias financieras.</li>
                </ul>
                <p><strong>Beneficios:</strong></p>
                <ul>
                    <li>Estrategias avanzadas para maximizar rendimientos.</li>
                    <li>Preparación para enfrentar desafíos financieros complejos.</li>
                </ul>
                <p><strong>Desventajas:</strong></p>
                <ul>
                    <li>Requiere conocimientos previos en planificación financiera.</li>
                </ul>
                <p><strong>Ejemplo:</strong> Gestión financiera sofisticada para empresas en crecimiento.</p>
            </div>
        </div>
        
        <h3 class="titulo-seccion">Cursos de Trading en Binario</h3>
        <div class="fila">
            <div class="curso">
                <h4>Curso Básico de Introducción al Trading ($25)</h4>
                <p><strong>Contenido:</strong></p>
                <ul>
                    <li>Conceptos fundamentales de trading en binario.</li>
                    <li>Estrategias simples de trading.</li>
                    <li>Cómo usar plataformas de trading.</li>
                    <li>Análisis básico del mercado.</li>
                    <li>Gestión básica de riesgos.</li>
                </ul>
                <p><strong>Beneficios:</strong></p>
                <ul>
                    <li>Introducción práctica al trading en binario.</li>
                    <li>Herramientas básicas para iniciar en el trading.</li>
                </ul>
                <p><strong>Desventajas:</strong></p>
                <ul>
                    <li>Limitado a conceptos básicos de trading.</li>
                </ul>
                <p><strong>Ejemplo:</strong> Inicio en trading para aumentar ingresos adicionales.</p>
            </div>
            
            <div class="curso">
                <h4>Curso Intermedio de Análisis y Estrategias de Trading ($50)</h4>
                <p><strong>Contenido:</strong></p>
                <ul>
                    <li>Análisis técnico y fundamental.</li>
                    <li>Estrategias intermedias de trading en binario.</li>
                    <li>Gestión de riesgos en trading.</li>
                    <li>Optimización de estrategias de trading.</li>
                    <li>Herramientas avanzadas de análisis de mercado.</li>
                </ul>
                <p><strong>Beneficios:</strong></p>
                <ul>
                    <li>Profundización en técnicas de análisis y estrategias de trading.</li>
                    <li>Herramientas avanzadas para mejorar rendimientos en trading.</li>
                </ul>
                <p><strong>Desventajas:</strong></p>
                <ul>
                    <li>Requiere conocimientos previos en trading básico.</li>
                </ul>
                <p><strong>Ejemplo:</strong> Análisis avanzado para traders en busca de mayores rendimientos.</p>
            </div>
            
            <div class="curso">
                <h4>Curso Avanzado de Estrategias Avanzadas de Trading ($75)</h4>
                <p><strong>Contenido:</strong></p>
                <ul>
                    <li>Estrategias avanzadas de trading en binario.</li>
                    <li>Trading algorítmico.</li>
                    <li>Gestión avanzada de riesgos.</li>
                    <li>Análisis de tendencias y previsión de mercados.</li>
                    <li>Optimización y automatización de estrategias de trading.</li>
                </ul>
                <p><strong>Beneficios:</strong></p>
                <ul>
                    <li>Estrategias avanzadas para traders experimentados.</li>
                    <li>Preparación para enfrentar mercados financieros volátiles.</li>
                </ul>
                <p><strong>Desventajas:</strong></p>
                <ul>
                    <li>Requiere experiencia previa en trading intermedio.</li>
                </ul>
                <p><strong>Ejemplo:</strong> Estrategias avanzadas para maximizar rendimientos en mercados complejos.</p>
            </div>
        </div>
    </section>
    
    <section id="conclusion">
        <h3 class="titulo-seccion">Conclusión</h3>
        <p>En "WebTech Financial Mastery", nos comprometemos a proporcionarte conocimientos profundos y prácticos que no solo mejorarán tu comprensión financiera y habilidades de trading, sino que también te prepararán para alcanzar tus metas financieras con confianza. Aunque el camino pueda presentar desafíos, nuestros cursos están diseñados para equiparte con las herramientas necesarias para asegurar un futuro financiero más estable y cómodo.</p>
        <p><strong>¡Empieza hoy mismo tu viaje hacia el éxito financiero!</strong></p>
        <a href="#" class="boton-contacto">Contáctanos</a>
    </section>
    
</body>
</html>
// Función para manejar el menú responsivo
function toggleResponsiveMenu() {
    var nav = document.getElementById('nav');
    nav.classList.toggle('nav-main');
    nav.classList.toggle('responsive');
}

// Event listener para el icono de navegación responsivo
document.getElementById('icono-nav').addEventListener('click', function() {
    toggleResponsiveMenu();
});

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que se envíe el formulario de manera predeterminada

    // Validación de campos
    var nombre = document.getElementById('nombre').value.trim();
    var email = document.getElementById('email').value.trim();
    var mensaje = document.getElementById('mensaje').value.trim();

    if (nombre === '' || email === '' || mensaje === '') {
        alert('Por favor, completa todos los campos.');
        return;
    }

    // Envío del formulario usando Fetch API
    fetch('https://formspree.io/f/mwpekdpo', {
        method: 'POST',
        body: new FormData(document.getElementById('contactForm')),
        headers: {
            'Accept': 'application/json'
        }
    }).then(response => {
        if (response.ok) {
            alert('¡Formulario enviado con éxito!');
            document.getElementById('contactForm').reset(); // Reinicia el formulario después de enviarlo
        } else {
            alert('Hubo un problema al enviar el formulario. Por favor, intenta de nuevo.');
        }
    }).catch(error => {
        alert('Hubo un problema al enviar el formulario. Por favor, intenta de nuevo.');
    });
});

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gracias</title>
    <link rel="stylesheet" href="Contacto.css">
</head>
<body>
    <div class="container">
        <h1>¡Gracias por contactarnos!</h1>
        <p>Tu mensaje ha sido enviado con éxito. Nos pondremos en contacto contigo pronto.</p>
        <a href="index.html">Volver al inicio</a>
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <link rel="stylesheet" href="styles.css"/>
    <script src="script.js" defer></script>
    <title>WebTech Financial Mastery</title>
</head>
<body>
    <div class="contenido-header">
        <div id="logo">
            <img src="imagenes/_78881fc4-1efe-4915-bb51-8f76768ae06b.jpeg" alt="Logo">
        </div>
        <div id="icono-nav" class="menu-btn">
            <i class="fas fa-bars fa-2x"></i>
        </div>
        <nav id="nav" class="nav-main">
            <ul class="nav-menu">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="Sobre-nosotros.html">Sobre Nosotros</a></li>
                <li><a href="Servicio.html">Servicios</a></li>
                <li><a href="Cursos.html">Cursos</a></li>
                <li><a href="alojamiento.html">Alojamiento web</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
            <div class="redes">
                <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            </div>
        </nav>
    </div>
    
    <div class="presentacion-container">
        <div class="presentacion">
            <h1 class="texto-redondeado">Bienvenidos</h1>
            <br>
            <h2 class="texto-redondeado">Hola somos <strong class="texto-redondeado"> WebTech Financial Mastery</strong></h2>
            <h3 class="texto-redondeado">“Descubre el Poder de tus Finanzas y el Arte del Desarrollo Web”</h3>
            <p class="descripcion texto-redondeado">
                ¡Bienvenido a WebTech Financial Mastery! Aquí, fusionamos el conocimiento financiero con las habilidades técnicas para impulsar tu éxito. 🚀💡

¿Listo para aprender, crecer y dominar? Explora nuestros cursos, optimiza tu código y descubre oportunidades financieras. ¡Tu viaje comienza ahora!
            </p>
            <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank">Síguenos en Facebook</a>
        </div>
    </div>
</body>
</html>

// Función para manejar el menú responsivo
function toggleResponsiveMenu() {
    var nav = document.getElementById('nav');
    nav.classList.toggle('nav-main');
    nav.classList.toggle('responsive');
}

// Event listener para el icono de navegación responsivo
document.getElementById('icono-nav').addEventListener('click', function() {
    toggleResponsiveMenu();
});

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}

/* Estilos del cuerpo del documento */
body {
    font-family: 'Roboto', sans-serif;
    scroll-behavior: smooth;
    background-color: #d3d3d3;
    margin: 0px;
    padding: 0px;
}

.texto-redondeado {
    font-family: 'Roboto', sans-serif;
}

.contenido-header {
    background-color: rgba(0, 0, 0, 0.8);
    position: fixed;
    width: 100vw;
    z-index: 100;
    top: 0;
    left: 0px;
    margin: 0px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 20px 30px;
    flex-grow: 2;
}

#logo img {
    border-radius: 25%;
    width: 50px;
    height: 50px;
}

.nav-main {
    flex-grow: 1;
    display: flex;
    justify-content: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-menu li a:hover {
    color: #1ad5ee;
}

.redes {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* Alineación a la derecha */
  margin-right: 20px; /* Espacio a la derecha */
  flex-shrink: 0; /* Evita que las redes sociales se encogan */
}

.redes a {
  text-decoration: none;
  color: #fff;
  margin-left: 10px; /* Espacio entre íconos */
  transition: color 0.3s ease;
}

.redes a:hover {
  color: #12ddef;
}

.presentacion-container {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(imagenes/_22eedba3-5180-4087-a579-cda14da58dc2.jpeg) center center / cover;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-align: center;
    position: relative;
}

.presentacion {
    max-width: 1100px;
    margin: auto;
    color: #fff;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
}

.presentacion .bienvenida {
    font-size: 16px;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 5px;
}

.presentacion h2 {
    font-size: 20px;
    margin-bottom: 25px;
    text-align: left;
}

.presentacion h2 span {
    font-size: 25px;
    color: red;
}

.presentacion .descripcion {
    max-width: 100%;
    margin: 25px 50px;
    font-size: 18px;
    text-align: center;
}

.presentacion a {
    text-decoration: none;
    display: inline-block;
    margin: 25px 0;
    padding: 20px 25px;
    border: 2px solid #fff;
    border-radius: 50px;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: 0.5s;
}

.presentacion a:hover {
    background-color: aqua;
}

#icono-nav {
    color: #fff;
    display: none;
    cursor: pointer;
}

/*Servicios*/
#servicios {
    margin: 0;
    padding: 50px 0;
    text-align: center;
    
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('imagenes/_1333e096-ee69-4f8c-a9f9-dd98a9a1e705.jpeg'); /* Ruta de la imagen de fondo */
    background-size: cover; /* Ajusta la imagen para que cubra todo el fondo */
    background-position: center; /* Centra la imagen de fondo */
    background-repeat: no-repeat; /* Evita que la imagen se repita */
}

#servicios .titulo-seccion {
    margin-top: 20px;
    margin-bottom: 50px;
    font-size: 28px;
    text-transform: capitalize;
    color: #f7f7f7;
}

#servicios .fila {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
}

#servicios .servicio {
    width: 300px;
    background-color: #fff;
    padding: 20px;
    margin: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease;
}

#servicios .servicio:hover {
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}

#servicios .servicio h4 {
    font-size: 20px;
    margin-bottom: 15px;
}

#servicios .servicio hr {
    width: 50%;
    margin: auto;
    margin-bottom: 15px;
    border-color: #ddd;
}

#servicios .servicio p {
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 15px;
}

#servicios .servicio .caracteristicas {
    list-style-type: none;
    padding: 0;
    text-align: left;
}

#servicios .servicio .caracteristicas li {
    margin-bottom: 8px;
}

#servicios .servicio .caracteristicas li i {
    margin-right: 8px;
    color: #5cb85c; /* Verde para características disponibles */
}

#servicios .servicio .caracteristicas li .fa-xmark {
    color: #d9534f; /* Rojo para características no disponibles */
}

.btn-contacto {
    display: inline-block;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.btn-contacto:hover {
    background-color: #0056b3;
}

.btn-servicio {
    display: inline-block;
    padding: 10px 20px;
    margin-top: 20px;
    background-color: #111135;
    color: #fff;
    border-radius: 5px;
    text-decoration: none;
    transition: 0.3s;
}

.btn-servicio:hover {
    background-color: #333;
}


/*Conclusion*/
#conclusion {
    background-image: url('imagenes/_f27c292f-e342-4251-9b79-cc718d4384c9.jpeg');
    background-size: cover;
    background-position: center;
    padding: 50px 0;
    text-align: center;
}

#conclusion .container {
    max-width: 800px;
    margin: 0 auto;
}

#conclusion .contenido {
    background-color: rgba(255, 255, 255, 0.8); /* Fondo semitransparente blanco */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1); /* Sombra ligera */
}

#conclusion .titulo-seccion {
    font-size: 24px;
    color: #111135;
    text-transform: capitalize;
    margin-bottom: 20px;
}

#conclusion p {
    font-size: 16px;
    line-height: 1.6;
    color: #333;
}


/* Media queries para dispositivos móviles */
@media (max-width: 768px) {
  /* Estilos para el menú responsivo */
  #nav.responsive {
      display: block;
      background-color: rgba(0, 0, 0, 0.8);
      width: 100%; /* Ocupa todo el ancho disponible */
      height: calc(100vh - 60px); /* Calcula el alto del viewport menos la altura del header */
      position: absolute;
      top: 60px; /* Posiciona debajo del header */
      left: 0;
      padding: 10px 0;
      margin: 0;
  }

  #nav.responsive ul {
      display: block;
      text-align: center;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
  }

  #nav.responsive ul li {
      margin: 10px 0;
      text-align: left; /* Alinea los elementos del menú a la izquierda */
  }
}


  #nav.responsive ul {
      display: block !important;
      text-align: center;
  }

  #nav.responsive ul li {
      margin: 5px 0;
      text-align: left; /* Alinea los elementos del menú a la izquierda */
  }

  @media screen and (max-width: 800px) {
    nav.responsive ul {
        display: block !important;
        text-align: center;
    }

    nav.responsive ul li {
        margin-bottom: 10px; /* Ajusta el margen inferior entre elementos */
    }
}


/* Media queries para tabletas y dispositivos móviles */
@media (max-width: 768px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños pequeños */
    }

    .presentacion h2 {
        font-size: 18px; /* Ajusta el tamaño del título en tamaños pequeños */
    }

    .presentacion .descripcion {
        font-size: 16px; /* Ajusta el tamaño del texto de descripción en tamaños pequeños */
    }
}

/* Media queries para dispositivos móviles */
@media (max-width: 480px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños muy pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños muy pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños muy pequeños */
    }

    .presentacion h2 {
        font-size: 16px; /* Ajusta el tamaño del título en tamaños muy pequeños */
    }

    .presentacion .descripcion {
        font-size: 14px; /* Ajusta el tamaño del texto de descripción en tamaños muy pequeños */
    }
}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <link rel="stylesheet" href="servicio.css"/>
    <script src="servicio.js" defer></script>
    <title>Servicios</title>
</head>
<body>
    <div class="contenido-header">
        <div id="logo">
            <img src="imagenes/_78881fc4-1efe-4915-bb51-8f76768ae06b.jpeg" alt="Logo">
        </div>
        <div id="icono-nav" class="menu-btn">
            <i class="fas fa-bars fa-2x"></i>
        </div>
        <nav id="nav" class="nav-main">
            <ul class="nav-menu">
                <li><a href="Inicio.html">Inicio</a></li>
                <li><a href="Sobre-nosotros.html">Sobre Nosotros</a></li>
                <li><a href="Servicio.html">Servicios</a></li>
                <li><a href="Cursos.html">Cursos</a></li>
                <li><a href="alojamiento.html">Alojamiento web</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
            <div class="redes">
                <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            </div>
        </nav>
    </div>

    <div class="presentacion-container">
        <div class="presentacion">
            <h1 class="texto-redondeado">Nuestros Servicios</h1>
            <br>
            <p class="descripcion texto-redondeado">
                En "WebTech Financial Mastery", ofrecemos una gama de servicios diseñados para mejorar tu presencia en línea, promover tus servicios, tiendas y ideas mediante el desarrollo de sitios web efectivos y optimizados. Nuestros servicios están diseñados para adaptarse a tus necesidades específicas y ofrecerte soluciones que impulsen tu negocio hacia el éxito.
            </p>
            <a href="https://www.facebook.com/profile.php?id=61558466327819" target="_blank">Síguenos en Facebook</a>
        </div>
    </div>

    <br>
    <br>

    <!--Servicios-->
    <section id="servicios">
        <h3 class="titulo-seccion">Nuestros Servicios</h3>
        <div class="fila">
            <div class="servicio">
                <span class="icono"><i class="fa-solid fa-code"></i></span>
                <h4>Servicio Básico de Desarrollo Web Front-End ($50)</h4>
                <hr>
                <p>Diseñamos y desarrollamos sitios web estáticos básicos que son ideales para blogs personales, páginas de inicio simple o pequeñas presentaciones de servicios.</p>
                <ul class="caracteristicas">
                    <li><i class="fa-solid fa-check"></i> Uso de HTML y CSS</li>
                    <li><i class="fa-solid fa-check"></i> Diseño básico y adaptable a dispositivos móviles</li>
                    <li><i class="fa-solid fa-check"></i> Integración de secciones para contenido estático como texto, imágenes y enlaces</li>
                    <li><i class="fa-solid fa-check"></i> Funcionalidad básica de navegación y contacto</li>
                    <li><i class="fa-solid fa-xmark"></i> Integración de JavaScript para interactividad</li>
                    <li><i class="fa-solid fa-xmark"></i> Uso de frameworks como Bootstrap para diseño responsivo</li>
                    <li><i class="fa-solid fa-xmark"></i> Optimización básica para SEO</li>
                    <li><i class="fa-solid fa-xmark"></i> Formularios de contacto y suscripción</li>
                    <li><i class="fa-solid fa-xmark"></i> Diseño personalizado y branding</li>
                    <li><i class="fa-solid fa-xmark"></i> Integración con sistemas avanzados como React o Angular</li>
                    <li><i class="fa-solid fa-xmark"></i> Optimización avanzada para SEO y rendimiento</li>
                    <li><i class="fa-solid fa-xmark"></i> Funcionalidades específicas según las necesidades del cliente (por ejemplo, integración de sistemas de pago, gestión de usuarios, etc.)</li>
                </ul>
                <p><strong>Ejemplo:</strong> Creación de un blog de anime.</p>
                <p><strong>Tiempo Estimado de Entrega:</strong> 1-2 semanas.</p>
                <a href="Contacto.html" class="btn-contacto" target="_blank">Contactar</a>
            </div>
            <div class="servicio">
                <span class="icono"><i class="fa-solid fa-code"></i></span>
                <h4>Servicio Intermedio de Desarrollo Web Front-End ($100)</h4>
                <hr>
                <p>Desarrollamos sitios web dinámicos y más complejos adecuados para pequeñas empresas, artistas o proyectos más avanzados que requieren interactividad y funcionalidades adicionales.</p>
                <ul class="caracteristicas">
                    <li><i class="fa-solid fa-check"></i> Uso de HTML y CSS</li>
                    <li><i class="fa-solid fa-check"></i> Diseño básico y adaptable a dispositivos móviles</li>
                    <li><i class="fa-solid fa-check"></i> Integración de secciones para contenido estático como texto, imágenes y enlaces</li>
                    <li><i class="fa-solid fa-check"></i> Funcionalidad básica de navegación y contacto</li>
                    <li><i class="fa-solid fa-check"></i> Integración de JavaScript para interactividad</li>
                    <li><i class="fa-solid fa-check"></i> Uso de frameworks como Bootstrap para diseño responsivo</li>
                    <li><i class="fa-solid fa-check"></i> Optimización básica para SEO</li>
                    <li><i class="fa-solid fa-check"></i> Formularios de contacto y suscripción</li>
                    <li><i class="fa-solid fa-xmark"></i> Diseño personalizado y branding</li>
                    <li><i class="fa-solid fa-xmark"></i> Integración con sistemas avanzados como React o Angular</li>
                    <li><i class="fa-solid fa-xmark"></i> Optimización avanzada para SEO y rendimiento</li>
                    <li><i class="fa-solid fa-xmark"></i> Funcionalidades específicas según las necesidades del cliente (por ejemplo, integración de sistemas de pago, gestión de usuarios, etc.)</li>
                </ul>
                <p><strong>Ejemplo:</strong> Desarrollo de un sitio web para un juego.</p>
                <p><strong>Tiempo Estimado de Entrega:</strong> 2-3 semanas.</p>
                <a href="Contacto.html" class="btn-contacto" target="_blank">Contactar</a>
            </div>
            <div class="servicio">
                <span class="icono"><i class="fa-solid fa-code"></i></span>
                <h4>Servicio Avanzado/Personalizado de Desarrollo Web Front-End ($120 o más)</h4>
                <hr>
                <p>Ofrecemos soluciones personalizadas y avanzadas para negocios que necesitan sitios web sofisticados y altamente funcionales, como plataformas de comercio electrónico, sistemas de gestión de contenidos complejos o aplicaciones web personalizadas.</p>
                <ul class="caracteristicas">
                    <li><i class="fa-solid fa-check"></i> Uso de HTML y CSS</li>
                    <li><i class="fa-solid fa-check"></i> Diseño básico y adaptable a dispositivos móviles</li>
                    <li><i class="fa-solid fa-check"></i> Integración de secciones para contenido estático como texto, imágenes y enlaces</li>
                    <li><i class="fa-solid fa-check"></i> Funcionalidad básica de navegación y contacto</li>
                    <li><i class="fa-solid fa-check"></i> Integración de JavaScript para interactividad</li>
                    <li><i class="fa-solid fa-check"></i> Uso de frameworks como Bootstrap para diseño responsivo</li>
                    <li><i class="fa-solid fa-check"></i> Optimización básica para SEO</li>
                    <li><i class="fa-solid fa-check"></i> Formularios de contacto y suscripción</li>
                    <li><i class="fa-solid fa-check"></i> Diseño personalizado y branding</li>
                    <li><i class="fa-solid fa-check"></i> Integración con sistemas avanzados como React o Angular</li>
                    <li><i class="fa-solid fa-check"></i> Optimización avanzada para SEO y rendimiento</li>
                    <li><i class="fa-solid fa-check"></i> Funcionalidades específicas según las necesidades del cliente (por ejemplo, integración de sistemas de pago, gestión de usuarios, etc.)</li>
                </ul>
                <p><strong>Ejemplo:</strong> Creación de una plataforma de cursos en línea.</p>
                <p><strong>Tiempo Estimado de Entrega:</strong> 4-6 semanas, dependiendo de la complejidad del proyecto.</p>
                <a href="Contacto.html" class="btn-contacto" target="_blank">Contactar</a>
            </div>

            <!-- Alojamiento de Sitios Web -->
        <div class="servicio">
            <span class="icono"><i class="fa-solid fa-server"></i></span>
            <h4>Alojamiento de Sitios Web con Hosting y Dominio</h4>
            <hr>
            <p>Ofrecemos servicios completos de alojamiento web para que tu sitio esté siempre accesible y seguro. Según el plan que elijas, incluimos:</p>
            <ul class="caracteristicas">
                <li><i class="fa-solid fa-check"></i> Plan Básico de Alojamiento: Hosting confiable, Dominio incluido, Soporte técnico básico</li>
                <li><i class="fa-solid fa-check"></i> Plan Intermedio de Alojamiento: Hosting avanzado, Dominio incluido, Certificado SSL, Soporte técnico prioritario</li>
                <li><i class="fa-solid fa-check"></i> Plan Avanzado de Alojamiento: Hosting premium, Dominio incluido, Certificado SSL, Soporte técnico 24/7, Backups automáticos</li>
            </ul>
            <a href="alojamiento.html" class="btn-servicio">Ver Detalles</a>
        </div>

        </div>
    </section>

    <br>
    <br>

<!--Conclusion-->
<section id="conclusion">
    <div class="container">
        <div class="contenido">
            <h3 class="titulo-seccion">Conclusión</h3>
            <p>En "WebTech Financial Mastery", nos comprometemos a proporcionar soluciones de desarrollo web que no solo cumplan con tus expectativas, sino que también impulsen tu presencia en línea y apoyen el crecimiento de tu negocio. Cada nivel de servicio está diseñado para ofrecer valor agregado y resultados tangibles que te ayuden a alcanzar tus objetivos empresariales.</p>
        </div>
    </div>
</section>


</body>
</html>
// Función para manejar el menú responsivo
function toggleResponsiveMenu() {
    var nav = document.getElementById('nav');
    nav.classList.toggle('nav-main');
    nav.classList.toggle('responsive');
}

// Event listener para el icono de navegación responsivo
document.getElementById('icono-nav').addEventListener('click', function() {
    toggleResponsiveMenu();
});

// Función para manejar el menú responsivo
function toggleResponsiveMenu() {
    var nav = document.getElementById('nav');
    nav.classList.toggle('nav-main');
    nav.classList.toggle('responsive');
}

// Event listener para el icono de navegación responsivo
document.getElementById('icono-nav').addEventListener('click', function() {
    toggleResponsiveMenu();
});

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Estilos del cuerpo del documento */
body {
    font-family: 'Roboto', sans-serif;
    scroll-behavior: smooth;
    background-color: #d3d3d3;
}

.texto-redondeado {
    font-family: 'Roboto', sans-serif;
}

.contenido-header {
    background-color: rgba(0, 0, 0, 0.8);
    position: fixed;
    width: 100%;
    z-index: 100;
    top: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 20px 30px;
}

#logo img {
    border-radius: 25%;
    width: 50px;
    height: 50px;
}

.nav-main {
    flex-grow: 1;
    display: flex;
    justify-content: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-menu li a:hover {
    color: #1ad5ee;
}

.redes {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-right: 20px;
    flex-shrink: 0;
}

.redes a {
    text-decoration: none;
    color: #fff;
    margin-left: 10px;
    transition: color 0.3s ease;
}

.redes a:hover {
    color: #12ddef;
}

.presentacion-container {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(imagenes/_b65a0d98-0b11-42cc-ab41-256336c73072.jpeg) center center / cover;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-align: center;
    position: relative;
    overflow: hidden; /* Evita que el contenido se extienda más allá del contenedor */
}

.presentacion {
    max-width: 800px; /* Reducir el ancho máximo para centrar el contenido */
    margin: auto;
    color: #fff;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
    position: relative; /* Añadir posición relativa para z-index funcione correctamente */
}

.presentacion .bienvenida {
    font-size: 16px;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 5px;
}

.presentacion h2 {
    font-size: 36px; /* Aumentar tamaño de fuente para mayor legibilidad */
    margin-bottom: 25px;
}

.presentacion h2 span {
    font-size: 40px; /* Aumentar tamaño de fuente para mayor contraste */
    color: red;
}

.presentacion .descripcion {
    max-width: 100%;
    margin: 25px 50px;
    font-size: 18px;
}

.presentacion a {
    text-decoration: none;
    display: inline-block;
    margin: 25px 0;
    padding: 20px 25px;
    border: 2px solid #fff;
    border-radius: 50px;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: 0.5s;
}

.presentacion a:hover {
    background-color: aqua;
}

#icono-nav {
    color: #fff;
    display: none;
    cursor: pointer;
}



/* Seccion de preguntas frecuentes */
/* Sección de preguntas frecuentes */
#FAQ {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 30px auto;
    width: 100%; /* Ajuste para ocupar todo el ancho */
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('imagenes/_2b05413c-c5e1-430c-b77f-b1ae0db0a715.jpeg') center center / cover no-repeat;
    color: #fff; /* Texto en blanco para mejor visibilidad */
    padding: 50px; /* Espacio adicional para contenido */
}

#FAQ .titulo-seccion {
    font-size: 24px;
    text-align: center;
    margin-bottom: 25px;
    color: #fff; /* Texto en blanco para mejor visibilidad */
}

.fila {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    margin: 20px 0;
}

.servicio {
    max-width: 350px;
    background-color: rgba(255, 255, 255, 0.8); /* Fondo blanco semitransparente */
    padding: 30px;
    margin: 10px;
    border-radius: 5px;
    transition: 0.5s;
}

.servicio:hover {
    box-shadow: 5px 5px 10px #201f1f, -5px -5px 10px #8a8a8a;
}

.servicio h4 {
    font-size: 22px;
    text-align: center;
    margin-bottom: 15px;
    color: #000; /* Texto en negro */
}

.servicio p {
    font-size: 14px;
    line-height: 22px;
    color: #000; /* Texto en negro */
}

.servicio hr {
    margin: 20px 0;
    border: none;
    border-top: 1px solid #ccc;
}

/* Estilo para la sección "Nuestra Filosofía y Compromiso" */
#Nuestra-Filosofía-y-Compromiso {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 30px auto;
    width: 100%; /* Ajuste para ocupar todo el ancho */
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('imagenes/descargar.jpeg') center center / cover no-repeat;
    color: #fff; /* Texto en blanco para mejor visibilidad */
    padding: 50px; /* Espacio adicional para contenido */
}

.Titulo-f{
    font-size: 22px;
    margin-bottom: 15px;
    text-align: center; /* Alineación centrada */
    color: #000; /* Texto en negro */
}

.seccion-pares {
    display: flex;
    justify-content: space-evenly;
    margin: 20px auto; /* Ajuste el margen según su preferencia */
    max-width: 1100px;
}

.section {
    max-width: 350px;
    background-color: rgba(255, 255, 255, 0.8); /* Fondo blanco semitransparente */
    padding: 30px;
    margin: 0 10px;
    border-radius: 5px;
    transition: 0.5s;
}

.section:hover {
    box-shadow: 5px 5px 10px #201f1f, -5px -5px 10px #8a8a8a;
}

.section h3 {
    font-size: 22px;
    margin-bottom: 15px;
    text-align: center; /* Alineación centrada */
    color: #000; /* Texto en negro */
}

.section p {
    font-size: 14px;
    line-height: 22px;
    color: #000; /* Texto en negro */
}

.section ul {
    list-style: none;
    margin-bottom: 10px;
}

.section li {
    margin-bottom: 10px;
}

.section hr {
    margin: 20px 0;
    border: none;
    border-top: 1px solid #ccc;
}


/* Media queries para dispositivos móviles */
@media (max-width: 768px) {
    /* Estilos para el menú responsivo */
#nav.responsive {
    display: block;
    background-color: rgba(0, 0, 0, 0.8);
    width: 100%; /* Ocupa todo el ancho disponible */
    height: calc(100vh - 60px); /* Calcula el alto del viewport menos la altura del header */
    position: absolute;
    top: 60px; /* Posiciona debajo del header */
    left: 0;
    padding: 10px 0;
    margin: 0;
}

#nav.responsive ul {
    display: block;
    text-align: center;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

    #nav.responsive ul li {
        margin: 10px 0;
        text-align: left; /* Alinea los elementos del menú a la izquierda */
    }
}

#nav.responsive ul {
    display: block !important;
    text-align: center;
}

#nav.responsive ul li {
    margin: 5px 0;
    text-align: left; /* Alinea los elementos del menú a la izquierda */
} 

@media screen and (max-width: 800px) {
nav.responsive ul {
    display: block !important;
    text-align: center;
    }
    
nav.responsive ul li {
margin-bottom: 10px; /* Ajusta el margen inferior entre elementos */
}
}

/* Media queries para tabletas y dispositivos móviles */
@media (max-width: 768px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños pequeños */
    }

    .presentacion h2 {
        font-size: 18px; /* Ajusta el tamaño del título en tamaños pequeños */
    }

    .presentacion .descripcion {
        font-size: 16px; /* Ajusta el tamaño del texto de descripción en tamaños pequeños */
    }
}

/* Media queries para dispositivos móviles */
@media (max-width: 480px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños muy pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños muy pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños muy pequeños */
    }

    .presentacion h2 {
        font-size: 16px; /* Ajusta el tamaño del título en tamaños muy pequeños */
    }

    .presentacion .descripcion {
        font-size: 14px; /* Ajusta el tamaño del texto de descripción en tamaños muy pequeños */
    }
}

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <link rel="stylesheet" href="Sobre-nosotros.css"/>
    <title>Sobre Nosotros</title>
</head>
<body>
    <div class="contenido-header">
        <div id="logo">
            <img src="imagenes/_78881fc4-1efe-4915-bb51-8f76768ae06b.jpeg" alt="Logo">
        </div>
        <div id="icono-nav" class="menu-btn">
            <i class="fas fa-bars fa-2x"></i>
        </div>
        <nav id="nav" class="nav-main">
            <ul class="nav-menu">
                <li><a href="Inicio.html">Inicio</a></li>
                <li><a href="Sobre-nosotros.html">Sobre Nosotros</a></li>
                <li><a href="Servicio.html">Servicios</a></li>
                <li><a href="Cursos.html">Cursos</a></li>
                <li><a href="alojamiento.html">Alojamiento web</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
            <div class="redes">
                <a href="https://www.facebook.com/profile.php?id=61558466327819&sk=about" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            </div>
        </nav>
    </div>

    <br>

    <!-- Sección de Sobre Nosotros -->
<section class="presentacion-container" id="SobreNosotros">
    <div class="presentacion">
        <h3 class="bienvenida">Bienvenido a</h3>
        <h2>WebTech Financial Mastery</h2>
        <br>
        <div class="descripcion">
            <h3>Hola, somos <span>WebTech Financial Mastery</span></h3>
            <p>Desde que tengo memoria, siempre he sido apasionado por la tecnología y las finanzas. A mis 19 años, me di cuenta de la importancia de una buena educación financiera, pero también noté que muchas personas no tenían acceso a recursos accesibles y de calidad en esta área. Un día, durante una conversación con un amigo, surgió la idea de crear un negocio que abordara esta necesidad insatisfecha.</p>
            <br>
            <p>Inspirado por esta conversación y motivado por el deseo de hacer una diferencia, decidí fundar WebTech Financial Mastery. La misión es clara: ofrecer educación financiera y servicios de trading de alta calidad a precios accesibles, utilizando la última tecnología para mejorar la experiencia de aprendizaje y hacerla más efectiva. Además, busco ayudar a las personas a mejorar la presencia de sus negocios o servicios en internet, tal como lo estoy haciendo con el mío. Estoy decidido a expandir mi alcance y ayudar a más personas a alcanzar sus metas financieras y comerciales.</p>
        </div>
    </div>
</section>


<!-- Sección de Preguntas Frecuentes -->
<section id="FAQ">
    <h3 class="titulo-seccion">Preguntas Frecuentes</h3>

    <div class="fila">
        <div class="servicio">
            <h4>¿Qué inspiró a Malik Chavez a fundar WebTech Financial Mastery?</h4>
            <hr>
            <p>La idea de WebTech Financial Mastery nació de una conversación reveladora con un amigo sobre la falta de opciones accesibles y de calidad en la educación financiera. Motivado por el deseo de cambiar esto, Malik decidió crear un negocio que ofreciera servicios financieros y de trading a precios razonables, utilizando la tecnología para mejorar la experiencia de aprendizaje.</p>
        </div>

        <div class="servicio">
            <h4>¿Qué distingue a WebTech Financial Mastery de otros negocios similares?</h4>
            <hr>
            <p>Lo que nos distingue es nuestra combinación única de educación financiera personalizada, tecnología avanzada y precios competitivos. Nos enfocamos en hacer que el conocimiento financiero sea accesible para todos, ofreciendo cursos y servicios que se adaptan a las necesidades individuales de nuestros clientes.</p>
        </div>
    </div>

    <div class="fila">
        <div class="servicio">
            <h4>¿Cuál es la visión a largo plazo de WebTech Financial Mastery?</h4>
            <hr>
            <p>Nuestra visión a largo plazo es convertirnos en un referente en educación financiera y servicios de trading, expandiendo nuestra oferta para llegar a una audiencia global. Queremos seguir innovando y adaptándonos a las tendencias emergentes en tecnología financiera para proporcionar el mejor servicio posible a nuestros clientes.</p>
        </div>

        <div class="servicio">
            <h4>¿Cómo ha sido la experiencia de los primeros clientes de WebTech Financial Mastery?</h4>
            <hr>
            <p>Aunque estamos en las etapas iniciales, nuestros primeros clientes han reportado mejoras significativas en su comprensión y manejo de sus finanzas. La retroalimentación ha sido muy positiva, y estamos comprometidos a seguir brindando servicios que realmente hagan una diferencia en la vida financiera de las personas.</p>
        </div>
    </div>

    <div class="fila">
        <div class="servicio">
            <h4>¿Qué impacto espera tener WebTech Financial Mastery en la comunidad?</h4>
            <hr>
            <p>Esperamos empoderar a las personas con el conocimiento y las herramientas necesarias para tomar decisiones financieras informadas. Al hacerlo, no solo mejoramos la situación financiera individual de nuestros clientes, sino que también contribuimos al bienestar económico general de la comunidad.</p>
        </div>
    </div>
</section>


    <!-- Sección de Nuestra Filosofía y Compromiso -->
<section id="Nuestra Filosofía y Compromiso">
    <h2 class="Titulo-f">Nuestra Filosofía y Compromiso</h2>
    <div class="seccion-pares">
        <!-- Sección de Misión -->
        <div id="mision" class="section">
            <h3>Misión</h3>
            <p>En WebTech Financial Mastery, nuestra misión es ayudar a nuestros clientes a alcanzar sus objetivos financieros, proporcionando soluciones educativas innovadoras y servicios personalizados que impulsen su éxito.</p>
        </div>

        <!-- Sección de Visión -->
        <div id="vision" class="section">
            <h3>Visión</h3>
            <p>Nos esforzamos por ser líderes en la industria de la educación financiera y el trading, ofreciendo constantemente servicios de vanguardia y manteniéndonos a la vanguardia de las últimas tendencias y avances en tecnología financiera.</p>
        </div>
    </div>
    <br>

    <div class="seccion-pares">
        <!-- Sección de Valores -->
        <div id="valores" class="section">
            <h3>Valores</h3>
            <ul>
                <li>Pasión por la Tecnología: Estamos apasionados por la tecnología y creemos en su poder para transformar vidas y negocios.</li>
                <li>Dedicación a la Mejora Continua: Nos comprometemos a aprender y crecer constantemente para mejorar nuestros servicios y ofrecer nuevas soluciones innovadoras a nuestros clientes.</li>
                <li>Creatividad y Proactividad: Más allá de simplemente cumplir con las expectativas del cliente, nos esforzamos por ofrecer recomendaciones creativas y proactivas para mejorar sus proyectos tecnológicos y maximizar su potencial.</li>
            </ul>
        </div>

        <!-- Sección de Enfoque de Servicio -->
        <div id="enfoque-servicio" class="section">
            <h3>Enfoque de Servicio</h3>
            <ul>
                <li>Asesoramiento Personalizado: Ofrecemos asesoramiento personalizado para cada cliente, recomendando soluciones tecnológicas que se adapten a sus necesidades específicas y objetivos.</li>
                <li>Soporte Continuo: Nos comprometemos a brindar soporte técnico continuo a nuestros clientes, garantizando que sus sistemas tecnológicos funcionen de manera óptima en todo momento.</li>
                <li>Comunicación Transparente: Mantenemos una comunicación abierta y transparente con nuestros clientes en todo momento, manteniéndolos informados sobre el progreso de sus proyectos y disponibles para responder a cualquier pregunta o inquietud que puedan tener.</li>
            </ul>
        </div>
    </div>
    <br>

    <div class="seccion-pares">
        <!-- Sección de Compromiso con la Calidad -->
        <div id="compromiso-calidad" class="section">
            <h3>Compromiso con la Calidad</h3>
            <ul>
                <li>Excelencia en el Servicio: Nos esforzamos por superar las expectativas de nuestros clientes en términos de calidad y profesionalismo en cada interacción.</li>
                <li>Garantía de Satisfacción: Garantizamos la satisfacción del cliente, trabajando incansablemente para resolver cualquier problema o inquietud que puedan surgir y asegurando que estén completamente satisfechos con nuestros servicios.</li>
            </ul>
        </div>

        <!-- Sección de Futuro -->
        <div id="futuro" class="section">
            <h3>Futuro</h3>
            <p>A medida que crecemos y adquirimos nuevos conocimientos y habilidades, estamos comprometidos a expandir nuestros servicios y ofrecer soluciones aún más innovadoras en áreas adicionales de la tecnología.</p>
        </div>
    </div>
    <br>
</section>

    <!-- Scripts -->
    <script src="Sobre.js"></script>
</body>
</html>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}

/* Estilos del cuerpo del documento */
body {
    font-family: 'Roboto', sans-serif;
    scroll-behavior: smooth;
    background-color: #d3d3d3;
    margin: 0px;
    padding: 0px;
}

.texto-redondeado {
    font-family: 'Roboto', sans-serif;
}

.contenido-header {
    background-color: rgba(0, 0, 0, 0.8);
    position: fixed;
    width: 100vw;
    z-index: 100;
    top: 0;
    left: 0px;
    margin: 0px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 20px 30px;
    flex-grow: 2;
}

#logo img {
    border-radius: 25%;
    width: 50px;
    height: 50px;
}

.nav-main {
    flex-grow: 1;
    display: flex;
    justify-content: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-menu li a:hover {
    color: #1ad5ee;
}

.redes {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* Alineación a la derecha */
  margin-right: 20px; /* Espacio a la derecha */
  flex-shrink: 0; /* Evita que las redes sociales se encogan */
}

.redes a {
  text-decoration: none;
  color: #fff;
  margin-left: 10px; /* Espacio entre íconos */
  transition: color 0.3s ease;
}

.redes a:hover {
  color: #12ddef;
}

.presentacion-container {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(imagenes/_22eedba3-5180-4087-a579-cda14da58dc2.jpeg) center center / cover;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-align: center;
    position: relative;
}

.presentacion {
    max-width: 1100px;
    margin: auto;
    color: #fff;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
}

.presentacion .bienvenida {
    font-size: 16px;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 5px;
}

.presentacion h2 {
    font-size: 20px;
    margin-bottom: 25px;
    text-align: left;
}

.presentacion h2 span {
    font-size: 25px;
    color: red;
}

.presentacion .descripcion {
    max-width: 100%;
    margin: 25px 50px;
    font-size: 18px;
    text-align: center;
}

.presentacion a {
    text-decoration: none;
    display: inline-block;
    margin: 25px 0;
    padding: 20px 25px;
    border: 2px solid #fff;
    border-radius: 50px;
    color: #fff;
    font-weight: bold;
    text-transform: uppercase;
    transition: 0.5s;
}

.presentacion a:hover {
    background-color: aqua;
}

#icono-nav {
    color: #fff;
    display: none;
    cursor: pointer;
}

/* Media queries para dispositivos móviles */
@media (max-width: 768px) {
  /* Estilos para el menú responsivo */
  #nav.responsive {
      display: block;
      background-color: rgba(0, 0, 0, 0.8);
      width: 100%; /* Ocupa todo el ancho disponible */
      height: calc(100vh - 60px); /* Calcula el alto del viewport menos la altura del header */
      position: absolute;
      top: 60px; /* Posiciona debajo del header */
      left: 0;
      padding: 10px 0;
      margin: 0;
  }

  #nav.responsive ul {
      display: block;
      text-align: center;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
  }

  #nav.responsive ul li {
      margin: 10px 0;
      text-align: left; /* Alinea los elementos del menú a la izquierda */
  }
}


  #nav.responsive ul {
      display: block !important;
      text-align: center;
  }

  #nav.responsive ul li {
      margin: 5px 0;
      text-align: left; /* Alinea los elementos del menú a la izquierda */
  }

  @media screen and (max-width: 800px) {
    nav.responsive ul {
        display: block !important;
        text-align: center;
    }

    nav.responsive ul li {
        margin-bottom: 10px; /* Ajusta el margen inferior entre elementos */
    }
}


/* Media queries para tabletas y dispositivos móviles */
@media (max-width: 768px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños pequeños */
    }

    .presentacion h2 {
        font-size: 18px; /* Ajusta el tamaño del título en tamaños pequeños */
    }

    .presentacion .descripcion {
        font-size: 16px; /* Ajusta el tamaño del texto de descripción en tamaños pequeños */
    }
}

/* Media queries para dispositivos móviles */
@media (max-width: 480px) {
    .nav-main {
        display: none; /* Oculta la barra de navegación en tamaños muy pequeños */
    }

    #icono-nav {
        display: block; /* Muestra el icono de navegación en tamaños muy pequeños */
    }

    .redes {
        display: none; /* Oculta las redes sociales en tamaños muy pequeños */
    }

    .presentacion h2 {
        font-size: 16px; /* Ajusta el tamaño del título en tamaños muy pequeños */
    }

    .presentacion .descripcion {
        font-size: 14px; /* Ajusta el tamaño del texto de descripción en tamaños muy pequeños */
    }
}agenes…]()
