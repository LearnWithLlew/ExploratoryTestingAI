# SACKED Exploratory Testing Process - James Bach Heuristic

A systematic approach to exploratory testing using the SACKED heuristic framework. This method provides comprehensive coverage by examining six critical dimensions of any software system through structured investigation.

## Overview

SACKED is a mnemonic that guides testers to explore different aspects of a system:
- **S**tructure - Physical elements, architecture, and organization
- **A**ttributes - Properties, characteristics, and qualities  
- **C**apability - Functions, features, and what the system can do
- **K**nowledge - Information, data, and content the system handles
- **E**nvironment - Context, conditions, and external factors
- **D**ependencies - Relationships, integrations, and external systems

## Pre-Session Preparation

### 1. Mission Definition
- Define the testing charter: What are we investigating?
- Identify stakeholders and their concerns
- Establish session time boundaries (typically 60-90 minutes)
- Gather available documentation and context
- Set up test environment and tools

### 2. Initial Product Tour
- Perform a brief walkthrough to build mental model
- Identify obvious features and workflows
- Note areas that seem complex or risky
- Document initial observations and questions

## SACKED Investigation Process

### Structure (S) - "What is it made of?"

**Focus**: Examine the physical elements, architecture, and organizational aspects

**Investigation Steps**:
1. **Code Structure** (if accessible)
   - Review file organization and naming conventions
   - Examine configuration files and settings
   - Look for architectural patterns and dependencies
   - Check for unused or dead code

2. **UI Structure**
   - Analyze page layouts and navigation patterns
   - Test responsive design across different screen sizes
   - Examine form structures and input validation
   - Check accessibility markup and structure

3. **Data Structure**
   - Investigate database schemas and relationships
   - Test data import/export formats
   - Examine file structures and naming conventions
   - Check data validation rules and constraints

**Key Questions**:
- How is this system organized?
- What patterns can I identify in the structure?
- Are there structural inconsistencies?
- How does the structure support or hinder functionality?

### Attributes (A) - "What qualities does it have?"

**Focus**: Examine properties, characteristics, and non-functional aspects

**Investigation Steps**:
1. **Performance Attributes**
   - Test response times under normal load
   - Measure resource consumption (CPU, memory, network)
   - Check for performance degradation over time
   - Test with large datasets or high user loads

2. **Quality Attributes**
   - Evaluate usability and user experience
   - Test reliability and error recovery
   - Check security measures and access controls
   - Assess maintainability and code quality

3. **Visual Attributes**
   - Test visual consistency across the application
   - Check color schemes and contrast ratios
   - Verify font rendering and sizing
   - Test visual feedback for user actions

**Key Questions**:
- What qualities make this system good or bad?
- How does it perform under stress?
- What attributes might users care about most?
- Are there hidden quality issues?

### Capability (C) - "What can it do?"

**Focus**: Explore functions, features, and system capabilities

**Investigation Steps**:
1. **Core Functions**
   - Test primary user workflows end-to-end
   - Verify each feature works as intended
   - Test feature combinations and interactions
   - Check for undocumented or hidden features

2. **Edge Case Capabilities**
   - Test boundary conditions and limits
   - Try unusual but valid input combinations
   - Test error handling and recovery mechanisms
   - Explore administrative or power-user features

3. **Integration Capabilities**
   - Test API endpoints and data exchange
   - Verify third-party service integrations
   - Check import/export functionality
   - Test cross-platform compatibility

**Key Questions**:
- What is this system supposed to do?
- What can I make it do that might be unexpected?
- Are there capabilities that don't work as advertised?
- What happens when capabilities are pushed to their limits?

### Knowledge (K) - "What does it know?"

**Focus**: Investigate information, data, and content handling

**Investigation Steps**:
1. **Data Handling**
   - Test data input validation and sanitization
   - Verify data storage and retrieval accuracy
   - Check data transformation and processing
   - Test data backup and recovery procedures

2. **Information Architecture**
   - Examine how information is organized and presented
   - Test search and filtering capabilities
   - Verify data relationships and integrity
   - Check for data consistency across the system

3. **Content Management**
   - Test content creation, editing, and deletion
   - Verify version control and change tracking
   - Check content approval and publishing workflows
   - Test content localization and internationalization

**Key Questions**:
- What information does the system store and process?
- How accurate and reliable is the data handling?
- Can I corrupt or lose data through normal usage?
- Are there information security concerns?

### Environment (E) - "Where does it live?"

**Focus**: Examine context, conditions, and environmental factors

**Investigation Steps**:
1. **Platform Environment**
   - Test across different operating systems
   - Verify browser compatibility and versions
   - Check mobile device compatibility
   - Test network connectivity scenarios

