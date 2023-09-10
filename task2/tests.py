import asyncio
from solution import main, ans_for_csv

asyncio.run(main())

true_values_for_letter = {"Й": 4, "А": 1225}

for key, value in true_values_for_letter:
    assert ans_for_csv[key] == value
