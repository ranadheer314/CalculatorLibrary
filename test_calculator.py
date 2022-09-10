import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(Self):
        assert 2 == calculator.subtract(4, 2)
