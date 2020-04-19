# Pyomo but with decorators

I love pyomo but I find that writing models can require
more keystrokes than I care to give, particularly when defining
constraints, objectives and expressions.

This package saves some keystrokes by wrapping these bois
up with a decorator.

# Usage

Instead of writing something like 

```
def x_plus_y(m):
   return m.x + m.y

model.x_plus_y = Expression(
   rule=x_plus_y
)
```

you can write

```
@expression(model)
def x_plus_y(m):
   return m.x + m.y
```

The `@expression` decorator has the side-effect of creating
an `Expression` object with the wrapped function as a `rule`
and adding it to the model as an attribute named, in this case,
`x_plus_y__Expression`.

See `test/test_pyomo_decorators.py` for an example
