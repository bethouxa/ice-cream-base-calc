from ice_cream_base import ice_cream_base_calculator, YOLK_FAT_PERCENTAGE

import pytest

# Test cases as fixtures
@pytest.fixture
def basic_recipe():
    return {
        "M_total": 1000, "fat_pct": 12, "sugar_pct": 20,
        "milk_fat": 3.25,  # whole milk
        "cream_fat": 36.0,  # heavy cream
        "milk_sugar": 4.8,  # whole milk lactose
        "cream_sugar": 3.0  # heavy cream lactose
    }

@pytest.fixture
def skim_milk_recipe():
    return {
        "M_total": 500, "fat_pct": 15, "sugar_pct": 18,
        "milk_fat": 0.1,   # skim milk
        "cream_fat": 20.0,  # light cream
        "milk_sugar": 5.0,  # skim milk lactose
        "cream_sugar": 4.0  # light cream lactose
    }

@pytest.fixture
def low_fat_recipe():
    return {
        "M_total": 2000, "fat_pct": 10, "sugar_pct": 22,
        "milk_fat": 1.0,   # low-fat milk
        "cream_fat": 30.0,  # whipping cream
        "milk_sugar": 4.9,  # low-fat milk lactose
        "cream_sugar": 3.5  # whipping cream lactose
    }

@pytest.fixture
def extra_liquid_recipe():
    return {
        "M_total": 1000, "fat_pct": 12, "sugar_pct": 20,
        "milk_fat": 3.25,  # whole milk
        "cream_fat": 36.0,  # heavy cream
        "milk_sugar": 4.8,  # whole milk lactose
        "cream_sugar": 3.0, # heavy cream lactose
        "extra_liquid_mass": 100
    }

@pytest.fixture
def egg_yolk_recipe():
    return {
        "M_total": 1000, "fat_pct": 12, "sugar_pct": 20,
        "milk_fat": 2.0,   # 2% milk
        "cream_fat": 25.0,  # medium cream
        "milk_sugar": 4.85, # 2% milk lactose
        "cream_sugar": 3.8, # medium cream lactose
        "num_yolks": 4
    }

class TestIceCreamCalculator:
    def _verify_recipe(self, recipe_name, recipe):
        """Helper method to verify all aspects of a recipe calculation"""
        result = ice_cream_base_calculator(**recipe)
        
        # Check fat percentage
        total_fat = (
            result["milk (g)"] * recipe["milk_fat"] / 100 +  # milk fat
            result["cream (g)"] * recipe["cream_fat"] / 100 +  # cream fat
            result["egg yolks (g)"] * YOLK_FAT_PERCENTAGE / 100  # yolk fat
        )
        actual_fat_pct = (total_fat / recipe["M_total"]) * 100
        fat_diff = abs(actual_fat_pct - recipe["fat_pct"])
        assert fat_diff <= 0.1, \
            f"{recipe_name}: Fat percentage off by {fat_diff} percentage points"

        # Check sugar percentage
        total_sugar = (
            result["milk (g)"] * recipe["milk_sugar"] / 100 +  # milk sugar
            result["cream (g)"] * recipe["cream_sugar"] / 100 +  # cream sugar
            result["added sugar (g)"]  # added sugar
        )
        actual_sugar_pct = (total_sugar / recipe["M_total"]) * 100
        sugar_diff = abs(actual_sugar_pct - recipe["sugar_pct"])
        assert sugar_diff <= 0.1, \
            f"{recipe_name}: Sugar percentage off by {sugar_diff} percentage points"

        # Check total mass
        total_mass = sum([
            result["milk (g)"],
            result["cream (g)"],
            result["added sugar (g)"],
            result["extra liquid (g)"],
            result["egg yolks (g)"]
        ])
        mass_diff = abs(total_mass - recipe["M_total"])
        assert mass_diff <= 0.1, \
            f"{recipe_name}: Total mass off by {mass_diff}g"

    def test_basic_whole_milk_heavy_cream_recipe(self, basic_recipe):
        """Test basic recipe using whole milk and heavy cream"""
        self._verify_recipe("Basic recipe", basic_recipe)

    def test_skim_milk_light_cream_recipe(self, skim_milk_recipe):
        """Test recipe using skim milk and light cream"""
        self._verify_recipe("Skim milk recipe", skim_milk_recipe)

    def test_low_fat_whipping_cream_recipe(self, low_fat_recipe):
        """Test recipe using low-fat milk and whipping cream"""
        self._verify_recipe("Low-fat recipe", low_fat_recipe)

    def test_recipe_with_extra_liquid(self, extra_liquid_recipe):
        """Test recipe with additional liquid ingredients"""
        self._verify_recipe("Extra liquid recipe", extra_liquid_recipe)

    def test_recipe_with_egg_yolks(self, egg_yolk_recipe):
        """Test recipe including egg yolks"""
        self._verify_recipe("Egg yolk recipe", egg_yolk_recipe)
