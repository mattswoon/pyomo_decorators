__version__ = '0.1.0'

from pyomo.environ import Expression, Constraint, Objective


def decorator_factory(component):
    """Creates decorators that can be used to make components that
    require a `rule` function"""

    def component_decorator(model, *args, **kwargs):
        def decorator(func):
            """Has a side effect of adding a component to `model`"""

            setattr(
                model,
                f'{func.__name__}__{component.__name__}',
                component(
                    *args,
                    **kwargs,
                    rule=func
                )
            )
            return func
        return decorator
    return component_decorator

expression = decorator_factory(Expression)
constraint = decorator_factory(Constraint)
objective = decorator_factory(Objective)

__all__ = ['expression', 'constraint', 'objective']
