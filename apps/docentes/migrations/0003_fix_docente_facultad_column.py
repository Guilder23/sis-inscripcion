from django.db import migrations


def fix_docente_columns(apps, schema_editor):
    if schema_editor.connection.vendor != 'postgresql':
        return

    schema_editor.execute(
        """
        ALTER TABLE docentes_docente
        ADD COLUMN IF NOT EXISTS facultad_id bigint NULL REFERENCES academico_facultad(id) DEFERRABLE INITIALLY DEFERRED;
        """
    )
    schema_editor.execute(
        """
        ALTER TABLE docentes_docente
        ADD COLUMN IF NOT EXISTS carrera_id bigint NULL REFERENCES academico_carrera(id) DEFERRABLE INITIALLY DEFERRED;
        """
    )


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0002_docente_carrera_docente_facultad'),
    ]

    operations = [
        migrations.RunPython(fix_docente_columns, reverse_func),
    ]
