#!/usr/bin/env python3

import re

# Read the file
with open('/Users/llewellynfalco/Github/ExploratoryTestingAI/internal_documentation/linting.diagram.md', 'r') as f:
    content = f.read()

print("File content preview:")
print(content[:200])
print("\n" + "="*50 + "\n")

# Try different regex patterns to extract mermaid
patterns = [
    r'```mermaid\n(.*?)\n```',
    r'```mermaid(.*?)```',
    r'```mermaid\s*(.*?)\s*```'
]

for i, pattern in enumerate(patterns):
    match = re.search(pattern, content, re.DOTALL)
    if match:
        print(f"Pattern {i+1} worked!")
        mermaid_content = match.group(1)
        print(f"Extracted content length: {len(mermaid_content)}")
        print(f"First 200 chars: {mermaid_content[:200]}")
        break
else:
    print("No mermaid pattern matched")
    
# Manual extraction
start_marker = "```mermaid"
end_marker = "```"
start_idx = content.find(start_marker)
if start_idx != -1:
    start_idx += len(start_marker)
    end_idx = content.find(end_marker, start_idx)
    if end_idx != -1:
        mermaid_content = content[start_idx:end_idx].strip()
        print(f"\nManual extraction successful!")
        print(f"Content length: {len(mermaid_content)}")
        
        # Now find all nodes
        lines = mermaid_content.split('\n')
        node_count = 0
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('flowchart') or line.startswith('subgraph') or line.startswith('end') or line.startswith('%%') or line.startswith('style'):
                continue
                
            # Look for node definitions
            if any(bracket in line for bracket in ['([', '{', '["']):
                if '-->' not in line:  # Not a connection
                    print(f"Node definition: {line}")
                    node_count += 1
                    
        print(f"\nTotal node definitions found: {node_count}")
