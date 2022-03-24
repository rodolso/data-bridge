# Generated by Django 2.1.2 on 2022-03-24 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=20)),
                ('type_company', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Formularios',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_id', models.IntegerField()),
                ('score', models.FloatField()),
                ('datetime', models.DateField()),
                ('company_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fullstack_communication.Companies')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('question', models.CharField(max_length=140)),
                ('type_company', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('result', models.FloatField()),
                ('active', models.CharField(max_length=6)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack_communication.Category')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack_communication.Formularios')),
            ],
        ),
        migrations.CreateModel(
            name='Typeresponses',
            fields=[
                ('type_response', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('answer_id', models.IntegerField()),
                ('answer_string', models.CharField(max_length=25)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='typeresponses',
            unique_together={('type_response', 'answer_id')},
        ),
        migrations.AddField(
            model_name='results',
            name='type_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack_communication.Typeresponses'),
        ),
        migrations.AlterUniqueTogether(
            name='results',
            unique_together={('question_id', 'type_company')},
        ),
        migrations.AlterUniqueTogether(
            name='formularios',
            unique_together={('employee_id', 'question_id', 'datetime')},
        ),
    ]
