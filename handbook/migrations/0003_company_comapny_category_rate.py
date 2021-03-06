# Generated by Django 4.0 on 2021-12-18 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0002_company_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='comapny_category',
            field=models.CharField(choices=[('IS', 'Internet Shop'), ('SM', 'SuperMarket'), ('SP', 'Shopping center'), ('FR', 'Furniture Shop'), ('DF', 'DEFAULT')], default='DF', max_length=40),
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('VB', '1'), ('R', '2'), ('G', '3'), ('B', '4'), ('D', '5')], max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handbook.company')),
            ],
        ),
    ]
