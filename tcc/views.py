from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string

from datetime import date
from weasyprint import HTML
from calendar import monthrange
import datetime
import json

from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
#from django.http import HttpResponse

from .models import Paciente, Consulta, Medicamento, Receita, Medico, Recepcionista, Exames, Login, Agenda, TipoExame


from .forms import PacienteForm, ConsultaForm, MedicamentoForm, ReceitaForm, ExamesForm, MedicoForm, RecepcionistaForm, LoginForm


def index(request):
	return valida_login(request)



#################################################################################
#Paciente
#################################################################################	

def create_paciente(request):

	if request.method == 'POST':

		nome_pac = request.POST['nome_p']
		email_pac = request.POST['email_p']
		cpf_pac = request.POST['cpf_p']
		data_pac = request.POST['data_p']

		paciente = Paciente(nome_paciente=nome_pac, email_paciente=email_pac, cpf_paciente=cpf_pac, dtnasc_paciente=data_pac)
		paciente.save()
		return redirect('/paciente')


	return render(request, "tcc/paciente-create.html", {})



def update_paciente(request, paciente_id):

	paciente = Paciente.objects.get(pk=paciente_id)

	if request.method == 'POST':

		nome_pac = request.POST['nome_p']
		email_pac = request.POST['email_p']
		

		paciente.nome_paciente = nome_pac
		paciente.email_paciente = email_pac
		

		paciente.save()
		return redirect('/paciente')

	return render(request, "tcc/paciente-update.html", {'paciente': paciente})






def get_paciente_byid(request, paciente_id):

	paciente = Paciente.objects.get(pk=paciente_id)
	return render(request, "tcc/paciente-details.html", {'paciente': paciente})

def get_all_paciente(request):

	paciente = Paciente.objects.all()
	return render(request, "tcc/paciente-all.html", {'paciente': paciente})


def delete_paciente(request, paciente_id):

	paciente = Paciente.objects.get(pk=paciente_id)
	paciente.delete()
	#return redirect('http://127.0.0.1:8000/paciente')
	return redirect('/paciente')
	#return render(request, "tcc/paciente_all.html")



#################################################################################
#Consulta
#################################################################################


def json_agenda(agenda):

	version_agenda = [{"title": a['id_paciente'], "start": a['data_consulta'].strftime('%Y-%m-%d %H:%M')} for a in agenda]
	return json.dumps({"versionAgenda": version_agenda}, indent=4)




def create_consulta(request, medico_id):

	agenda = Agenda.objects.filter(id_medico=medico_id).values('data_consulta', 'id_paciente')
		
	for a in agenda:
		paciente = Paciente.objects.get(pk=a['id_paciente'])
		a['id_paciente'] = paciente.nome_paciente
		
	

	lista_ag = json_agenda(agenda)
	

	medico = Medico.objects.get(pk=medico_id)

	message = 'oi'

	if request.method == 'POST':

		try:
			consulta_pid = request.POST['paciente']
			consulta_dia = request.POST['data']
			consulta_hr = request.POST['time']
			consulta_dt = consulta_dia+"T"+consulta_hr

			paciente = Paciente.objects.get(pk=consulta_pid)
			

			consulta = Consulta(id_paciente=paciente, id_medico=medico, data_consulta=consulta_dt)
			agenda = Agenda(id_medico=medico, data_consulta=consulta_dt, id_paciente=paciente)
			consulta.save()
			agenda.save()

			return redirect('/medico')
		except Paciente.DoesNotExist:
			message = 'Número de paciente incorreto'
			return render(request, "tcc/consulta-create.html", {'message': message, 'agenda': lista_ag, 'medico': medico})
		

	return render(request, "tcc/consulta-create.html", {'message': message, 'agenda': lista_ag, 'medico': medico})







def update_consulta(request, consulta_id):

	
	consulta = Consulta.objects.get(pk=consulta_id)
	medico_id = consulta.id_medico.id_medico
	agenda = Agenda.objects.filter(id_medico=medico_id).values('data_consulta', 'id_paciente')
	agenda1 = Agenda.objects.get(id_medico=medico_id, data_consulta=consulta.data_consulta)
	
	for a in agenda:
		paciente = Paciente.objects.get(pk=a['id_paciente'])
		a['id_paciente'] = paciente.nome_paciente
		
	

	lista_ag = json_agenda(agenda)


	if request.method == 'POST':

		consulta_dia = request.POST['data']
		consulta_hr = request.POST['time']
		consulta_dt = consulta_dia+"T"+consulta_hr

		consulta.data_consulta = consulta_dt
		agenda1.data_consulta = consulta_dt
		consulta.save()
		agenda1.save()
		return redirect('/consulta')
	
	data = consulta.data_consulta.date().strftime('%Y-%m-%d')
	hora = consulta.data_consulta.time()

	return render(request, "tcc/consulta-update.html", { 'agenda': lista_ag, 'consulta': consulta, 'data': data, 'time': hora})
			




