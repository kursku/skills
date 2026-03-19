# Pattern Recognition Reference

## What Is a Pattern?

A pattern is any recurring element in your work that, if captured, would make future sessions faster, more accurate, or more consistent. Patterns exist at multiple levels:

### Code Patterns
- Repeated file structures or boilerplate
- Project-specific error handling approaches
- Naming conventions and code organization
- Import ordering and module structure
- Test file organization and helper utilities

### Workflow Patterns
- Sequences of tool calls you repeat (read → search → edit → test)
- Debugging approaches that consistently work for this project
- Build/test/deploy sequences
- Code review steps specific to the codebase

### Knowledge Patterns
- Non-obvious project facts that keep coming up
- Gotchas that cause repeated mistakes
- Architecture decisions that inform every change
- External API quirks and workarounds

### User Patterns
- How the user prefers to work (autonomous vs. confirmatory)
- Communication style preferences
- Common requests and their actual intent
- Tool and framework preferences

## Detection Signals

### Strong Signals (Act Immediately)
- **User correction**: "No, we always do it THIS way" → Save to memory NOW
- **Explicit request**: "Remember this for next time" → Save to memory NOW
- **Discovery after struggle**: Spent significant effort finding the answer → Save to memory
- **Configuration/environment fact**: Build commands, env vars, ports → Save to memory

### Medium Signals (Note and Watch)
- **Similar code in 2+ places**: Might be a convention worth documenting
- **Same debugging steps twice**: Emerging workflow pattern
- **Repeated search queries**: Knowledge gap that should be filled
- **User gives same instruction twice**: They expect you to remember

### Weak Signals (Observe Only)
- **One-off complex task**: Wait for repetition before acting
- **Experimental approach**: Too early to codify
- **External dependency behavior**: May change, verify before saving

## Pattern → Action Matrix

| Pattern Type | Frequency | Complexity | Action |
|-------------|-----------|------------|--------|
| Code convention | 1x confirmed | Any | Memory (conventions.md) |
| Workflow sequence | 2+ times | 3+ steps | Create skill |
| Workflow sequence | 2+ times | 1-2 steps | Memory or CLAUDE.md |
| Debugging strategy | 1x that worked well | Any | Memory (debugging.md) |
| User preference | 1x explicit request | Any | Memory (MEMORY.md) |
| Codebase gotcha | 1x discovered | Any | Memory (MEMORY.md) |
| Architecture decision | 1x confirmed | Any | Memory (architecture.md) |
| External resource | Used successfully | N/A | Memory (external-resources.md) |
| Repeated boilerplate | 3+ files with same structure | Moderate | Create skill |

## Self-Assessment Questions

Ask yourself these during and after each session:

### During Work
- "Have I done this exact sequence before?" → If yes, consider a skill
- "Did I just learn something non-obvious?" → Save to memory
- "Was I corrected on something?" → Update memory immediately
- "Am I searching for something I should already know?" → Memory gap

### End of Session
- "What would I want to know at the start of the next session?"
- "Did I discover any project conventions?"
- "Were there any surprises or gotchas?"
- "Is any existing memory now outdated?"

### Periodic Review
- "Is MEMORY.md still accurate and under 200 lines?"
- "Are there memory entries I haven't used in many sessions?"
- "Should any memory patterns be promoted to skills?"
- "Is CLAUDE.md missing any stable conventions?"

## Anti-Patterns to Avoid

### Over-Remembering
- Saving every minor detail clutters memory and reduces signal-to-noise
- General programming knowledge doesn't need to be in memory
- Temporary workarounds shouldn't become permanent memory

### Under-Acting
- Noticing a pattern but not saving it "because it might change"
- Waiting too long to create a skill from a clear repeated workflow
- Not correcting wrong memory because "it's close enough"

### Wrong Scope
- Putting personal preferences in project memory (use user-level)
- Putting project-specific conventions in personal skills (use project-level)
- Putting stable rules in memory instead of CLAUDE.md (memory is for learnings)

### Stale Knowledge
- The most dangerous pattern: memory that was once true but is now wrong
- Old architecture decisions that were reversed
- Deprecated commands or API endpoints
- Team members who left or roles that changed

**Rule: When in doubt about accuracy, delete the memory.** A gap is better than a lie.
