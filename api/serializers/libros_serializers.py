from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from api.models import  Libros
from api.serializers.general_serializers import AutoresSerializer, CategoriasSerializer, EditorialesSerializer, IdiomasSerializer


#Serializer libros
class LibrosSerializer(serializers.ModelSerializer):

  class Meta:
    model = Libros
    fields = "__all__"

class LibrosListSerializer(serializers.ModelSerializer):

  id_editorial = EditorialesSerializer(many=False, read_only=True)
  autores = AutoresSerializer(many=True, read_only=True)
  id_idioma = IdiomasSerializer(many=False, read_only=True)
  categorias = CategoriasSerializer(many=True, read_only=True)

  
  class Meta:
    model= Libros
    fields= ['id_libro', 'isbn', 'imagen_libro', 'nombre', 'id_editorial', 'edicion', 'autores', 'id_idioma', 'categorias', 'descripcion', 'numero_paginas', 'numero_capitulos', 'presentacion', 'anexos', 'palabras_clave', 'estado']




"""class EjemplaresLibrosSerializer(serializers.Serializer):

    class Meta:
            model = Ejemplares
            fields = ["id_libro", ]"""


class LibrosConEjemplaresSerializer(serializers.ModelSerializer):
    cantEjemplares = serializers.IntegerField(default=1)

    class Meta:
        model = Libros
        fields = ["id_libro","isbn","imagen_libro","nombre","edicion","descripcion","numero_paginas","numero_capitulos","presentacion","anexos","palabras_clave","estado","id_editorial","id_idioma","autores","categorias", "cantEjemplares"]