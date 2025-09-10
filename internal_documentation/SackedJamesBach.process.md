# SACKED Exploratory Testing Process - AI Agent Guide

Systematic exploration framework examining six dimensions of software systems.

## SACKED Dimensions

**S**tructure - Architecture, organization, code/UI/data structure
**A**ttributes - Performance, quality, visual properties, non-functional aspects  
**C**apability - Functions, features, integrations, edge cases
**K**nowledge - Data handling, information architecture, content management
**E**nvironment - Platform compatibility, user contexts, system conditions
**D**ependencies - External services, internal components, user workflows

## Investigation Process

### Structure (S)
- Examine file organization, configuration, architectural patterns
- Analyze UI layouts, navigation, form structures, accessibility
- Investigate data schemas, import/export formats, validation rules

### Attributes (A)
- Test performance under load, resource consumption, degradation
- Evaluate usability, reliability, security, maintainability
- Check visual consistency, rendering, user feedback

### Capability (C)
- Test core workflows, feature interactions, hidden functionality
- Explore boundary conditions, unusual inputs, error handling
- Verify API endpoints, third-party integrations, cross-platform behavior

### Knowledge (K)
- Test data validation, storage accuracy, transformation processes
- Examine information organization, search capabilities, data integrity
- Verify content management, version control, localization

### Environment (E)
- Test across operating systems, browsers, mobile devices, network conditions
- Verify user roles, permissions, accessibility, configurations
- Check system loads, resource limits, time zones, disaster recovery

### Dependencies (D)
- Test external service failures, API integrations, library dependencies
- Examine component interactions, failure cascades, data flows
- Verify user-dependent workflows, permissions, collaborative features

## Key Questions Per Dimension
- **Structure**: How is this organized? What patterns exist? Any inconsistencies?
- **Attributes**: What qualities matter? How does it perform under stress?
- **Capability**: What can it do? What happens at limits? Any undocumented features?
- **Knowledge**: What data does it handle? How reliable is processing? Security concerns?
- **Environment**: Where will it be used? How do changes affect behavior?
- **Dependencies**: What does it rely on? What happens when dependencies fail?

## Investigation Approach
- Follow interesting observations and pursue anomalies
- Question assumptions and challenge expected behavior
- Focus on high business impact areas and complex integrations
- Document findings with reproduction steps and business impact assessment