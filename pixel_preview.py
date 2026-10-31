from pathlib import Path
from fractions import Fraction
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

import main as story
from main import GameApp


class Art:
    """Scene files and interaction areas."""

    SCENE_FILES = {
        "bedroom": "bedroom.png",
        "bedroom_night": "bedroom_night.png",
        "bathroom": "bathroom.png",
        "kitchen": "kitchen.png",
        "company": "company.png",
        "cafe": "cafe.png",
        "hospital": "hospital.png",
        "bus_stop": "bus_stop.png",
        "library_exterior": "library_exterior.png",
        "library": "library.png",
        "lab": "lab.png",
    }

    CAST_COLUMNS = 4
    CAST_ROWS = 2
    CAST_FILE = "characters.png"

    CAST_INDEX = {
        "mara": 0,
        "adrian": 1,
        "noah": 2,
        "daniel": 3,
        "evelyn": 4,
        "manager": 5,
        "coworker": 6,
        "voss": 7,
    }

    # Backgrounds for the seventeen opening scenes.

    INTRO_SCENES = [
        "bedroom",
        "bathroom",
        "kitchen",
        "bus_stop",
        "company",
        "company",
        "company",
        "company",
        "cafe",
        "hospital",
        "hospital",
        "library_exterior",
        "company",
        "cafe",
        "bus_stop",
        "kitchen",
        "bedroom_night",
    ]

    PLACE_SCENES = {
        "Home": "bedroom",
        "Bus Stop": "bus_stop",
        "Company": "company",
        "Cafe": "cafe",
        "Hospital": "hospital",
        "Library": "library_exterior",
    }

    # Coordinates are left, top, right and bottom, between zero and one.

    SCENE_HOTSPOTS = {
        "bedroom": {
            "window": (0.830, 0.025, 0.998, 0.515),
            "clock": (0.110, 0.495, 0.195, 0.590),
            "phone": (0.202, 0.545, 0.270, 0.602),
            "calendar": (0.320, 0.250, 0.365, 0.360),
            "milk": (0.490, 0.420, 0.530, 0.510),
            "mug": (0.430, 0.400, 0.480, 0.470),
            "bed": (0.000, 0.610, 0.390, 0.990),
        },
        "bedroom_night": {
            "window": (0.820, 0.010, 0.998, 0.500),
            "clock": (0.120, 0.520, 0.170, 0.590),
            "phone": (0.177, 0.540, 0.225, 0.590),
            "calendar": (0.320, 0.250, 0.365, 0.360),
            "milk": (0.490, 0.420, 0.530, 0.510),
            "mug": (0.430, 0.400, 0.480, 0.470),
            "bed": (0.000, 0.600, 0.500, 0.990),
        },
        "bathroom": {
            "sink": (0.18, 0.52, 0.51, 0.88),
            "mirror": (0.22, 0.08, 0.48, 0.50),
            "razor": (0.57, 0.62, 0.68, 0.75),
        },
        "kitchen": {
            "breakfast": (0.18, 0.58, 0.48, 0.92),
            "milk": (0.49, 0.62, 0.59, 0.87),
            "phone": (0.68, 0.76, 0.85, 0.95),
            "calendar": (0.05, 0.12, 0.20, 0.39),
            "mug": (0.65, 0.50, 0.73, 0.63),
        },
        "company": {
            "mail": (0.08, 0.25, 0.32, 0.64),
            "wrapper": (0.43, 0.77, 0.53, 0.87),
            "folder": (0.56, 0.71, 0.84, 0.95),
            "office": (0.56, 0.14, 0.74, 0.63),
            "coffee": (0.84, 0.27, 0.94, 0.46),
            "shipment": (0.42, 0.18, 0.56, 0.42),
            "report": (0.09, 0.74, 0.27, 0.92),
            "debt": (0.65, 0.74, 0.80, 0.92),
        },
        "cafe": {
            "menu": (0.04, 0.67, 0.35, 0.96),
            "photo": (0.37, 0.71, 0.56, 0.94),
            "newspaper": (0.63, 0.70, 0.94, 0.96),
            "mailbox": (0.02, 0.21, 0.16, 0.50),
            "letter": (0.69, 0.63, 0.82, 0.80),
            "map": (0.67, 0.83, 0.88, 0.98),
        },
        "hospital": {
            "bill": (0.08, 0.56, 0.29, 0.79),
            "medical": (0.38, 0.72, 0.63, 0.91),
            "seat": (0.53, 0.36, 0.75, 0.59),
            "cabinet": (0.75, 0.16, 0.97, 0.65),
            "voice": (0.56, 0.83, 0.66, 0.95),
            "aid": (0.72, 0.79, 0.91, 0.95),
        },
        "bus_stop": {
            "timetable": (0.22, 0.13, 0.32, 0.71),
            "locker": (0.88, 0.32, 0.998, 0.96),
            "transport": (0.44, 0.69, 0.65, 0.88),
        },
        "library_exterior": {
            "notice": (0.415, 0.405, 0.470, 0.530),
            "side": (0.80, 0.39, 0.90, 0.75),
        },
        "library": {
            "notice": (0.03, 0.04, 0.19, 0.15),
            "side": (0.03, 0.18, 0.17, 0.57),
            "thesis": (0.08, 0.69, 0.33, 0.95),
            "review": (0.36, 0.69, 0.60, 0.94),
            "formula": (0.63, 0.70, 0.88, 0.94),
            "lab": (0.81, 0.08, 0.998, 0.60),
        },
        "lab": {
            "alpha": (0.03, 0.70, 0.20, 0.85),
            "beta": (0.20, 0.71, 0.34, 0.86),
            "voss_log": (0.37, 0.70, 0.49, 0.87),
            "projection": (0.40, 0.10, 0.70, 0.45),
            "scanner": (0.72, 0.30, 0.94, 0.70),
            "console": (0.35, 0.40, 0.71, 0.55),
        },
    }

    DOOR_ZONES = {
        "bedroom": {
            "continue": (0.560, 0.185, 0.700, 0.610),
        },
    }

    # Positions are horizontal center, feet position and body height.

    ACTOR_POSITIONS = {
        "bedroom": {},
        "bedroom_night": {},
        "bathroom": {},
        "kitchen": {},
        "company": {
            "manager": (0.79, 0.72, 0.54),
            "coworker": (0.79, 0.72, 0.54),
            "adrian": (0.79, 0.72, 0.54),
        },
        "cafe": {
            "adrian": (0.55, 0.72, 0.54),
            "mara": (0.55, 0.72, 0.54),
            "noah": (0.55, 0.72, 0.44),
        },
        "hospital": {
            "mara": (0.34, 0.72, 0.54),
            "noah": (0.52, 0.72, 0.44),
        },
        "bus_stop": {
            "daniel": (0.55, 0.90, 0.54),
        },
        "library_exterior": {
            "evelyn": (0.61, 0.84, 0.54),
        },
        "library": {
            "evelyn": (0.73, 0.72, 0.54),
        },
        "lab": {
            "voss": (0.76, 0.48, 0.30),
        },
    }

    @staticmethod
    def scene_key(state):
        """Choose the current background."""
        if state.mode == "intro":
            return Art.INTRO_SCENES[state.intro_index]

        if state.location == "Home":
            return "bedroom_night" if state.mode == "home" else "bedroom"

        if state.location == "Library":
            if state.mode == "reverse":
                return "library"
            if state.area == "lab":
                return "lab"
            if "library_open" in state.events:
                return "library"
            return "library_exterior"

        return Art.PLACE_SCENES[state.location]


art = Art

# Crop transparent margins so the anchor is under the real feet.

SPRITE_BOUNDS = {
    "mara": (93, 75, 305, 512),
    "adrian": (82, 57, 286, 512),
    "noah": (86, 88, 293, 512),
    "daniel": (76, 56, 304, 512),
    "evelyn": (83, 60, 292, 488),
    "manager": (89, 49, 289, 488),
    "coworker": (86, 50, 275, 488),
    "voss": (91, 42, 293, 488),
}

# Foreground desks cover the lower part of people standing behind them.

