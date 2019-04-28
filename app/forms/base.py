import abc
import cerberus
from cerberus import Validator


class BaseValidator(Validator):
    """ Custom implementation of the cerberus Validator class """

    def _validate_equal(self, equal, field, value):
        """ Validate the equation of one field to another """

        match_field, match_value = self._lookup_field(equal)
        if value != match_value:
            self._error(field, 'Does not match the {}'.format(match_field))


class FormException(Exception):
    """ Form exception class """

    def __init__(self, *args, **kwargs):
        """ Initialization class; Setting form exception parameters """

        self.field = kwargs.get('field', None)
        self.errors = kwargs.get('errors', None)

        if not self.field:
            raise NotImplementedError('You must set field key')

        if not self.errors:
            raise NotImplementedError('You must set errors key')

        super(Exception, self).__init__(self)


class BaseForm(abc.ABC):
    """ Base form-object class """

    errors = {}

    @property
    @abc.abstractmethod
    def schema(self):
        pass

    def __init__(self, **kwargs):
        """ Base class init method """

        if not self.schema:
            raise NotImplementedError('Subclasses must define schema property')

        self.validator = BaseValidator(self.schema)
        self.obj = kwargs.get('obj', None)
        self.params = kwargs.get('params', None)

    def is_valid(self):
        """ Return whether or not the receiving data are valid """

        try:
            result = self.validator.validate(self.params, self.schema)
            if not result:
                self.errors = self.validator.errors

            return result
        except cerberus.validator.DocumentError:
            self.errors['base'] = ['Invalid structure']
            return False
