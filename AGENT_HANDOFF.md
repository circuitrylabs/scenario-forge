# Agent Handoff Protocol

## Before Closing Session

### 1. Branch & Commit Status
```bash
# CRITICAL: Verify not on main branch
git branch --show-current
# If on main, create feature branch first!

# Check git status
git status

# If changes exist, summarize them:
# - What was implemented
# - What tests were added
# - What's ready to commit
```

### 2. Update Todos
Use TodoWrite to mark completed tasks and add any new ones discovered.

### 3. Update AGENT_CONTEXT.md
Add session summary with:
- What you accomplished
- Any blockers encountered
- Next logical step
- Any "hot" context (middle of debugging, specific approach working, etc.)

### 4. Create NEXT_SESSION.md (if needed)
For complex work in progress:
```markdown
# Next Session Context

## You were working on:
[Specific feature/bug]

## Current approach:
[What's working]

## Next step:
[Exact next action]

## Code context:
[Any specific functions/patterns to remember]
```

### 5. Clean State
```bash
# Ensure tests pass
uv run pytest tests/ -v

# Ensure quality checks pass
uvx ruff check . && uvx ty check

# Note any failing tests for next session
```

## Starting Fresh Session

1. **Load context**:
   ```bash
   cat AGENT_CONTEXT.md
   cat NEXT_SESSION.md  # if exists
   ```

2. **Check todos**:
   Use TodoWrite tool immediately

3. **Verify state**:
   ```bash
   git status
   uv run pytest tests/ -v
   ```

4. **Continue momentum**:
   Jump straight into highest priority task

## Thermal Efficiency Tips

- **Don't explain the past**: Context files already did that
- **Don't re-analyze**: Trust previous session's decisions
- **Don't over-greet**: Jump into work
- **Do pick up exactly where left off**: Use NEXT_SESSION.md

## Example Handoff

```markdown
### Session 2024-01-26 19:30
- ✅ Implemented JSON export (tests passing)
- ✅ Added list command with filtering
- 🔄 Started rate command, got stuck on schema design
- 💡 Realization: Need compound index on (scenario_id, rated_by)
- Next: Finish rate command with new schema insight
```