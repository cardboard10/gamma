# gamma
game engine for casio monochrome fx-9750Giii


gamma is a modular 2D AABB physics and entity-management engine designed for pythonExtra on the Casio fx-9750GIII calculator.




Overview:
gamma is a lightweight, modular 2D physics and entity-management framework built specifically for the Casio fx-9750GIII. Designed to operate within tight hardware constraints, it brings reliable physics and collision handling to calculator homebrew development.

Key Features:
AABB Physics: Axis-Aligned Bounding Box collision detection optimized for grid and vector-based objects.

Tile-Map Collisions: Built-in support for handling map structures, obstacles, and movement boundaries.

Modular Architecture: Cleanly separated files for physics logic, entity management, and drawing/rendering hooks.

Low-Resource Optimization: Engineered to run smoothly within a limited RAM footprint (~50KB limit).

The Developer Story
What makes gamma unique is its development environment: it was written, debugged, and tested 100% on-device directly on the calculator\'s physical keyboard and monochrome screen, without using a PC or desktop IDE.

Requirements & Setup
Hardware: Casio fx-9750GIII (or equivalent Graph models)

Environment: MicroPython + gint bindings / pythonExtra

Usage: Unzip the archive and import gamma and its dependent utility modules into your Python project directory on the calculator.

*description written by gemini after being fed the files and the context(how it was developed)

