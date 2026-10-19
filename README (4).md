# Mobile Money Agent Network Data Clean-Up

## Project Summary
This project cleans mobile money agent transaction data by removing duplicate
transactions, standardizing transaction types, converting transaction amounts
and dates, flagging high-value outliers, and merging agent county information.

## Files
- `generate_data.py`: Generates sample agents and transactions.
- `cleaning_pipeline.py`: Contains the data-cleaning function.
- `agent_cleanup.ipynb`: Notebook for running and checking the pipeline.
- `outputs/agent_transactions_clean.csv`: Cleaned transaction data.
- `requirements.txt`: Required Python libraries.

## Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
