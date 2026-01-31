# AI-Agents_CrewAI : Construction d’agents IA collaboratifs avec CrewAI et modèles locaux en Python

Ce projet vise à développer un système multi-agents intelligent utilisant le framework CrewAI pour orchestrer plusieurs agents IA spécialisés, chacun doté d’un rôle, d’un objectif et d’une mémoire propre. Les agents collaborent pour accomplir des tâches complexes en plusieurs étapes, comme l’analyse de marché et la création de stratégies marketing.

L’originalité du projet réside dans l’utilisation d’un modèle de langage local open source puissant (Mistral-7B Instruct) via la bibliothèque llama-cpp-python, permettant un fonctionnement entièrement hors ligne, sans dépendance à des API externes payantes. Le projet est développé en Python et structuré pour faciliter l’extension, la maintenance et l’intégration dans des workflows plus larges.

Objectifs : 
Créer des agents IA spécialisés avec des rôles et objectifs clairs.
Orchestrer la collaboration entre agents via CrewAI.
Utiliser un modèle de langage local open source pour garantir confidentialité, contrôle et coût nul.
Définir des tâches dépendantes pour simuler des workflows réalistes.
Fournir une base modulaire et évolutive pour des applications IA collaboratives.
Technologies utilisées
- Python 3.11+
- CrewAI : framework d’orchestration multi-agents
- llama-cpp-python : interface Python pour modèles LLM locaux (Mistral-7B Instruct)
- Mistral-7B Instruct : modèle de langage open source quantifié au format GGUF
- Huggingface Hub : pour le téléchargement des modèles
- Visual Studio Build Tools & CMake : outils nécessaires à la compilation des dépendances natives sous Windows

Cas d’usage
- Analyse collaborative de données complexes
- Automatisation de stratégies marketing multi-étapes
- Prototypage rapide de systèmes IA multi-agents hors ligne
- Recherche et développement en intelligence artificielle décentralisée
