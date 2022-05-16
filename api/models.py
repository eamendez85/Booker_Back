from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.



#Usuarios

class Grados(models.Model):
    id_grado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'grados'


class Grupos(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    letra_grupo = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'grupos'


class Estudiantes(models.Model):
    id_estudiante = models.AutoField(primary_key=True, unique=True)
    doc_estudiante = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='doc' )
    tipodoc = models.CharField(max_length=5, blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    id_grupo = models.ForeignKey('Grupos', models.DO_NOTHING, db_column='id_grupo', blank=True, null=True)
    id_grado = models.ForeignKey('Grados', models.DO_NOTHING, db_column='id_grado', blank=True, null=True)

    class Meta:
        db_table = 'estudiantes'

class Bibliotecarios(models.Model):
    id_bibliotecario = models.AutoField(primary_key=True, unique=True)
    doc_bibliotecario = models.ForeignKey('Usuario', models.CASCADE, db_column='doc')
    tipodoc = models.CharField(max_length=5, blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'bibliotecarios'


class UsuarioManager(BaseUserManager):
    def create_user(self, email, doc, name,password=None):
        if not doc:
            raise ValueError('El usuario debe tener un numero de documento')

        user = self.model(
            doc = doc,
            email = self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, doc, name, password):
        user = self.create_user(
            email,
            doc = doc,
            name=name,
            password=password,
        )
        user.usuario_administrador = True
        user.save()
        return user
        
        

class Usuario(AbstractBaseUser):
    doc = models.CharField('Numero de documento', unique=True, max_length=20, primary_key=True)
    name = models.CharField('Nombre de usuario', max_length=50, blank=True, null=True)
    email = models.CharField('Email',max_length=60, blank=True, null=True)
    imagen = models.ImageField('Imagen del perfil', upload_to='perfil/', max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default = True)
    tipo_usuario = models.CharField('Tipo usuario', max_length=1)
    #[A, B, E]
    objects = UsuarioManager()
    USERNAME_FIELD = 'doc'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return f'{self.name},  doc: {self.doc}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.tipo_usuario == 'A' or self.tipo_usuario == 'B'




#Libros

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'categorias'
        


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'autores'
    

class Editoriales(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'editoriales'

    def __str__(self):
        return self.nombre

    


class Idiomas(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'idiomas'

    def __str__(self):
        return self.nombre



class Libros(models.Model):
    id_libro = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20)
    imagen_libro = models.ImageField('Imagen del libro', upload_to='images/libros/', max_length=200, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    id_editorial = models.ForeignKey(Editoriales, models.DO_NOTHING, db_column='id_editorial', blank=True, null=True)
    edicion = models.CharField(max_length=50, blank=True, null=True)
    autores = models.ManyToManyField(Autores)
    id_idioma = models.ForeignKey(Idiomas, models.DO_NOTHING, db_column='id_idioma', blank=True, null=True)
    categorias = models.ManyToManyField(Categorias)
    descripcion = models.TextField(blank=True, null=True)
    numero_paginas = models.IntegerField(blank=True, null=True)
    numero_capitulos = models.IntegerField(blank=True, null=True)
    presentacion = models.CharField(max_length=30, blank=True, null=True)
    anexos = models.CharField(max_length=200, blank=True, null=True)
    palabras_clave = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=3, blank=True, null=True)


    class Meta:
        db_table = 'libros'


class Favoritos(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante')
    libros = models.ManyToManyField(Libros)

    class Meta:
        db_table = 'favoritos'


class Ejemplares(models.Model):
    id_ejemplar = models.AutoField(primary_key=True)
    num_ejemplar = models.CharField(max_length=3, blank=True, null=True)
    estado = models.CharField(max_length=3, blank=True, null=True)
    id_libro = models.ForeignKey('Libros', models.DO_NOTHING, db_column='id_libro')

    class Meta:
        db_table = 'ejemplares'



#Infracciones

class TipoInfraccion(models.Model):
    id_tipo_infraccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'tipo_infraccion'


class Infracciones(models.Model):
    id_infraccion = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)
    ejemplares = models.ManyToManyField(Ejemplares)
    id_tipo_infraccion = models.ForeignKey('TipoInfraccion', models.DO_NOTHING, db_column='id_tipo_infraccion', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=3, blank=True, null=True)
    id_administrador = models.ForeignKey(Bibliotecarios, models.DO_NOTHING, db_column='id_administrador', blank=True, null=True)

    class Meta:
        db_table = 'infracciones'



#Prestamos

class DePrestamos(models.Model):
    id_de_prestamo = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='id_estudiante')
    ejemplares = models.ManyToManyField(Ejemplares)
    fec_prestamo = models.DateTimeField()
    fec_devolucion = models.DateTimeField()
    estado = models.CharField(max_length=3)
    id_administrador = models.ForeignKey(Bibliotecarios, models.DO_NOTHING, db_column='id_administrador')

    class Meta:
        db_table = 'de_prestamos'


class Prestados(models.Model):
    id_prestado = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)
    id_ejemplar = models.ForeignKey(Ejemplares, models.DO_NOTHING, db_column='id_ejemplar')
    estado = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'prestados'



#Reservas

class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante')
    ejemplares = models.ManyToManyField(Ejemplares)
    estado = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'reservas'

"""class Eventos(models.Model):
    id_evento = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)"""
