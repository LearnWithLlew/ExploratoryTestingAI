# Exploratory Testing Process - Michael Bolton Approach

A learning-oriented approach to exploratory testing focused on investigation, questioning, and building understanding of the product while simultaneously designing and executing tests. The goal is to learn about the product and discover information that matters to stakeholders.

## Preparation Phase

### 1. Establish Learning Objectives
- Ask for the URL of the website/application to test
- Understand the product's mission and value proposition
- Identify who the stakeholders are and what they care about
- Discover the product's intended behaviors and quality criteria
- Understand the testing mission: What questions need answers?
- Clarify what "good enough" means in this context

### 2. Set Testing Charter
- Define the learning mission: What do we need to discover?
- Identify areas of uncertainty and risk
- Set time boundaries for the testing session
- Choose investigation techniques that reveal important information
- Frame testing as an experiment to answer specific questions

## Execution Phase

### 3. Initial Investigation
- Open the application and begin systematic observation
- Take screenshots and notes for evidence gathering
- Perform a coverage tour to understand the product landscape
- Notice what the product does and how it behaves
- Form initial hypotheses about quality and functionality

### 4. Systematic Investigation
- **Question Everything**: Challenge assumptions about intended behavior
- **Follow Your Nose**: Pursue interesting observations and anomalies
- **Vary Your Approach**: Change inputs, timing, sequence, and environment
- **Model the Product**: Build mental models of how it should work
- **Test Your Models**: Design experiments to validate or refute your understanding
- **Seek Inconsistencies**: Look for contradictions in behavior or design

### 5. Deep Investigation
- When you find something interesting, investigate thoroughly
- Ask "What else might be affected by this?"
- Vary one thing at a time to isolate factors
- Look for patterns in the problems you discover
- Consider the broader implications of each finding
- Test related functionality that might share similar risks

## Documentation Phase

While working, record observations, questions, and findings in a document called
TestSession.01.md
Figure out the number by incrementing the last number by 1

## Investigation Heuristics

### The SFDPOT Heuristics (Structure, Function, Data, Platform, Operations, Time)
- **Structure**: How is the product organized and configured?
- **Function**: What functions does the product perform?
- **Data**: What data does the product process?
- **Platform**: What external elements does the product depend on?
- **Operations**: What operations and methods are used?
- **Time**: How does time affect the product?

### Quality Criteria Investigation
- **Capability**: Can the product perform required functions?
- **Reliability**: Does the product work consistently?
- **Usability**: Can users operate the product effectively?
- **Charisma**: Is the product appealing to users?
- **Security**: Is the product protected from threats?
- **Scalability**: Can the product handle growth?
- **Compatibility**: Does the product work with other systems?
- **Performance**: Does the product operate with acceptable speed?

### Learning Patterns
- **Goldilocks Testing**: Try inputs that are too big, too small, and just right
- **Boundary Analysis**: Test at the edges of acceptable ranges
- **Interference Testing**: Interrupt operations at different points
- **Stress Testing**: Push the product beyond normal operating conditions
- **Configuration Testing**: Vary settings and environmental factors

## Session Management

- Document observations, not just problems
- Record questions that arise during testing
- Note what you learned about the product
- Identify areas that need further investigation
- Communicate findings in terms stakeholders understand
- Recommend follow-up testing based on discoveries

## Key Principles

- Testing is investigation, not verification
- Every test is an experiment designed to answer questions
- The goal is learning, not just finding bugs
- Context drives testing strategy and techniques
- Testers are information service providers
- Good testing requires critical thinking and skepticism
