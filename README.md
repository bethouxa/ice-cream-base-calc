# Ice Cream Base Calculator

[build status](https://img.shields.io/github/actions/workflow/status/bethouxa/ice-cream-base-calc/python-package.yml?label=tests)

A Python tool to calculate the required amounts of milk, cream, and sugar for ice cream base preparation, with support for various milk/cream fat percentages (because I don't always stock whole milk and cream fat % aren't the same as in many recipes I could find) and optional ingredients like egg yolks or liquid flavorings like coffee.

This project was AI-assisted, see disclaimer below.

## Usage

```python
from ice_cream_base import ice_cream_base_calculator

# Example: Basic recipe calculation
result = ice_cream_base_calculator(
    M_total=1000,        # Total mass in grams
    fat_pct=12,          # Target fat percentage
    sugar_pct=20,        # Target sugar percentage
    milk_fat=3.5,        # Milk fat percentage
    cream_fat=30.0,      # Cream fat percentage
    milk_sugar=5.0,      # Milk sugar percentage
    cream_sugar=4.0      # Cream sugar percentage
)

# Result contains quantities for each ingredient in grams
print(result)
```

The script also has an interactive mode when ran as a script:

```bash
./ice_cream_base.py
```

## Testing

Run the tests using pytest:

```bash
pytest test_ice_cream_base.py -v
```

## AI Assistance Disclaimer

This project was mostly vibe coded (developed with significant assistance from an LLM agent) as a personal project to try out and test agent reliability and integration into VS Code.

The code is fully endorsed by me. An LLM is only a tool as any other and I am solely to blame if code I wrote using an LLM is inaccurate or erroneous, just as it would if I blindly trusted my IDE's autocomplete features.
