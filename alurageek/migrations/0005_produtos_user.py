# Generated by Django 4.1.2 on 2022-10-12 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("alurageek", "0004_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="produtos",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="alurageek.users",
            ),
        ),
    ]
