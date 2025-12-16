from orchestrator.orchestrator import Orchestrator

if __name__ == "__main__":
    orchestrator = Orchestrator()
    result = orchestrator.run()

    print("✅ Orchestrator Output")
    print(result)
