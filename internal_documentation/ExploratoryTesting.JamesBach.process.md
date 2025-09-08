# Exploratory Testing Process - James Bach Approach

A disciplined approach to exploratory testing that emphasizes simultaneous learning, test design, and test execution. The goal is to investigate the product through skilled questioning and critical thinking to discover important problems that matter to stakeholders.

## Preparation Phase

### 1. Mission Definition
- Establish the testing mission: What problems are we looking for?
- Identify who cares about this product and why
- Understand the product's value proposition and critical functions
- Define "good enough" quality criteria for this context
- Establish time boundaries and reporting expectations

### 2. Product Analysis
- Study available documentation, requirements, and specifications
- Identify testable claims and assumptions about the product
- Map the product's intended behaviors and boundaries
- Note areas of uncertainty or ambiguity that need investigation
- Consider the product's context: users, environment, constraints

## Execution Phase

### 3. Skilled Investigation
- Begin with a product tour to build a mental model
- Question everything: "How do I know this works?"
- Follow your curiosity and investigate interesting behaviors
- Use heuristics to guide exploration systematically
- Apply critical thinking to evaluate what you observe

### 4. Simultaneous Activities
- **Learning**: Continuously build understanding of the product
- **Test Design**: Create new test ideas based on what you discover
- **Test Execution**: Perform tests and observe results carefully
- **Bug Advocacy**: Evaluate whether problems matter to stakeholders

### 5. Heuristic-Guided Testing

#### SFDPOT (San Francisco Depot) Heuristics
- **Structure**: Test the physical elements and architecture
- **Function**: Test what the product does
- **Data**: Test the information the product processes
- **Platform**: Test the environment dependencies
- **Operations**: Test how people use the product
- **Time**: Test time-related behaviors and constraints

#### Consistency Heuristics
- Compare with comparable products
- Compare with company image and reputation
- Compare with stated purpose and claims
- Compare with user expectations
- Compare within the product itself

## Documentation Phase

### 6. Intelligent Reporting
- Focus on problems that matter to stakeholders
- Provide clear, reproducible steps for significant issues
- Include context about why the problem is important
- Distinguish between observations and inferences
- Recommend further investigation where needed

## Investigation Strategies

### Risk-Based Exploration
- Focus on areas where failure would be most costly
- Test complex interactions and integrations
- Investigate edge cases and boundary conditions
- Challenge assumptions about normal usage
- Explore error handling and recovery mechanisms

### Oracles for Problem Recognition
- **Comparable Products**: How do similar products behave?
- **User Expectations**: What would users reasonably expect?
- **Product Claims**: Does it do what it says it does?
- **Standards**: Does it follow relevant standards and conventions?
- **Statutes**: Does it comply with applicable laws and regulations?

### Testing Techniques
- **Scenario Testing**: Test realistic user stories and workflows
- **Stress Testing**: Push the product beyond normal operating conditions
- **Interaction Testing**: Test how features work together
- **Claims Testing**: Verify explicit and implicit product claims
- **User Testing**: Consider diverse user perspectives and abilities

## Session Management

### Continuous Learning
- Maintain awareness of what you're learning about the product
- Adjust testing strategy based on new information
- Question your own assumptions and biases
- Seek disconfirming evidence for your beliefs about the product

### Skilled Questioning
- What could go wrong here?
- How might this fail in ways I haven't considered?
- What would happen if...?
- How do I know this is working correctly?
- What evidence supports or contradicts this behavior?

### Reporting Philosophy
- Report problems, not just bugs
- Focus on impact and importance, not just technical details
- Provide actionable information for decision-makers
- Acknowledge uncertainty and areas needing further investigation
- Advocate for users and stakeholders who aren't in the room

## Meta-Testing Considerations

- **Context-Driven**: Adapt your approach to the specific context
- **Skill-Dependent**: Recognize that testing quality depends on tester skill
- **Investigative**: Approach testing as detective work, not mechanical checking
- **Collaborative**: Work with developers and stakeholders to understand needs
- **Continuous**: Testing is an ongoing investigation, not a phase that ends
