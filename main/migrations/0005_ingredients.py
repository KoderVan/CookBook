# Generated by Django 5.0.2 on 2024-02-23 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_recipemodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(blank=True, max_length=100)),
                ('recipe_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.recipemodel')),
            ],
        ),
    ]