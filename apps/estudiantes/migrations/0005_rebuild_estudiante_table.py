from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0004_fix_estudiante_facultad_column'),
    ]

    operations = [
        migrations.RunSQL(
            """
            PRAGMA foreign_keys=off;
            CREATE TABLE estudiantes_estudiante_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo varchar(20) NOT NULL UNIQUE,
                nombre varchar(100) NOT NULL,
                apellido varchar(100) NOT NULL,
                email varchar(254) NOT NULL UNIQUE,
                activo bool NOT NULL,
                user_id INTEGER,
                facultad_id bigint REFERENCES academico_facultad(id),
                carrera_id bigint REFERENCES academico_carrera(id)
            );
            INSERT INTO estudiantes_estudiante_new (id, codigo, nombre, apellido, email, activo, user_id, facultad_id, carrera_id)
            SELECT id, codigo, nombre, apellido, email, activo, user_id, facultad_id, carrera_id
            FROM estudiantes_estudiante;
            DROP TABLE estudiantes_estudiante;
            ALTER TABLE estudiantes_estudiante_new RENAME TO estudiantes_estudiante;
            PRAGMA foreign_keys=on;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
