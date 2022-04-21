#!/usr/bin/env python

"""Tests for `fake_dataset` package."""


from fake_dataset.columns import (FloatRandomColumn,
                                  IntegerRandomColumn,
                                  CategoricalRandomColumn,
                                  CategoricalProportionalColumn)

from fake_dataset.generators import DataGenerator
import numpy as np

class TestFloatColumns():

    def test_length(self):
        col = FloatRandomColumn()
        sample = col.sample(10)
        assert len(sample) == 10

    def test_range(self):
        min_value = -5.3
        max_value = 10.5
        col = FloatRandomColumn(values_range=(min_value, max_value))
        sample = col.sample(10)
        assert sample.max() <= max_value
        assert sample.min() > min_value

    def test_missing(self):
        min_value = 0.1
        max_value = 0.3
        col = FloatRandomColumn(missing_rate=(min_value, max_value))
        sample = col.sample(10)
        missing_rate = (np.isnan(sample).sum()/sample.shape[0])
        assert missing_rate <= max_value
        assert missing_rate >= min_value

class TestIntegerColumns():

    def test_length(self):
        col = IntegerRandomColumn()
        sample = col.sample(10)
        assert len(sample) == 10

    def test_range(self):
        min_value = -5
        max_value = 10
        col = IntegerRandomColumn(values_range=(min_value, max_value))
        sample = col.sample(10)
        assert sample.max() <= max_value
        assert sample.min() >= min_value

    def test_missing(self):
        min_value = 0.1
        max_value = 0.3
        col = IntegerRandomColumn(missing_rate=(min_value, max_value))
        sample = col.sample(10)
        missing_rate = ((sample == None).sum()/sample.shape[0])
        assert missing_rate <= max_value
        assert missing_rate >= min_value

class TestCategoricalColumns():

    def test_length(self):
        categories = ["car", "bus", "bicycle"]
        col = CategoricalRandomColumn(categories=categories)
        sample = col.sample(10)
        assert len(sample) == 10

    def test_range(self):
        categories = ["car", "bus", "bicycle"]
        col = CategoricalRandomColumn(categories=categories, missing_rate=(0, 0))
        sample = col.sample(10)
        assert "car" in sample
        assert "bus" in sample
        assert "bicycle" in sample

    def test_missing(self):
        categories = ["car", "bus", "bicycle"]
        min_value = 0.1
        max_value = 0.3
        col = CategoricalRandomColumn(
            categories=categories,
            missing_rate=(min_value, max_value),
            na_value="NA")
        sample = col.sample(10)
        missing_rate = ((sample == "NA").sum()/sample.shape[0])
        assert missing_rate <= max_value
        assert missing_rate >= min_value

class TestCategoricalProportionsColumns():

    def test_length(self):
        categories = ["car", "bus", "bicycle"]
        proportions = [0.5, 0.3, 0.2]
        col = CategoricalProportionalColumn(categories=categories, proportions=proportions)
        sample = col.sample(10)
        assert len(sample) == 10

    def test_proportions(self):
        categories = ["car", "bus", "bicycle"]
        proportions = [0.5, 0.3, 0.2]
        col = CategoricalProportionalColumn(categories=categories,
                                            proportions=proportions,
                                            missing_rate=(0, 0))
        sample = col.sample(10)
        assert (sample == "car").sum() == 5
        assert (sample == "bus").sum() == 3
        assert (sample == "bicycle").sum() == 2

    def test_range(self):
        categories = ["car", "bus", "bicycle"]
        col = CategoricalRandomColumn(categories=categories, missing_rate=(0, 0))
        sample = col.sample(10)
        assert "car" in sample
        assert "bus" in sample
        assert "bicycle" in sample

    def test_missing(self):
        categories = ["car", "bus", "bicycle"]
        min_value = 0.1
        max_value = 0.3
        col = CategoricalRandomColumn(
            categories=categories,
            missing_rate=(min_value, max_value),
            na_value="NA")
        sample = col.sample(10)
        missing_rate = ((sample == "NA").sum()/sample.shape[0])
        assert missing_rate <= max_value
        assert missing_rate >= min_value

class TestCategoricalProportionsColumns():

    def test_length(self):
        categories = ["car", "bus", "bicycle"]
        proportions = [0.5, 0.3, 0.2]
        col = CategoricalProportionalColumn(categories=categories, proportions=proportions)
        sample = col.sample(10)
        assert len(sample) == 10

    def test_values(self):
        categories = ["car", "bus", "bicycle"]
        proportions = [0.5, 0.3, 0.2]
        col = CategoricalProportionalColumn(categories=categories, proportions=proportions, missing_rate=(0, 0))
        sample = col.sample(10)
        assert ("car" in sample) and ("bus" in sample) and ("bicycle" in sample)

    def test_proportions(self):
        categories = ["car", "bus", "bicycle"]
        proportions = [0.5, 0.3, 0.2]
        col = CategoricalProportionalColumn(categories=categories,
                                            proportions=proportions,
                                            missing_rate=(0, 0))
        sample = col.sample(10)
        assert (sample == "car").sum() == 5
        assert (sample == "bus").sum() == 3
        assert (sample == "bicycle").sum() == 2

    def test_missing(self):
        categories = ["car", "bus", "bicycle"]
        proportions = [0.5, 0.3, 0.2]
        min_value = 0.1
        max_value = 0.3
        col = CategoricalProportionalColumn(
            categories=categories,
            proportions=proportions,
            missing_rate=(min_value, max_value),
            na_value="NA")
        sample = col.sample(10)
        missing_rate = ((sample == "NA").sum()/sample.shape[0])
        assert missing_rate <= max_value
        assert missing_rate >= min_value


