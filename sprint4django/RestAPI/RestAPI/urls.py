"""RestAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importación de módulos necesarios de Django
from django.contrib import admin
from django.urls import path

# Importación de las vistas definidas en la aplicación "webserviceapp"
from webserviceapp import views

# Configuración de las URL para la aplicación

# La lista urlpatterns define las rutas URL y las vistas asociadas a esas rutas.

# Ruta para acceder a la interfaz de administración de Django
urlpatterns = [
    path('admin/', admin.site.urls),

    # Ruta de prueba que llama a la vista 'pagina_de_prueba' definida en 'views'
    path('test/', views.pagina_de_prueba),

    # Ruta para obtener la lista de canciones llamando a la vista 'devolver_canciones'
    path('canciones/', views.devolver_canciones),

    # Ruta para obtener información detallada de una canción por su ID, llamando a la vista 'devolver_canciones_por_id'
    # El '<int:id_solicitado>' indica que se espera un parámetro entero en la URL y se pasará como argumento a la vista
    path('canciones/<int:id_solicitado>', views.devolver_canciones_por_id),

    # Ruta para guardar un comentario en una canción específica, llamando a la vista 'guardar_comentario'
    # El '<int:cancion_id>' indica que se espera un parámetro entero en la URL y se pasará como argumento a la vista
    path('canciones/<int:cancion_id>/comentarios', views.guardar_comentario),
]
