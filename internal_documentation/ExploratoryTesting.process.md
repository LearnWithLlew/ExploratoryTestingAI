# Exploratory Testing Process

A systematic approach to exploratory testing that balances structure with the freedom to investigate and discover issues through hands-on exploration.

## Preparation Phase

### 1. Gather Context
- Ask for the URL of the website/application to test
- Understand the application's purpose and target audience
- Identify key user workflows and business-critical features
- Note any known issues or areas of concern
- Determine testing time constraints and scope

### 2. Set Testing Charter
- Define the mission: What are we trying to learn?
- Identify focus areas (functionality, usability, performance, security)
- Set time boundaries for the testing session
- Choose testing techniques and heuristics to apply

## Execution Phase

### 3. Initial Reconnaissance
- Open the application in browser
- Take initial screenshots for documentation
- Perform a quick tour to understand the application structure
- Note first impressions and obvious issues
- Identify main navigation paths and user flows

### 4. Systematic Exploration
- **Happy Path Testing**: Test intended user workflows
- **Boundary Testing**: Test edge cases and limits
- **Error Handling**: Try invalid inputs and unexpected actions
- **Cross-browser/Device Testing**: Test on different platforms
- **Accessibility Testing**: Check keyboard navigation, screen readers
- **Performance Observation**: Note slow loading, responsiveness issues

### 5. Deep Dive Investigation
- Follow interesting observations and anomalies
- Test integrations between different features
- Explore less obvious user paths
- Test with different user roles/permissions if applicable
- Investigate security concerns (input validation, authentication)

## Documentation Phase

While working, record steps, todos and findings in a document called
TestSession.01.md
Figure out the number by incrementing the last number by 1

## Testing Heuristics

### CRUD Operations
- Create, Read, Update, Delete functionality
- Data validation and error handling
- Permissions and access control

### User Interface
- Visual consistency and alignment
- Responsive design across screen sizes
- Form validation and user feedback
- Navigation clarity and intuitiveness

### Data Flow
- Input/output validation
- Data persistence across sessions
- Integration points between systems
- API responses and error handling

## Session Management

- Debrief after each session to capture learnings
- Plan follow-up sessions based on findings
