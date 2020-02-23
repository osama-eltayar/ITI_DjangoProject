# Generated by Django 3.0.3 on 2020-02-21 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts', '0013_merge_20200221_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='post_name',
        ),
        migrations.AddField(
            model_name='post',
            name='tag_name',
            field=models.ManyToManyField(db_table='PostTags', to='Posts.Tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscribes',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag_name',
            field=models.CharField(max_length=20),
        ),
    ]
