# Combis-Escolares en la zona de Canning-Ezeiza

Comisión: 54140

Alumno: Ezequiel Souza Arraigada

## Explicación breve del proyecto en cuanto al servicio
-Este proyecto busca crear una pagina en donde puedas ver, modificar, eliminar o incluso crear una asignación de combis escolares en donde se muestre el nombre de las mismas, es decir a que zona pertenece (zona a, zona b, etc.). También se muestra a que colegio pertenece esa combi, que cantidad de pasajeros lleva y el nombre del conductor de la combi. Podes administrar las distintas combis que se encuentran en los diferentes colegios y agregar o borrar una combi que pertenezca a determinada zona y a determinado colegio.

## Explicación breve técnica: urls, modelos, plantillas
-urls: En las "urls" lo que hice fue definir primero el nombre de mi aplicación, que es 'Vehiculo', y despues use las importaciones de django.urls para importar el path, y también la importación de Vehiculo.views en donde lo que importe fueron todas las funciones que se encuetran en el archivo de "models" para que me funcione a la hora de correr el programa. Y por ultimo, use la variable 'urlpatterns' en modo de lista donde utilice la variable de entorno PATH que habia importado para ubicar mis archivos ejecutables en el sistema de archivos. Ubique el nombre de la función que había importado y le dí un nombre en el cuál mantuve el mismo que la función.

-modelos: primero importe los modelos con el comando "import models", en donde definí 4 clases principales, Combi, Pasajero, Conductor y Turno_de_recorrido en donde esta última clase engloba a las anteriores para formar una especie de "listado" donde se muestren los datos, y a su vez esta clase tiene un nombre.

-plantillas: En las plantillas use el "base.html" y el "Index" (este en ambos, tanto en core como en Vehículo) en donde se ve el cuerpo de la pagina principal, con su titulo y su navbar y footer, que estos también son otras plantillas en donde se importan de la principal para poder funcionar. Esta la plantilla donde definí el "Inicio" y otro apartado llamado Asignación de combis donde se ve el listado, la creacion y eliminarión de nuevas asignacioens, etc.
## Mejoras futuras
-Darle mas formato
-Mas colores
-Mas mensajes interactivos a la hora de apretar un boton para volver a cierto apartado de la pagina o de guardar una nueva asignacion.
-Mas opciones para administar el registro y asignacion de nuevas combis.

## Problemas conocidos
-tuve problmas con el views a la hora de definir bien las funciones y poner bien el hipervinculo que lleve a cierta plantilla, como turno_de_recorrido_list.html. También se me generaron algunos problemas en el arhivo de turno_form.html para mostrar el mensaje de que se guardo correctamnete el registro y que el boton de "guardar" no me de error. Y tambien en el archivo de turno_detail.html en donde no se me mostraba en pantalla los datos a los cuales yo estab haciendo referencia, ya que el hipervinculo no estaba siendo encontrado por la pagina, no se veia esa importacion o esa url especificada.
