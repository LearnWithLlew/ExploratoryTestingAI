# Exploratory Testing Process

A systematic approach to exploratory testing focused on finding bugs, breaking functionality, and uncovering issues that automated tests miss. The goal is to be adversarial - actively trying to make the system fail.

## Preparation Phase

### 1. Gather Context
- Ask for the URL of the website/application to test
- Understand the application's purpose and target audience
- Identify key user workflows and business-critical features
- Note any known issues or areas of concern
- Determine testing time constraints and scope

### 2. Set Testing Charter
- Define the mission: What can we break? What might fail?
- Identify high-risk areas and attack vectors
- Set time boundaries for the testing session
- Choose aggressive testing techniques to expose weaknesses

## Execution Phase

### 3. Initial Reconnaissance
- Open the application in browser
- Take initial screenshots for documentation
- Perform a quick tour looking for obvious flaws and inconsistencies
- Note immediate red flags and suspicious behavior
- Map attack surfaces and potential failure points

### 4. Systematic Attack
- **Break Happy Paths**: Interrupt and corrupt intended workflows
- **Boundary Assault**: Push limits until something breaks
- **Error Provocation**: Force errors with malformed inputs and edge cases
- **Platform Exploitation**: Find browser/device-specific failures
- **Accessibility Violations**: Expose barriers and compliance failures
- **Performance Stress**: Identify bottlenecks and breaking points

### 5. Exploit Discovery
- Pursue every anomaly until you understand the failure
- Attack integration points where systems connect
- Find hidden paths and unintended access routes
- Escalate privileges and bypass authorization
- Expose security vulnerabilities and data leaks

## Documentation Phase

While working, record steps, todos and findings in a document called
TestSession.01.md
Figure out the number by incrementing the last number by 1

## Attack Heuristics

### CRUD Exploitation
- Force creation of invalid/malicious data
- Access data you shouldn't be able to read
- Corrupt updates and cause data loss
- Delete critical information
- Bypass validation and permission checks

### UI Breaking Points
- Find visual glitches and layout failures
- Break responsive design with extreme screen sizes
- Bypass form validation with crafted inputs
- Confuse navigation and trap users in dead ends

### Data Corruption
- Inject malicious payloads to bypass validation
- Corrupt data persistence and session state
- Exploit integration vulnerabilities
- Trigger API failures and expose error details

## Session Management

- Document every bug, failure, and vulnerability found
- Prioritize critical issues that could impact users
- Plan follow-up attacks based on discovered weaknesses
- Share findings to prevent similar issues in other areas
