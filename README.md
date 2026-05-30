# Overview  

# 1. Tic-Tac-Toe AI  

Algorithms  
Minimax  
Alpha-Beta Pruning  
Heuristic Alpha-Beta  
Monte-Carlo Tree Search (MCTS)  

## Board Representation  

X = Maximizing Player  
O = Minimizing Player  
. = Empty Cell  

## Test Case  

Initial Board  

X | X | .  
O | O | .  
. | . | .  

Expected Move  

2  

## Expected Output  

Minimax Move: 2  
AlphaBeta Move: 2  
Heuristic AlphaBeta Move: 2  
MCTS Move: 2  

# 2. AI-Based Travel Planner using Ontology  
# Tools  
Protégé  
Python  
Owlready2  
VS Code  

## Ontology Structure  
## Classes  
Destination  
Activity  
Hotel    
Interest    
## Destinations    
Goa    
Manali  
Jaipur    
## Activities  
ScubaDiving  
BeachVisit  
Trekking  
FortTour  
## Interests  
Adventure  
Nature  
History  
## Relationships  
Goa → ScubaDiving  
Goa → BeachVisit    
Manali → Trekking    
Jaipur → FortTour    
ScubaDiving → Adventure    
Trekking → Adventure    
BeachVisit → Nature    
FortTour → History    

## Test Case  

Input  

Interest = Adventure  

Output  

## Recommended Destinations:  

Goa  
 - ScubaDiving  

Manali  
 - Trekking  

# 3. Knowledge Graphs (KG)  

A Knowledge Graph represents entities and relationships.  

Example  
Goa  
 ├── hasActivity → ScubaDiving  
 ├── hasActivity → BeachVisit  
 └── hasHotel → SeaViewResort  

# 4. Bayesian Networks (BN)  

A Bayesian Network is a probabilistic graphical model represented as a Directed Acyclic Graph (DAG).  

Example  
Rain  
 ├── Traffic  
 └── Accident    
   
## Sample Code    
from pgmpy.models import BayesianNetwork  
model = BayesianNetwork([  
    ('Rain', 'Traffic'),  
    ('Rain', 'Accident')  
])  
