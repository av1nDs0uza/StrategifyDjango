# Generated by Django 4.0.3 on 2022-03-13 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Strategify', '0003_deploy_algocycles'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploy',
            name='username',
            field=models.ForeignKey(default=21, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='Strategify.userregistration'),
            preserve_default=False,
        ),
    ]