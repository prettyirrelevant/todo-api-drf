from rest_framework.compat import INDENT_SEPARATORS, LONG_SEPARATORS, SHORT_SEPARATORS
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return b""

        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)

        if indent is None:
            separators = SHORT_SEPARATORS if self.compact else LONG_SEPARATORS
        else:
            separators = INDENT_SEPARATORS

        new_data = {}
        if renderer_context.get("response").status_code > 299:
            new_data["status"] = "error"
            new_data["message"] = data.get("detail") or data

        else:
            new_data["status"] = "success"

            # if response object contains `data` attribute
            if hasattr(data, "data") or data:
                new_data["data"] = data.get("data") or data

            # if response object contains `message`
            if hasattr(data, "message"):
                new_data["message"] = data["message"]

        new_data["status_code"] = renderer_context.get("response").status_code
        ret = json.dumps(
            new_data,
            cls=self.encoder_class,
            indent=indent,
            ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict,
            separators=separators,
        )

        ret = ret.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
        return ret.encode()
