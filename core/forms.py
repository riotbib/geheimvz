from crispy_forms.layout import Field, Fieldset, LayoutObject
from crispy_forms.utils import TEMPLATE_PACK
from crispy_tailwind.tailwind import CSSContainer
from crispy_tailwind.templatetags.tailwind_field import CrispyTailwindFieldNode
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string


Field.template = "forms/layout/field.html"
Fieldset.template = "forms/layout/fieldset.html"

base_input = "block w-full px-1 leading-normal border appearance-none text-base-content bg-base-100 border-secondary-300 focus:outline-none"

default_styles = {
    "text": base_input,
    "number": base_input,
    "radioselect": "",
    "email": base_input,
    "url": base_input,
    "password": base_input,
    "hidden": "",
    "multiplehidden": "",
    "file": "",
    "clearablefile": "",
    "textarea": base_input,
    "date": base_input,
    "datetime": base_input,
    "time": base_input,
    "checkbox": "",
    "select": base_input,
    "nullbooleanselect": "",
    "selectmultiple": "",
    "checkboxselectmultiple": "",
    "multi": "",
    "splitdatetime": "text-gray-700 bg-white focus:outline border border-gray-300 leading-normal px-4 "
    "appearance-none rounded-lg py-2 focus:outline-none mr-2",
    "splithiddendatetime": "",
    "selectdate": "",
    "error_border": "border-red-500",
}

default_css_container = CSSContainer(default_styles)
CrispyTailwindFieldNode.default_container = default_css_container


class RightColumn(LayoutObject):
    template = "forms/layout/right-column.html"

    def __init__(self, *fields):
        self.fields = list(fields)

    def render(self, form, context, template_pack=TEMPLATE_PACK, **kwargs):
        fields = self.get_rendered_fields(form, context, template_pack, **kwargs)
        template = self.get_template_name(template_pack)
        return render_to_string(template, {"fields": fields})
