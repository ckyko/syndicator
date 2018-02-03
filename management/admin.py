from django.contrib import admin
from .models import Product, ProductType


class SimpleObjectModelAdmin(admin.ModelAdmin):
    readonly_fields = ('object_id', 'date_created', 'date_modified', 'created_by', 'modified_by')

    list_display = ('name', 'description', 'created_by', 'modified_by')
    list_filter = ('date_created', 'date_modified', 'created_by', 'modified_by')

    search_fields = [
        'name',
        'description',
    ]

    fieldsets = [
        ('Management Record', {
            'fields': [
                'object_id',
                'date_created',
                'date_modified',
                'created_by',
                'modified_by',
            ]
        }),
        ('Details', {
            'fields': [
                'name',
                'description',
            ]
        }),
    ]


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('object_id', 'date_created', 'date_modified', 'created_by', 'modified_by')

    list_display = ('name', 'active', 'is_posted_to_other', 'date_created', 'date_modified', 'created_by',
                    'modified_by')
    list_filter = ('active', 'is_posted_to_other', 'date_created', 'date_modified', 'created_by', 'modified_by',)

    search_fields = [
        'name',
    ]

    fieldsets = [
        ('Management Record', {
            'classes': ('collapse',),
            'fields': [
                'object_id',
                ('date_created', 'created_by'),
                ('date_modified', 'modified_by'),
            ]
        }),
        ('Product Details', {
            'fields': [
                'active',
                'is_posted_to_other',
                'name',
                'type',
                'description',
                'price',
                ('start_time', 'end_time'),
            ]
        }),
    ]


admin.site.register(ProductType, SimpleObjectModelAdmin)
admin.site.register(Product, ProductAdmin)
