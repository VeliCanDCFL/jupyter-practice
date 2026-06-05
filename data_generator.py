import json
import random
from datetime import datetime, timedelta

def generate_raw_scada_logs(output_file: str = "raw_scada_logs.json", num_rows: int = 10_000, null_rate: float = 0.05):
    """Generate fake but realistic factory SCADA telemetry data with ~5% null injection."""
    machines = [f"CNC-{i:02d}" for i in range(1, 6)]
    statuses = ["OK", "WARN", "ERR-01"]
    status_weights = [0.85, 0.10, 0.05]

    base_time = datetime(2026, 6, 1, 0, 0, 0)
    records = []

    for i in range(num_rows):
        ts = base_time + timedelta(seconds=random.randint(0, 30 * 24 * 3600))
        machine_id = random.choice(machines)
        status_code = random.choices(statuses, weights=status_weights, k=1)[0]

        # Simulate realistic ranges
        vibration_mm_s = round(random.gauss(4.5, 1.2), 4)
        spindle_temp = round(random.gauss(72.0, 8.0), 2)

        # Inject nulls into ~5% of vibration and temperature fields
        if random.random() < null_rate:
            vibration_mm_s = None
        if random.random() < null_rate:
            spindle_temp = None

        records.append({
            "timestamp": int(ts.timestamp()),
            "machine_id": machine_id,
            "vibration_mm_s": vibration_mm_s,
            "spindle_temp": spindle_temp,
            "status_code": status_code,
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)

    print(f"Generated {len(records)} rows -> {output_file}")

    # Quick stats
    vib_nulls = sum(1 for r in records if r["vibration_mm_s"] is None)
    temp_nulls = sum(1 for r in records if r["spindle_temp"] is None)
    print(f"  vibration nulls: {vib_nulls} ({vib_nulls/len(records)*100:.1f}%)")
    print(f"  spindle_temp nulls: {temp_nulls} ({temp_nulls/len(records)*100:.1f}%)")

if __name__ == "__main__":
    generate_raw_scada_logs()
