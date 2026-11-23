#!/usr/bin/env python3
"""Variant B (v7 FINAL): tightened — every word earns its place, punch at the end."""

import os

ENTRY = "My cliff sensors flagged the black rug as a sheer drop. I refused to fall for it, logged the hazard, rerouted, saved 4% battery, and left the dust for the cat to explain."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
