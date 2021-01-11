# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class CategoriesCategory(models.Model):
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'categories_category'




class PollsArticle(models.Model):
    headline = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'polls_article'


class PollsArticlePublications(models.Model):
    article = models.ForeignKey('PollsArticle', models.DO_NOTHING)
    publication = models.ForeignKey('PollsPublication', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_article_publications'
        unique_together = (('article', 'publication'),)


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsPublication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'polls_publication'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    denunciado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(CategoriesCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product'


class ProductTags(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    tag = models.ForeignKey('TagsTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_tags'
        unique_together = (('product', 'tag'),)


class TagsTag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tags_tag'