2. **User Environment**
   - Test with different user roles and permissions
   - Verify accessibility features and compliance
   - Check internationalization and localization
   - Test with various user configurations

3. **System Environment**
   - Test under different system loads
   - Verify behavior with limited resources
   - Check time zone and date handling
   - Test backup and disaster recovery scenarios

**Key Questions**:
- In what environments will this system be used?
- How does environmental change affect behavior?
- What environmental assumptions might be wrong?
- Are there environmental risks or constraints?

### Dependencies (D) - "What does it rely on?"

**Focus**: Explore relationships, integrations, and external dependencies

**Investigation Steps**:
1. **External Dependencies**
   - Test behavior when external services are unavailable
   - Verify API integrations and data synchronization
   - Check third-party library and framework dependencies
   - Test database connectivity and failover scenarios

2. **Internal Dependencies**
   - Examine module and component interactions
   - Test cascading effects of component failures
   - Verify data flow between system components
   - Check configuration and environment dependencies

3. **User Dependencies**
   - Test workflows that depend on user actions
   - Verify role-based access and permissions
   - Check collaborative features and shared resources
   - Test notification and communication dependencies

**Key Questions**:
- What does this system depend on to function?
- What happens when dependencies fail or change?
- Are there hidden or undocumented dependencies?
- How resilient is the system to dependency issues?

## Session Execution Strategy

### Time Management
- Allocate 10-15 minutes per SACKED dimension
- Spend more time on areas that reveal interesting issues
- Reserve 10 minutes at the end for documentation
- Use timeboxing to maintain focus and coverage

### Investigation Techniques
- **Follow Your Nose**: Pursue interesting observations
- **Vary Your Approach**: Alternate between systematic and exploratory
- **Question Everything**: Challenge assumptions and expected behavior
- **Document as You Go**: Note observations, questions, and issues immediately

### Risk-Based Prioritization
- Focus first on areas with highest business impact
- Investigate complex integrations and data flows
- Pay attention to recently changed or new features
- Explore areas with known historical problems

## Documentation and Reporting

### During the Session
- Record observations for each SACKED dimension
- Note specific steps to reproduce interesting behaviors
- Capture screenshots or recordings of issues
- Document questions that arise during investigation

### Session Summary
- **Mission**: What was the testing charter?
- **Coverage**: Which SACKED dimensions were explored?
- **Findings**: What issues or risks were discovered?
- **Questions**: What needs further investigation?
- **Recommendations**: What actions should be taken?

### Issue Reporting
- Provide clear reproduction steps
- Include relevant environment and context information
- Assess business impact and user experience effects
- Suggest potential workarounds or solutions
- Link issues to specific SACKED dimensions for traceability

## Advanced Techniques

### Combining SACKED with Other Heuristics
- Use with CRUD operations (Create, Read, Update, Delete)
- Apply boundary value analysis within each dimension
- Combine with user persona-based testing
- Integrate with risk-based testing approaches

### Collaborative SACKED Sessions
- Assign different team members to different dimensions
- Share findings in real-time during paired testing
- Use SACKED as a framework for test case reviews
- Apply in bug triage to ensure comprehensive coverage

### Continuous Application
- Use SACKED for regression testing after changes
- Apply during code reviews and design discussions
- Integrate into automated testing strategy planning
- Use for post-incident analysis and prevention

## Success Metrics

### Coverage Indicators
- All six SACKED dimensions investigated
- Multiple test techniques applied per dimension
- Both positive and negative test scenarios explored
- Integration points and dependencies verified

### Quality Indicators
- Issues found that matter to stakeholders
- Risks identified before they impact users
- Improved understanding of system behavior
- Actionable recommendations provided

### Learning Indicators
- New insights about system architecture
- Better understanding of user workflows
- Identification of testing gaps or blind spots
- Enhanced mental model of system behavior

## Common Pitfalls and Mitigations

### Avoiding Tunnel Vision
- Set timers for each SACKED dimension
- Regularly step back and assess overall coverage
- Switch between dimensions when stuck
- Collaborate with others for fresh perspectives

### Managing Information Overload
- Focus on the most important findings first
- Use structured note-taking templates
- Prioritize issues by business impact
- Schedule follow-up sessions for deep dives

### Maintaining Objectivity
- Challenge your own assumptions regularly
- Seek disconfirming evidence for beliefs
- Consider multiple user perspectives
- Document both positive and negative findings

Remember: SACKED is a guide, not a rigid checklist. Adapt the approach based on your context, time constraints, and the specific risks you're investigating. The goal is thorough, intelligent exploration that uncovers important information about system quality and behavior.