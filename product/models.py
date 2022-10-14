from email.policy import default
from django.db import models
from stdimage.models import StdImageField
from django.utils.text import slugify

# Create your models here.

class Offer(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image = StdImageField('Imagem', upload_to='offer', variations={'thumb': {'width': 423, 'height': 681, 'crop': True }}) 
	title = models.CharField('Título', max_length=255)
	description = models.TextField('Descrição', max_length=300)
	discount = models.IntegerField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Oferta'
		verbose_name_plural = 'Ofertas'    	


class Category(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image = StdImageField('Imagem', upload_to='category', variations={'thumb': {'width': 250, 'height': 250, 'crop': True }}) 
	title = models.CharField('Título', max_length=255)
	 
	def __str__(self):
		return self.title 

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'	


class Product(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria') 
	title = models.CharField('Título', max_length=255)
	subtitle =  models.CharField('Subtítulo', max_length=255)
	description = models.TextField('Descrição do produto', )
	slug = models.SlugField(max_length=255, unique=True, null=True, blank=True,)
	price = models.IntegerField('Preço', )
	image1 = StdImageField('01. Imagem', default='exemple.png', upload_to='product', variations={'thumb': {'width': 460, 'height': 597, 'crop': True }}) 
	image2 = StdImageField('02. Imagem', default='exemple.png', upload_to='product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 597, 'crop': True }})
	image3 = StdImageField('03. Imagem', default='exemple.png', upload_to='product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 557, 'crop': True }})
	image4 = StdImageField('04. Imagem', default='exemple.png', upload_to='product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 597, 'crop': True }})
	image5 = StdImageField('05. Imagem', default='exemple.png', upload_to='product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 597, 'crop': True }})
	stock = models.IntegerField(default=1) 
	# Featuring  

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'

	def save(self, *args, **kwargs):
		value = f'{self.title}, {self.subtitle}, {self.id}' 
		self.slug = slugify(value, allow_unicode=False)
		super().save(*args, **kwargs)


