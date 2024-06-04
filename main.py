
import ai_benchmark
from loguru import logger
import sys

def main():
    benchmark = ai_benchmark.AIBenchmark()
    logger.info("Start running the ai_benchmark")
    results = benchmark.run_training(precision="high")
    logger.info("Finished running the ai_benchmark with results: {results}", results=results)
    sys.exit(0)




if __name__ == "__main__":
    # execute only if run as a script
    main()
