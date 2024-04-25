# Generated by Django 5.0.4 on 2024-04-12 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site_app", "0004_influencer_produtos_produto_prod_categoria_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="influencer",
            old_name="createAt",
            new_name="createdAt",
        ),
        migrations.RenameField(
            model_name="produto",
            old_name="createAt",
            new_name="createdAt",
        ),
        migrations.CreateModel(
            name="Venda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vend_total", models.DecimalField(decimal_places=2, max_digits=6)),
                ("vend_quantidade", models.IntegerField()),
                ("createdAt", models.DateTimeField()),
                (
                    "vend_influencer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="site_app.influencer",
                    ),
                ),
                (
                    "vend_produto",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="site_app.produto",
                    ),
                ),
            ],
        ),
    ]