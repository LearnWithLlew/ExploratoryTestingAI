#!/usr/bin/env python3
"""
Personal Voice Usage Example

This script demonstrates how to use macOS Personal Voice after authorization.
It includes functions to list available voices, find Personal Voices, and speak text.
"""

import subprocess
import re
import sys
from typing import List, Dict, Optional


def get_available_voices() -> List[Dict[str, str]]:
    """Get all available voices from the say command."""
    try:
        result = subprocess.run(['say', '-v', '?'], capture_output=True, text=True)
        voices = []
        
        for line in result.stdout.strip().split('\n'):
            # Parse voice line format: "VoiceName    locale    # Sample text"
            match = re.match(r'^(.+?)\s+([a-z_A-Z]+)\s+#\s*(.+)$', line.strip())
            if match:
                name, locale, sample = match.groups()
                voices.append({
                    'name': name.strip(),
                    'locale': locale.strip(),
                    'sample': sample.strip()
                })
        
        return voices
    except Exception as e:
        print(f"Error getting voices: {e}")
        return []


def find_personal_voices(voices: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Find Personal Voices from the voice list."""
    # Personal voices typically don't have locale codes or have specific patterns
    personal_voices = []
    
    for voice in voices:
        # Personal voices might not have standard locale codes
        # or might be identified by specific naming patterns
        if not re.match(r'^[a-z]{2}_[A-Z]{2}$', voice['locale']):
            # Check if it's not a standard system voice
            system_voices = [
                'Alex', 'Alice', 'Allison', 'Ava', 'Bahh', 'Bells', 'Boing', 'Bruce',
                'Bubbles', 'Cellos', 'Deranged', 'Fred', 'Good News', 'Hysterical',
                'Junior', 'Kathy', 'Pipe Organ', 'Princess', 'Ralph', 'Samantha',
                'Trinoids', 'Whisper', 'Zarvox', 'Albert', 'Bad News', 'Jester',
                'Organ', 'Superstar'
            ]
            
            if voice['name'] not in system_voices:
                personal_voices.append(voice)
    
    return personal_voices


def speak_with_voice(text: str, voice_name: str) -> bool:
    """Speak text using specified voice."""
    try:
        result = subprocess.run(['say', '-v', voice_name, text], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Successfully spoke with voice '{voice_name}'")
            return True
        else:
            print(f"❌ Error speaking with voice '{voice_name}': {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Exception speaking with voice '{voice_name}': {e}")
        return False


def test_personal_voice():
    """Test Personal Voice functionality."""
    print("Personal Voice Test")
    print("=" * 30)
    
    # Get all voices
    print("Getting available voices...")
    voices = get_available_voices()
    print(f"Found {len(voices)} total voices")
    
    # Find personal voices
    personal_voices = find_personal_voices(voices)
    
    if not personal_voices:
        print("\n❌ No Personal Voices found.")
        print("Make sure you have:")
        print("1. Created a Personal Voice in System Settings")
        print("2. Run the authorization script: python3 request_personal_voice_auth.py")
        return False
    
    print(f"\n🎉 Found {len(personal_voices)} Personal Voice(s):")
    for voice in personal_voices:
        print(f"  - {voice['name']} ({voice['locale']})")
    
    # Test speaking with the first personal voice
    if personal_voices:
        test_voice = personal_voices[0]
        test_text = "Hello! This is a test of my personal voice."
        
        print(f"\n🗣️  Testing voice '{test_voice['name']}'...")
        print(f"Speaking: '{test_text}'")
        
        success = speak_with_voice(test_text, test_voice['name'])
        return success
    
    return False


def interactive_voice_test():
    """Interactive voice testing."""
    voices = get_available_voices()
    personal_voices = find_personal_voices(voices)
    
    if not personal_voices:
        print("No Personal Voices available for testing.")
        return
    
    print("\nInteractive Personal Voice Test")
    print("Available Personal Voices:")
    for i, voice in enumerate(personal_voices, 1):
        print(f"{i}. {voice['name']}")
    
    try:
        choice = input(f"\nSelect voice (1-{len(personal_voices)}) or 'q' to quit: ")
        if choice.lower() == 'q':
            return
        
        voice_idx = int(choice) - 1
        if 0 <= voice_idx < len(personal_voices):
            selected_voice = personal_voices[voice_idx]
            
            while True:
                text = input(f"\nEnter text to speak with '{selected_voice['name']}' (or 'q' to quit): ")
                if text.lower() == 'q':
                    break
                
                speak_with_voice(text, selected_voice['name'])
        else:
            print("Invalid selection.")
            
    except (ValueError, KeyboardInterrupt):
        print("\nExiting...")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--interactive":
            interactive_voice_test()
        elif sys.argv[1] == "--list":
            voices = get_available_voices()
            personal_voices = find_personal_voices(voices)
            print("Personal Voices:")
            for voice in personal_voices:
                print(f"  {voice['name']} ({voice['locale']})")
        else:
            print("Usage: python3 personal_voice_example.py [--interactive|--list]")
    else:
        test_personal_voice()