def get_consulta_byid(request, consulta_id):

	consulta = Consulta.objects.get(pk=consulta_id)
	return render(request, "tcc/consulta-details.html", {'consulta': consulta})

def get_consulta(request, consulta_id):

	consulta = Consulta.objects.get(pk=consulta_id)
	return consulta


def get_all_consulta(request):

	consulta = Consulta.objects.all()
	return render(request, "tcc/consulta-all.html", {'consulta': consulta})


def delete_consulta(request, consulta_id):

	consulta = Consulta.objects.get(pk=consulta_id)
	consulta.delete()
	return redirect('/consulta')



#################################################################################
#Medicamento
#################################################################################

def create_medicamento(request):


	if request.method == 'POST':

		nome_gen = request.POST['nome_gen']
		nome_fab = request.POST['nome_fab']
		fabricante = request.POST['fab']
		medicamento = Medicamento(nomegen_medicamento=nome_gen, nomefab_medicamento=nome_fab, fabricante=fabricante)
		
		medicamento.save()
		return redirect('/home')


	return render(request, "tcc/medicamento-create.html")

def update_medicamento(request, medicamento_id):

	medicamento = Medicamento.objects.get(pk=medicamento_id)

	if request.method == 'POST':

		nome_gen = request.POST['nome_gen']
		nome_fab = request.POST['nome_fab']
		fabricante = request.POST['fab']

		medicamento.nomegen_medicamento = nome_gen
		medicamento.nomefab_medicamento = nome_fab
		medicamento.fabricante = fabricante
		medicamento.save()
		return redirect('/home')


	return render(request, "tcc/medicamento-create.html", {'medicamento': medicamento})


	# medicamento = Medicamento.objects.get(pk=medicamento_id)
	# form = MedicamentoForm(request.POST or None, instance=medicamento)

	# if form.is_valid():
	# 	form.save()
	# 	return redirect('/login')

	# return render(request, "tcc/medicamento-create.html", {'form': form, 'medicamento': medicamento})




def get_medicamento_byid(request, medicamento_id):

	medicamento = Medicamento.objects.get(pk=medicamento_id)
	return render(request, "tcc/medicamento-details.html", {'medicamento': medicamento})


def get_all_medicamento(request):

	medicamento = Medicamento.objects.all()
	return render(request, "tcc/medicamento-all.html", {'medicamento': medicamento})


def delete_medicamento(request, medicamento_id):

	medicamento = Medicamento.objects.get(pk=medicamento_id)
	medicamento.delete()
	return redirect('/medicamento')



#################################################################################
#Receita
#################################################################################
def create_receita(request):

	medicamentos = Medicamento.objects.all()
	

	if request.method == 'POST':

		consulta_r = request.POST['consulta']
		descricao_r = request.POST['desc']
		medicamento_r = request.POST.getlist('remedios')
		data_r = date.today()
		

		try:
			consulta = Consulta.objects.get(pk=consulta_r)

			receita = Receita(id_consulta=consulta, descricao_receita=descricao_r, data_receita=data_r)
			receita.save()

			for m in medicamento_r:
				med = Medicamento.objects.get(pk=m)
				receita.id_medicamento.add(med)
			

			return redirect('/receita/' + str(receita.id_receita))

		except Consulta.DoesNotExist:
			message = 'Numero de consulta nao existe'
			return render(request, "tcc/receita-create.html", {'medicamentos': medicamentos, 'message': message})

	return render(request, "tcc/receita-create.html", {'medicamentos': medicamentos})



def update_receita(request, receita_id):

	receita = Receita.objects.get(pk=receita_id)
	form = ReceitaForm(request.POST or None, instance=receita)

	if form.is_valid():
		form.save()
		return redirect('/login')

	return render(request, "tcc/receita-create.html", {'form': form, 'receita': receita})


def get_receita_byid(request, receita_id):

	receita = Receita.objects.get(pk=receita_id)
	return render(request, "tcc/receita-details.html", {'receita': receita})


def get_all_receita(request):

	receita = Receita.objects.all()
	return render(request, "tcc/receita-all.html", {'receita': receita})


def delete_receita(request, receita_id):

	receita = Receita.objects.get(pk=receita_id)
	receita.delete()
	return redirect('/receita')



#################################################################################
#Exames
#################################################################################

