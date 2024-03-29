# Generated by Django 3.2 on 2021-04-27 16:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid')),
                ('content', models.CharField(max_length=150, verbose_name='Content')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Is Complete')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
