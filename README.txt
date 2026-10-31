MONDAY, AGAIN
A Python narrative exploration and time-loop mystery game.

REQUIREMENTS
- Developed and tested on Windows with Python 3.13.
- Requires Tkinter/Tk and a graphical desktop.
- Uses only Python's standard library. No pip packages are required.
- This GUI game should be run locally, not in Ed's online console.

HOW TO RUN
1. Keep main.py, pixel_preview.py and the assets folder together.
2. Open a terminal in the project folder.
3. On Windows, run:
   py pixel_preview.py

   Alternatively, use your Python 3 command:
   python3 pixel_preview.py

pixel_preview.py is the entry point for the pixel-art version.
main.py provides the story rules and shared interface.

CONTROLS
- Click objects and choose LOOK, TAKE or USE.
- Click characters and choose TALK.
- SCENE ITEMS provides an alternative list of available interactions.
- GO OUT or MAP opens the destination menu.
- END PHASE advances to the next part of the day.
- END OUTING returns home and ends the day's exploration.
- SLEEP begins the next Monday.
- STAY AWAKE lets the player observe the midnight transition.

GAMEPLAY
The first day follows a fixed introductory route.
Later days have morning, afternoon and evening phases.
Each phase allows up to two destination visits.
Inspecting objects and talking do not consume visits.
Important discoveries remain between Mondays, while carried items reset.
Evidence and dialogue become available gradually across seven Mondays.
The final reverse route follows separate rules explained in the game.

SAVING AND LOADING
SAVE records the current progress in monday_save.json beside main.py.
There is one manual save slot. Saving again overwrites it.
LOAD restores the most recently saved progress.
Progress after the last SAVE is not automatically recorded.
Saves from earlier story versions may be incompatible.

PROGRAMMING CONCEPTS
- Classes and inheritance organise game state and the interface.
- File input/output and JSON support saving and loading.
- Exception handling and data validation handle missing or invalid saves.
- Dictionaries, lists and sets manage scenes, dialogue and discoveries.

TROUBLESHOOTING
If images are missing, restore the complete assets folder.
If a save is incompatible, choose NEW GAME.
Keep the project in a writable folder so that saving can succeed.