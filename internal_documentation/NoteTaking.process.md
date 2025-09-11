# Note-Taking Process for Exploratory Testing

A structured approach to documenting exploratory testing sessions that separates the recording of results from the actual testing activities.

## Document Structure

Create a session document named `TestSession.XX.md` where XX is incremented from the last session number.
This document should record a high level of what happened and what was found. The important parts of what was found should come first.
It should also include a tl;dr at the top.

## Two-Track Documentation

### Track 1: Testing Activities (What You're Doing)

Record your current testing approach and strategy:

#### Session Setup
```markdown
## Session Info
- **Date**: [Current date]
- **Tester**: [Your name]
- **Charter**: [What are you trying to break/explore?]
- **Time Box**: [Planned duration]
- **Target**: [URL/Application being tested]
```

#### Current Activity Log
```markdown
## Testing Activities

### [Timestamp] - [Activity Name]
**Approach**: [What testing technique you're using]
**Target**: [Specific area/feature being attacked]
**Strategy**: [How you're trying to break it]
**Status**: [In Progress/Completed/Paused]
```

### Track 2: Results Documentation (What You Found)

Record discoveries, bugs, and observations:

#### Findings Section
```markdown
## Findings

### Bug #[Number] - [Severity: Critical/High/Medium/Low]
**Title**: [Brief description]
**Steps to Reproduce**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Result**: [What should happen]
**Actual Result**: [What actually happened]
**Impact**: [How this affects users/business]
**Evidence**: [Screenshots, error messages, etc.]

---
```

#### Observations Section
```markdown
## Observations

### [Timestamp] - [Observation Category]
**What**: [What you noticed]
**Context**: [Where/when it occurred]
**Significance**: [Why this matters]
**Follow-up**: [Actions needed]
```

## Documentation Guidelines

### While Testing (Real-time)
- Keep activities log updated with current focus
- Immediately capture bugs when found
- Take screenshots of issues before they disappear
- Note anomalies even if you can't reproduce them yet

### Between Testing Bursts
- Review and organize findings
- Prioritize bugs by severity and impact
- Plan next attack vectors based on discoveries
- Update session charter if scope changes

### End of Session
- Summarize key findings
- List unfinished investigations for next session
- Rate session effectiveness
- Plan follow-up actions

## Template Sections

### Session Header
```markdown
# Test Session [Number] - [Date]

## Charter
**Mission**: [What you're trying to break]
**Scope**: [Areas included/excluded]
**Duration**: [Time allocated]
**Risk Areas**: [High-priority targets]
```

### Activity Tracking
```markdown
## Current Focus
- **Now Testing**: [Current activity]
- **Next**: [Planned next steps]
- **Blocked**: [Any impediments]
```

### Results Capture
```markdown
## Session Results

### Bugs Found: [Count]
### Observations: [Count]
### Areas Covered: [List]
### Areas Remaining: [List]

### Critical Issues
[List any show-stoppers]

### Recommendations
[Immediate actions needed]
```

## Best Practices

### Separation of Concerns
- **Activities**: Focus on methodology and approach
- **Results**: Focus on evidence and impact
- Keep them visually distinct in your document

### Real-time Capture
- Don't wait to document bugs - capture immediately
- Use timestamps to correlate activities with findings
- Screenshot everything suspicious

### Evidence Quality
- Include reproduction steps that others can follow
- Capture error messages exactly as displayed
- Note environmental factors (browser, device, etc.)

### Prioritization
- Mark critical issues that need immediate attention
- Distinguish between bugs and enhancement opportunities
- Note security implications clearly

## Session Flow

1. **Start**: Set up session document with charter and scope
2. **Test**: Update activities as you work, capture results immediately
3. **Pause**: Review findings, plan next attacks
4. **Continue**: Resume with updated focus based on discoveries
5. **End**: Summarize session, prioritize findings, plan follow-up
