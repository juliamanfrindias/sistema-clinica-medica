from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby
from calendar import HTMLCalendar, monthrange


import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Paciente(models.Model):


	# def DV_maker(v):
	#     if v >= 2:
	#         return 11 - v
	#     return 0


	# def validate_CPF(value):
	#     """
	#     Value can be either a string in the format XXX.XXX.XXX-XX or an
	#     11-digit number.
	#     """


	#     error_messages = {
	# 	    'invalid': _("Invalid CPF number."),
	# 	    'digits_only': _("This field requires only numbers."),
	# 	    'max_digits': _("This field requires exactly 11 digits."),
	# 	}

	#     if value in EMPTY_VALUES:
	#         return u''
	#     if not value.isdigit():
	#         value = re.sub("[-\.]", "", value)
	#     orig_value = value[:]
	#     try:
	#         int(value)
	#     except ValueError:
	#         raise ValidationError(error_messages['digits_only'])
	#     if len(value) != 11:
	#         raise ValidationError(error_messages['max_digits'])
	#     orig_dv = value[-2:]

	#     new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
	#     new_1dv = DV_maker(new_1dv % 11)
	#     value = value[:-2] + str(new_1dv) + value[-1]
	#     new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
	#     new_2dv = DV_maker(new_2dv % 11)
	#     value = value[:-1] + str(new_2dv)
	#     if value[-2:] != orig_dv:
	#         raise ValidationError(error_messages['invalid'])

	    # return orig_value

	

	id_paciente = models.AutoField(primary_key=True)
	nome_paciente = models.CharField(max_length=200)
	dtnasc_paciente = models.DateTimeField()
	endereco_paciente = models.CharField(max_length=250)
	cpf_paciente = models.CharField(unique=True, max_length=11)
	email_paciente = models.CharField(max_length=250)
# 	validators=[validate_CPF]




class Funcionario(models.Model):
	class Meta:
		abstract = True

	nome_funcionario = models.CharField(max_length=200)
	email_funcionario = models.CharField(max_length=250, default='funcionario@email.com')
	cpf_funcionario = models.CharField(unique=True, max_length=11)
	#validators=[validate_CPF]


class Medico(Funcionario):

	
	id_medico = models.AutoField(primary_key=True)
	especialidade_medico = models.CharField(max_length=200)
	#cpf_medico = models.CharField(unique=True, max_length=14)
	

	


class Recepcionista(Funcionario):

	id_recepcionista = models.AutoField(primary_key=True)
	#cpf_recepcionista = models.CharField(unique=True, max_length=14)
	

class Consulta(models.Model):

	id_consulta = models.AutoField(primary_key=True)
	id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
	#id_receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
	data_consulta = models.DateTimeField()
	

class Agenda(models.Model):

	class Meta:
		unique_together = (('id_medico', 'data_consulta'),)

	id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
	data_consulta = models.DateTimeField()
	id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	



class Medicamento(models.Model):

	
	id_medicamento = models.AutoField(primary_key=True)
	nomegen_medicamento = models.CharField(max_length=200)
	nomefab_medicamento = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)




class Receita(models.Model):

	
	id_receita = models.AutoField(primary_key=True)
	id_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
	id_medicamento = models.ManyToManyField(Medicamento) 
	descricao_receita = models.TextField()
	data_receita = models.DateField(auto_now_add=True)


class Exames(models.Model):

	id_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
	id_exame = models.AutoField(primary_key=True)
	tipo_exame = models.TextField()
	descricao_exame = models.TextField()
	resultado_exame = models.FileField(upload_to='resultados_exames/%d_%m_%Y/')
	data_exame = models.DateField(auto_now_add=True)
	id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

	
class TipoExame(models.Model):

	id_tipoexame = models.AutoField(primary_key=True)
	nome_tipoexame = models.TextField()



class Login(models.Model):

			# def DV_maker(v):
	#     if v >= 2:
	#         return 11 - v
	#     return 0


	# def validate_CPF(value):
	#     """
	#     Value can be either a string in the format XXX.XXX.XXX-XX or an
	#     11-digit number.
	#     """


	#     error_messages = {
	# 	    'invalid': _("Invalid CPF number."),
	# 	    'digits_only': _("This field requires only numbers."),
	# 	    'max_digits': _("This field requires exactly 11 digits."),
	# 	}

	#     if value in EMPTY_VALUES:
	#         return u''
	#     if not value.isdigit():
	#         value = re.sub("[-\.]", "", value)
	#     orig_value = value[:]
	#     try:
	#         int(value)
	#     except ValueError:
	#         raise ValidationError(error_messages['digits_only'])
	#     if len(value) != 11:
	#         raise ValidationError(error_messages['max_digits'])
	#     orig_dv = value[-2:]

	#     new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
	#     new_1dv = DV_maker(new_1dv % 11)
	#     value = value[:-2] + str(new_1dv) + value[-1]
	#     new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
	#     new_2dv = DV_maker(new_2dv % 11)
	#     value = value[:-1] + str(new_2dv)
	#     if value[-2:] != orig_dv:
	#         raise ValidationError(error_messages['invalid'])

	    # return orig_value

	user_login = models.CharField(max_length=11, unique=True)
	password_login = models.CharField(max_length=10)
	type_login = models.IntegerField()
# 	validators=[validate_CPF]



