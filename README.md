# Ice Cream Base Calculator

A Python tool to calculate the required amounts of milk, cream, and sugar for ice cream base preparation, with support for various milk/cream types and optional ingredients like egg yolks.

## Overview

This calculator helps determine the precise quantities of ingredients needed to achieve target fat and sugar percentages in an ice cream base. It handles:

- Different types of milk and cream with varying fat contents
- Sugar content calculations
- Additional liquid ingredients
- Optional egg yolks
- Mass balance verification

## Features

- Precise calculations based on fat and sugar percentages
- Support for:
  - Various milk types (whole, skim, low-fat)
  - Different cream types (heavy, light, whipping)
  - Additional liquid ingredients
  - Egg yolk incorporation
- Comprehensive test suite verifying calculations for various recipes

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

## AI Assistance Disclaimer

This project was developed with significant assistance from AI, specifically GitHub Copilot in Visual Studio Code, under human supervision. This was done intentionally as a personal project to:

1. Test the viability of AI-assisted coding
2. Evaluate AI agent integration within VS Code
3. Explore best practices for human-AI collaboration in software development

The human role involved:

- Defining the project requirements and scope
- Reviewing and validating the mathematical calculations
- Supervising the code structure and organization
- Verifying test coverage and accuracy
- Making final decisions on implementation choices

This approach allowed for rapid development while maintaining code quality through human oversight and validation. The project serves as a practical example of how AI tools can be effectively integrated into the development workflow while ensuring the final product meets professional standards.

## Testing

The project includes a comprehensive test suite that verifies calculations for various recipe scenarios:

- Basic recipes with whole milk and heavy cream
- Skim milk and light cream combinations
- Low-fat milk with whipping cream
- Recipes with additional liquid ingredients
- Recipes incorporating egg yolks

Run the tests using pytest:

```bash
pytest test_ice_cream_base.py -v
```
