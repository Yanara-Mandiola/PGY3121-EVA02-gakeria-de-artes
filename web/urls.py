from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('impresionismo/', views.impresionismo, name='impresionismo'),
    path('romanticismo/', views.romanticismo, name='romanticismo'),
    path('surrealismo/', views.surrealismo, name='surrealismo'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login_view, name='login'),
    path('publicar/', views.publicar_obra, name='publicar_obra'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('logout/', views.logout_view, name='logout'),
    path('mi-cuenta/', views.mi_cuenta, name='mi_cuenta'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('dashboard-contacto/', views.dashboard_contacto, name='dashboard_contacto'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('obras/', views.lista_obras, name='lista_obras'),
    path('obra/<int:obra_id>/', views.detalle_obra, name='detalle_obra'),
    path('obra/nueva/', views.crear_obra, name='crear_obra'),
    path('obra/<int:obra_id>/editar/', views.editar_obra, name='editar_obra'),
    path('obra/<int:obra_id>/eliminar/', views.eliminar_obra, name='eliminar_obra'),
    path('dashboard-contacto/<int:contacto_id>/cambiar-estado/<str:nuevo_estado>/', views.cambiar_estado_contacto, name='cambiar_estado_contacto'),
    path('obras/', views.lista_obras, name='lista_obras'),
    path('obra/<int:obra_id>/', views.detalle_obra, name='detalle_obra'),
    path('obra/nueva/', views.crear_obra, name='crear_obra'),
    path('obra/<int:obra_id>/editar/', views.editar_obra, name='editar_obra'),
    path('obra/<int:obra_id>/eliminar/', views.eliminar_obra, name='eliminar_obra'),
]