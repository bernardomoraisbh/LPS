# Generated by Django 3.0.5 on 2020-05-03 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TccAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.DateTimeField()),
                ('h2', models.DateTimeField()),
                ('h3', models.DateTimeField()),
                ('h4', models.DateTimeField()),
                ('h5', models.DateTimeField()),
                ('h6', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Horario',
            new_name='Apresentacao',
        ),
        migrations.AddField(
            model_name='professor',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TccAdmin.Grade'),
        ),
    ]
