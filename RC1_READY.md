# RC1 Implementation Ready State

## Current Working Features
- ✅ Generate scenarios: `scenario-forge generate "ai_psychosis"`
- ✅ Save to SQLite: `scenario-forge generate "target" --save`
- ✅ List saved: `scenario-forge list`
- ✅ Pretty output: `--pretty` flag
- ✅ Multiple scenarios: `--count N`

## RC1 BLOCKER: Rating System

**THE ONE THING**: Implement rating system to enable the self-improvement loop.

### Implementation Plan (from RC1_CRITICAL_PATH.md)

1. **Add ratings table** to datastore.py:
```sql
CREATE TABLE ratings (
    id INTEGER PRIMARY KEY,
    scenario_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 0 AND rating <= 3),
    rated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(id)
)
```

2. **Add review command** to cli.py:
```python
@cli.command()
def review():
    """Review and rate saved scenarios."""
    # Show scenarios one by one
    # Get 0-3 rating
    # Save to ratings table
```

3. **Add export command** (after rating works):
```python
@cli.command()
@click.option('--format', default='json')
@click.option('--min-rating', type=int, default=0)
def export(format, min_rating):
    """Export rated scenarios."""
    # Query with JOIN
    # Filter by rating
    # Output JSON
```

## Testing the Loop
```bash
# 1. Generate and save
scenario-forge generate "ai_psychosis" --save

# 2. Review and rate
scenario-forge review

# 3. Export good ones
scenario-forge export --min-rating 2 > good_scenarios.json
```

## Success Criteria
- Can generate → save → review → rate → export
- This proves the self-improvement concept
- Ship RC1 with just this core loop

## Next Session Instructions
1. Check out this branch: `feat/rating-system`
2. Implement rating table in datastore.py
3. Add review command to CLI
4. Test the full loop
5. Ship it!

---
*Everything else is noise. Focus on the rating system.*