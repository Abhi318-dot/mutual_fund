"""
Master execution script
"""

import os

scripts = [
    "etl_pipeline.py",
    "eda_analysis.py",
    "performance_analysis.py",
    "advanced_analytics.py"
]

for script in scripts:
    print(f"Running {script}")
    os.system(f"python {script}")

print("Pipeline completed successfully")