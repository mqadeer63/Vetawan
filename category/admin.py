from django.contrib import admin
from .models import Category,Subcategory
from store.models import Product
# Register your models here.

class SubCategoryInline(admin.StackedInline):
    prepopulated_fields = {'slug': ('subcategory_name',)}
    model = Subcategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

    def apply_discount5(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 5
                product.save()
        self.message_user(request, f"Discount of 5% applied to {queryset.count()} categories and their products.")
    apply_discount5.short_description = "Apply Discount of 5 percent"

    def apply_discount10(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 10
                product.save()
        self.message_user(request, f"Discount of 10% applied to {queryset.count()} categories and their products.")

    apply_discount10.short_description = "Apply Discount of 10 percent"

    def apply_discount20(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 20
                product.save()
        self.message_user(request, f"Discount of 20% applied to {queryset.count()} categories and their products.")
    apply_discount20.short_description = "Apply Discount of 20 percent"

    def apply_discount30(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 30
                product.save()
        self.message_user(request, f"Discount of 30% applied to {queryset.count()} categories and their products.")
    apply_discount30.short_description = "Apply Discount of 30 percent"

    def apply_discount40(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 40
                product.save()
        self.message_user(request, f"Discount of 40% applied to {queryset.count()} categories and their products.")
    apply_discount40.short_description = "Apply Discount of 40 percent"

    def apply_discount50(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 50
                product.save()
        self.message_user(request, f"Discount of 50% applied to {queryset.count()} categories and their products.")
    apply_discount50.short_description = "Apply Discount of 50 percent"

    def apply_discount60(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 60
                product.save()
        self.message_user(request, f"Discount of 60% applied to {queryset.count()} categories and their products.")
    apply_discount60.short_description = "Apply Discount of 60 percent"

    def apply_discount70(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 70
                product.save()
        self.message_user(request, f"Discount of 70% applied to {queryset.count()} categories and their products.")
    apply_discount70.short_description = "Apply Discount of 70 percent"

    def apply_discount80(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 80
                product.save()
        self.message_user(request, f"Discount of 80% applied to {queryset.count()} categories and their products.")

    apply_discount80.short_description = "Apply Discount of 80 percent"

    def apply_discount90(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 90
                product.save()
        self.message_user(request, f"Discount of 90% applied to {queryset.count()} categories and their products.")

    apply_discount90.short_description = "Apply Discount of 90 percent"

    def apply_discount15(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 15
                product.save()
        self.message_user(request, f"Discount of 15% applied to {queryset.count()} categories and their products.")

    apply_discount15.short_description = "Apply Discount of 15 percent"

    def apply_discount25(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 25
                product.save()
        self.message_user(request, f"Discount of 25% applied to {queryset.count()} categories and their products.")

    apply_discount25.short_description = "Apply Discount of 25 percent"

    def apply_discount35(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 35
                product.save()
        self.message_user(request, f"Discount of 35% applied to {queryset.count()} categories and their products.")

    apply_discount35.short_description = "Apply Discount of 35 percent"

    def apply_discount45(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 45
                product.save()
        self.message_user(request, f"Discount of 45% applied to {queryset.count()} categories and their products.")

    apply_discount45.short_description = "Apply Discount of 45 percent"

    def apply_discount55(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 55  # apply a 10% discount
                product.save()
        self.message_user(request, f"Discount of 55% applied to {queryset.count()} categories and their products.")

    apply_discount55.short_description = "Apply Discount of 55 percent"

    def apply_discount65(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 65  # apply a 10% discount
                product.save()
        self.message_user(request, f"Discount of 65% applied to {queryset.count()} categories and their products.")

    apply_discount65.short_description = "Apply Discount of 65 percent"

    def apply_discount75(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 75  # apply a 10% discount
                product.save()
        self.message_user(request, f"Discount of 75% applied to {queryset.count()} categories and their products.")

    apply_discount75.short_description = "Apply Discount of 75 percent"

    def apply_discount85(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 85  # apply a 10% discount
                product.save()
        self.message_user(request, f"Discount of 85% applied to {queryset.count()} categories and their products.")

    apply_discount85.short_description = "Apply Discount of 85 percent"

    def apply_discount95(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 95  # apply a 10% discount
                product.save()
        self.message_user(request, f"Discount of 95% applied to {queryset.count()} categories and their products.")

    apply_discount95.short_description = "Apply Discount of 95 percent"

    def remove_discount(self, request, queryset):
        for category in queryset:
            products = Product.objects.filter(category=category)
            for product in products:
                product.discount_price = 0  # apply a 10% discount
                product.save()
        self.message_user(request, f"Discount Removed from {queryset.count()} categories and their products.")
    remove_discount.short_description = "Remove Discount"

    actions = ['apply_discount5', 'apply_discount10', 'apply_discount15', 'apply_discount20', 'apply_discount25',
               'apply_discount30', 'apply_discount35', 'apply_discount40', 'apply_discount45',
               'apply_discount50', 'apply_discount55', 'apply_discount60', 'apply_discount65',
               'apply_discount70', 'apply_discount75', 'apply_discount80', 'apply_discount85',
               'apply_discount90', 'apply_discount95', 'remove_discount']


admin.site.register(Category, CategoryAdmin)
