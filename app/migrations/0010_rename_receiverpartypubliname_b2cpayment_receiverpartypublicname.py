# Generated by Django 4.0.4 on 2022-07-06 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_receiverpartypublicname_b2cpayment_receiverpartypubliname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b2cpayment',
            old_name='ReceiverPartyPubliName',
            new_name='ReceiverPartyPublicName',
        ),
    ]
