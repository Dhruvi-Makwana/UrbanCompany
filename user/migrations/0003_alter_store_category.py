# Generated by Django 4.1.5 on 2023-01-16 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_store_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="categorychoice",
                to="user.category",
            ),
        ),
    ]
