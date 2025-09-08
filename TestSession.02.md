# Test Session 02 - Nonograms.org Exploratory Testing

**Target:** https://www.nonograms.org/  
**Date:** 2025-09-07  
**Time Started:** 21:23  
**Mission:** Find bugs, break functionality, expose vulnerabilities in nonograms puzzle website

## Testing Charter
- **What can we break?** Puzzle solving interface, user accounts, game logic, data persistence
- **Attack vectors:** Form validation bypass, session manipulation, puzzle data corruption, UI breaking
- **High-risk areas:** User registration/login, puzzle creation, solving mechanics, leaderboards

## Initial Context
- Nonograms (also known as Paint by Numbers, Picross) - logic puzzle website
- Likely has user accounts, puzzle solving interface, possibly user-generated content
- Target audience: puzzle enthusiasts, casual gamers

## Findings Log

### Initial Reconnaissance
- Site loaded successfully: https://www.nonograms.org/
- Title: "Color and black and white Japanese crosswords on-line"
- Basic navigation structure identified

**Key Features Discovered:**
- Black & white nonograms
- Color nonograms  
- User registration/authorization system
- Search functionality
- User-generated content (Send crossword)
- Author profiles
- Rating system (unrated section exists)

## Attack Surface Map

**High-Value Targets:**
1. **Authentication System** - Registration/Authorization endpoints
2. **User Content Creation** - "Send the crossword" functionality
3. **Search System** - Potential for injection attacks
4. **Rating/Voting System** - Data manipulation opportunities
5. **User Profiles** - Author pages, potential for XSS/data exposure

**Entry Points:**
- /register - User registration
- /auth - User login
- /addcrossword - Content submission
- /search - Search functionality
- /authors - User profiles
- /nonograms & /nonograms2 - Puzzle interfaces

## Bugs & Vulnerabilities Found

### 🔍 Information Disclosure Issues
1. **Direct Answer Access** - Puzzle answers are directly accessible via static URLs
   - Example: https://static.nonograms.org/files/nonograms/large/doma_12_1_1p.png
   - Impact: Users can bypass puzzle-solving entirely
   - Severity: Medium - Breaks game mechanics

### 🔍 Potential Attack Vectors Identified
1. **Static File Structure** - Predictable file naming patterns for answers
2. **User-Generated Content** - Comment system without visible moderation
3. **Direct File Access** - No authentication required for answer images
4. **Print Functionality** - Potential for abuse or resource exhaustion

### 🔍 Areas Requiring Deeper Investigation
1. **Search Injection** - Need to test search parameters for SQL/XSS
2. **Registration Bypass** - Form validation and input sanitization
3. **Session Management** - Cookie security and session fixation
4. **File Upload** - Crossword submission security

## Follow-up Actions
*Areas requiring deeper investigation*
