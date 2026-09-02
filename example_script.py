"""Run this script to check that your ACLS Python environment is working.

    python example_script.py
"""

import platform
import random
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BANNER = r"""
     _    ____ _     ____
    / \  / ___| |   / ___|
   / _ \| |   | |   \___ \
  / ___ \ |___| |___ ___) |
 /_/   \_\____|_____|____/

  environment check
"""

def check_python():
    version = sys.version_info
    ok = version >= (3, 10)
    print(f"Python {platform.python_version()} on {platform.system()} ... "
          f"{'ok' if ok else 'too old, please upgrade'}")
    return ok


def check_numbers():
    rng = np.random.default_rng(seed=42)
    dice_rolls = rng.integers(1, 7, size=10_000)
    average = dice_rolls.mean()
    print(f"Rolled 10,000 six-sided dice with numpy, average was {average:.3f} "
          f"(should be close to 3.5) ... {'ok' if abs(average - 3.5) < 0.1 else 'hmm'}")
    return dice_rolls


def check_dataframe(dice_rolls):
    counts = pd.Series(dice_rolls).value_counts().sort_index()
    print("Roll distribution (courtesy of pandas):")
    print(counts.to_string())
    return counts


def check_plot(counts):
    fig, ax = plt.subplots()
    ax.bar(counts.index, counts.values, color="teal")
    ax.set_xlabel("die face")
    ax.set_ylabel("count")
    ax.set_title("10,000 simulated dice rolls")
    output_path = "dice_rolls.png"
    fig.savefig(output_path)
    print(f"Saved a plot to {output_path} ... open it and see if it looks like a bar chart")


def fortune():
    messages = [
        "You will debug a tricky bug on the first try today.",
        "A semicolon you forgot in Python will haunt your R code tomorrow.",
        "Your next `git push` will not need a `--force`.",
        "Someone in your cohort will ask the exact question you were too shy to ask.",
        "Your environment.yml will solve on the first attempt, forever.",
    ]
    print(f"\nFortune cookie: {random.choice(messages)}")


def main():
    print(BANNER)
    python_ok = check_python()
    dice_rolls = check_numbers()
    counts = check_dataframe(dice_rolls)
    check_plot(counts)
    fortune()

    print("\nIf you can read this, your environment can run Python scripts,")
    print("use numpy and pandas, and produce plots with matplotlib.")
    print("Welcome to the ACLS master program!" if python_ok else
          "Please fix your Python version before continuing.")


if __name__ == "__main__":
    main()
