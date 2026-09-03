"""Run every analysis stage in order and regenerate all tables and figures."""
from __future__ import annotations

import runpy
import sys
import time

STAGES = [
    ("A0  audit of the submitted manuscript's own tables", "run_a0_published_audit"),
    ("A1  identifiability of the eight-cluster partition", "run_a1_identifiability"),
    ("A2  circularity, depth artefact, metric sensitivity", "run_a2_circularity"),
    ("A3  declustering, Omori-Utsu decay, rate change", "run_a3_triggering"),
    ("A4  frequency-magnitude analysis", "run_a4_fmd"),
    ("A5  focal mechanisms and Kagan angles", "run_a5_focal"),
    ("A6  supported spatial structure and method benchmark", "run_a6_structure"),
    ("A7  migration with time held out of the clustering", "run_a7_migration"),
    ("A9  study-boundary sensitivity", "run_a9_boundary"),
    ("A8  figures", "run_a8_figures"),
]

if __name__ == "__main__":
    sys.path.insert(0, "reanalysis")
    for title, mod in STAGES:
        print("\n" + "=" * 72 + f"\n{title}\n" + "=" * 72)
        t0 = time.time()
        runpy.run_module(mod, run_name="__main__")
        print(f"[{time.time() - t0:.1f} s]")
    print("\nAll stages complete.")
