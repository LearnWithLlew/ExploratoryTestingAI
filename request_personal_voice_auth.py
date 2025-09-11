#!/usr/bin/env python3
"""
Request Personal Voice authorization for macOS Sonoma.

This script uses PyObjC to access the AVFoundation framework and request
Personal Voice permissions, similar to the C++ solution but in Python.

After running this script and granting permission, you can use Personal Voice
with the `say` command like: say -v "YourVoiceName" "Hello world"
"""

import sys
import time
from Foundation import NSRunLoop, NSDate
from AVFoundation import AVSpeechSynthesizer


def request_personal_voice_authorization():
    """Request Personal Voice authorization from macOS."""
    print("Requesting Personal Voice authorization...")
    print("A system dialog should appear asking for permission.")
    
    authorization_completed = [False]  # Use list for closure
    
    def completion_handler(status):
        """Handle the authorization response."""
        status_names = {
            0: "NotDetermined",
            1: "Denied", 
            2: "Restricted",
            3: "Authorized"
        }
        
        status_name = status_names.get(status, f"Unknown({status})")
        print(f"Authorization status: {status_name}")
        
        if status == 3:  # Authorized
            print("✅ Personal Voice authorization granted!")
            print("You can now use Personal Voice with the 'say' command.")
            print("Example: say -v 'YourVoiceName' 'Hello world'")
        elif status == 1:  # Denied
            print("❌ Personal Voice authorization denied.")
            print("You can change this in System Settings > Privacy & Security > Personal Voice")
        elif status == 2:  # Restricted
            print("⚠️  Personal Voice is restricted on this system.")
        else:
            print("ℹ️  Authorization status not determined yet.")
            
        authorization_completed[0] = True
    
    # Request authorization
    AVSpeechSynthesizer.requestPersonalVoiceAuthorizationWithCompletionHandler_(
        completion_handler
    )
    
    # Run the event loop until authorization completes
    print("Waiting for user response...")
    run_loop = NSRunLoop.currentRunLoop()
    
    # Wait up to 60 seconds for user response
    timeout = 60
    start_time = time.time()
    
    while not authorization_completed[0] and (time.time() - start_time) < timeout:
        # Run the loop for a short time to process events
        run_loop.runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.1))
    
    if not authorization_completed[0]:
        print("⏰ Timeout waiting for authorization response.")
        return False
        
    return True


def check_current_authorization():
    """Check the current Personal Voice authorization status."""
    try:
        # This might not be available in all macOS versions
        # The main approach is to request authorization which will show current status
        print("Checking current authorization status...")
        return request_personal_voice_authorization()
    except Exception as e:
        print(f"Could not check authorization status: {e}")
        return False


if __name__ == "__main__":
    print("macOS Personal Voice Authorization Tool")
    print("=" * 40)
    
    try:
        success = request_personal_voice_authorization()
        
        if success:
            print("\n🎉 Authorization process completed!")
            print("\nNext steps:")
            print("1. Find your Personal Voice name with: say -v '?'")
            print("2. Test it with: say -v 'YourVoiceName' 'Hello, this is my personal voice'")
        else:
            print("\n❌ Authorization process failed or timed out.")
            
    except ImportError as e:
        print(f"❌ Error: Missing required dependencies: {e}")
        print("\nTo install PyObjC:")
        print("pip install pyobjc-framework-AVFoundation pyobjc-framework-Foundation")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
