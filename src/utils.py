# utils.py

def print_metrics(metrics: dict):
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")