FOREGROUND_TOP = {
    "company": 0.675,
    "cafe": 0.660,
    "hospital": 0.680,
    "library": 0.650,
}


# Gradual evidence discovery.

PACING_VERSION = 2

PACING_INSPECT_DAY = {
    "wrapper": 3,
    "bill": 3,
    "medical": 3,
    "photo": 3,
    "newspaper": 3,
    "voice": 3,
    "aid": 3,
    "letter": 3,
    "map": 3,
    "report": 4,
    "debt": 4,
    "shipment": 5,
    "timetable": 5,
}

PACING_HIDDEN_DAY = {
    "voice": 3,
    "aid": 3,
    "letter": 3,
    "map": 3,
    "report": 4,
    "debt": 4,
    "transport": 5,
    "thesis": 5,
    "review": 5,
    "formula": 5,
    "lab": 5,
    "alpha": 5,
    "beta": 5,
    "console": 5,
    "voss_log": 6,
    "projection": 6,
    "scanner": 6,
}

PACING_USE_DAY = {
    "cabinet": 3,
    "mailbox": 3,
    "voice": 3,
    "office": 4,
    "report": 4,
    "locker": 5,
    "side": 5,
    "lab": 5,
    "scanner": 6,
    "console": 6,
}

# Reading requires context as well as the correct day.

PACING_READ_REQUIRES = {
    "wrapper": {"mail"},
    "medical": {"bill"},
    "newspaper": {"photo"},
    "thesis": {"map"},
    "review": {"evelyn_story"},
    "formula": {"thesis"},
    "voss_log": {"review"},
    "projection": {"full_formula"},
}

PACING_TOPIC_DAY = {
    ("adrian", "identity"): 3,
    ("adrian", "access"): 3,
    ("adrian", "funding"): 4,
    ("mara", "story"): 3,
    ("mara", "collection"): 3,
    ("mara", "selection"): 3,
    ("noah", "story"): 3,
    ("noah", "mail"): 3,
    ("noah", "boundary"): 4,
    ("daniel", "story"): 5,
    ("daniel", "locker"): 5,
    ("daniel", "sequence"): 5,
    ("evelyn", "story"): 5,
    ("evelyn", "method"): 6,
}

# Early descriptions contain no hidden evidence.

PACING_SURFACE_TEXT = {
    "wrapper": (
        "An ordinary gum wrapper. "
        "Its small markings are difficult to read."
    ),
    # An ordinary wrapper with unclear markings.


    "bill": "A woman is sorting a stack of medical bills.",
    # A woman sorts medical bills.


    "medical": (
        "Your appointment paperwork recommends "
        "rest after the examination."
    ),
    # Ordinary appointment paperwork recommends rest.


    "photo": "An old photograph is tucked inside the book.",
    # There is an old photograph inside the book.


    "newspaper": (
        "A local newspaper lies on the table. "
        "You skim the ordinary headlines."
    ),
    # You skim the local newspaper's ordinary headlines.


    "shipment": "A delivery invoice is pinned beside the work documents.",
    # An invoice is pinned beside the documents.


    "timetable": (
        "Every service is marked DELAYED. "
        "The route numbers look familiar."
    ),
    # Services are delayed and the route numbers look familiar.

}

PACING_LATER = (
    "You cannot make sense of this yet. "
    "Follow another lead for now."
)
# You need another lead before understanding this.


PACING_PARTIAL_FORMULA = (
    "Only part of the formula is legible: "
    "two separated spaces can remain coupled. "
    "The final calibration lines are missing."
)
# The formula only explains coupled spaces; calibration is missing.


PACING_PARTIAL_RECORDS = {
    "alpha": (
        "ALPHA: five subjects; progressive memory loss. "
        "The remaining fields are unreadable.",
        "Alpha lists five subjects and progressive memory loss; "
        "the other fields are unreadable.",
    ),
    # Alpha lists five subjects and memory loss.


    "beta": (
        "BETA: a second independent loop. "
        "Reserve: seven Mondays. "
        "Creator and transferred contents: ENCRYPTED.",
        "Beta is a second independent loop with seven Mondays "
        "of reserve; its creator and contents remain encrypted.",
    ),
    # Beta is an independent loop with seven cycles of reserve.


}

PACING_SAFE_NOTES = {
    "adrian_story": (
        "Adrian inherited his father's gambling debt "
        "and kept trying to recover his losses."
    ),
    # Adrian inherited gambling debt and chased his losses.


    "truth_selection": (
        "SELECTION: the aid programme screened Mara's behaviour "
        "before she entered the district."
    ),
    # The aid programme screened Mara before she entered the district.


    "truth_boundary": (
        "BOUNDARY: the affected people were drawn "
        "into the same prepared district."
    ),
    # The affected people were brought into one prepared district.

}

PACING_MAP_PLAIN = (
    "Lily's street sketch shows local streets "
    "and a side door behind the library."
)
# The sketch shows streets and a library side entrance.


PACING_MAP_FULL = (
    "Lily's map marks the experimental boundary "
    "and the library side door."
)
# The map is now understood as the experimental boundary.


PACING_LETTER_PLAIN = (
    "Noah's returned complaints bear the same forwarding address "
    "and handwritten marks. Someone handled them before they came back."
)
# Someone processed Noah's letters before returning them.




