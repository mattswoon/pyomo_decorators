from pyomo_decorators import __version__, expression

from pyomo.environ import *
from pyomo_decorators import *


def test_version():
    assert __version__ == '0.1.0'


def test_expression():
    model = AbstractModel()
    model.x = Var(within=NonNegativeReals)
    model.y = Var(within=NonNegativeReals)

    @expression(model)
    def x_plus_y(m):
        return m.x + m.y

    @constraint(model)
    def not_too_big(m):
        return m.x_plus_y__Expression <= 10

    @objective(model, sense=maximize)
    def obj(m):
        return m.x + 2 * m.y

    assert hasattr(model, 'x_plus_y__Expression')
    assert isinstance(model.x_plus_y__Expression, Expression)

    assert hasattr(model, 'not_too_big__Constraint')
    assert isinstance(model.not_too_big__Constraint, Constraint)

    assert hasattr(model, 'obj__Objective')
    assert isinstance(model.obj__Objective, Objective)

    # Quick check the model solves and we get the answer
    # I think we ought to get
    instance = model.create_instance()
    opt = SolverFactory('glpk')
    opt.solve(instance)
    assert instance.x.get_values()[None] == 0
    assert instance.y.get_values()[None] == 10
