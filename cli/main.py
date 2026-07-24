import argparse
from packages.core import DataLake, ReasoningEngine
from packages.utils.logging import Logger
from packages.services.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description='Reasoning Engine CLI')
    parser.add_argument('--data', required=True, help='Path to data file')
    parser.add_argument('--target', required=True, help='Path to target file')
    args = parser.parse_args()
    data = pd.read_csv(args.data)
    target = pd.read_csv(args.target)
    data_lake = DataLake(data)
    data_lake.target = target
    orchestrator = Orchestrator(data_lake)
    orchestrator.run()

def cli_entry_point():
    main()