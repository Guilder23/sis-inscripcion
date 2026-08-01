from django.db import migrations, models
import django.db.models.deletion


def forwards(apps, schema_editor):
    Docente = apps.get_model('docentes', 'Docente')
    Grupo = apps.get_model('academico', 'Grupo')
    for grupo in Grupo.objects.all():
        if not hasattr(grupo, 'docente'):
            pass


class Migration(migrations.Migration):
    dependencies = [('academico', '0001_initial'), ('docentes', '0001_initial')]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grupos', to='docentes.docente'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='horario',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
