# Generated by Django 3.0.3 on 2020-02-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0016_auto_20200222_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='react',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], default='none', max_length=7),
        ),
    ]
