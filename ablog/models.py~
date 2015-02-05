from django.db import models
from django.core.urlresolvers import reverse
class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)
	def __str__(self):
		return self.slug
class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	tags = models.ManyToManyField(Tag)
	objects = EntryQuerySet.as_manager()
	def __str__(self):
		return self.body
	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"slug": self.slug})
		""" kwargs : The keyword arguments that would be passed to the view function, as parsed from the URL.
		#If you need to use something similar to the url template tag in your code, Django provides the 	 			following function:

		#reverse(viewname[, urlconf=None, args=None, kwargs=None, current_app=None])[source]
"""
		"""#viewname can be a string containing the Python path to the view object, a URL pattern name, or the 		callable view object. For example, given the following url:"""
	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]
