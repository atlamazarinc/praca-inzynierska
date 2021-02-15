# Generated by Django 3.1.6 on 2021-02-15 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('adres_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('wojewodztwo', models.CharField(max_length=50)),
                ('miejscowosc', models.CharField(max_length=50)),
                ('ulica', models.CharField(max_length=50)),
                ('numer_domu', models.IntegerField()),
                ('kod_pocztowy', models.CharField(default=None, max_length=50)),
                ('adres_poczatkowy', models.CharField(max_length=50)),
                ('adres_koncowy', models.CharField(max_length=50)),
                ('adres_spotkania', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ocenianie',
            fields=[
                ('ocena_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('punkt', models.CharField(choices=[('1', 'Bardzo Zle'), ('2', 'Zle'), ('3', 'Umiarkowany'), ('4', 'Dobrze'), ('5', 'Bardzo Dobrze')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Oferty',
            fields=[
                ('oferty_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('czas_odjazdu', models.TimeField()),
                ('ilosc_miejsc', models.IntegerField()),
                ('cena', models.IntegerField()),
                ('komentarz', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pasazer', models.BooleanField(default=False)),
                ('kierowca', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trasa',
            fields=[
                ('trasa_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('adres_koncowy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adres_kon', to='MainApp.adres')),
                ('adres_poczatkowy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adres_pocz', to='MainApp.adres')),
                ('adres_spotkania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adres_spot', to='MainApp.adres')),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uzytkownik_imie', models.CharField(max_length=50)),
                ('uzytkownik_nazwisko', models.CharField(max_length=50)),
                ('uzytkownik_telefon', models.IntegerField()),
                ('uzytkownik_mail', models.EmailField(max_length=100)),
                ('ocena_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.ocenianie')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.role')),
                ('trasa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.trasa')),
                ('uzytkownik', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trasaoferty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oferty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.oferty')),
                ('trasa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.trasa')),
            ],
        ),
        migrations.CreateModel(
            name='Pojazd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100)),
                ('model', models.IntegerField()),
                ('oferty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.oferty')),
                ('uzytkownik', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.uzytkownik')),
            ],
        ),
        migrations.AddField(
            model_name='oferty',
            name='trasa_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.trasa'),
        ),
        migrations.AddField(
            model_name='oferty',
            name='uzytkownik',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.uzytkownik'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocena_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.ocenianie')),
                ('oferty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.oferty')),
            ],
        ),
    ]
