from django.forms import CheckboxInput as DjangoCheckboxInput


class CheckboxInput(DjangoCheckboxInput):

    def __init__(self, display_checkbox_label=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display_checkbox_label = display_checkbox_label

    def get_context(self, *args, **kwargs):

        context = super().get_context(*args, **kwargs)

        print("context", context)

        context['widget'].update({
            'display_checkbox_label': self.display_checkbox_label,
        })

        return context
