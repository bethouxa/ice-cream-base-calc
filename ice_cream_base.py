from scipy.optimize import fsolve

# Constants
YOLK_FAT_PERCENTAGE = 27.0  # Fat percentage in egg yolks


def ice_cream_base_calculator(
    M_total, fat_pct=12, sugar_pct=20,
    milk_fat=3.5, cream_fat=30.0,
    milk_sugar=5.0, cream_sugar=4.0,
    extra_liquid_mass=0.0,
    num_yolks=0, yolk_mass=18.0, yolk_fat=YOLK_FAT_PERCENTAGE
):
    """
    Calculates required mass of milk, cream, and added sugar
    to achieve target fat and sugar percentages in ice cream base,
    accounting for extra liquids and optional egg yolks.

    Parameters:
    - M_total: total mass of ice cream base (grams)
    - fat_pct: desired fat percentage (e.g., 12 for 12%)
    - sugar_pct: desired sugar percentage (e.g., 15 for 15%)
    - milk_fat, cream_fat: fat % in milk and cream
    - milk_sugar, cream_sugar: sugar % in milk and cream
    - extra_liquid_mass: mass of other liquid ingredients (e.g., coffee)
    - num_yolks: number of egg yolks
    - yolk_mass: mass per yolk (default 18g)
    - yolk_fat: fat % in yolk (default 27%)

    Returns:
    - Dictionary with masses of milk, cream, added sugar,
      extra liquid, and egg yolks
    """

    total_yolk_mass = num_yolks * yolk_mass
    total_yolk_fat = total_yolk_mass * yolk_fat / 100

    def equations(vars):
        m_milk, m_cream, m_sugar = vars
        return [
            (m_milk + m_cream + m_sugar + extra_liquid_mass + total_yolk_mass - M_total),
            (m_milk * milk_fat / 100) + (m_cream * cream_fat / 100) + total_yolk_fat - (M_total * fat_pct / 100),
            (m_milk * milk_sugar / 100) + (m_cream * cream_sugar / 100) + m_sugar - (M_total * sugar_pct / 100),
        ]

    available_mass = M_total - extra_liquid_mass - total_yolk_mass
    guess = [available_mass / 3, available_mass / 3, available_mass / 3]

    solution = fsolve(equations, guess)
    m_milk, m_cream, m_sugar = solution

    return {
        "milk (g)": round(m_milk, 2),
        "cream (g)": round(m_cream, 2),
        "added sugar (g)": round(m_sugar, 2),
        "extra liquid (g)": round(extra_liquid_mass, 2),
        "egg yolks (g)": round(total_yolk_mass, 2),
        "egg yolks (count)": num_yolks
    }


def input_retry(prompt: str, cast_type: type, default):
    while True:
        try:
            val = input(prompt).strip() or default
            return cast_type(val)
        except (ValueError, TypeError):
            pass


if __name__ == "__main__":
    print("Ice Cream Base Calculator")
    print("-----------------------")

    # Get required inputs
    M_total = input_retry("Enter total mass of ice cream base (in grams):", int, None)

    # Get optional inputs with defaults
    fat_pct = input_retry("Enter desired fat percentage (default 12%): ", int, 12)
    sugar_pct = input_retry("Enter desired sugar percentage (default 20%): ", int, 20)

    # Get milk and cream composition
    milk_fat = input_retry("Enter milk fat percentage (default 3.5%): ", float, 3.5)
    cream_fat = input_retry("Enter cream fat percentage (default 30.0%): ", float, 30.0)
    milk_sugar = input_retry("Enter milk sugar percentage (default 5.0%): ", float, 5.0)
    cream_sugar = input_retry("Enter cream sugar percentage (default 4.0%): ", float, 4.0)

    # Ask about extra ingredients
    extra_liquid_mass = input_retry("Enter mass of extra liquid in grams (default 0): ", float, 0)

    # Ask about egg yolks
    num_yolks = input_retry("Enter number of egg yolks (default 0): ", int, 0)

    # Calculate and display results
    result = ice_cream_base_calculator(
        M_total=M_total,
        fat_pct=fat_pct,
        sugar_pct=sugar_pct,
        milk_fat=milk_fat,
        cream_fat=cream_fat,
        milk_sugar=milk_sugar,
        cream_sugar=cream_sugar,
        extra_liquid_mass=extra_liquid_mass,
        num_yolks=num_yolks
    )

    print("\nRecipe Results:")
    print("--------------")
    for ingredient, amount in result.items():
        print(f"{ingredient}: {amount}")
