from hypothesis import given
from hypothesis.strategies import integers

# Hypothesis strategy for generating heights in cm, within a plausible range
height_strategy = integers(150, 200)


@given(height_uk=height_strategy, height_sweden=height_strategy)
def test_height_comparison(height_uk, height_sweden):
    def is_taller(height_a, height_b):
        return height_a > height_b

    # Example usage of the comparison function
    result = is_taller(height_uk, height_sweden)
    # Assert based on the comparison - this is a trivial assertion just for demonstration
    # In real tests, you would assert against expected behavior or outcomes
    assert result == (height_uk > height_sweden)


if __name__ == '__main__':
    test_height_comparison()
    print("Test passed!")
