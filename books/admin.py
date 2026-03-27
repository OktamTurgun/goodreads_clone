from django.contrib import admin
from .models import Author, Book, BookAuthor, UserBook, Review

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('name', 'email')
  search_fields = ('name', 'email')

class BookAuthorInline(admin.TabularInline):
  model = BookAuthor
  extra = 1
  

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  search_fields = ('title', 'isbn')
  list_display = ('title', 'isbn')
  list_filter = ('title', 'isbn', 'authors__name')
  inlines = [BookAuthorInline]

@admin.register(Review)
class RewiewAdmin(admin.ModelAdmin):
  list_display = ('user', 'book', 'rating', 'created_at')
  list_filter = ('rating',)
  search_fields = ('user__username', 'book__title')

@admin.register(UserBook)
class UserBookAdmin(admin.ModelAdmin):
  list_display = ('user', 'book', 'status', 'added_at')
  list_filter = ('status',)
  search_fields = ('user__username', 'book__title')
