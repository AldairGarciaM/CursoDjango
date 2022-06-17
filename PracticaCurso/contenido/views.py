from django.shortcuts import render, HttpResponse

# Create your views here.

menu="""
    <a href="/">Home</a>
    <a href="/cursos">Cursos</a>
    <a href="/contacto">Contacto</a>
"""    


def principal(request):
    contenido="""<h1> Bienvenido a nuestro proyecto !!!</h1> 
    <h3> Este curso servira para la creacion de un proyecto de Django con el fin de conocer mejor esta tecnolo"""
    return HttpResponse(menu + contenido)

def cursos(request):
    contenido="""<h1> Nuestros cursos disponibles!!!! </h1>
    <ol>
        <li> Base de datos </li>
        <li> Programacion </li>
        <li> Redes </li>
        <li> Animacion digital </li>
        <li> Seguridad web </li>
        <li> Hacking Etico </li>
    </ol>
    """
    return HttpResponse(menu+contenido)    

def contacto(request):
    contenido="""<h1> Contactanos!!! </h1>
    <p>Nombre: <input type="text" name="nombre"> </p>
    <p>Correo Electronico: <input type="text" name="correo"> </p>
    <p>Elige un Curso: 
        <select name="curso">
            <option> Base de datos </option>
            <option> Programacion </option>
            <option> Animacion digital </option>
            <option> Seguridad web </option>
            <option> Hacking Etico </option>
        </select>
    </p><br>

    <p> Comentarios: </p> <p> <textarea cols="50" rows="10"></textarea> </p>
    <p> <input type="Button" name="enviar" value="Enviar" /> </p>"""

    return HttpResponse(menu+contenido)