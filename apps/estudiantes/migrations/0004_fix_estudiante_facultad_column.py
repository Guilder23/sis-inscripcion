from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_estudiante_facultad_alter_estudiante_carrera'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE estudiantes_estudiante ADD COLUMN facultad_id bigint NULL REFERENCES academico_facultad(id) DEFERRABLE INITIALLY DEFERRED;
            ALTER TABLE estudiantes_estudiante ADD COLUMN carrera_id bigint NULL REFERENCES academico_carrera(id) DEFERRABLE INITIALLY DEFERRED;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
