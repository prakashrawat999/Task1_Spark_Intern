# Generated by Django 4.0.3 on 2022-06-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_rename_destination_name_transaction_details_destiname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_details',
            name='date',
            field=models.DateTimeField(),
        ),
    ]