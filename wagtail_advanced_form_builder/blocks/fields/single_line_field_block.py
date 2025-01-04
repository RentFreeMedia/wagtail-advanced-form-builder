from .base_field_block import BaseFieldBlock


class SingleLineFieldBlock(BaseFieldBlock):

    html = None

    choices = None

    empty_label = None

    display_side_by_side = None

    display_checkbox_label = None

    class Meta:

        form_classname = 'waf--field form-control'
        icon = 'extraicons--basic-field'