def create_exames(request):


	tipoexame = TipoExame.objects.all()

	if request.method == 'POST':

		consulta_ex = request.POST['consulta']
		tipo_ex = request.POST['tipo']
		desc_ex = request.POST['desc']
		

		try:
			consulta = Consulta.objects.get(pk=consulta_ex)
			id_medico=consulta.id_medico
			exame = Exames(id_consulta=consulta, tipo_exame=tipo_ex, descricao_exame=desc_ex, id_medico=id_medico)
			exame.save()

			return redirect('/home')

		except Consulta.DoesNotExist:
			message = 'Consulta nao realizada'
			return render(request, "tcc/exames-create.html", {'message': message, 'tipoexame': tipoexame})

		

	return render(request, "tcc/exames-create.html", {'tipoexame': tipoexame})



def update_exames(request, exame_id):

	exame = Exames.objects.get(pk=exame_id)

	if request.method == 'POST':

		desc_ex = request.POST['desc']

		try:
			consulta = Consulta.objects.get(pk=consulta_ex)
		
			exame.descricao_exame = desc_ex
		
			exame.save()

			return redirect('/exames')

		except Consulta.DoesNotExist:
			message = 'Consulta nao realizada'
			return render(request, "tcc/exames-create.html", {'message': message})

	return render(request, "tcc/exames-create.html", {'exame': exame})



def result_exames(request, exame_id):

	exames = Exames.objects.get(pk=exame_id)

	if request.method == 'POST':
		file = request.POST
		newdoc = request.FILES['resultado']	
		print("FILE: ", type(newdoc))
		exames.resultado_exame = newdoc
		exames.save()

		return redirect('/exames')

	
	return render(request, "tcc/exames-results.html", {'exame': exames})






def get_exames_byid(request, exame_id):

	exames = Exames.objects.get(pk=exame_id)
	return render(request, "tcc/exames-details.html", {'exames': exames})


def get_all_exames(request):

		
	if request.session['tipo_user'] == 2 or request.session['tipo_user'] == 0:
		exames = Exames.objects.all()		
		return render(request, "tcc/exames-all.html", {'exames': exames})
	else:
		medico_id = request.session['medico_id']
		exames = Exames.objects.filter(id_medico=medico_id)
		print("Exames: ", exames)
		return render(request, "tcc/exames-all.html", {'exames': exames})

def delete_exames(request, exame_id):

	exame = Exames.objects.get(pk=exame_id)
	exame.delete()
	return redirect('/exames')



def create_tipoexame(request):

	if request.method == 'POST':

		tipo = request.POST['tipoexame']
		tipoexame = TipoExame(nome_tipoexame=tipo)
		tipoexame.save()
		return redirect('/home')

	return render(request, "tcc/tipoexame-create.html")


def add_exames(request):
	list_exame = ["Testes Alérgicos", "Eletrocardiograma", "Ecocardiograma Colorido", "Duplex scan Venoso/Arterial Carótidas e Vertebrais", "Exames Laboratoriais", "Colonoscopia", "Endoscopia", "Raios-X", "Ultrassonografia", "Tomografia", "Ressonância Magnética", "Mamografia", "Angioressonância", "Densitometria Óssea", "Eletroencefalograma", "Mapeamento Cerebral", "Polissonografia", "Eletroneuromiografia", "Audiometria Tonal / Limiar", "Audiometria Vocal", "Impedanciometria", " Emissões Otoacústicas (teste da orelhinha)", "Videolaringoscopia", "Raios-X Odontológicos"]
	for e in list_exame:
		tipo = e
		tipoexame = TipoExame(nome_tipoexame=tipo)
		tipoexame.save()
	print("Fim do for")
	return redirect('/home')

#################################################################################
#Medico
#################################################################################

def create_medico(request):

	form = MedicoForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('/home')

	return render(request, "tcc/medico-create.html", {'form': form})

def update_medico(request, medico_id):

	medico = Medico.objects.get(pk=medico_id)

	if request.method == 'POST':

		nome = request.POST['nome']
		email = request.POST['email']
		especialidade = request.POST['especialidade']

		medico.nome_funcionario = nome
		medico.email_funcionario = email
		medico.especialidade = especialidade
		medico.save()
		return redirect('/home')


	return render(request, "tcc/medico-create.html", {'medico': medico})




def get_medico_byid(request, medico_id):

	medico = Medico.objects.get(pk=medico_id)
	agenda = Agenda.objects.filter(id_medico=medico_id).values('data_consulta', 'id_paciente')
		
	for a in agenda:
		paciente = Paciente.objects.get(pk=a['id_paciente'])
		a['id_paciente'] = paciente.nome_paciente
		
	

	lista_ag = json_agenda(agenda)


	return render(request, "tcc/medico-details.html", {'medico': medico, 'agenda': lista_ag})

