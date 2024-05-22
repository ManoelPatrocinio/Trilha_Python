# Generated by Django 5.0.4 on 2024-05-01 11:44

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Locais',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.TextField(null=True)),
                ('matricula', models.TextField(null=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senhas_app.cargo')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senhas_app.local')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Chamada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senhas_app.local')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senhas_app.usuario')),
            ],
            options={
                'verbose_name_plural': 'Senhas',
            },
        ),
    ]
