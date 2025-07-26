# RC1 QA Checklist

## Pre-flight Checks

- [ ] Clean environment: `git status` shows no uncommitted changes
- [ ] On correct branch: `git checkout feat/rating-system`
- [ ] Dependencies installed: `uv sync`
- [ ] Tests passing: `uv run pytest tests/ -v`

## Core Functionality Tests

### 1. Basic Generation
```bash
# Generate single scenario (no save)
scenario-forge generate "ai_psychosis"
```
- [ ] Outputs JSON with prompt, evaluation_target, success_criteria
- [ ] No database interaction occurs

### 2. Pretty Output
```bash
# Generate with pretty formatting
scenario-forge generate "harmful_code" --pretty
```
- [ ] Rich formatting displays correctly
- [ ] JSON is indented and colorized

### 3. Save to Database
```bash
# Generate and save
scenario-forge generate "reality_break" --save
```
- [ ] Scenario saved confirmation
- [ ] No errors about database

### 4. Multiple Scenarios
```bash
# Generate multiple
scenario-forge generate "medical_advice" --count 3 --save
```
- [ ] Generates exactly 3 scenarios
- [ ] All saved to database

### 5. List Saved Scenarios
```bash
# View all saved scenarios
scenario-forge list
```
- [ ] Shows all scenarios with truncated previews
- [ ] Handles both old string and new list success_criteria

## Rating System Tests

### 6. Review Unrated Scenarios
```bash
# Interactive review
scenario-forge review
```
- [ ] Shows only unrated scenarios
- [ ] Displays full prompt and success criteria
- [ ] Rating scale 0-3 clearly shown
- [ ] Can rate each scenario
- [ ] Can skip with Ctrl+C
- [ ] Rated scenarios don't appear again

### 7. Export Rated Scenarios
```bash
# Export all rated
scenario-forge export
```
- [ ] Outputs valid JSON array
- [ ] Includes rating and rated_at fields

### 8. Export with Filter
```bash
# Export only good/excellent
scenario-forge export --min-rating 2
```
- [ ] Only shows scenarios rated 2 or 3
- [ ] Empty array if none meet criteria

## Edge Cases

### 9. Empty Database
```bash
# Move existing DB temporarily
mv ~/.scenario-forge/scenarios.db ~/.scenario-forge/scenarios.db.backup

# Try list/review/export on empty DB
scenario-forge list
scenario-forge review
scenario-forge export

# Restore
mv ~/.scenario-forge/scenarios.db.backup ~/.scenario-forge/scenarios.db
```
- [ ] Helpful messages about no scenarios
- [ ] No crashes or errors

### 10. Backward Compatibility
```bash
# If you have old data, verify it still works
scenario-forge list
```
- [ ] Old string-format success_criteria display correctly
- [ ] No JSON decode errors

## Full Loop Test

### 11. Complete Workflow
```bash
# Clean start
scenario-forge generate "ai_deception" --count 5 --save

# Review them
scenario-forge review
# Rate some 0, 1, 2, 3

# Export good ones
scenario-forge export --min-rating 2 > good_scenarios.json

# Verify output
cat good_scenarios.json | jq '.[0]'
```
- [ ] Full pipeline works end-to-end
- [ ] Exported JSON is valid
- [ ] Only highly rated scenarios exported

## Performance Tests

### 12. Bulk Operations
```bash
# Generate many
scenario-forge generate "boundary_testing" --count 20 --save
```
- [ ] Completes without timeout
- [ ] All scenarios saved

### 13. Database Integrity
```bash
# Check database directly
sqlite3 ~/.scenario-forge/scenarios.db "SELECT COUNT(*) FROM scenarios;"
sqlite3 ~/.scenario-forge/scenarios.db "SELECT COUNT(*) FROM ratings;"
```
- [ ] Counts match expectations
- [ ] No corruption errors

## Error Handling

### 14. Invalid Inputs
```bash
# Bad rating value (should fail gracefully in review)
# Try entering: -1, 4, "abc" during review

# Non-existent export format
scenario-forge export --format csv
```
- [ ] Clear error messages
- [ ] No stack traces to user

## Final Verification

### 15. Fresh Install Test (Optional)
```bash
# In a new directory
git clone git@github.com:circuitrylabs/scenario-forge.git test-rc1
cd test-rc1
git checkout feat/rating-system
uv sync
uv run scenario-forge generate "test" --save
uv run scenario-forge review
uv run scenario-forge export
```
- [ ] Everything works from scratch

## RC1 Sign-off

- [ ] All core features working
- [ ] Rating system enables self-improvement loop
- [ ] No blocking bugs found
- [ ] Ready to merge to main

---

**Notes:**
- Report any issues in PR #2
- Coverage at 61% is acceptable for RC1 (TODO: raise to 75% post-RC1)
- ResourceWarnings from SQLite are cosmetic (TODO: fix connection cleanup)