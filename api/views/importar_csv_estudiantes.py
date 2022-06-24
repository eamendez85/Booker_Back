import csv

from django.conf import settings
from api.models import CsvEstudiantes, Estudiantes, Grados, Grupos, Usuario
import os

def importar_csv_estudiantes():
    
    csv_bd = CsvEstudiantes.objects.filter(id_csv = 1).first().csv
    url_csv = "media/"+ str(csv_bd)
    estudiantes = []
    with open(url_csv, "r") as csv_file:
        data = list(csv.reader(csv_file, delimiter=";"))
        for row in data[1:]:
            id_grupo_request = Grupos.objects.filter(id_grupo = row[6]).first()
            id_grado_request = Grados.objects.filter(id_grado = row[7]).first()
            
            usuario = Usuario(
                    doc=row[0],
                    email= row[8],
                    tipo_usuario="E"
                )
            usuario.set_password(row[0])
            usuario.save()
            
            doc_request = Usuario.objects.filter(doc = row[0]).first()
            
            estudiantes.append(
                Estudiantes(
                    doc_estudiante=doc_request,
                    tipodoc=row[1],
                    nombres=row[2],
                    apellidos=row[3],
                    telefono=row[4],
                    direccion=row[5],
                    id_grupo=id_grupo_request,
                    id_grado=id_grado_request
                )
            )
    if len(estudiantes) > 0:
        Estudiantes.objects.bulk_create(estudiantes)

    csv_objeto = CsvEstudiantes.objects.filter(id_csv = 1).first()
    csv_objeto.delete()

    ruta_csv = "media/" + str(csv_bd)
    os.remove(ruta_csv)