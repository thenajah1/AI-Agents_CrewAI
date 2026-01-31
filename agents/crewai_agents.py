# Import des bibliothèques nécessaires
from llama_cpp import Llama
from crewai import Agent, Task, Crew
import os

# Étape 1 : Charger le modèle local Mistral-7B Instruct
# Assurez-vous que le chemin vers le modèle est correct
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'mistral-7b-instruct.Q4_K_M.gguf')

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,
    n_gpu_layers=0
)

def local_llm(prompt: str) -> str:
    """
    Fonction simple qui envoie une invite au modèle local et retourne la réponse.
    """
    output = llm(prompt, max_tokens=500, stop=["</s>"])
    return output["choices"][0]["text"].strip()

# Étape 2 : Wrapper pour rendre local_llm compatible avec CrewAI
class LocalLLMWrapper:
    def __init__(self, engine):
        self.engine = engine

    def complete(self, prompt: str) -> str:
        """
        Méthode attendue par CrewAI pour générer une complétion à partir d'une invite.
        """
        return self.engine(prompt)

llm_wrapper = LocalLLMWrapper(local_llm)

# Étape 3 : Définir les agents avec rôle, objectif et backstory
researcher = Agent(
    role='Market Research Analyst',
    goal='Analyze competitors and summarize their marketing strategies',
    backstory='An expert in market intelligence and competitive analysis.',
    llm=llm_wrapper,
    allow_delegation=False
)

writer = Agent(
    role='Content Strategist',
    goal='Use research to create a compelling marketing strategy document',
    backstory='A seasoned content strategist with a flair for storytelling.',
    llm=llm_wrapper
)

# Étape 4 : Définir les tâches à accomplir par chaque agent
task1 = Task(
    description="List top 3 competitors and their marketing strategies based on current trends.",
    agent=researcher,
    expected_output="A summary of 3 competitors with key marketing strategies."
)

task2 = Task(
    description="Create a content marketing strategy based on the competitor summary.",
    agent=writer,
    expected_output="A structured document with our content strategy inspired by competitors.",
    depends_on=[task1]  # task2 dépend de la sortie de task1
)

# Étape 5 : Créer la Crew pour orchestrer les agents et les tâches
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True  # Affiche les étapes d'exécution en temps réel
)
