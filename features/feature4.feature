Feature: Feature 4 - Edición del perfil de usuario
  Esta funcionalidad permite a los usuarios modificar sus datos personales,
  como nombre, correo electrónico y contraseña, asegurando validaciones básicas
  para mantener la integridad y seguridad de la información.

  Scenario: Actualización exitosa del nombre y correo electrónico
    Given que el usuario "cristobal" ha iniciado sesión correctamente
    When actualiza su nombre a "Cristóbal Muñoz" y su correo a "cristobal@ejemplo.com"
    Then los datos actualizados deben mostrarse correctamente en su perfil

  Scenario: Cambio exitoso de contraseña
    Given que el usuario "cristobal" tiene registrada la contraseña "1234"
    When cambia su contraseña a "nueva1234"
    Then la contraseña del usuario debe ser actualizada a "nueva1234"

  Scenario: Fallo al intentar cambiar la contraseña con clave actual incorrecta
    Given que el usuario "cristobal" tiene registrada la contraseña "1234"
    When intenta cambiar su contraseña ingresando "0000" como clave actual
    Then el sistema debe mostrar un mensaje de error indicando que la clave actual es incorrecta

  Scenario: Fallo al intentar actualizar el correo con formato inválido
    Given que el usuario "cristobal" ha iniciado sesión correctamente
    When intenta actualizar su correo a "correo-sin-arroba"
    Then el sistema debe mostrar un mensaje de error indicando que el correo ingresado no es válido
