# SLIME - Adam Goucher Process

A prioritization heuristic for determining what to test first when schedule is short and you need to focus on the most important areas.

## Overview

SLIME helps testers prioritize testing efforts by focusing on five critical dimensions that typically yield the highest-impact bugs and risks. Originally shared by Adam Goucher at CAST 2008.

## Dimensions

### S - Security
The first priority when testing under time constraints.
- Investigate authentication and authorization mechanisms
- Test input validation and sanitization
- Examine data exposure and access controls
- Verify encryption and secure communication

### L - Languages (Internationalization)
Testing for global compatibility and localization issues.
- Test with different character sets and languages
- Verify text expansion and UI layout with longer translations
- Check date, time, and number formatting across locales
- Investigate right-to-left language support

### I - Requirements (New Features)
Focus on newly implemented functionality rather than regression testing.
- Investigate core functionality of new features
- Test integration points between new and existing systems
- Verify business logic implementation
- Examine edge cases specific to new requirements

### M - Measure (Performance, Stress, Scalability)
Testing system behavior under load and performance constraints.
- Investigate response times under normal load
- Test system behavior at capacity limits
- Verify resource usage and memory management
- Examine scalability bottlenecks

### E - Existing (Regression)
Testing previously working functionality for unintended changes.
- Investigate critical user workflows
- Test core business processes
- Verify integration points remain functional
- Examine areas touched by recent changes

## Key Questions

- Which SLIME dimension poses the highest risk for this release?
- What are the potential business impacts if each dimension fails?
- Where are the integration points most likely to break?
- What would cause the most user frustration if it failed?
