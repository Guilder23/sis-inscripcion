from django.db import migrations


def rebuild_materia(apps, schema_editor):
    if schema_editor.connection.vendor == 'postgresql':
        return
    else:
        schema_editor.execute('PRAGMA foreign_keys=off;')
        schema_editor.execute(
            'CREATE TABLE academico_materia_new ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'nombre varchar(100) NOT NULL, '
            'codigo varchar(20) NOT NULL UNIQUE, '
            'creditos integer unsigned NOT NULL, '
            'semestre integer unsigned NOT NULL, '
            'carrera_id bigint REFERENCES academico_carrera(id)'
            ');'
        )
        schema_editor.execute(
            'INSERT INTO academico_materia_new (id, nombre, codigo, creditos, semestre, carrera_id) '
            'SELECT id, nombre, codigo, creditos, semestre, carrera_id FROM academico_materia;'
        )
        schema_editor.execute('DROP TABLE academico_materia;')
        schema_editor.execute('ALTER TABLE academico_materia_new RENAME TO academico_materia;')
        schema_editor.execute('PRAGMA foreign_keys=on;')


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0005_fix_academic_relationship_columns'),
    ]

    operations = [
        migrations.RunPython(rebuild_materia, reverse_func),
    ]
