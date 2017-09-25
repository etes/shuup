# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shuup.core.fields
import shuup.front.models.stored_basket
import shuup.utils.properties


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoredBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=shuup.front.models.stored_basket.generate_key, max_length=32, verbose_name='key')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='updated on')),
                ('persistent', models.BooleanField(db_index=True, default=False, verbose_name='persistent')),
                ('deleted', models.BooleanField(db_index=True, default=False, verbose_name='deleted')),
                ('finished', models.BooleanField(db_index=True, default=False, verbose_name='finished')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='title')),
                ('data', shuup.core.fields.TaggedJSONField(verbose_name='data')),
                ('taxless_total_price_value', shuup.core.fields.MoneyValueField(blank=True, decimal_places=9, default=0, max_digits=36, null=True, verbose_name='taxless total price')),
                ('taxful_total_price_value', shuup.core.fields.MoneyValueField(blank=True, decimal_places=9, default=0, max_digits=36, null=True, verbose_name='taxful total price')),
                ('currency', shuup.core.fields.CurrencyField(max_length=4, verbose_name='currency')),
                ('prices_include_tax', models.BooleanField(verbose_name='prices include tax')),
                ('product_count', models.IntegerField(default=0, verbose_name='product_count')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='baskets_created', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_baskets', to='shuup.Contact', verbose_name='customer')),
                ('orderer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderer_baskets', to='shuup.PersonContact', verbose_name='orderer')),
                ('products', models.ManyToManyField(blank=True, to='shuup.Product', verbose_name='products')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuup.Shop', verbose_name='shop')),
            ],
            options={
                'verbose_name': 'stored basket',
                'verbose_name_plural': 'stored baskets',
            },
            bases=(shuup.utils.properties.MoneyPropped, models.Model),
        ),
    ]