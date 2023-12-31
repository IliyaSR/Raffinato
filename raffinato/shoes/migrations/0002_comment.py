# Generated by Django 4.2.4 on 2023-08-15 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('to_suit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.shoes')),
            ],
            options={
                'ordering': ['-date_time_of_publication'],
            },
        ),
    ]
