# Generated by Django 2.1.7 on 2019-04-20 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id_consulta', models.AutoField(primary_key=True, serialize=False)),
                ('data_consulta', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Exames',
            fields=[
                ('id_exame', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_exame', models.TextField()),
                ('descricao_exame', models.TextField()),
                ('resultado_exame', models.FileField(upload_to='resultados_exames/%d_%m_%Y/')),
                ('data_exame', models.DateField(auto_now_add=True)),
                ('id_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=11, unique=True)),
                ('password_login', models.CharField(max_length=10)),
                ('type_login', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.AutoField(primary_key=True, serialize=False)),
                ('nomegen_medicamento', models.CharField(max_length=200)),
                ('nomefab_medicamento', models.CharField(max_length=200)),
                ('fabricante', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('nome_funcionario', models.CharField(max_length=200)),
                ('email_funcionario', models.CharField(default='funcionario@email.com', max_length=250)),
                ('cpf_funcionario', models.CharField(max_length=11, unique=True)),
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('especialidade_medico', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_paciente', models.CharField(max_length=200)),
                ('dtnasc_paciente', models.DateTimeField()),
                ('endereco_paciente', models.CharField(max_length=250)),
                ('cpf_paciente', models.CharField(max_length=11, unique=True)),
                ('email_paciente', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id_receita', models.AutoField(primary_key=True, serialize=False)),
                ('descricao_receita', models.TextField()),
                ('data_receita', models.DateField(auto_now_add=True)),
                ('id_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.Consulta')),
                ('id_medicamento', models.ManyToManyField(to='tcc.Medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcionista',
            fields=[
                ('nome_funcionario', models.CharField(max_length=200)),
                ('email_funcionario', models.CharField(default='funcionario@email.com', max_length=250)),
                ('cpf_funcionario', models.CharField(max_length=11, unique=True)),
                ('id_recepcionista', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exames',
            name='id_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.Paciente'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='id_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.Medico'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.Paciente'),
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('id_medico', 'data_consulta')},
        ),
    ]
