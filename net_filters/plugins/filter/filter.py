from net_templates.filters import NetFilters
from net_templates.filters import namespace_decorator


class FilterModule(object):

    def filters(self):
        return {k.split('.')[-1]: v for k, v in NetFilters().filters().items()}
