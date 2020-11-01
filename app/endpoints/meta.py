from rest_framework.metadata import BaseMetadata


class EndpointMetaData(BaseMetadata):

    def determine_metadata(self, request, view):
        return {
            'name': view.get_view_name(),
            'description': view.get_view_description(),
            'required fields': view.request_obj.required,
            'optional fields': view.request_obj.optional,
            'DTO response': self.fields(view.model) if view.model else {},
        }

    def fields(self, model):
        fields_dict = {}
        fields = model._meta.fields
        for f in fields:
            if f.name in model.DTO._fields:
                fields_dict[f.name] = {
                    'type': f.get_internal_type(),
                    'max_length': f.max_length,
                    'verbose_name': f.verbose_name,
                    'request_name': f.name
                }
        return fields_dict
