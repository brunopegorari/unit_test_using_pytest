from pytest import fixture
from src.employee import Funcionario

@fixture
def creating_employee():
    return Funcionario('Test Fulano', '01/01/2000', 10000)