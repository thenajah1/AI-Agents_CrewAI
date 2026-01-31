from agents.crewai_agents import crew

def main():
    """
    Lance la Crew pour exécuter les tâches définies.
    """
    print("Starting CrewAI workflow...")
    result = crew.kickoff()
    print("\nFinal output:\n", result)

if __name__ == "__main__":
    main()
