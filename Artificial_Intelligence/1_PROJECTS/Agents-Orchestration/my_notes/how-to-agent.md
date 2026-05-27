**Project Context Prompts** 
```md
# Context
Current pipeline:
YOLOv11-Pose -> Feature Extraction -> GRU classifier

# Objective
Improve violent-action inference stability.

# Constraints
- Must run real-time
- CPU-only deployment
- Need low false positives

# Explore
Analyze:
- temporal smoothing
- confidence filtering
- motion heuristics
- sequence buffering
- hybrid rules + ML

# Execute
Generate:
1. architecture proposal
2. revised inference pipeline
3. pseudocode
4. experimental plan
```

## Agents Files
`AGENTS.md` - like the laws, its a legal rulebook that any Agent must comply with rules listed out in this file. 
`AGENT.md` - current agent personal. *how* the agent think, reasoning depth and confidence threshold before taking proactive action
`BRAIN.md` - the Agent *Memory.* compressed library of wisdom (like a planted SEED that could growth into multiple ideas, architecture)
`TOPOLOGY.md` - project map/blueprint/structure. It maps where the entry points, databases, network boundaries and risky files are located. 


## How to Collaborate with Agent
Make sure your Context is Sufficient. 
+ ! *Insufficient context:* Error Log, each pipeline's module Input, Output structure are not track, making it impossible for Agent to help debug, audit or diff comparison. Because once the session end (out of token), the data is lost. 
+ $ Sufficient context: System workflow mapout, In/Output of each stage have log, "goal, plan, problems and current state (where we are now ?)" are clear -> Making sure Agent don't have to start over everytime. 


So we are ours "collaboration system" follow: 
+ **topology-first approach** (prioritizes mapping out system communication, dataflows and infrastructure env before diving into code or feature development) 
	-> by *observing the "shape" of the system* first, engineer can identify bottlenecks, scalability limits and security constraints early. *Detect Risk early*. 
+ building a system around the prompt instead of following the prompts. 