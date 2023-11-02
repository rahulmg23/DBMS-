# Generated by Django 4.0.1 on 2022-01-14 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('deal_date', models.DateTimeField(auto_created=True)),
                ('order_date', models.DateTimeField(auto_created=True)),
                ('sale_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(max_length=100)),
                ('cost', models.IntegerField()),
                ('status', models.CharField(choices=[('Sold', 'Sold'), ('On hold', 'On hold'), ('Rejected', 'Rejected')], max_length=20)),
                ('tax_id', models.IntegerField(unique=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.customer')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.IntegerField()),
                ('description', models.TextField(max_length=100)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], max_length=20)),
                ('tax_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.sale', to_field='tax_id')),
            ],
        ),
    ]