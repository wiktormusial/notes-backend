from django.views.generic import TemplateView

class SchemaView(TemplateView):
    template_name = "docs/swagger-ui.html"
    extra_context = {
        'schema_url': 'openapi-schema'
    }
