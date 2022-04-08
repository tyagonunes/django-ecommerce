from django.contrib import admin

from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
  model = Variacao
  extra = 1


class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'get_preco_formatado']
  inlines = [VariacaoInline]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)