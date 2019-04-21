from django.urls import path
from django.contrib.auth import views

from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [

    

    path('cadastrar', views.register_login, name='register_login'),
    path('' ,  views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('home', views.authenticate_login, name='authenticate_login'),
    path('login', views.index, name='index'),
    path('pdf/<int:receita_id>/', views.gera_pdf, name='gera_pdf'),
    

    path('paciente/create', views.create_paciente, name='create_paciente'),
    path('paciente/update/<int:paciente_id>/', views.update_paciente, name='update_paciente'),
    path('paciente/<int:paciente_id>/', views.get_paciente_byid, name='get_paciente_byid'),
    path('paciente', views.get_all_paciente, name='get_all_paciente'),
    path('paciente/delete/<int:paciente_id>/', views.delete_paciente, name='delete_paciente'),

    path('consulta/create/<int:medico_id>', views.create_consulta, name='create_consulta'),
    path('consulta/update/<int:consulta_id>/', views.update_consulta, name='update_consulta'),
    path('consulta/<int:consulta_id>/', views.get_consulta_byid, name='get_consulta_byid'),
    path('consulta', views.get_all_consulta, name='get_all_consulta'),
    path('consulta/delete/<int:consulta_id>/', views.delete_consulta, name='delete_consulta'),

    path('medicamento/create', views.create_medicamento, name='create_medicamento'),
    path('medicamento/update/<int:medicamento_id>/', views.update_medicamento, name='update_medicamento'),
    path('medicamento/<int:medicamento_id>/', views.get_medicamento_byid, name='get_medicamento_byid'),
    path('medicamento', views.get_all_medicamento, name='get_all_medicamento'),
    path('medicamento/delete/<int:medicamento_id>/', views.delete_medicamento, name='delete_medicamento'),

    path('receita/create', views.create_receita, name='create_receita'),
    path('receita/update/<int:receita_id>/', views.update_receita, name='update_receita'),
    path('receita/<int:receita_id>/', views.get_receita_byid, name='get_receita_byid'),
    path('receita', views.get_all_receita, name='get_all_receita'),
    path('receita/delete/<int:receita_id>/', views.delete_receita, name='delete_receita'),

    path('exames/create/', views.create_exames, name='create_exames'),
    path('exames/update/<int:exame_id>/', views.update_exames, name='update_exames'),
    path('exames/<int:exame_id>/', views.get_exames_byid, name='get_exames_byid'),
    path('exames', views.get_all_exames, name='get_all_exames'),
    path('exames/delete/<int:exame_id>/', views.delete_exames, name='delete_exames'),
    path('exames/result/<int:exame_id>/', views.result_exames, name='result_exames'),

    path('tipoexame', views.create_tipoexame, name='create_tipoexame'),
    path('add-exame', views.add_exames, name='add_exames'),

    path('medico/create', views.create_medico, name='create_medico'),
    path('medico/update/<int:medico_id>/', views.update_medico, name='update_medico'),
    path('medico/<int:medico_id>/', views.get_medico_byid, name='get_medico_byid'),
    path('medico', views.get_all_medico, name='get_all_medico'),
    path('medico/delete/<int:medico_id>/', views.delete_medico, name='delete_medico'),

    path('recepcionista/create', views.create_recepcionista, name='create_recepcionista'),
    path('recepcionista/update/<int:recepcionista_id>/', views.update_recepcionista, name='update_recepcionista'),
    path('recepcionista/<int:recepcionista_id>/', views.get_recepcionista_byid, name='get_recepcionista_byid'),
    path('recepcionista', views.get_all_recepcionista, name='get_all_recepcionista'),
    path('recepcionista/delete/<int:recepcionista_id>/', views.delete_recepcionista, name='delete_recepcionista')



]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

