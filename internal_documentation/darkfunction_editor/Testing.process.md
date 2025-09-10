# darkFunction Editor Exploratory Testing Session

## Test Session Information
- **Date**: 2025-09-09
- **Tester**: Llewellyn + Cascade AI
- **Application**: darkFunction Editor (2D sprite animation tool)
- **Testing Approach**: MCP-automated exploratory testing
- **Tools**: MCP desktop automation server for coordinate-based interaction

## Test Environment Setup
- **Location**: `/Users/llewellynfalco/Github/darkFunction-Editor/`
- **MCP Server**: `mcp-desktop-automation` (coordinate-based automation)
- **Test Resources**: `TestingResources/StarWarsImages/` and `TestingResources/Tämä!/`

## Test Scenario 1: Spritesheet Import & Slicing

### Objective
Test the core functionality of importing large spritesheets and the application's ability to automatically detect sprite boundaries vs manual slicing workflows.

### Test Steps

#### Step 1: Launch Application

**Command**: `./run.sh`
**Time**: 20:29:33

**Observation**: Application launch encountered dependency issues:
- `ClassNotFoundException: org.jdesktop.swingworker.SwingWorker`
- TinyLaF v1.4.0 theme loaded successfully
- Application appears to be running but with errors

**Issue**: Missing SwingWorker dependency - this is a known issue with newer Java versions where SwingWorker was moved from separate library to built-in javax.swing package.

**Result**: ✅ Application GUI launched successfully despite dependency warnings
- Screenshot captured shows darkFunction Editor interface is running
- Main window visible with typical sprite editor layout
- Ready to proceed with testing

#### Step 2: Load Large Spritesheet (All.png)

**Target File**: `TestingResources/StarWarsImages/All.png` (382KB spritesheet)
**Time**: 20:30:15

**Test Actions**:
1. Navigate to File menu to import spritesheet
2. Browse to TestingResources/StarWarsImages/All.png
3. Observe auto-detection behavior
4. Test manual slicing if auto-detection fails

**Permission Issue**: System permissions required for MCP desktop automation
**Time**: 20:31:39
**Action**: User granted necessary permissions for screen capture and input control

**Restart Required**: Both darkFunction Editor and MCP server need restart after permission grant

#### Step 2a: Restart Applications

**darkFunction Editor**: ✅ Restarted successfully
**MCP Server**: ✅ Ready with permissions granted
**Screenshot**: Application interface visible and ready for testing

#### Step 2b: Import Large Spritesheet

**Action**: Navigate to File menu to import spritesheet
**Time**: 20:32:00

**UI Elements Observed**:
- Main window with menu bar (File, Edit, etc.)
- Left panel for sprite management
- Center canvas area
- Right panel for properties

**Test Execution**:

1. **Click File Menu** - Access import functionality
   - Expected: Dropdown menu with import options
   - Location: Top menu bar, leftmost item

2. **Look for Import/Open Spritesheet option**
   - Expected: Menu item for importing image files
   - Common names: "Import Image", "Open", "Load Spritesheet"

3. **Navigate to test file**
   - Target: `TestingResources/StarWarsImages/All.png`
   - File size: 382KB
   - Expected: File browser dialog

**Manual Testing Steps** (for Llewellyn to execute):
- Click File menu in darkFunction Editor
- Select appropriate import option
- Browse to `/Users/llewellynfalco/Github/darkFunction-Editor/TestingResources/StarWarsImages/All.png`
- Observe application behavior during import

**Expected Behaviors to Test**:
- Auto-detection of sprite boundaries
- Manual slicing tools availability
- Performance with large spritesheet
- UI responsiveness during load

**Observations to Document**:
- Import dialog behavior and options
- File loading time and progress indicators
- Auto-detection accuracy for sprite boundaries
- Available manual editing tools
- Memory usage during large file import
- Any error messages or warnings
- UI layout changes after import

---

## Test Results (To be filled during execution)

### File Menu Navigation
**Result**: [Pending - awaiting manual execution]

### Spritesheet Import Process  
**Result**: [Pending - awaiting manual execution]

### Auto-Detection Performance
**Result**: [Pending - awaiting manual execution]

### Manual Slicing Tools
**Result**: [Pending - awaiting manual execution]

---

## Next Test Scenarios Ready

### Test Scenario 2: Animation Creation Workflow
- Load existing `.anim` files (`yoda.anim`, `maul.anim`)
- Test frame timing and playback
- Create new animations from imported sprites

### Test Scenario 3: Export Format Testing
- Export as GIF and compare with existing files
- Test XML export functionality
- Validate different quality settings