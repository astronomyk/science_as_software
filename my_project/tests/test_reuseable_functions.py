from my_project.reusable_functions import make_dataset


def test_make_dataset_returns_tuple_of_x_y():
    data = make_dataset(100)
    assert isinstance(data, tuple)


def test_make_dataset_returns_100_numbers_for_n_equals_100():
    x, y = make_dataset(100)
    assert len(x) == 100 and len(y) == 100