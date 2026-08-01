from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0002_docente_carrera_docente_facultad'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE docentes_docente ADD COLUMN facultad_id bigint NULL REFERENCES academico_facultad(id) DEFERRABLE INITIALLY DEFERRED;
            ALTER TABLE docentes_docente ADD COLUMN carrera_id bigint NULL REFERENCES academico_carrera(id) DEFERRABLE INITIALLY DEFERRED;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
