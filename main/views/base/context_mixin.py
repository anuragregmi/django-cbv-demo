class ContextMixin:
    """
    A default context mixin that passes the keyword arguments received by
    get_context_data() as the template context.
    """
    extra_context = None

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self  # pass instance of view in context
        if self.extra_context is not None:
            kwargs.update(self.extra_context)  # add extra context in context if defined
        return kwargs
