from django.db import migrations


def fix_estudiante_columns(apps, schema_editor):
    if schema_editor.connection.vendor != 'postgresql':
        return

    schema_editor.execute(
        """
        ALTER TABLE estudiantes_estudiante
        ADD COLUMN IF NOT EXISTS facultad_id bigint NULL REFERENCES academico_facultad(id) DEFERRABLE INITIALLY DEFERRED;
        """
    )
    schema_editor.execute(
        """
        ALTER TABLE estudiantes_estudiante
        ADD COLUMN IF NOT EXISTS carrera_id bigint NULL REFERENCES academico_carrera(id) DEFERRABLE INITIALLY DEFERRED;
        """
    )


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_estudiante_facultad_alter_estudiante_carrera'),
    ]

    operations = [
        migrations.RunPython(fix_estudiante_columns, reverse_func),
    ]
