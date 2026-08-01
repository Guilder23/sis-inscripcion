from django.db import migrations


def fix_academic_relationship_columns(apps, schema_editor):
    if schema_editor.connection.vendor == 'postgresql':
        schema_editor.execute(
            """
            CREATE TABLE IF NOT EXISTS academico_carrera (
                id bigserial PRIMARY KEY,
                nombre varchar(100) NOT NULL,
                facultad_id bigint NOT NULL REFERENCES academico_facultad(id) DEFERRABLE INITIALLY DEFERRED
            );
            """
        )
        schema_editor.execute(
            """
            ALTER TABLE academico_materia ADD COLUMN IF NOT EXISTS carrera_id bigint NULL REFERENCES academico_carrera(id) DEFERRABLE INITIALLY DEFERRED;
            """
        )
    else:
        schema_editor.execute(
            """
            CREATE TABLE IF NOT EXISTS academico_carrera (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(100) NOT NULL,
                facultad_id bigint NOT NULL REFERENCES academico_facultad(id) DEFERRABLE INITIALLY DEFERRED
            );
            """
        )
        schema_editor.execute(
            """
            ALTER TABLE academico_materia ADD COLUMN carrera_id bigint NULL REFERENCES academico_carrera(id) DEFERRABLE INITIALLY DEFERRED;
            """
        )


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_remove_materia_facultad_carrera_materia_carrera'),
    ]

    operations = [
        migrations.RunPython(fix_academic_relationship_columns, reverse_func),
    ]
