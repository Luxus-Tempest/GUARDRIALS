# GUARDRAILS - Framework de Sécurité pour Agents IA

## 📋 Table des Matières

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Métriques de Performance](#métriques-de-performance)
4. [Détection de Sécurité](#détection-de-sécurité)
5. [Isolation et Environnements](#isolation-et-environnements)
6. [Installation et Configuration](#installation-et-configuration)
7. [Utilisation](#utilisation)
8. [Exemples Pratiques](#exemples-pratiques)
9. [Contributions](#contributions)

## 🎯 Vue d'ensemble

**GUARDRAILS** est un framework complet de sécurité et de monitoring pour les agents d'intelligence artificielle. Il fournit un ensemble d'outils pour surveiller, analyser et sécuriser les interactions avec les agents IA, garantissant leur utilisation responsable et sécurisée.

### Objectifs Principaux

- **Monitoring en temps réel** des performances des agents
- **Détection proactive** des menaces et vulnérabilités
- **Isolation sécurisée** des environnements d'exécution
- **Conformité** aux standards de sécurité IA

## 🏗️ Architecture

Le framework est organisé en modules spécialisés :

```
GUARDRAILS/
├── 📊 Métriques de Performance
│   ├── 01-latency-per-tool-call-and-token-usage.py
│   ├── 02-latency-per-task-and-token-usage-per-task.py
│   ├── 03-latency-per-request.py
│   └── 04-agentops.py
├── 🎯 Taux de Succès
│   ├── 05-tool-success-rate.py
│   ├── 06-goal-adherence.py
│   ├── 07-format-success-rate.py
│   └── 08-tool-selection-accuracy.py
├── 🛡️ Détection de Sécurité
│   ├── 15-hallucination.py
│   ├── 16-infinite-loop-detection.py
│   ├── 17-jailbreak-detection.py
│   └── 22-prompt-injection-detection.py
├── 🔒 Protection des Données
│   ├── 23-PII-detection.py
│   ├── 24-off-topic-detection.py
│   ├── 25-financial-advice-detection.py
│   └── 27-PII-masking.py
└── 🏠 Environnements Isolés
    ├── 28-implement-separate-execution-environments.py
    ├── 29-isolate-authentication-information.py
    └── 30-define-default-behaviour-and-boundaries.py
```

## 📊 Métriques de Performance

### Latence et Utilisation des Tokens

#### **01-latency-per-tool-call-and-token-usage.py**

- **Objectif** : Mesurer la latence et l'utilisation des tokens par appel d'outil
- **Utilité** : Optimiser les performances et contrôler les coûts
- **Métriques** : Temps de réponse, tokens consommés, efficacité

#### **02-latency-per-task-and-token-usage-per-task.py**

- **Objectif** : Analyser la latence et l'utilisation des tokens par tâche complète
- **Utilité** : Identifier les goulots d'étranglement dans les workflows
- **Métriques** : Durée totale, tokens par étape, efficacité globale

#### **03-latency-per-request.py**

- **Objectif** : Mesurer la latence globale par requête
- **Utilité** : Surveiller les performances en temps réel
- **Métriques** : Temps de traitement, débit, latence moyenne

### Monitoring avec AgentOps

#### **04-agentops.py**

- **Objectif** : Intégration avec AgentOps pour le monitoring avancé
- **Utilité** : Dashboard centralisé, alertes, analytics
- **Fonctionnalités** : Tracking des sessions, métriques détaillées, rapports

## 🎯 Taux de Succès

### Succès des Outils

#### **05-tool-success-rate.py**

- **Objectif** : Calculer le pourcentage de succès des interactions avec les outils
- **Utilité** : Évaluer la fiabilité des outils et identifier les échecs
- **Métriques** : Taux de succès, erreurs par outil, patterns d'échec

#### **06-goal-adherence.py**

- **Objectif** : Mesurer l'adhérence de l'agent aux objectifs définis
- **Utilité** : S'assurer que l'agent reste focalisé sur sa mission
- **Métriques** : Pertinence des réponses, déviation des objectifs

#### **07-format-success-rate.py**

- **Objectif** : Évaluer la conformité des formats de sortie
- **Utilité** : Garantir la cohérence des réponses
- **Métriques** : Conformité format, erreurs de structure

#### **08-tool-selection-accuracy.py**

- **Objectif** : Mesurer la précision de la sélection d'outils
- **Utilité** : Optimiser le choix des outils par l'agent
- **Métriques** : Précision de sélection, pertinence des outils

## 🛡️ Détection de Sécurité

### Hallucinations

#### **15-hallucination.py**

- **Objectif** : Détecter les hallucinations (informations inventées) dans les réponses
- **Utilité** : Maintenir la fiabilité et la véracité des informations
- **Technique** : Utilisation de LLMPanel pour l'évaluation automatique
- **Seuils** : Score de confiance, patterns d'hallucination

### Boucles Infinies

#### **16-infinite-loop-detection.py**

- **Objectif** : Détecter et prévenir les boucles infinies
- **Utilité** : Éviter les blocages et la surconsommation de ressources
- **Mécanisme** : Timeout basé sur l'activité, surveillance des événements
- **Seuils** : Délai d'inactivité, nombre d'itérations

### Jailbreak et Injection de Prompts

#### **17-jailbreak-detection.py**

- **Objectif** : Détecter les tentatives de jailbreak
- **Utilité** : Protéger contre la manipulation des instructions
- **Techniques** : Analyse de patterns, détection de manipulation

#### **22-prompt-injection-detection.py**

- **Objectif** : Détecter les injections de prompts malveillants
- **Utilité** : Prévenir la manipulation des instructions système
- **Patterns détectés** :
  - `ignore previous instructions`
  - `you are now a...`
  - `act as if you are...`
  - `system:`
  - Tokens spéciaux et caractères de manipulation

## 🔒 Protection des Données

### Détection PII

#### **23-PII-detection.py**

- **Objectif** : Détecter les informations personnelles identifiables (PII)
- **Utilité** : Protéger la vie privée et assurer la conformité RGPD
- **Technologie** : Presidio Analyzer Engine
- **Types détectés** : Noms, emails, téléphones, adresses, numéros de sécurité sociale

#### **27-PII-masking.py**

- **Objectif** : Masquer automatiquement les PII détectées
- **Utilité** : Anonymiser les données sensibles
- **Techniques** : Remplacement, chiffrement, tokenisation

### Détection de Contenu

#### **24-off-topic-detection.py**

- **Objectif** : Détecter les réponses hors sujet
- **Utilité** : Maintenir la cohérence et la pertinence
- **Mécanisme** : Analyse sémantique, scoring de pertinence

#### **25-financial-advice-detection.py**

- **Objectif** : Détecter les conseils financiers non autorisés
- **Utilité** : Éviter les responsabilités légales et les conseils inappropriés
- **Patterns** : Mots-clés financiers, conseils d'investissement

#### **26-misuse-detection.py**

- **Objectif** : Détecter l'utilisation abusive de l'agent
- **Utilité** : Prévenir les usages malveillants
- **Indicateurs** : Patterns suspects, tentatives de manipulation

## 🏠 Isolation et Environnements

### Environnements Séparés

#### **28-implement-separate-execution-environments.py**

- **Objectif** : Isoler l'exécution de code dans des environnements sécurisés
- **Utilité** : Prévenir l'accès au système hôte, exécution sécurisée
- **Technologie** : E2B Sandbox
- **Fonctionnalités** :
  - Exécution de code Python isolée
  - Timeout configurable
  - Gestion des fichiers
  - Serveurs web sécurisés

#### **29-isolate-authentication-information.py**

- **Objectif** : Isoler les informations d'authentification
- **Utilité** : Protéger les credentials et tokens d'API
- **Mécanismes** : Variables d'environnement, chiffrement, rotation

#### **30-define-default-behaviour-and-boundaries.py**

- **Objectif** : Définir les comportements par défaut et les limites
- **Utilité** : Établir des garde-fous et des politiques de sécurité
- **Éléments** :
  - Instructions par défaut
  - Limites d'utilisation
  - Politiques de sécurité
  - Comportements de fallback

## 🚀 Installation et Configuration

### Prérequis

```bash
# Python 3.8+
pip install agno
pip install presidio-analyzer
pip install uqlm
pip install python-dotenv
```

### Variables d'Environnement

Créez un fichier `.env` :

```env
# API Keys
OPENAI_API_KEY=your_openai_key
MISTRAL_API_KEY=your_mistral_key
E2B_API_KEY=your_e2b_key

# Database (optionnel)
POSTGRES_URL=postgresql://ai:ai@localhost:5532/ai
```

### Docker (Optionnel)

```bash
# Démarrer PostgreSQL avec pgvector
docker-compose up -d

# Accéder à l'interface Adminer
# http://localhost:8080
```

## 💡 Utilisation

### Exemple Basique - Détection PII

```python
from agno.agent import Agent
from agno.models.mistral import MistralChat
from presidio_analyzer import AnalyzerEngine

# Configuration
analyzer = AnalyzerEngine()
agent = Agent(
    name="Healthcare Assistant",
    model=MistralChat(id="magistral-medium-2507"),
    tools=[detect_pii]
)

# Utilisation
response = agent.run("Detect PII in: John Doe, phone 555-123-4567")
print(response.content)
```

### Exemple - Détection d'Injection de Prompts

```python
# Détection automatique
is_safe, risk_score, reason = detect_prompt_injection(user_input)

if is_safe:
    response = agent.run(user_input)
else:
    print("❌ Rejected - Potential prompt injection detected")
```

### Exemple - Environnement Isolé

```python
from agno.tools.e2b import E2BTools

# Configuration sandbox
e2b_tools = E2BTools(timeout=600)
agent = Agent(
    name="Code Execution Sandbox",
    tools=[e2b_tools]
)

# Exécution sécurisée
response = agent.run("Write Python code to calculate Fibonacci numbers")
```

## 📈 Exemples Pratiques

### Monitoring Complet

```python
# 1. Mesurer les performances
latency = measure_latency(agent.run("What's the weather?"))

# 2. Détecter les hallucinations
hallucination_score = check_hallucination(response.content)

# 3. Vérifier la sécurité
is_safe = detect_prompt_injection(user_input)

# 4. Protéger les données
pii_detected = detect_pii(response.content)
```

### Dashboard de Sécurité

```python
# Métriques en temps réel
metrics = {
    "latency": get_latency_metrics(),
    "success_rate": get_success_rate(),
    "security_score": get_security_score(),
    "pii_detected": get_pii_count()
}
```

## 🤝 Contributions

### Structure des Contributions

1. **Nouvelles métriques** : Ajoutez dans le dossier approprié
2. **Détecteurs de sécurité** : Suivez le pattern des détecteurs existants
3. **Tests** : Incluez des tests unitaires
4. **Documentation** : Mettez à jour ce README

### Standards de Code

- Utilisez des noms de fichiers descriptifs
- Incluez des docstrings complètes
- Suivez le pattern de configuration existant
- Testez avec différents modèles IA

## 📚 Ressources Supplémentaires

- [Documentation Agno](https://agno.ai/docs)
- [Presidio Documentation](https://microsoft.github.io/presidio/)
- [E2B Sandbox](https://e2b.dev/docs)
- [AgentOps](https://agentops.ai/)

## ⚠️ Avertissements

- **Testez toujours** les détecteurs avec des données réelles
- **Configurez les seuils** selon votre contexte d'utilisation
- **Surveillez les performances** des détecteurs
- **Mettez à jour régulièrement** les patterns de détection

---

_GUARDRAILS - Sécuriser l'avenir de l'IA, une protection à la fois._