def get_all_medico(request):

	medico = Medico.objects.all()
	return render(request, "tcc/medico-all.html", {'medico': medico})


def delete_medico(request, medico_id):

	medico = Medico.objects.get(pk=medico_id)
	medico.delete()
	return redirect('/medico')




#################################################################################
#Recepcionista
#################################################################################

def create_recepcionista(request):
	

	form = RecepcionistaForm(request.POST or None)

	if form.is_valid():
		form.save()
		redirect('/login')

	return render(request, "tcc/recepcionista-create.html", {'form': form})


def update_recepcionista(request, recepcionista_id):


	recepcionista = Recepcionista.objects.get(pk=recepcionista_id)

	if request.method == 'POST':

		nome = request.POST['nome']
		email = request.POST['email']

		recepcionista.nome_funcionario = nome
		recepcionista.email_funcionario = email
		recepcionista.save()
		return redirect('/home')


	return render(request, "tcc/recepcionista-create.html", {'recepcionista': recepcionista})

	
def get_recepcionista_byid(request, recepcionista_id):

	recepcionista = Recepcionista.objects.get(pk=recepcionista_id)
	return render(request, "tcc/recepcionista-details.html", {'recepcionista': recepcionista})

def get_all_recepcionista(request):

	recepcionista = Recepcionista.objects.all()
	return render(request, "tcc/recepcionista-all.html", {'recepcionista': recepcionista})

def delete_recepcionista(request, recepcionista_id):

	recepcionista = Recepcionista.objects.get(pk=recepcionista_id)
	recepcionista.delete()
	return redirect('/recepcionista')







	



#################################################################################
#Login
#################################################################################



def register_login(request):

	if request.method == 'POST':

		user = request.POST['user']
		password = request.POST['password']
		type_l = request.POST['tipo_func']
		name = request.POST['nome']
		email = request.POST['email']
		especialidade = ''
		if 'especialidade' in request.POST:
			especialidade = request.POST['especialidade']



		login = Login(user_login=user, password_login=password, type_login=type_l)
		login.save()
		if type_l == '1':
			#cria med
			medico = Medico(nome_funcionario=name, email_funcionario=email, cpf_funcionario=user, especialidade_medico=especialidade)
			medico.save()

		elif type_l == '0':
			#cria recep
			recepcionista = Recepcionista(nome_funcionario=name, email_funcionario=email, cpf_funcionario=user)
			recepcionista.save()

		else:
			return render(request, "tcc/login-register.html", {})
		return render(request, "tcc/login-enter.html", {})
	else:
		return render(request, "tcc/login-register.html", {})



def authenticate_login(request):

	
	if request.method == 'POST':

		user = request.POST['user']
		password = request.POST['password']

		try:
			usuario = Login.objects.get(user_login = user, password_login = password)


			user_db = usuario.user_login
			password_db = usuario.password_login
			person_db = usuario.type_login


			
			if person_db == 1:
				medico = Medico.objects.get(cpf_funcionario=user_db)
				idmed = medico.id_medico
				print("Medico :", idmed)
				request.session['medico_id'] = idmed

			request.session['tipo_user'] = person_db
			request.session['logado'] = True

			return index_usuario(request, person_db)

			

		except Login.DoesNotExist:
			request.session['logado'] = False
			return render(request, "tcc/login-register.html", {}) 
	else:
		return valida_login(request)

		



def logout(request):
	request.session['logado'] = False
	return valida_login(request)




def valida_login(request):
	
	try:
		if request.session['logado']:
			
			return index_usuario(request, request.session['tipo_user'])
		else:
			
			return render(request, "tcc/login-enter.html", {})
	except Exception as e:
		request.session['logado'] = False
		return render(request, "tcc/login-enter.html", {})
	
	




def index_usuario(request, person_db):
	if person_db == 1:
		return render(request, "tcc/index-medico.html",)
	elif person_db == 0:
		return render(request, "tcc/index-recepcionista.html")
	else: 
		return render(request, "tcc/index-administrador.html")





#################################################################################
#Emitir relatorio
#################################################################################



def gera_pdf(request, receita_id):
	#request.session['logado'] = True

	receita = Receita.objects.get(pk=receita_id)
	html_string = render_to_string('tcc/receita-print.html', {'receita': receita})

	html = HTML(string=html_string)
	html.write_pdf(target='/tmp/mypdf.pdf')

	fs = FileSystemStorage('/tmp')

	with fs.open('mypdf.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
		return response

	return response




