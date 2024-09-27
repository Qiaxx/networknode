from django.contrib import admin


from django.contrib import admin
from networknode.models import NetworkNode, Product

# Admin Action для очистки задолженности перед поставщиком
@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0.00)

# Регистрация NetworkNode в админке
@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке объектов
    list_display = ('name', 'city', 'supplier', 'debt_to_supplier', 'created_at')

    # Фильтрация по городу
    list_filter = ('city',)

    # Действия
    actions = [clear_debt]

# Регистрация Product в админке
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