class PreviewState(story.GameState):
    """Preserve the story while pacing discoveries."""

    def objects(self):
        """Hide milk and prevent window interactions at night."""
        night = (
            self.mode == "home"
            or self.phase == 2
            or (
                self.clock[:2].isdigit()
                and int(self.clock[:2]) >= 18
            )
        )

        return [
            key
            for key in super().objects()
            if self.day >= PACING_HIDDEN_DAY.get(key, 1)
            and key != "milk"
            and not (key == "window" and night)
        ]

    def characters(self):
        """Protect map transitions and final anchor scenes."""
        if self.mode == "explore" and not self.active:
            return []

        if self.mode == "reverse":
            if self.active:
                return [story.REVERSE[self.reverse_index][1]]
            return []

        if self.mode in {"ending", "verdict"}:
            return []

        return super().characters()

    def learn(self, key, text=None):
        """Keep journal summaries within current understanding."""
        if key in PACING_SAFE_NOTES:
            text = PACING_SAFE_NOTES[key]

        elif key == "map":
            text = (
                PACING_MAP_FULL
                if self.map_understood()
                else PACING_MAP_PLAIN
            )

        elif key == "letter" and self.day < 4:
            text = PACING_LETTER_PLAIN

        elif key == "formula" and "full_formula" not in self.known:
            text = PACING_PARTIAL_FORMULA

        super().learn(key, text)

        if key == "truth_boundary" and "map" in self.known:
            self.notes["map"] = PACING_MAP_FULL

    def map_understood(self):
        return (
            self.day >= 4
            and {"letter", "noah_story"} <= self.known
        )

    def inspect(self, key):
        if key not in self.objects() or key in story.CHAR_NAMES:
            return "There is nothing to inspect here."
            # Nothing here can be inspected.


        if (
            key == "window"
            and self.mode == "explore"
            and self.phase == 1
        ):
            return (
                "Afternoon light falls across the room. "
                "The street outside is quiet."
            )
            # Afternoon light enters the room; the street is quiet.


        if self.day < PACING_INSPECT_DAY.get(key, 1):
            return PACING_SURFACE_TEXT.get(key, PACING_LATER)

        required = PACING_READ_REQUIRES.get(key, set())
        if not required <= self.known:
            return (
                "You need more context to connect this detail. "
                "Follow the leads in your journal."
            )
            # More context is needed.


        if key == "map":
            text = (
                PACING_MAP_FULL
                if self.map_understood()
                else PACING_MAP_PLAIN
            )
            self.learn(key, text)
            self.notes[key] = text
            return text

        if key == "letter" and self.day < 4:
            self.learn(key, PACING_LETTER_PLAIN)
            return PACING_LETTER_PLAIN

        if key == "formula":
            self.learn("formula", PACING_PARTIAL_FORMULA)

            if self.day >= 6:
                self.learn("full_formula", "")
                self.notes["formula"] = story.NOTES["formula"]
                return story.OBJECTS["formula"][1]

            return PACING_PARTIAL_FORMULA

        if (
            key in PACING_PARTIAL_RECORDS
            and "full_formula" not in self.known
        ):
            text, note = PACING_PARTIAL_RECORDS[key]
            self.learn(key, note)
            self.notes[key] = note
            return text

        if key in PACING_PARTIAL_RECORDS:
            self.learn(key, story.NOTES[key])
            self.notes[key] = story.NOTES[key]
            return story.OBJECTS[key][1]

        if key == "console" and self.day < 6:
            return "The console lacks complete calibration information."
            # The calibration is incomplete.


        text = super().inspect(key)

        if key == "letter" and self.day >= 4:
            self.notes[key] = story.NOTES[key]

        return text

    def use(self, key):
        """Guard actions as well as object visibility."""
        if key not in self.objects():
            return "That object is not here."
            # The object is not here.


        if self.day < PACING_USE_DAY.get(key, 1):
            return PACING_LATER

        if key == "scanner" and "full_formula" not in self.known:
            return (
                "The incomplete formula is not enough "
                "to interpret the scan."
            )
            # Complete the formula first.


        return super().use(key)

    def topics(self, actor):
        result = []

        for topic in super().topics(actor):
            earliest = PACING_TOPIC_DAY.get((actor, topic[0]), 1)

            if self.day < earliest:
                continue

            if (
                actor == "evelyn"
                and topic[0] == "method"
                and "full_formula" not in self.known
            ):
                continue

            result.append(topic)

        return result

    def can_use_console(self):
        return (
            self.day >= 6
            and len(self.truths) == 5
            and "full_formula" in self.known
        )

    def check_order(self):
        if not self.can_use_console():
            self.order.clear()
            return False

        return super().check_order()

    def begin_reverse(self):
        if "full_formula" not in self.known:
            return False

        return super().begin_reverse()

    def tasks(self):
        """Create objectives only from known information."""
        tasks = []
        known = self.known

        if self.day == 1:
            return [
                "Follow your usual day and complete the current scene."
            ]
            # Complete the ordinary day.


        if self.day == 2:
            return [
                "Follow the familiar route. Notice what repeats, "
                "and speak to the people you met."
            ]
            # Notice repetition and speak to familiar people.


        if (
            {"bill", "medical"} <= known
            and "truth_selection" not in known
        ):
            tasks.append("Ask Mara about the hospital records.")
            # Ask Mara about the records.


        if (
            {"photo", "newspaper"} <= known
            and "mail_code" not in known
        ):
            tasks.append(
                "Ask Noah about the photograph and the complaints."
            )
            # Ask Noah about the photograph and complaints.


        if "mail_code" in known and "letter" not in known:
            tasks.append("Return to the cafe mailbox.")
            # Return to the cafe mailbox.


        if (
            {"mail", "wrapper"} <= known
            and "finance_code" not in known
        ):
            tasks.append(
                "Ask Adrian about the number on the wrapper."
            )
            # Ask Adrian about the wrapper's number.


        if "finance_code" in known and "truth_funding" not in known:
            if self.day < 4:
                tasks.append("Return to finance on a later Monday.")
                # Return to finance on a later Monday.

            else:
                tasks.append(
                    "Examine the finance documents, "
                    "then speak to Adrian."
                )
                # Examine the documents, then speak to Adrian.


        if (
            {"letter", "map", "noah_story"} <= known
            and "truth_boundary" not in known
        ):
            tasks.append(
                "Compare Noah's account with the letters "
                "and street sketch."
            )
            # Compare Noah's story with the evidence.


        if "shipment" in known and "transport" not in known:
            tasks.append(
                "Show the delivery routes to Daniel "
                "at the morning bus stop."
            )
            # Show Daniel the routes at the morning bus stop.


        if (
            self.day >= 5
            and "map" in known
            and "formula" not in known
        ):
            tasks.append(
                "Investigate the library side entrance "
                "shown on Lily's sketch."
            )
            # Investigate the entrance on Lily's sketch.


        if "formula" in known and "full_formula" not in known:
            tasks.append(
                "The formula is incomplete. "
                "Read it again on a later Monday."
            )
            # Revisit the incomplete formula later.


        if (
            "full_formula" in known
            and len(self.truths) >= 4
            and "truth_method" not in known
        ):
            tasks.append(
                "Discuss the completed formula "
                "and the accounts with Evelyn."
            )
            # Discuss the completed formula with Evelyn.


        if len(self.truths) == 5:
            if "order_solved" not in known:
                tasks.append(
                    "Use the laboratory console "
                    "to reconstruct the causal order."
                )
                # Reconstruct the causal order.

            else:
                tasks.append(
                    "Begin the reverse route in the laboratory "
                    "on Monday seven."
                )
                # Begin the reversal on Monday seven.


        if "beta" in known and self.day == 7:
            tasks.append(
                "Beta's reserve ends tonight. "
                "Complete what is still missing."
            )
            # The reserve ends tonight.


        return tasks or [
            "Revisit the people and places you already know."
        ]
        # Revisit familiar people and places.


    def dump(self):
        saved = super().dump()
        data = saved["state"]
        data["notes"] = dict(data["notes"])
        data["today"] = dict(data["today"])
        data["order"] = list(data["order"])
        saved["pacing_version"] = PACING_VERSION
        return saved

    @classmethod
    def restore(cls, saved):
        if (
            not isinstance(saved, dict)
            or saved.get("pacing_version") != PACING_VERSION
        ):
            raise ValueError(
                "This save belongs to an earlier story version. "
                "Choose NEW GAME."
            )
            # Old saves contain discoveries from the previous rules.


        return super().restore(saved)


# Align prerequisite discoveries with their usable dates.

PACING_VERSION = 3

# Reveal the wrapper numbers and confirm their purpose on Monday four.

PACING_INSPECT_DAY["wrapper"] = 4
PACING_TOPIC_DAY[("adrian", "access")] = 4

# Funding can be confirmed after collecting the finance documents.

PACING_TOPIC_DAY[("adrian", "funding")] = 5

# Both inspecting and using the scanner require the complete formula.

PACING_READ_REQUIRES["scanner"] = {"full_formula"}


PACING_MAP_PLAIN = (
    "Lily's sketch marks local streets and several delivery routes."
)
# Lily's sketch shows streets and delivery routes.


PACING_MAP_FULL = (
    "Lily's map marks the experimental boundary of the district."
)
# The map identifies the experimental boundary.



PACING_SAFE_NOTES.update({
    "library_access": (
        "Evelyn identified the library service entrance "
        "and gave you its staff access sequence."
    ),
    # Evelyn supplied the service entrance access sequence.


    "calibration_key": (
        "Evelyn reconstructed the calibration key. "
        "Use it to read the complete temporal formula."
    ),
    # Use Evelyn's key to interpret the complete formula.

})


TOPIC_LIBRARY_ACCESS = (
    "library_access",

    "Can you explain this mark on Lily's street sketch?",
    # Ask about the mark on the sketch.


    ("map",),

    '"That is the library service entrance," Evelyn says. '
    '"I used it when the main doors were closed." '
    "She writes down the staff access sequence. "
    "You can now open the side door.",
    # Evelyn identifies the entrance and provides access.



    ("library_access",),
)


TOPIC_CALIBRATION = (
    "calibration",

    "Can you reconstruct the missing calibration?",
    # Ask Evelyn to reconstruct the calibration.


    ("formula", "evelyn_story", "review"),

    "Evelyn studies the incomplete equations. "
    "For once, she stops correcting the finished parts. "
    '"These lines were overwritten, not lost. '
    'Use this reference key to separate them." '
    "She reconstructs the calibration key. "
    "Read the temporal formula again.",
    # Evelyn reconstructs the missing calibration.




    ("calibration_key",),
)


