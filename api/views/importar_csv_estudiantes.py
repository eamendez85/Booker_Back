from import_export import resources
import csv
from api.models import Estudiantes, Grados, Grupos, Usuario
import tablib
from rest_framework.response import Response
from django.http import HttpResponse

def importar_csv_estudiantes(request):
    #Native Import CSV
    
    estudiantes = []
    with open("Libro1.csv", "r") as csv_file:
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
    
    return HttpResponse("Importación completada correctamente.")

    # Import-Export library
"""
    with open("libro1.csv", "r") as csv_file:

        estudiante_resource = resources.modelresource_factory(model=Estudiantes)()
        dataset = tablib.Dataset(headers=[field.name for field in Estudiantes._meta.fields]).load(csv_file)
        result = estudiante_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            estudiante_resource.import_data(dataset, dry_run=False)
        return Response(
            "Successfully imported"
        )
"""