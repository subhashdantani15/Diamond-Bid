# Generated by Django 4.1.2 on 2023-01-31 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20, verbose_name='User Name')),
                ('useremail', models.EmailField(max_length=50, verbose_name='Email')),
                ('usercontactno', models.IntegerField(default='', verbose_name='Contact No')),
                ('usergender', models.CharField(choices=[(None, 'select gender'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=None, max_length=12)),
                ('user_DOB', models.DateField()),
                ('user_address', models.TextField()),
                ('userpassword', models.CharField(max_length=20, verbose_name='Password')),
            ],
        ),
    ]