class GateCheckedState(PreviewState):
    """Align prerequisites with available actions."""

    def topics(self, actor):
        if actor not in self.objects():
            return []

        result = list(super().topics(actor))

        if actor == "evelyn" and self.mode == "explore":
            extra_topics = (
                (5, TOPIC_LIBRARY_ACCESS),
                (6, TOPIC_CALIBRATION),
            )

            for earliest, topic in extra_topics:
                if (
                    self.day >= earliest
                    and set(topic[2]) <= self.known
                    and not set(topic[4]) <= self.known
                ):
                    result.append(topic)

        return result

    def inspect(self, key):
        if (
            key == "side"
            and key in self.objects()
            and "library_access" not in self.known
        ):
            return (
                "The staff entrance is locked. "
                "You do not know its access sequence."
            )
            # The entrance needs an access sequence.


        if (
            key == "formula"
            and key in self.objects()
            and PACING_READ_REQUIRES.get(key, set()) <= self.known
            and "calibration_key" not in self.known
        ):
            self.learn("formula", PACING_PARTIAL_FORMULA)
            text = PACING_PARTIAL_FORMULA

            if self.day >= 6:
                text += (
                    "\n\nYou need someone who understands this notation "
                    "to reconstruct the calibration."
                )
                # Someone familiar with the notation must help.


            return text

        return super().inspect(key)

    def use(self, key):
        if (
            key == "side"
            and key in self.objects()
            and "library_access" not in self.known
        ):
            return "You have not learned the staff access sequence."
            # The access sequence has not been obtained.


        return super().use(key)

    def tasks(self):
        # Remove instructions that no longer match the revised rules.

        outdated = {
            "Investigate the library side entrance shown on Lily's sketch.",
            "The formula is incomplete. Read it again on a later Monday.",
            "Return to finance on a later Monday.",
            "Examine the finance documents, then speak to Adrian.",
        }

        result = [
            text for text in super().tasks()
            if text not in outdated
        ]

        known = self.known

        if "finance_code" in known and "truth_funding" not in known:
            if not {"report", "debt", "fund_mark"} <= known:
                result.append(
                    "Use the confirmed code to open finance "
                    "and examine its documents."
                )
                # Use the confirmed code now.

            else:
                result.append(
                    "Discuss the finance evidence with Adrian "
                    "during his afternoon cafe shift."
                )
                # Discuss the evidence during Adrian's afternoon shift.


        if self.day >= 5 and "map" in known and "formula" not in known:
            if "library_access" not in known:
                result.append(
                    "Ask Evelyn at the library "
                    "about the marks on Lily's sketch."
                )
                # Ask Evelyn about the sketch.

            else:
                result.append(
                    "Use Evelyn's access sequence "
                    "at the library service entrance."
                )
                # Use Evelyn's sequence to open the service entrance.


        if "formula" in known and "full_formula" not in known:
            if "calibration_key" in known:
                result.append(
                    "Read the temporal formula again "
                    "using Evelyn's calibration key."
                )
                # Re-read the formula with the calibration key.


            elif self.day >= 6:
                result.append(
                    "Ask Evelyn to reconstruct the calibration; "
                    "bring the formula and Voss's review."
                )
                # Bring both documents to Evelyn.


            else:
                result.append(
                    "Keep the partial formula and research review. "
                    "The calibration is still missing."
                )
                # Keep the incomplete research materials.


        return result

PreviewState = GateCheckedState
story.GameState = PreviewState

ROOT_DIR = Path(__file__).resolve().parent
ART_DIR = ROOT_DIR / "assets"

# Recovered materials are displayed in a separate row.

PAPER_ITEMS = {
    "report", "debt", "letter", "map",
    "voice", "aid", "transport",
}


