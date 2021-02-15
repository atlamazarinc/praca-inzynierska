# Generated by Django 3.1.6 on 2021-02-15 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzytkownik',
            name='ocena_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.ocenianie'),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.role'),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='trasa_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.trasa'),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='uzytkownik',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='uzytkownik_imie',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='uzytkownik_mail',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='uzytkownik_nazwisko',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='uzytkownik_telefon',
            field=models.IntegerField(null=True),
        ),
    ]
