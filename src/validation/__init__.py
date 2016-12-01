"""Common infrastructure classes for validation."""

import jsonschema


class Error(Exception):
    """Error raised by validation methods."""

    def __init__(self, reason):
        self._reason = reason

    def __str__(self):
        return self._reason


class Validator(object):
    """Base class for all validators."""

    SCHEMA = None

    def validate(self, raw):
        """Validate raw and produce a cleaned copy of it."""

        if self.SCHEMA is not None:
            try:
                jsonschema.validate(raw, self.SCHEMA)
            except jsonschema.ValidationError as e:
                raise Error('Could not structurally validate raw') from e

        return self._post_schema_validate(raw)

    def validate_against(self, raw, reference):
        """Validate raw against a reference object and produce a cleaned copy of it."""

        return self.validate(raw)

    def _post_schema_validate(self, raw):
        """Validate raw, assuming the schema is correct, and produce a cleand copy of it."""
        
        raise Exception('Not implemented')
