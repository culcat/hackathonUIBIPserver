# Generated by Django 4.1.6 on 2023-04-07 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.status'),
        ),
    ]