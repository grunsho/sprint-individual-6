# sprint-individual-6

Como finalización de este módulo se introdujeron pequeños cambios al trabajo realizado:

- Se crea la aplicación *authentication*, separando así la lógica del login de la del resto del sitio.
- Además, se agregó la opción en el mismo login de que el visitante cree una nueva cuenta. Esta cuenta está limitada al grupo "Usuarios", de acuerdo a lo concluído en el ejercicio anterior.
- Se movió la carpeta statics/ a la raíz del proyecto, con el fin de ser utilizada por todas las aplicaciones. Se hicieron los respectivos cambios en setting.py para cumplir con esto.
- La lógica de permisos de usuarios se mantiene. Un nuevo usuario pertenece al grupo *Usuarios*, y sólo un *Moderador* puede crear nuevos usuarios dentro del sistema, además de ver su información (excepto contraseña).
- El usuario del grupo *Usuario* por el momento sólo puede ver la página de inicio. La idea es crear una página de perfil en donde pueda agregar mayor información.
- Por razones de seguridad, **el nuevo usuario no puede elegir el grupo al que pertenecerá**, ya que de elegir el grupo *Moderadores* puede modificar la información de todos los usuarios del sistema.

# Credenciales de acceso
Si bien se puede crear un nuevo usuario para entrar al sitio privado, no será posible hacerlo desde el perfil de un moderador, por lo que se incluyen las siguientes cuentas para acceso:

**- Moderador**
Nombre de usuario: moderador1 | Contraseña: moderapass
Nombre de usuario: moderador2 | Contraseña: passmodera

**- Usuario**
Nombre de usuario: otrousuario | Contraseña: otropass
Nombre de usuario: Chimichanga | Contraseña: passwordchanga