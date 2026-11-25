import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("Our team-building exercise was trust falls. HR caught no one. Accounting caught the invoice.")
