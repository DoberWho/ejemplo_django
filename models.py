# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Cart(models.Model):
    id_producto = models.ForeignKey('ProductoVariante', models.DO_NOTHING, db_column='id_producto')
    amount = models.PositiveIntegerField(blank=True, null=True)
    id_user = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_user')
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Categoria(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria'


class MnCategoriaProducto(models.Model):
    id_producto = models.ForeignKey('Product', models.DO_NOTHING, db_column='id_producto')
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'mn_categoria_producto'


class MnProductTag(models.Model):
    id_product = models.ForeignKey('Product', models.DO_NOTHING, db_column='id_product', blank=True, null=True)
    id_tag = models.ForeignKey('Tag', models.DO_NOTHING, db_column='id_tag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mn_product_tag'


class Person(models.Model):
    lastname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'person'


class Product(models.Model):
    description = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    id_category = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_category')
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product'


class ProductoVariante(models.Model):
    id_producto = models.ForeignKey(Product, models.DO_NOTHING, db_column='id_producto')
    stock = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'producto_variante'


class Tag(models.Model):
    created = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tag'


class Usuario(models.Model):
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.
    edad = models.PositiveIntegerField()
    login = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'
