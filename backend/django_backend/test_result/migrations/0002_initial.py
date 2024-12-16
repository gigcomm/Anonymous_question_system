# Generated by Django 4.2.16 on 2024-12-11 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test_result', '0001_initial'),
        ('test_management', '0002_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='anonymous_participant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='user.anonymousparticipant'),
        ),
        migrations.AddField(
            model_name='testresult',
            name='authenticated_participant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='user.authenticatedparticipant'),
        ),
        migrations.AddField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='test_management.test'),
        ),
        migrations.AddField(
            model_name='participantanswer',
            name='anonymous_participant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='user.anonymousparticipant'),
        ),
        migrations.AddField(
            model_name='participantanswer',
            name='authenticated_participant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='user.authenticatedparticipant'),
        ),
        migrations.AddField(
            model_name='participantanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_answers', to='test_management.question'),
        ),
        migrations.AddField(
            model_name='participantanswer',
            name='selected_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen_answers', to='test_management.answer'),
        ),
        migrations.AddField(
            model_name='participantanswer',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_answers', to='test_management.test'),
        ),
    ]
