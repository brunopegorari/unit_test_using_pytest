from src.employee import Funcionario
from pytest import mark

class TestEmployee:

    @mark.age_calculation
    def test_when_receive_a_date_bigger_than_actual_year_must_return_a_message_Invalid_date(self):
        employee = Funcionario('Test Fulano', '01/01/2024', 10000)
        assert employee.idade() == 'Invalid date'
    
    @mark.age_calculation
    @mark.xfail
    def test_when_receive_a_date_different_format_return_22(self):
        employee = Funcionario('Test Fulano', '01-01-2000', 10000)
        assert employee.idade == 22
    
    @mark.return_last_name
    def test_when_receive_Test_Fulano_Tests_must_return_Tests(self):
        employee = Funcionario('Test Fulano Tests', '01/01/2000', 10000)
        assert employee.sobrenome() == 'Tests'
    
    @mark.return_last_name
    def test_when_receive_only_a_name_Test_must_return_a_message(self):
        employee = Funcionario('Test', '01/01/2000', 10000)
        assert employee.sobrenome() == "There isn't Last Name, please insert a Last Name!"
    
    @mark.bonus_calculation
    def test_when_receive_a_salary_equal_9999_99_must_return_999_99(self):
        employee = Funcionario('Test Fulano', '01/01/2000', 9999.90)
        assert employee.calcular_bonus() == 999.99
    
    @mark.bonus_calculation
    def test_when_receive_a_salary_equal_10001_must_return_0(self):
        employee = Funcionario('Test Fulano', '01/01/2000', 10001)
        assert employee.calcular_bonus() == 0

    @mark.bonus_calculation    
    def test_when_receive_salary_equal_10000_01_must_return_0(self):
        employee = Funcionario('Test Fulano', '01/01/2000', 10000.01)
        assert  employee.calcular_bonus() == 0
    
    @mark.bonus_calculation
    @mark.skip
    def test_when_receive_a_negative_salary_equal_negative_10000_must_return_0(self):
        employee = Funcionario('Test Fulano', '01/01/2000', -10000)
        assert employee.calcular_bonus() == 'Invalid salary, please insert a valid salary.'

    