class PixelGame(GameApp):
    """Connect the story to the pixel scenes."""

    def __init__(self, root):
        self.room = None
        self.context = None
        self.image_bounds = None
        self.picture = None
        self.backgrounds = {}
        self.scaled_background = None
        self.cast_sheet = None
        self.cast_cells = {}
        self.sprite_cache = {}
        self.sprite_refs = []
        self.actor_images = {}
        self.foreground_key = None
        self.foreground_picture = None
        self.hitboxes = []
        self.hovered = None
        self.popups = []
        self.current_scene = "bedroom"
        self.scene_scrollbar = None
        self.generation = 0

        super().__init__(root)

        width = min(1180, max(640, root.winfo_screenwidth() - 80))
        height = min(860, max(480, root.winfo_screenheight() - 100))
        root.geometry(f"{width}x{height}")
        root.minsize(min(980, width), min(700, height))
        root.protocol("WM_DELETE_WINDOW", self.close_game)

    def button(self, parent, text, command):
        """Create readable buttons."""
        button = super().button(parent, text, command)
        button.configure(
            font=("Arial", 12),
            bg="#263647",
            fg="#eee5d0",
            activebackground="#40556a",
            relief="solid",
            bd=1,
            padx=10,
            pady=6,
        )
        return button

    def build(self):
        """Keep a large picture and compact narration."""
        super().build()

        left = self.canvas.master
        main_panel = left.master

        main_panel.grid_columnconfigure(0, weight=1, uniform="")
        main_panel.grid_columnconfigure(1, weight=0, uniform="")
        main_panel.grid_rowconfigure(1, weight=0)
        left.grid_configure(columnspan=2, padx=0)

        self.scene_scrollbar = next(
            (
                widget
                for widget in left.winfo_children()
                if isinstance(widget, tk.Scrollbar)
            ),
            None,
        )

        if self.scene_scrollbar is not None:
            self.scene_scrollbar.pack_forget()

        self.story.grid_forget()
        self.story.configure(
            height=4,
            pady=8,
            font=("Arial", 15),
            bg="#17212d",
        )
        self.story.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(6, 0),
        )
        self.story.vbar.pack_forget()

        header = self.root.grid_slaves(row=0, column=0)[0]
        title = header.winfo_children()[0]
        title.configure(
            font=("Arial", 20, "bold"),
            fg="#eee5d0",
        )
        title.pack_configure(padx=14, pady=10)

        self.status.pack_forget()
        self.status = tk.Label(
            header,
            bg="#171e2c",
            fg="#b7cae0",
            font=("Arial", 11),
            wraplength=260,
            justify="left",
        )
        self.status.pack(side="left", padx=10, pady=5)

        for button in self.action_buttons:
            button.pack_forget()

        self.selection.pack_forget()
        self.selection.master.pack_configure(padx=12, pady=3)

        self.button(
            self.selection.master,
            "SCENE ITEMS",
            self.show_objects,
        ).pack(side="left")
        # List all currently available interactions.


        self.canvas.bind(
            "<Configure>",
            self.resize_view,
            add="+",
        )

    def popup(self, title, width=650, height=520, locked=False):
        """Open one modal window."""
        self.close_popups()

        window = tk.Toplevel(self.root)
        window.title(title)
        window.configure(bg="#192330")

        x = self.root.winfo_rootx() + 60
        y = self.root.winfo_rooty() + 70
        window.geometry(f"{width}x{height}+{x}+{y}")

        window.transient(self.root)
        window.grab_set()
        window.minsize(420, 300)
        self.popups.append(window)

        if locked:
            window.protocol("WM_DELETE_WINDOW", lambda: None)

        return window

    def close_popups(self):
        for window in self.popups:
            if window.winfo_exists():
                window.destroy()
        self.popups.clear()

    def close_context(self):
        if self.context is not None:
            self.context.destroy()
            self.context = None

        if self.room is not None and self.room.winfo_exists():
            self.room.delete("context")

    def clear(self):
        self.generation += 1
        self.close_context()
        self.close_popups()
        self.room = None
        self.image_bounds = None
        self.hitboxes = []
        self.hovered = None
        self.sprite_refs = []
        super().clear()

    def status_text(self):
        state = self.state

        if state.ending == "void":
            return "BETWEEN MOMENTS"


        prefix = f"LOOP {state.day} | " if state.knows_loop else ""

        if state.ending in {"normal", "reversal"}:
            date = "TUESDAY 07:00"
        else:
            date = f"MONDAY {state.clock}"

        visits = ""
        if state.mode == "explore":
            visits = f" | {state.visits}/2 VISITS"

        return (
            f"{prefix}{date} | "
            f"{story.PLACES[state.location]}{visits}"
        )

    def render(self):
        self.clear()
        state = self.state
        self.status.configure(text=self.status_text())
        self.current_scene = art.scene_key(state)

        if state.mode in {"ending", "verdict"}:
            self.current_scene = (
                "kitchen" if state.ending == "normal" else "lab"
            )

        self.room = tk.Canvas(
            self.body,
            height=max(300, self.canvas.winfo_height()),
            bg="#101820",
            highlightthickness=0,
        )
        self.room.pack(fill="both", expand=True)
        self.room.bind("<Configure>", self.paint_scene)
        self.room.bind("<Motion>", self.pointer_move)
        self.room.bind("<Leave>", self.pointer_leave)
        self.room.bind("<Button-1>", self.scene_click)

        self.navigation()

        if state.mode == "ending":
            self.tell(story.ENDINGS[state.ending][1])

        elif state.mode == "verdict":
            self.tell(
                "The live observer link remains open. "
                "Make your final choice."
            )
            # Make the final choice while the connection remains open.

            self.root.after_idle(self.open_verdict)

        elif state.mode in {"explore", "reverse"} and not state.active:
            self.root.after_idle(self.open_pending_map)

    def open_pending_map(self):
        if (
            self.state.mode in {"explore", "reverse"}
            and not self.state.active
            and not self.busy
        ):
            self.map()

    def resize_view(self, event):
        if self.room is not None and self.room.winfo_exists():
            self.room.configure(height=max(240, event.height))

    def background(self, name):
        if name not in self.backgrounds:
            image = tk.PhotoImage(
                master=self.root,
                file=str(ART_DIR / art.SCENE_FILES[name]),
            )
            factor = max(
                1,
                min(image.width() // 480, image.height() // 270),
            )
            self.backgrounds[name] = image.subsample(factor)

        return self.backgrounds[name]

    def sprite(self, actor, height):
        """Scale the body rather than the transparent tile."""
        if actor not in self.cast_cells:
            if self.cast_sheet is None:
                self.cast_sheet = tk.PhotoImage(
                    master=self.root,
                    file=str(ART_DIR / art.CAST_FILE),
                )

            cell_width = (
                self.cast_sheet.width() // art.CAST_COLUMNS
            )
            cell_height = (
                self.cast_sheet.height() // art.CAST_ROWS
            )
            index = art.CAST_INDEX[actor]

            origin_x = index % art.CAST_COLUMNS * cell_width
            origin_y = index // art.CAST_COLUMNS * cell_height

            bounds = SPRITE_BOUNDS[actor]
            x1 = int(bounds[0] * cell_width / 384)
            y1 = int(bounds[1] * cell_height / 512)
            x2 = int(bounds[2] * cell_width / 384)
            y2 = int(bounds[3] * cell_height / 512)

            cell = tk.PhotoImage(
                master=self.root,
                width=x2 - x1,
                height=y2 - y1,
            )
            cell.tk.call(
                cell,
                "copy",
                self.cast_sheet,
                "-from",
                origin_x + x1,
                origin_y + y1,
                origin_x + x2,
                origin_y + y2,
                "-to",
                0,
                0,
            )
            self.cast_cells[actor] = cell

        cell = self.cast_cells[actor]
        target = max(48, int(height))
        cache_key = (actor, target)

        if cache_key not in self.sprite_cache:
            ratio = Fraction(
                target,
                cell.height(),
            ).limit_denominator(64)

            numerator = ratio.numerator
            denominator = ratio.denominator

            # Scale each axis separately to limit temporary memory.

            vertical = cell.zoom(
                1, numerator
            ).subsample(
                1, denominator
            )
            picture = vertical.zoom(
                numerator, 1
            ).subsample(
                denominator, 1
            )

            if len(self.sprite_cache) >= 48:
                oldest = next(iter(self.sprite_cache))
                self.sprite_cache.pop(oldest)

            self.sprite_cache[cache_key] = picture

        return self.sprite_cache[cache_key]

    def rectangle(self, area):
        left, top, width, height = self.image_bounds
        x1, y1, x2, y2 = area

        return (
            left + x1 * width,
            top + y1 * height,
            left + x2 * width,
            top + y2 * height,
        )

    def paint_scene(self, event=None):
        """Draw people behind foreground furniture."""
        if self.room is None or not self.room.winfo_exists():
            return

        if event is not None and event.widget is not self.room:
            return

        width = self.room.winfo_width()
        height = self.room.winfo_height()
        if min(width, height) < 20:
            return

        self.close_context()
        self.room.delete("all")
        self.hovered = None
        self.hitboxes = []
        self.actor_images = {}
        self.sprite_refs = []

        state = self.state
        available = state.objects()
        papers = [
            key for key in available
            if key in PAPER_ITEMS
        ]

        tray_height = (
            56 if papers and state.mode != "ending" else 0
        )

        image = self.background(self.current_scene)
        fit = min(
            (width - 12) / image.width(),
            (height - tray_height - 12) / image.height(),
        )
        step = max(1, min(12, int(fit * 4)))
        cache_key = (self.current_scene, step)

        if self.scaled_background != cache_key:
            self.picture = image.zoom(step).subsample(4)
            self.scaled_background = cache_key

        image_width = self.picture.width()
        image_height = self.picture.height()
        left = (width - image_width) // 2
        top = (height - tray_height - image_height) // 2

        self.image_bounds = (
            left,
            top,
            image_width,
            image_height,
        )
        self.room.create_image(
            left,
            top,
            image=self.picture,
            anchor="nw",
        )

        dusk = (
            self.evening_scene()
            and self.current_scene != "bedroom_night"
        )

        if dusk:
            self.room.create_rectangle(
                left,
                top,
                left + image_width,
                top + image_height,
                fill="#17233b",
                stipple="gray50",
                outline="",
            )

        if state.mode == "ending":
            self.room.create_rectangle(
                left,
                top + image_height * 0.3,
                left + image_width,
                top + image_height * 0.7,
                fill="#111b27",
                outline="",
            )
            self.room.create_text(
                left + image_width / 2,
                top + image_height / 2,
                text=story.ENDINGS[state.ending][0],
                fill="#f5ead0",
                font=("Arial", 26, "bold"),
                width=max(200, image_width - 40),
            )
            return

        zones = art.SCENE_HOTSPOTS[self.current_scene]

        for key in available:
            if key not in zones or key in PAPER_ITEMS:
                continue

            box = self.rectangle(zones[key])
            self.hitboxes.append((key, box, "object"))

            if (
                self.current_scene in {"bedroom", "bedroom_night"}
                and key == "milk"
            ):
                self.room.create_rectangle(
                    *box,
                    fill="#ddd3b9",
                    outline="#6c604b",
                )
                self.room.create_text(
                    (box[0] + box[2]) / 2,
                    (box[1] + box[3]) / 2,
                    text="MILK",
                    fill="#242b31",
                    font=("Arial", 10),
                )

        if state.mode == "intro" and state.intro_index == 0:
            zone = art.DOOR_ZONES["bedroom"]["continue"]
            self.hitboxes.append(
                ("@continue", self.rectangle(zone), "door")
            )

        actors = [
            key for key in available
            if key in story.CHAR_NAMES
        ]

        ambient = []
        if state.mode == "intro" and state.intro_index == 13:
            ambient = ["mara"]

        foreground = FOREGROUND_TOP.get(self.current_scene)
        if foreground is not None:
            cutoff = top + int(image_height * foreground)
        else:
            cutoff = top + image_height

        for actor in actors + ambient:
            center_x, feet_y, size = (
                art.ACTOR_POSITIONS[self.current_scene].get(
                    actor,
                    (0.65, 0.85, 0.54),
                )
            )

            picture = self.sprite(
                actor,
                int(image_height * size),
            )
            self.sprite_refs.append(picture)

            x = max(
                left + picture.width() / 2 + 3,
                min(
                    left + center_x * image_width,
                    left + image_width - picture.width() / 2 - 3,
                ),
            )
            y = top + feet_y * image_height

            # A small ground shadow helps connect feet to the floor.

            self.room.create_oval(
                x - picture.width() * 0.32,
                y - 4,
                x + picture.width() * 0.32,
                y + 4,
                fill="#17212a",
                outline="",
                stipple="gray50",
            )

            self.room.create_image(
                x,
                y,
                image=picture,
                anchor="s",
            )

            if actor in actors:
                visible_bottom = min(y, cutoff)
                box = (
                    x - picture.width() * 0.46,
                    y - picture.height(),
                    x + picture.width() * 0.46,
                    visible_bottom,
                )
                self.hitboxes.append((actor, box, "actor"))
                self.actor_images[actor] = (
                    picture,
                    x - picture.width() / 2,
                    y - picture.height(),
                )

        if foreground is not None and actors + ambient:
            # Redraw the desk over the lower body.

            row = int(image_height * foreground)
            foreground_key = (cache_key, row)

            if self.foreground_key != foreground_key:
                self.foreground_picture = tk.PhotoImage(
                    master=self.root,
                    width=image_width,
                    height=image_height - row,
                )
                self.foreground_picture.tk.call(
                    self.foreground_picture,
                    "copy",
                    self.picture,
                    "-from",
                    0,
                    row,
                    image_width,
                    image_height,
                    "-to",
                    0,
                    0,
                )
                self.foreground_key = foreground_key

            self.room.create_image(
                left,
                top + row,
                image=self.foreground_picture,
                anchor="nw",
            )

            if dusk:
                self.room.create_rectangle(
                    left,
                    top + row,
                    left + image_width,
                    top + image_height,
                    fill="#17233b",
                    stipple="gray50",
                    outline="",
                )

        if tray_height:
            # Recovered materials get their own clean row.

            y1 = height - tray_height + 7
            y2 = height - 7

            self.room.create_text(
                12,
                (y1 + y2) / 2,
                anchor="w",
                text="FOUND ITEMS",
                fill="#b7cae0",
                font=("Arial", 10, "bold"),
            )

            card_width = min(
                310,
                (width - 150) / len(papers) - 8,
            )

            for index, key in enumerate(papers):
                x1 = 142 + index * (card_width + 8)
                box = (
                    x1,
                    y1,
                    x1 + card_width,
                    y2,
                )

                self.room.create_rectangle(
                    *box,
                    fill="#263647",
                    outline="#71849a",
                )
                self.room.create_text(
                    x1 + card_width / 2,
                    (y1 + y2) / 2,
                    text=story.OBJECTS[key][0],
                    fill="#f1e6cf",
                    font=("Arial", 11, "bold"),
                    width=card_width - 10,
                )
                self.hitboxes.append((key, box, "object"))

    def evening_scene(self):
        state = self.state

        if state.mode == "home":
            return True

        if state.mode == "explore" and state.phase == 2:
            return True

        return (
            state.mode == "intro"
            and state.intro_index in {13, 14, 15, 16}
        )

    def find_hit(self, x, y):
        allowed = set(self.state.objects())
        hits = []

        for key, box, kind in self.hitboxes:
            if key != "@continue" and key not in allowed:
                continue

            if key == "@continue":
                if not (
                    self.state.mode == "intro"
                    and self.state.intro_index == 0
                ):
                    continue

            if box[0] <= x <= box[2] and box[1] <= y <= box[3]:
                if kind == "actor" and key in self.actor_images:
                    picture, actor_x, actor_y = self.actor_images[key]
                    pixel_x = int(x - actor_x)
                    pixel_y = int(y - actor_y)

                    if not (
                        0 <= pixel_x < picture.width()
                        and 0 <= pixel_y < picture.height()
                    ):
                        continue

                    if picture.transparency_get(pixel_x, pixel_y):
                        continue

                area = (
                    (box[2] - box[0])
                    * (box[3] - box[1])
                )
                priority = 0 if kind == "actor" else 1
                hits.append((priority, area, key, box))

        if hits:
            result = min(hits, key=lambda row: row[:2])
            return result[2], result[3]

        return None, None

    def pointer_move(self, event):
        if self.busy or self.room is None:
            return

        key, box = self.find_hit(event.x, event.y)
        if key == self.hovered:
            return

        self.hovered = key
        self.room.delete("hover")
        self.room.configure(cursor="hand2" if key else "")

        if key is None:
            return

        name = "HALLWAY" if key == "@continue" else self.label(key)

        self.room.create_rectangle(
            *box,
            outline="#f0d899",
            width=2,
            tags="hover",
        )
        self.room.create_text(
            (box[0] + box[2]) / 2,
            max(18, box[1] - 5),
            text=name,
            anchor="s",
            fill="white",
            font=("Arial", 12, "bold"),
            tags="hover",
        )

    def pointer_leave(self, event):
        if self.room is not None and self.room.winfo_exists():
            self.room.delete("hover")
            self.room.configure(cursor="")

        self.hovered = None

    def label(self, key):
        return story.CHAR_NAMES.get(
            key,
            story.OBJECTS.get(key, (key, ""))[0],
        )

    def select(self, key):
        """Select without overwriting narration."""
        if self.busy or key not in self.state.objects():
            return

        self.selected = key
        self.selection.configure(text=self.label(key))

    def scene_click(self, event):
        if self.busy:
            return

        key, _ = self.find_hit(event.x, event.y)
        self.close_context()

        if key is None:
            return

        self.context = tk.Frame(
            self.room,
            bg="#d7ccb1",
            bd=2,
            relief="solid",
        )

        if key == "@continue":
            choices = [("CONTINUE", "continue")]
        elif key in story.CHAR_NAMES:
            choices = [("TALK", "talk")]
        else:
            choices = [
                ("LOOK", "look"),
                ("TAKE", "take"),
                ("USE", "use"),
            ]

        token = self.generation

        for caption, action in choices:
            self.button(
                self.context,
                caption,
                lambda k=key, a=action, t=token:
                    self.run_action(k, a, t),
            ).pack(fill="x", padx=1, pady=1)

        self.context.update_idletasks()

        if self.context is None or not self.context.winfo_exists():
            return

        x = max(
            0,
            min(
                event.x + 10,
                self.room.winfo_width()
                - self.context.winfo_reqwidth(),
            ),
        )
        y = max(
            0,
            min(
                event.y + 8,
                self.room.winfo_height()
                - self.context.winfo_reqheight(),
            ),
        )

        self.room.create_window(
            x,
            y,
            window=self.context,
            anchor="nw",
            tags="context",
        )

    def run_action(self, key, action, token=None):
        if self.busy:
            return

        if token is not None and token != self.generation:
            return

        self.close_context()
        self.close_popups()

        if key == "@continue":
            self.intro_next()
            return

        if key not in self.state.objects():
            return

        self.select(key)

        if action == "talk" or key in story.CHAR_NAMES:
            self.dialogue(key)

        elif action == "look":
            text = self.state.inspect(key)
            self.render()
            self.tell(text)

            if key == "projection":
                self.recording(text)

        elif action == "take":
            text = self.state.take(key)
            self.render()
            self.tell(text)

        elif key == "bed":
            can_sleep = (
                self.state.mode == "home"
                or (
                    self.state.mode == "intro"
                    and self.state.intro_index == len(story.INTRO) - 1
                )
            )

            if can_sleep:
                self.sleep()
            else:
                self.tell(
                    "You are not ready to sleep. "
                    "There is still daylight outside."
                )
                # It is still daytime.


        elif key == "menu":
            self.order_food()

        elif key == "console":
            self.console()

        elif key == "projection":
            text = self.state.inspect(key)
            self.render()
            self.tell(text)
            self.recording(text)

        else:
            text = self.state.use(key)
            self.render()
            self.tell(text)

    def show_objects(self):
        """List available objects without adding extra discoveries."""
        if self.busy:
            return

        window = self.popup("SCENE ITEMS / 场景物品", 650, 570)

        view = tk.Canvas(
            window,
            bg="#192330",
            highlightthickness=0,
        )
        scrollbar = tk.Scrollbar(
            window,
            command=view.yview,
        )
        view.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        view.pack(fill="both", expand=True)

        frame = tk.Frame(view, bg="#192330")
        frame_id = view.create_window(
            0,
            0,
            window=frame,
            anchor="nw",
        )

        frame.bind(
            "<Configure>",
            lambda event: view.configure(
                scrollregion=view.bbox("all"),
            ),
        )
        view.bind(
            "<Configure>",
            lambda event: view.itemconfigure(
                frame_id,
                width=event.width,
            ),
        )

        for key in self.state.objects():
            row = tk.Frame(frame, bg="#192330")
            row.pack(fill="x", padx=12, pady=5)

            tk.Label(
                row,
                text=self.label(key),
                bg="#192330",
                fg="white",
                font=("Arial", 12),
                wraplength=260,
                justify="left",
            ).pack(side="left")

            if key in story.CHAR_NAMES:
                actions = [("TALK", "talk")]
            else:
                actions = [
                    ("LOOK", "look"),
                    ("TAKE", "take"),
                    ("USE", "use"),
                ]

            for caption, action in reversed(actions):
                self.button(
                    row,
                    caption,
                    lambda k=key, a=action:
                        self.run_action(k, a),
                ).pack(side="right", padx=2)

        if not self.state.objects():
            tk.Label(
                frame,
                text="Choose the next destination first.",
                bg="#192330",
                fg="white",
            ).pack(padx=20, pady=25)
            # Choose a destination before investigating.


    def dialogue(self, actor, response=None):
        if self.busy or actor not in self.state.objects():
            return

        window = self.popup(self.label(actor), 760, 590)

        tk.Label(
            window,
            text=self.label(actor),
            font=("Arial", 18, "bold"),
            bg="#192330",
            fg="#f1e6cf",
        ).pack(pady=15)

        if response:
            view = ScrolledText(
                window,
                wrap="word",
                height=6,
                font=("Arial", 15),
                bg="#111b26",
                fg="#f1eadb",
                padx=12,
                pady=10,
            )
            view.pack(
                fill="both",
                expand=True,
                padx=18,
                pady=(0, 10),
            )
            view.insert("1.0", response)
            view.configure(state="disabled")

        if self.state.mode == "reverse":
            correct = story.REVERSE[self.state.reverse_index][3]
            choices = [
                "Nothing you did ever mattered.",
                # Your actions never mattered.


                correct,

                "Forget the past and keep repeating this day.",
                # Forget the past and continue repeating.

            ]

            for answer in choices:
                self.button(
                    window,
                    answer,
                    lambda value=answer: self.release(value),
                ).pack(fill="x", padx=22, pady=8)

        else:
            for topic in self.state.topics(actor):
                self.button(
                    window,
                    topic[1],
                    lambda value=topic[0]:
                        self.ask(actor, value),
                ).pack(fill="x", padx=22, pady=7)

        self.button(
            window,
            "BACK",
            self.close_popups,
        ).pack(pady=12)

    def ask(self, actor, topic):
        response = self.state.talk(actor, topic)
        self.render()
        self.tell(response)
        self.dialogue(actor, response)

    def order_food(self):
        if "menu" not in self.state.objects() or self.busy:
            return

        window = self.popup("ORDER / 点单", 620, 410)

        if "mara" in self.state.objects():
            lines = [
                '"I need another shift," Mara says.',
                # Mara needs another shift.


                '"Something warm helps me keep going," Mara says.',
                # Warmth helps Mara keep going.


                '"I should eat something too," Mara says.',
                # Mara should eat something.

            ]

        elif "adrian" in self.state.objects():
            lines = [
                '"Long day?" Adrian asks.',
                # Adrian asks if the day has been tiring.


                '"Some people order the same thing every day."',
                # Some people repeat the same order daily.


                '"I used to work nearby." He changes the subject.',
                # Adrian mentions his previous workplace, then avoids it.

            ]

        else:
            lines = [
                "You drink a bitter coffee.",
                # You drink a bitter coffee.


                "Steam rises from your tea.",
                # Steam rises from the tea.


                "You finish a simple meal.",
                # You finish a simple meal.

            ]

        for caption, line in zip(
            ("COFFEE", "TEA", "SANDWICH SET"),
            lines,
        ):
            self.button(
                window,
                caption,
                lambda value=line: self.food_chosen(value),
            ).pack(fill="x", padx=25, pady=10)

        self.button(
            window,
            "BACK",
            self.close_popups,
        ).pack(pady=12)

    def map(self):
        if self.busy:
            return

        if self.state.mode not in {"dawn", "explore", "reverse"}:
            return

        state = self.state
        locked = state.mode != "dawn" and not state.active

        window = self.popup(
            "DESTINATIONS / 地图",
            690,
            530,
            locked=locked,
        )

        if state.mode == "reverse":
            title = "REVERSE ROUTE"
        else:
            title = (
                f"{story.PHASES[state.phase]}"
                f" — {state.visits}/2 VISITS"
            )

        tk.Label(
            window,
            text=title,
            font=("Arial", 18, "bold"),
            bg="#192330",
            fg="#f0e4c9",
        ).pack(pady=18)

        grid = tk.Frame(window, bg="#192330")
        grid.pack(fill="both", expand=True, padx=20)

        for column in (0, 1):
            grid.grid_columnconfigure(column, weight=1)

        for index, (place, caption) in enumerate(story.PLACES.items()):
            button = self.button(
                grid,
                caption,
                lambda value=place: self.travel(value),
            )
            button.grid(
                row=index // 2,
                column=index % 2,
                sticky="nsew",
                padx=8,
                pady=9,
                ipady=10,
            )

            if state.mode != "reverse":
                unavailable = (
                    state.visits >= 2
                    or (
                        state.mode == "dawn"
                        and place == "Home"
                    )
                )

                if unavailable:
                    button.configure(state="disabled")

        if state.mode == "reverse":
            note = (
                "Follow the original anchors in reverse. "
                "A wrong destination ends the attempt."
            )
            # Follow the original anchors backwards.

        else:
            note = (
                "Choosing a destination uses one visit. "
                "Investigating and talking are free."
            )
            # One visit per destination; interactions are free.


        tk.Label(
            window,
            text=note,
            font=("Arial", 12),
            wraplength=610,
            bg="#192330",
            fg="#b7cae0",
        ).pack(pady=15)

        if not locked:
            self.button(
                window,
                "BACK",
                self.close_popups,
            ).pack(pady=10)

    def travel(self, place):
        if self.busy:
            return

        if self.state.mode == "reverse":
            confirmed = messagebox.askyesno(
                "REVERSE ROUTE",
                f"Travel to {story.PLACES[place]}?",
                parent=self.root,
            )

            if not confirmed:
                return

            self.state.reverse_enter(place)
            self.render()

            if self.state.mode != "ending":
                self.tell(
                    "A remembered scene forms around you. "
                    "Speak to the anchor."
                )
                # A remembered scene forms; speak to its anchor.


        elif self.state.enter(place):
            self.render()
            self.tell(
                "You arrive. Explore freely; "
                "objects and conversations do not spend time."
            )
            # Investigate freely during the visit.


    def navigation(self):
        for child in self.nav.winfo_children():
            child.destroy()

        for button in self.action_buttons:
            button.pack_forget()

        self.selection.pack_forget()

        if self.busy:
            self.nav.pack_forget()
            return

        state = self.state
        options = []

        if state.mode == "intro":
            if 0 < state.intro_index < len(story.INTRO) - 1:
                options = [("CONTINUE", self.intro_next)]
            elif state.intro_index == len(story.INTRO) - 1:
                options = [("SLEEP", self.sleep)]

        elif state.mode == "dawn":
            options = [("GO OUT", self.map)]

        elif state.mode == "explore":
            options = [
                ("MAP", self.map),
                ("END PHASE", self.end_phase),
                ("END OUTING", self.go_home),
            ]
            if state.area == "lab":
                options.append(
                    ("BACK TO LIBRARY", self.leave_lab)
                )

        elif state.mode == "home":
            options = [
                ("SLEEP", self.sleep),
                ("STAY AWAKE", self.stay_awake),
            ]

        elif state.mode == "reverse":
            options = [("NEXT ANCHOR", self.map)]

        if options:
            self.nav.pack(
                fill="x",
                padx=16,
                pady=(2, 7),
            )

            for caption, command in options:
                self.button(
                    self.nav,
                    caption,
                    command,
                ).pack(side="left", padx=(0, 7))

        else:
            self.nav.pack_forget()

    def intro_next(self):
        if self.busy or self.state.mode != "intro":
            return

        if self.state.intro_index == 0:
            ready = (
                "alarm_off" in self.state.events
                and "phone" in self.state.known
            )

            if not ready:
                self.tell(
                    "Stop the alarm and read your phone "
                    "before leaving."
                )
                # Stop the alarm and read the phone first.

                return

        text = self.state.intro_next()
        self.render()
        self.tell(text)

    def end_phase(self):
        if self.busy or not self.state.end_phase():
            return

        self.render()

        if self.state.mode == "home":
            self.tell(
                "22:00. You return home. "
                "Sleep, or watch the date change."
            )
            # Return home, then sleep or watch the date.


    def console(self):
        if self.busy or "console" not in self.state.objects():
            return

        if (
            self.state.day < 6
            or "full_formula" not in self.state.known
        ):
            self.tell(
                "The terminal needs a complete calibration. "
                "The equations are still incomplete."
            )
            # The terminal needs the completed formula.

            return

        window = self.popup(
            "TRUTH CONSOLE / 真相控制台",
            730,
            610,
        )

        tk.Label(
            window,
            text="RECONSTRUCT THE CAUSAL ORDER",
            font=("Arial", 17, "bold"),
            bg="#192330",
            fg="#f0e4c9",
        ).pack(pady=16)
        # Reconstruct the causal order.


        if len(self.state.truths) < 5:
            tk.Label(
                window,
                text="All five accounts are required.",
                bg="#192330",
                fg="white",
            ).pack(pady=25)
            # All five accounts are required.


        else:
            order = " > ".join(
                story.TRUTH_NAMES[key]
                for key in self.state.order
            )

            tk.Label(
                window,
                text=order or "Choose the first cause.",
                wraplength=650,
                bg="#192330",
                fg="white",
                font=("Arial", 12),
            ).pack(pady=12)
            # Choose the first cause.


            for key in story.TRUTH_ORDER:
                if key not in self.state.order:
                    self.button(
                        window,
                        story.TRUTH_NAMES[key],
                        lambda value=key:
                            self.order_piece(value),
                    ).pack(fill="x", padx=25, pady=5)

            self.button(
                window,
                "CLEAR ORDER",
                self.clear_order,
            ).pack(pady=8)

            if "order_solved" in self.state.known:
                if self.state.day == 7:
                    self.button(
                        window,
                        "START REVERSE",
                        self.begin_reverse,
                    ).pack(pady=8)
                    # Begin the reverse sequence.


                else:
                    tk.Label(
                        window,
                        text="FINAL SYNCHRONISATION: MONDAY 7",
                        font=("Arial", 12, "bold"),
                        bg="#192330",
                        fg="#b7cae0",
                    ).pack(pady=8)
                    # Final synchronisation becomes available on Monday seven.

        self.button(
            window,
            "BACK",
            self.close_popups,
        ).pack(pady=10)

    def begin_reverse(self):
        if not self.state.begin_reverse():
            self.tell(
                "Solve the order first. "
                "The final reverse begins on Monday seven."
            )
            # Solve the order; begin on Monday seven.

            return

        self.render()

    def release(self, answer):
        if not self.state.release(answer):
            response = (
                "The memory does not connect. "
                "Read the evidence and try another response."
            )
            # Try another response after reviewing the evidence.


            self.tell(response)
            actor = story.REVERSE[self.state.reverse_index][1]
            self.dialogue(actor, response)
            return

        self.render()

    def open_verdict(self):
        if self.state.mode != "verdict":
            return

        window = self.popup(
            "THE FINAL CHOICE / 最后的选择",
            700,
            420,
            locked=True,
        )

        tk.Label(
            window,
            text="The live observer link is still open.",
            font=("Arial", 16),
            bg="#192330",
            fg="white",
            wraplength=620,
        ).pack(padx=20, pady=30)
        # The observer link remains open.


        self.button(
            window,
            "Release everyone and close the link.",
            lambda: self.finish("normal"),
        ).pack(fill="x", padx=25, pady=10)
        # Release everyone and close the link.


        self.button(
            window,
            "Transfer the anchor to Voss.",
            lambda: self.finish("reversal"),
        ).pack(fill="x", padx=25, pady=10)
        # Transfer the anchor to Voss.


    def document(self, title, text):
        if self.busy:
            return

        window = self.popup(title, 740, 570)

        view = ScrolledText(
            window,
            wrap="word",
            font=("Arial", 14),
            bg="#192330",
            fg="#f1eadb",
            padx=20,
            pady=18,
        )
        view.pack(fill="both", expand=True)
        view.insert("1.0", text)
        view.configure(state="disabled")

    def help(self):
        """Explain controls without revealing future story."""
        text = (
            "Move the pointer over the picture "
            "to find objects and people.\n"
            "Click an object to LOOK, TAKE or USE. "
            "Click a person to TALK.\n"
            "SCENE ITEMS lists the same interactions "
            "if an item is hard to find.\n\n"
            # Hover to discover; click to interact.


            "JOURNAL stores important discoveries. "
            "INVENTORY holds items. "
            "SAVE and LOAD manage your progress.\n\n"
            # Journal, inventory, save and load.

        )

        if self.state.day == 1:
            text += (
                "USE the alarm clock and LOOK at your phone. "
                "Then click the brown door and CONTINUE. "
                "Complete each ordinary task before moving on."
            )
            # Complete the ordinary morning tasks.



        else:
            text += (
                "GO OUT opens the map. "
                "Each phase allows two destinations. "
                "Looking, taking, using and talking "
                "do not spend visits. "
                "END PHASE advances the time of day; "
                "END OUTING returns home.\n\n"
                # Two destinations per phase; interactions are free.



                "A familiar object may contain a new detail "
                "once you have enough context. "
                "Revisit people at the same times and "
                "follow the leads in your journal."
                # Revisit after gathering more context.


            )

            if "beta" in self.state.known:
                text += (
                    "\n\nThe reserve lasts seven Mondays. "
                    "The order of events matters."
                )
                # Seven Mondays of reserve; order matters.


        self.document("HOW TO PLAY / 玩法", text)

    def recording(self, text):
        """Voss appears only in a recorded image."""
        window = self.popup(
            "VOSS — RECORDED MESSAGE / Voss录像",
            740,
            600,
        )

        picture = self.sprite("voss", 160)
        tk.Label(
            window,
            image=picture,
            bg="#192330",
        ).pack(side="top", pady=8)

        window.recording_picture = picture

        view = ScrolledText(
            window,
            wrap="word",
            font=("Arial", 14),
            bg="#192330",
            fg="#f1eadb",
            padx=20,
            pady=18,
        )
        view.pack(fill="both", expand=True)
        view.insert("1.0", text)
        view.configure(state="disabled")

    def close_game(self):
        for job in self.jobs:
            try:
                self.root.after_cancel(job)
            except tk.TclError:
                pass

        self.close_popups()
        self.root.destroy()


def check_assets():
    """Check required image files."""
    required = [
        ART_DIR / filename
        for filename in art.SCENE_FILES.values()
    ]
    required.append(ART_DIR / art.CAST_FILE)

    missing = [
        str(path.relative_to(ROOT_DIR))
        for path in required
        if not path.is_file()
    ]

    if missing:
        raise FileNotFoundError(
            "Missing game images / 缺少游戏图片:\n"
            + "\n".join(missing)
        )


def main():
    """Start the pixel-scene version."""
    root = tk.Tk()

    try:
        check_assets()
        PixelGame(root)
    except (OSError, ValueError, tk.TclError) as error:
        messagebox.showerror(
            "CANNOT START / 无法启动",
            str(error),
            parent=root,
        )
        root.destroy()
        return

    root.mainloop()


if __name__ == "__main__":
    main()