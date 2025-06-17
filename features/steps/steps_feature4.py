from behave import *

# GIVEN

@given('que el usuario "{usuario}" ha iniciado sesión correctamente')
def step_impl(context, usuario):
    context.usuario = {"nombre": usuario, "correo": "", "clave": "1234"}

@given('que el usuario "{usuario}" tiene registrada la contraseña "{clave}"')
def step_impl(context, usuario, clave):
    context.usuario = {"nombre": usuario, "correo": "", "clave": clave}

# WHEN

@when('actualiza su nombre a "{nuevo_nombre}" y su correo a "{nuevo_correo}"')
def step_impl(context, nuevo_nombre, nuevo_correo):
    if "@" in nuevo_correo:
        context.usuario["nombre"] = nuevo_nombre
        context.usuario["correo"] = nuevo_correo
        context.update_successful = True
    else:
        context.update_successful = False

@when('cambia su contraseña a "{nueva_clave}"')
def step_impl(context, nueva_clave):
    context.usuario["clave"] = nueva_clave

@when('intenta cambiar su contraseña ingresando "{clave_ingresada}" como clave actual')
def step_impl(context, clave_ingresada):
    context.cambio_valido = (clave_ingresada == context.usuario["clave"])

@when('intenta actualizar su correo a "{correo}"')
def step_impl(context, correo):
    context.correo_valido = "@" in correo

# THEN

@then('los datos actualizados deben mostrarse correctamente en su perfil')
def step_impl(context):
    assert context.update_successful is True, "La actualización de datos falló"

@then('la contraseña del usuario debe ser actualizada a "{esperada_clave}"')
def step_impl(context, esperada_clave):
    assert context.usuario["clave"] == esperada_clave, "La contraseña no fue actualizada correctamente"

@then('el sistema debe mostrar un mensaje de error indicando que la clave actual es incorrecta')
def step_impl(context):
    assert context.cambio_valido is False, "La clave incorrecta fue aceptada erróneamente"

@then('el sistema debe mostrar un mensaje de error indicando que el correo ingresado no es válido')
def step_impl(context):
    assert context.correo_valido is False, "Se aceptó un correo con formato inválido"
