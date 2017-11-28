# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField(max_length=400)),
                ('street_address', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(default='', max_length=100)),
                ('zip', models.CharField(max_length=100, null=True)),
                ('cc_number', models.CharField(max_length=200)),
                ('cc_exp_date', models.BooleanField(default=False)),
                ('cc_security_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('developer_name', models.CharField(max_length=400)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(max_length=100, null=True)),
                ('zip', models.CharField(max_length=200)),
                ('phone_number', models.CharField(default=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DevelopersProducesProducts',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('developer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Developers')),
            ],
        ),
        migrations.CreateModel(
            name='Merchants',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('merchant_name', models.CharField(max_length=400)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(max_length=100, null=True)),
                ('zip', models.CharField(max_length=200)),
                ('phone_number', models.CharField(default=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=400)),
                ('product_description', models.CharField(max_length=200)),
                ('price', models.CharField(default='', max_length=100)),
                ('genre', models.CharField(max_length=100, null=True)),
                ('release_date', models.DateTimeField(max_length=200)),
                ('stock', models.BigIntegerField(max_length=200)),
                ('developer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Developers')),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Merchants')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('review_content', models.TextField(max_length=500)),
                ('review_date_time', models.DateTimeField(auto_now_add=True)),
                ('reivew_rating', models.DecimalField(decimal_places=1, max_digits=3, max_length=40)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Customers')),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Merchants')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Products')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Customers')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Products')),
            ],
        ),
        migrations.CreateModel(
            name='SupportTickets',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ticket_content', models.TextField(max_length=500)),
                ('ticket_date_time', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=50)),
                ('payment_method', models.CharField(max_length=40)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Customers')),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Merchants')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Products')),
            ],
        ),
        migrations.AddField(
            model_name='developersproducesproducts',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Products'),
        ),
    ]