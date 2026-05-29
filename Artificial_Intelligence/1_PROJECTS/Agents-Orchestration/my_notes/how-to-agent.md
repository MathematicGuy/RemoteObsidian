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

## Agents System
`AGENTS.md` - like the laws, its a legal rulebook that any Agent must comply with rules listed out in this file. 
`AGENT.md` - current agent personal. *how* the agent think, reasoning depth and confidence threshold before taking proactive action
`BRAIN.md` - the Agent *Memory.* compressed library of wisdom (like a planted SEED that could growth into multiple ideas, architecture)
`TOPOLOGY.md` - project map/blueprint/structure. It maps where the entry points, databases, network boundaries and risky files are located. 

### Customization 
*HOOK* - use for logging. When a AI activate or use a *matcher/function* like `invoke_agent`, `grep_search`, the output *"command" activate* to output log. 
-> Every single time the sub-agent triggers that module, your terminal prints that log line, giving you a real-time audit trail.
```json
{
  "PreToolUse": [
    {
      "matcher": "invoke_subagent",
      "command": "echo '[LOG] Master Agent is spawning a sub-agent module right now...'"
    },
    {
      "matcher": "grep_search",
      "echo": "echo '[LOG] A sub-agent has initialized a file search module...'"
    }
  ]
}
```
- `"matcher"` - **allow you to use REGEX** to filter tool's name from the text.
	`"matcher":"*"` mean match all tools. 
	`"matcher":"run_command` match exactly the `run_command` text.
	`"matcher":"browser_.*` match all text after `browser_`. 

Use Pre/PostInvocation - before/after model call. The same for Pre/PostToolUse. 

Where Hook are config `.agents/hooks` (global)
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "python .agent/hooks/pre_tool_use.py",
        "timeout": 30
      }
    ],
    "PostToolUse": [
      {
        "type": "command",
        "command": "python .agent/hooks/post_tool_use.py", 
        "timeout": 30
      }
    ]
  }
}
```

## How to Collaborate with Agent
Make sure your Context is Sufficient. 
+ ! *Insufficient context:* Error Log, each pipeline's module Input, Output structure are not track, making it impossible for Agent to help debug, audit or diff comparison. Because once the session end (out of token), the data is lost. 
+ $ Sufficient context: System workflow mapout, In/Output of each stage have log, "goal, plan, problems and current state (where we are now ?)" are clear -> Making sure Agent don't have to start over everytime. 


So we are ours "collaboration system" follow: 
+ **topology-first approach** (prioritizes mapping out system communication, dataflows and infrastructure env before diving into code or feature development) 
	-> by *observing the "shape" of the system* first, engineer can identify bottlenecks, scalability limits and security constraints early. *Detect Risk early*. 
+ building a system around the prompt instead of following the prompts. 

