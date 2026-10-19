import pandas as pd
import numpy as np

def generate_data():
    """Generate sample mobile money agents and transactions."""
    np.random.seed(44)

    agents = pd.DataFrame({
        "agent_id": [101, 102, 103, 104],
        "agent_name": ["Mary", "John", "Peter", "Grace"],
        "county": ["Nairobi", "Kisumu", "Nakuru", "Nyeri"]
    })

    txns = pd.DataFrame({
        "txn_id": [1001, 1002, 1002, 1003, 1004],
        "agent_id": [101, 102, 102, 103, 105],
        "txn_type": [
            "Deposit", "Withdrawal", "Withdrawal",
            "Deposit", "Unknown"
        ],
        "amount": ["1,000", "500", "500", "bad", "2,000"],
        "txn_date": [
            "2026-10-01", "2026-10-02", "2026-10-02",
            "2026-10-03", "2026-10-04"
        ]
    })

    return txns, agents

if __name__ == "__main__":
    txns, agents = generate_data()
    print("Agents:", len(agents))
    print("Transactions:", len(txns))
