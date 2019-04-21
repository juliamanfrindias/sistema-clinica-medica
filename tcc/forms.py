from django import forms
from .models import Paciente, Consulta, Medicamento, Receita, Medico, Recepcionista, Exames, Login



class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = ['id_paciente', 
				'nome_paciente', 
				'dtnasc_paciente', 
				'endereco_paciente', 
				'cpf_paciente', 
				'email_paciente']




class ConsultaForm(forms.ModelForm):
	class Meta:
		model = Consulta
		fields = ['id_consulta', 
				'id_paciente',
				'id_medico',
				'data_consulta']



class MedicamentoForm(forms.ModelForm):
	class Meta:
		model = Medicamento
		fields = ['id_medicamento',
				'nomegen_medicamento',
				'nomefab_medicamento',
				'fabricante']


class ReceitaForm(forms.ModelForm):
	class Meta:
		model = Receita
		fields = ['id_receita',
				'id_consulta',
				'id_medicamento',
				'descricao_receita']


class ExamesForm(forms.ModelForm):
	class Meta:
		model = Exames
		fields = ['id_consulta',
				'id_exame',
				'descricao_exame',
				'resultado_exame']


class MedicoForm(forms.ModelForm):
	class Meta:
		model = Medico
		fields = ['nome_funcionario',
				'email_funcionario',
				'id_medico',
				'especialidade_medico']



class RecepcionistaForm(forms.ModelForm):
	class Meta:
		model = Recepcionista
		fields = ['nome_funcionario',
				'email_funcionario',
				'id_recepcionista']


class LoginForm(forms.ModelForm):
	class Meta: 
		model = Login
		fields = ['user_login',
				  'password_login',
				  'type_login']



