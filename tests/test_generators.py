from fake_dataset import columns, generators
import numpy as np

class TestCategoricalProportionsColumns():

    def test_shape(self):
        data_gen = generators.DataGenerator(
            vehicle=columns.CategoricalRandomColumn(categories=["car", "bus", "bicycle"], missing_rate=(0.2, 0.5), na_value="NA"),
            year=columns.IntegerRandomColumn(values_range=(1950, 2010), missing_rate=(0.1, 0.2)),
            value=columns.FloatRandomColumn(values_range=(10e4, 10e5), missing_rate=(0.0, 0.0)),
        )
        sample = data_gen.sample(10)
        assert sample.shape[0] == 10
        assert sample.shape[1] == 3

    def test_columns(self):
        data_gen = generators.DataGenerator(
            vehicle=columns.CategoricalRandomColumn(categories=["car", "bus", "bicycle"], missing_rate=(0.2, 0.5), na_value="NA"),
            year=columns.IntegerRandomColumn(values_range=(1950, 2010), missing_rate=(0.1, 0.2)),
            value=columns.FloatRandomColumn(values_range=(10e4, 10e5), missing_rate=(0.0, 0.0)),
        )
        sample = data_gen.sample(10)
        assert "vehicle" in sample.columns
        assert "year" in sample.columns
        assert "value" in sample.columns

