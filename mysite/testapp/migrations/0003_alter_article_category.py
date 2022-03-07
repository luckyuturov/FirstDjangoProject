# Generated by Django 3.2.9 on 2022-01-28 20:31

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.rubric'),
        ),
    ]
