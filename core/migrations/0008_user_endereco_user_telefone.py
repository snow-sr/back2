# Generated by Django 4.1.4 on 2022-12-16 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='endereco',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telefone',
            field=models.CharField(max_length=500, null=True),
        ),
    ]