from django.contrib import admin
from easypage.models import QuickLink, Carousel, Featurette


class ThreeInstanceAdminMixin(object):
    """Hides the "Add" button when there is already an instance."""
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 3:
            return False
        return super(ThreeInstanceAdminMixin, self).has_add_permission(request)

class FiveInstanceAdminMixin(object):
    """Hides the "Add" button when there is already an instance."""
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 5:
            return False
        return super(FiveInstanceAdminMixin, self).has_add_permission(request)

# Register your models here.
class QuickLinkAdmin(ThreeInstanceAdminMixin, admin.ModelAdmin):
    model = QuickLink

class CarouselAdmin(FiveInstanceAdminMixin, admin.ModelAdmin):
    model = Carousel

class FeaturetteAdmin(ThreeInstanceAdminMixin, admin.ModelAdmin):
    model = Featurette

admin.site.register(QuickLink, QuickLinkAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Featurette, FeaturetteAdmin)
