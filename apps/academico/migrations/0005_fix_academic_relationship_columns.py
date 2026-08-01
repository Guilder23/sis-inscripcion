from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_remove_materia_facultad_carrera_materia_carrera'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS academico_carrera (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(100) NOT NULL,
                facultad_id bigint NOT NULL REFERENCES academico_facultad(id) DEFERRABLE INITIALLY DEFERRED
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS academico_carrera;",
        ),
        migrations.RunSQL(
            """
            ALTER TABLE academico_materia ADD COLUMN carrera_id bigint NULL REFERENCES academico_carrera(id) DEFERRABLE INITIALLY DEFERRED;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
