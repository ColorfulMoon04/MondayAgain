"""Monday, Again.

Run the pixel-art game:
    python pixel_preview.py

This module contains the story rules and shared interface.
Keep both Python files and the assets folder together.
Uses only the Python standard library; Tkinter is required.
Save data is stored in monday_save.json beside main.py.
"""

import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


PLACES = {
    "Home": "HOME",
    "Bus Stop": "BUS STOP",
    "Company": "COMPANY",
    "Cafe": "CAFE",
    "Hospital": "HOSPITAL",
    "Library": "LIBRARY",
}


PHASES = ("MORNING", "AFTERNOON", "EVENING")


TRUTH_ORDER = (
    "selection",
    "funding",
    "boundary",
    "sequence",
    "method",
)

TRUTH_NAMES = {
    "selection": "SELECTION",
    "funding": "FUNDING",
    "boundary": "BOUNDARY",
    "sequence": "SEQUENCE",
    "method": "METHOD",
}


TRUTH_DAYS = {
    "truth_selection": 3,
    "truth_funding": 4,
    "truth_boundary": 4,
    "truth_sequence": 5,
    "truth_method": 6,
}



SAVE_PATH = Path(__file__).resolve().with_name("monday_save.json")




OBJECTS = {
    "window": (
        "WINDOW",
        "A bird taps twice. The number 17 bus passes the window.",
    ),


    "clock": (
        "ALARM CLOCK",
        "The alarm is set for 07:00.",
    ),


    "phone": (
        "PHONE",
        'Monday. Your manager writes: '
        '"Come and see me. We need to discuss your work."',
    ),



    "sink": (
        "WASHBASIN",
        "Your toothbrush and towel are beside the tap.",
    ),


    "mirror": (
        "MIRROR",
        "You look tired. You need a shave.",
    ),


    "razor": (
        "RAZOR",
        "Your usual razor rests beside the mirror.",
    ),


    "breakfast": (
        "BREAKFAST",
        "Bread and milk are on the table.",
    ),


    "milk": (
        "MILK",
        "Half a glass of milk remains from breakfast.",
    ),


    "calendar": (
        "CALENDAR",
        "Monday, 12 October. An ordinary working day.",
    ),


    "bed": (
        "BED",
        "Your bed is beside the window.",
    ),


    "mug": (
        "TRAVEL MUG",
        "Your empty travel mug is on the counter.",
    ),


    "mail": (
        "WORK EMAIL",
        "Adrian Cole from finance has received a serious "
        "disciplinary penalty.",
    ),


    "wrapper": (
        "GUM WRAPPER",
        'Three pieces remain. On the wrapper: 17-4-09. '
        '"The result never changes."',
    ),



    "folder": (
        "TRANSFER REQUEST",
        "A transfer request is waiting on your desk.",
    ),


    "office": (
        "FINANCE OFFICE",
        "The door is locked. A notice says to contact Adrian Cole.",
    ),


    "coffee": (
        "COFFEE MACHINE",
        "You need your own mug to get coffee.",
    ),


    "shipment": (
        "DELIVERY INVOICE",
        "Five temporal regulators were delivered to this district. "
        "Voss Research paid.",
    ),



    "report": (
        "INVESTMENT REPORT",
        "Different trades. The same final loss: $417,000. "
        "A heat-sensitive seal covers the sponsor.",
    ),



    "debt": (
        "DEBT CONTRACT",
        "Voss Research purchased Adrian's father's gambling debt "
        "and demanded financial services.",
    ),



    "menu": (
        "MENU",
        "Coffee, tea, and a sandwich set are available.",
    ),


    "photo": (
        "BOOK AND PHOTO",
        "A photograph inside the book shows two children: "
        "Noah and Lily Reed.",
    ),



    "newspaper": (
        "NEWSPAPER",
        "The Voss Foundation funded a children's home "
        "despite repeated complaints.",
    ),



    "mailbox": (
        "STAFF MAILBOX",
        "The mailbox has a combination lock.",
    ),


    "letter": (
        "RETURNED LETTERS",
        "Noah's complaints were routed directly to a Voss observer. "
        "They were read, then suppressed.",
    ),



    "map": (
        "LILY'S MAP",
        "Lily drew the experimental boundary "
        "and a side entrance to the library.",
    ),


    "bill": (
        "MEDICAL BILL",
        "A stack of bills is addressed to Mara Ellis. "
        "Every copy carries the same date.",
    ),



    "medical": (
        "MEDICAL RECORD",
        "Mara's mother died after a long illness. "
        "Another appointment card belongs to Lily Reed.",
    ),



    "seat": (
        "WAITING CHAIR",
        "Your appointment number appears on the screen.",
    ),


    "cabinet": (
        "PHARMACY CABINET",
        "A patient's collection number is needed to open this cabinet.",
    ),


    "voice": (
        "OLD PHONE",
        "An unsent voice recording is stored on the phone. "
        "Use it to listen.",
    ),



    "aid": (
        "AID AGREEMENT",
        "Medical support was conditional on repeated psychological "
        "testing and entering the district.",
    ),



    "timetable": (
        "TIMETABLE",
        'Every service says "DELAYED". '
        "A regulator shipment used these route numbers.",
    ),



    "locker": (
        "STAFF LOCKER",
        "A staff identification code is required.",
    ),


    "transport": (
        "TRANSPORT LOG",
        "Activation: Mara/Hospital 09:00; "
        "Adrian/Company 11:00; Noah/Cafe 13:00; "
        "Daniel/Bus Stop 17:00; Evelyn/Library 19:00.",
    ),








    "notice": (
        "CLOSED NOTICE",
        "The library is closed on Mondays.",
    ),


    "side": (
        "SIDE DOOR",
        "A maintenance door is hidden behind the library.",
    ),


    "thesis": (
        "PERFECT PAPER",
        "Evelyn keeps correcting a paper already awarded full marks.",
    ),


    "review": (
        "VOSS'S REVIEW",
        'His proposal was rejected: '
        '"Brilliant, but without practical value."',
    ),



    "formula": (
        "TEMPORAL FORMULA",
        "A stable consciousness can anchor separated space. "
        "An unregistered observer can release it.",
    ),



    "lab": (
        "BASEMENT ENTRANCE",
        "The map and formula identify a hidden laboratory "
        "beneath the library.",
    ),



    "alpha": (
        "ALPHA RECORD",
        "Voss trapped five subjects. Their bodies became anchors; "
        "their memories began to erode.",
    ),



    "beta": (
        "BETA RECORD",
        "Before assimilation, the five copied their last autonomous "
        "consciousness into a second loop. "
        "Its reserve lasts seven Mondays.",
    ),



    "voss_log": (
        "VOSS'S DIARY",
        "He wanted years of research while the outside world "
        "barely moved. Being overtaken again terrified him.",
    ),



    "projection": (
        "VOSS RECORDING",
        '"Chronology is the structure of the experiment. '
        'Release the anchors in reverse." '
        "This is a recording, not a live conversation.",
    ),




    "scanner": (
        "RESONANCE SCANNER",
        "The outside observer's neural link remains active. "
        "A scan might identify another possible anchor.",
    ),



    "console": (
        "TRUTH CONSOLE",
        "Reconstruct the experiment's causal order "
        "before reversing it.",
    ),


}


CHAR_NAMES = {
    "manager": "MANAGER",
    "coworker": "COWORKER",
    "adrian": "ADRIAN COLE",
    "mara": "MARA ELLIS",
    "noah": "NOAH REED",
    "daniel": "DANIEL GREY",
    "evelyn": "EVELYN HART",
}




NOTES = {
    "window": "07:00: two taps on the window, then the number 17 bus.",


    "phone": "The manager requested a meeting at work.",


    "mail": "Adrian Cole has been penalized by the company.",


    "wrapper": "The gum wrapper reads 17-4-09.",


    "photo": "The children in the photograph are Noah and Lily Reed.",


    "newspaper": "Voss funded the children's home.",


    "bill": "Mara Ellis's medical bills repeat the same date.",


    "medical": "Mara's mother has died. Lily Reed also visited the hospital.",


    "shipment": "Voss paid for five regulators delivered to the district.",


    "report": "The investment report always ends at -$417,000.",


    "debt": "Voss bought Adrian's father's gambling debt.",


    "fund_mark": "Heat revealed the Temporal Segmentation Project sponsor.",


    "letter": "Noah's complaints were intercepted by Voss's observer.",


    "map": "Lily's map shows the boundary and library side door.",


    "voice": (
        'Mara\'s mother: "You do not have to save me '
        'to prove that you love me."'
    ),


    "aid": "Medical aid was used to screen and recruit subjects.",


    "transport": (
        "Original anchor order: Hospital 09, Company 11, "
        "Cafe 13, Bus Stop 17, Library 19."
    ),



    "thesis": "Evelyn cannot accept an already perfect result.",


    "review": "Voss's research was repeatedly rejected or overtaken.",


    "formula": "An unregistered consciousness can release the five anchors.",


    "finance_code": "Adrian confirmed the finance code: 17-4-09.",


    "mail_code": "Noah gave the staff mailbox combination.",


    "cabinet_code": "Mara gave the pharmacy collection number.",


    "locker_code": "Daniel remembered his staff locker code.",


    "mara_story": (
        "Mara kept earning money while her mother's illness progressed."
    ),


    "adrian_story": (
        "Adrian chased losses while Voss controlled the debt."
    ),


    "noah_story": "Noah's repeated calls for help were ignored.",


    "daniel_story": (
        "Daniel waited for a permanent job promised by the contractor."
    ),


    "evelyn_story": (
        "Evelyn tied her worth to being first, as Voss did."
    ),


    "truth_selection": (
        "SELECTION: stable patterns of pressure "
        "were used to choose the five."
    ),


    "truth_funding": (
        "FUNDING: aid and debt enabled Voss to control the subjects."
    ),


    "truth_boundary": (
        "BOUNDARY: the five were drawn into one prepared district."
    ),


    "truth_sequence": (
        "SEQUENCE: the anchor activation order forms the loop structure."
    ),


    "truth_method": (
        "METHOD: the five built Beta, lost their memories, "
        "and called the unregistered sixth subject."
    ),



    "midnight": "At 00:00, Tuesday changed back to the same Monday.",


    "alpha": "Alpha holds the five subjects' bodies and anchors.",


    "beta": (
        "Beta holds their last autonomous consciousness "
        "and can last only seven Mondays."
    ),



    "voss_log": "Voss sought unlimited research time to prove his worth.",


    "projection": (
        "Reverse the causal chain: Method, Sequence, "
        "Boundary, Funding, Selection."
    ),


    "voss_imprint": (
        "Voss has the strongest imprint. "
        "The live observer link permits anchor transfer."
    ),



    "order_solved": (
        "The causal order is solved. "
        "Reverse the five anchors on Monday seven."
    ),


}




TOPICS = {
    "manager": [
        (
            "meeting",
            "You asked to see me.",
            (),
            "Your manager asks for reports on time, then tells you "
            "to deliver the transfer request to finance before lunch.",
            ("assignment",),
        ),


    ],

    "coworker": [
        (
            "news",
            "What happened to Adrian?",
            (),
            "His decisions damaged the company's results. "
            "You feel unwell and plan to visit the hospital.",
            ("coworker_news",),
        ),



    ],

    "adrian": [
        (
            "ordinary",
            "How is your shift?",
            (),
            '"Long enough. Choose something from the menu." '
            "He avoids your eyes.",
            (),
        ),




        (
            "identity",
            "Are you Adrian from the finance email?",
            ("mail",),
            '"I used to be good at it. Then my father left me '
            "a gambling debt. Every attempt to recover "
            'made things worse."',
            ("adrian_story",),
        ),




        (
            "access",
            "The office is locked. Does 17-4-09 mean anything?",
            ("mail", "wrapper"),
            '"That is the access code. I wrote it on the wrapper. '
            'The reports are inside."',
            ("finance_code",),
        ),




        (
            "funding",
            "Voss bought the debt and fixed the losses.",
            ("adrian_story", "report", "debt", "fund_mark"),
            '"The debt was a leash. I moved his research money. '
            'We were recruited, not rescued." '
            "A memory returns: FUNDING.",
            ("truth_funding",),
        ),




    ],

    "mara": [
        (
            "ordinary",
            "Are you waiting for someone?",
            (),
            '"Just one more payment. Then it will be enough."',
            (),
        ),



        (
            "story",
            "Whose treatment are you paying for?",
            ("bill",),
            '"My mother. I worked every hour I could. '
            'Her illness still kept taking things away."',
            ("mara_story",),
        ),




        (
            "collection",
            "Can we check the collection record?",
            ("bill", "medical"),
            "She gives you the pharmacy collection number, "
            "then falls silent.",
            ("cabinet_code",),
        ),



        (
            "selection",
            "The aid programme was screening you.",
            ("mara_story", "voice", "aid"),
            '"They measured how I lived, not how she was treated. '
            'I was chosen before I ever entered the district." '
            "SELECTION returns.",
            ("truth_selection",),
        ),




    ],

    "noah": [
        (
            "ordinary",
            "Who are you waiting for?",
            (),
            '"My sister. There is a photo of us '
            'in a book at the cafe."',
            (),
        ),



        (
            "story",
            "I found your photograph.",
            ("photo",),
            '"I wrote to everyone. Nobody came. '
            "After a while, I stopped expecting "
            'anyone to listen."',
            ("noah_story",),
        ),




        (
            "mail",
            "What happened to the complaints?",
            ("photo", "newspaper"),
            "He remembers the cafe mailbox combination. "
            "The returned letters and Lily's drawing "
            "are still inside.",
            ("mail_code",),
        ),




        (
            "boundary",
            "The observer read your letters and mapped the district.",
            ("noah_story", "letter", "map"),
            '"They knew. They brought us into the same place. '
            'Lily drew where the ordinary streets stopped." '
            "BOUNDARY returns.",
            ("truth_boundary",),
        ),




    ],

    "daniel": [
        (
            "ordinary",
            "Which bus are you waiting for?",
            (),
            '"Not this one. The next one will be right."',
            (),
        ),



        (
            "story",
            "Have you worked on these routes?",
            ("timetable",),
            '"A contractor promised me a permanent job. '
            'I kept waiting for the next instruction."',
            ("daniel_story",),
        ),




        (
            "locker",
            "These routes match the equipment deliveries.",
            ("map", "shipment", "timetable"),
            "He recalls his staff locker code. "
            "A transport log should be inside.",
            ("locker_code",),
        ),



        (
            "sequence",
            "You were waiting for an activation signal.",
            ("daniel_story", "transport"),
            '"Five machines. Five signals. '
            'Their order held everything together." '
            "SEQUENCE returns.",
            ("truth_sequence",),
        ),




    ],

    "evelyn": [
        (
            "ordinary",
            "The library is closed. Why wait here?",
            (),
            '"There is still an error in my paper."',
            (),
        ),



        (
            "story",
            "This paper already has full marks.",
            ("thesis",),
            '"If I am not first, what am I worth? '
            'Voss used to ask the same question."',
            ("evelyn_story",),
        ),




        (
            "method",
            "We know who was chosen, how, where, and in what order.",
            (
                "evelyn_story",
                "review",
                "formula",
                "truth_selection",
                "truth_funding",
                "truth_boundary",
                "truth_sequence",
            ),
            '"We built Beta before losing ourselves. '
            "Our bodies remained in Alpha. You were the sixth "
            "subject he failed to register. "
            'Only you can release us." METHOD returns.',
            ("truth_method",),
        ),





    ],
}

ORDINARY = {"ordinary", "meeting", "news"}




INTRO = [
    (
        "07:00",
        "Home",
        "BEDROOM",
        ("window", "clock", "phone"),
        ("alarm_off", "phone"),
    ),
    (
        "07:00",
        "Home",
        "BATHROOM",
        ("sink", "mirror", "razor"),
        ("washed", "shaved"),
    ),
    (
        "07:30",
        "Home",
        "BREAKFAST",
        (),  # No interactive objects.
        (),  # No required actions.
    ),
    (
        "08:00",
        "Bus Stop",
        "BUS STOP",
        ("daniel", "timetable"),
        (),
    ),
    (
        "09:00",
        "Company",
        "WORKSTATION",
        ("mail", "wrapper"),
        ("mail",),
    ),
    (
        "09:30",
        "Company",
        "MANAGER'S OFFICE",
        ("manager",),
        ("assignment",),
    ),
    (
        "10:00",
        "Company",
        "DELIVERING THE REQUEST",
        ("folder", "office"),
        ("delivery_blocked",),
    ),
    (
        "10:30",
        "Company",
        "BREAK ROOM",
        ("coworker", "coffee"),
        ("coworker_news",),
    ),
    (
        "13:30",
        "Cafe",
        "LUNCH",
        ("adrian", "menu", "photo", "newspaper", "mailbox"),
        ("ordered",),
    ),
    (
        "14:30",
        "Hospital",
        "HOSPITAL LOBBY",
        ("mara", "bill", "cabinet"),
        (),
    ),
    (
        "15:00",
        "Hospital",
        "WAITING AREA",
        ("seat", "medical", "noah"),
        ("examined",),
    ),
    (
        "15:30",
        "Library",
        "PASSING THE LIBRARY",
        ("notice", "evelyn"),
        (),
    ),
    (
        "17:00",
        "Company",
        "LEAVING WORK",
        (),
        (),
    ),
    (
        "18:00",
        "Cafe",
        "PASSING THE CAFE",
        (),
        (),
    ),
    (
        "18:30",
        "Bus Stop",
        "BUS STOP NEAR HOME",
        (),
        (),
    ),
    (
        "19:00",
        "Home",
        "DINNER",
        (),
        (),
    ),
    (
        "21:00",
        "Home",
        "BEDROOM",
        ("bed",),
        (),
    ),
]

INTRO_TEXT = [
    "The alarm rings. A bird taps twice. Your phone vibrates.",


    "You get ready for work in the bathroom.",


    "You finish a quick breakfast before leaving for work.",
    # Breakfast is finished before leaving for work.


    "A man waits with a paper ticket. The number 17 bus approaches.",


    "You arrive at your desk and open the work email.",


    "Your manager is waiting for the meeting requested in the message.",


    "Read and take the request, then inspect the finance office door.",


    "You feel unwell. Your coworker has been following the finance scandal.",


    "You stop for lunch before your hospital appointment.",


    "A woman sorts her bills while you check in.",


    "Wait for your examination. A boy watches the corridor.",


    "Nothing serious was found. Passing the closed library, "
    "you notice a woman waiting outside.",



    "You collect your things and leave work.",


    "The woman from the hospital is now behind the cafe counter. "
    "Adrian has left.",



    "The man with the paper ticket is no longer at the bus stop.",


    "You finish dinner and put the dishes away.",
    # Dinner is finished and the dishes are put away.


    "You still feel unwell. Use the bed to go to sleep early.",

]



REVERSE = [
    (
        "Library",
        "evelyn",
        "19:00",
        "Your worth was never a rank.",
    ),


    (
        "Bus Stop",
        "daniel",
        "17:00",
        "We can choose to stop waiting for permission.",
    ),


    (
        "Cafe",
        "noah",
        "13:00",
        "Your letter was read. We will carry it outside.",
    ),



    (
        "Company",
        "adrian",
        "11:00",
        "The debt was a leash. You can stop chasing the losses.",
    ),



    (
        "Hospital",
        "mara",
        "09:00",
        "Accepting her death did not mean abandoning her.",
    ),


]

ENDINGS = {
    "normal": (
        "EVERYTHING AS USUAL",
        "TUESDAY — 07:00\n\n"
        "The bird does not return. The district is real again. "
        "The five wake with fragments of a shared dream.\n\n"
        "Monday was finally allowed to end.",
    ),





    "assimilation": (
        "ASSIMILATION",
        "MONDAY — 07:00\n\n"
        "Your alarm rings. You cannot remember what you "
        "were worried about. It is time to go to work.\n\n"
        "There is nothing unusual here.",
    ),





    "void": (
        "LOST BETWEEN MOMENTS",
        "The loop breaks without reconnecting to reality.\n\n"
        "There is no Monday here. There is no Tuesday either. "
        "Only the moment between them.",
    ),





    "reversal": (
        "REVERSAL",
        "SUBJECTS RELEASED: 6\n"
        "NEW ANCHOR: DR. ELIAS VOSS\n\n"
        "The live observer link closes around its owner. "
        "You return to reality.\n\n"
        "Did you end the experiment, or choose its next victim?",
    ),




}


class GameState:
    """Manage story rules independently from the interface."""

    def __init__(self):
        self.day = 1
        self.known = set()
        self.notes = {}
        self.today = {}
        self.knows_loop = False
        self.ending = ""
        self.reset_day()

    def reset_day(self):
        """Reset daily objects while retaining important knowledge."""
        self.phase = 0
        self.visits = 0
        self.active = False
        self.location = "Home"
        self.area = ""
        self.clock = "07:00"
        self.items = set()
        self.events = set()
        self.previous = set(self.known)
        self.today.clear()
        self.intro_index = 0
        self.reverse_index = 0
        self.order = []
        self.mode = "intro" if self.day == 1 else "dawn"

    @property
    def truths(self):
        """Return the truth fragments already recovered."""
        return {
            key
            for key in TRUTH_ORDER
            if "truth_" + key in self.known
        }

    def learn(self, key, text=None):
        """Record knowledge without duplicating journal entries."""
        self.known.add(key)
        summary = NOTES.get(key) if text is None else text

        if summary:
            self.notes.setdefault(key, summary)

    def tasks(self):
        """Build current objectives from the player's progress."""
        result = []

        if (
            "assignment" in self.known
            and "truth_funding" not in self.known
        ):
            result.append(
                "Find Adrian, open finance, and investigate the request."
            )


        if self.knows_loop and len(self.truths) < 5:
            result.append(
                f"Recover the five accounts: {len(self.truths)}/5."
            )


        if self.day >= 2 and len(self.truths) < 5:
            result.append(
                "Keep the same appointments on later Mondays. "
                "Fragmented memories return gradually."
            )



        if len(self.truths) == 5:
            result.append(
                "Reconstruct the causal order in the laboratory. "
                "Reverse the anchors on Monday seven."
            )



        return result

    def characters(self):
        """Return the characters present in this place and phase."""
        schedule = {
            ("Bus Stop", 0): ["daniel"],
            ("Company", 0): ["coworker"],
            ("Cafe", 1): ["adrian"],
            ("Cafe", 2): ["mara"],
            ("Hospital", 0): ["mara"],
            ("Hospital", 1): ["mara", "noah"],
            ("Library", 1): ["evelyn"],
            ("Library", 2): ["evelyn"],
        }

        return schedule.get((self.location, self.phase), [])

    def objects(self):
        """Return only the objects available in the current scene."""
        if self.mode == "intro":
            return list(INTRO[self.intro_index][3])

        if self.mode == "reverse":
            if self.active:
                return [REVERSE[self.reverse_index][1]]
            return []

        if self.mode in {"ending", "verdict"}:
            return []

        if self.mode == "explore" and not self.active:
            return []

        if self.location == "Library" and self.area == "lab":
            return [
                "alpha",
                "beta",
                "voss_log",
                "projection",
                "scanner",
                "console",
            ]

        objects = {
            "Home": [
                "window",
                "clock",
                "phone",
                "milk",
                "calendar",
                "mug",
                "bed",
            ],
            "Bus Stop": [
                "timetable",
                "locker",
            ],
            "Company": [
                "mail",
                "wrapper",
                "folder",
                "office",
                "coffee",
                "shipment",
            ],
            "Cafe": [
                "menu",
                "photo",
                "newspaper",
                "mailbox",
            ],
            "Hospital": [
                "bill",
                "medical",
                "cabinet",
            ],
            "Library": [
                "notice",
                "side",
            ],
        }[self.location]

        if (
            self.location == "Company"
            and "finance_open" in self.events
        ):
            objects += ["report", "debt"]

        if (
            self.location == "Cafe"
            and "mailbox_open" in self.events
        ):
            objects += ["letter", "map"]

        if (
            self.location == "Hospital"
            and "cabinet_open" in self.events
        ):
            objects += ["voice", "aid"]

        if (
            self.location == "Bus Stop"
            and "locker_open" in self.events
        ):
            objects += ["transport"]

        if (
            self.location == "Library"
            and "library_open" in self.events
        ):
            objects += ["thesis", "review", "formula", "lab"]

        if self.mode not in {"dawn", "home"}:
            objects += self.characters()

        return objects

    def inspect(self, key):
        """Inspect an object without spending a visit."""
        if key not in self.objects() or key in CHAR_NAMES:
            return "There is nothing to inspect here."


        text = OBJECTS[key][1]

        if key == "folder":
            if "assignment" not in self.known:
                return "Several documents await processing."


            self.events.add("folder_read")
            text = (
                "Read and take this request to finance, "
                "as your manager asked."
            )


        elif key == "office":
            if self.mode == "intro" and "request" in self.items:
                self.events.add("delivery_blocked")
                self.learn(
                    "delivery_blocked",
                    "Finance was locked. Contact Adrian Cole.",
                )


            elif "finance_open" in self.events:
                return "The finance office is open."


        if (
            key in {"window", "phone", "calendar"}
            and key in self.previous
        ):
            text += (
                "\n\nYou remember exactly this "
                "from the previous Monday."
            )


            self.learn(
                "repeat_" + key,
                "Repeated Monday: " + OBJECTS[key][0].lower(),
            )


        if key != "voice":
            self.learn(key)

        if key == "phone":
            self.events.add("phone")

        return text

    def take(self, key):
        """Take a portable object without spending time."""
        if key not in self.objects():
            return "That object is not here."


        if key == "folder" and "folder_read" not in self.events:
            return "Read the request before taking it."


        item = {
            "phone": "phone",
            "mug": "mug",
            "wrapper": "wrapper",
            "folder": "request",
        }.get(key)

        if item is None:
            return "You cannot take that."


        if item in self.items:
            return "You already have it."


        self.items.add(item)
        return "You put it in your bag or pocket."


    def use(self, key):
        """Use an available object or unlock an area."""
        if key not in self.objects():
            return "That object is not here."


        if key == "phone":
            return self.inspect(key)

        routines = {
            "clock": (
                "alarm_off",
                "You stop the alarm.",
            ),


            "sink": (
                "washed",
                "You brush your teeth and wash your face.",
            ),


            "razor": (
                "shaved",
                "You shave and rinse the razor.",
            ),


            "breakfast": (
                "breakfast_done",
                "You finish the bread, leaving half a glass of milk.",
            ),


            "seat": (
                "examined",
                "The examination finds nothing serious. "
                "You are advised to rest.",
            ),

        }

        if key in routines:
            flag, text = routines[key]

            if flag in self.events:
                return "You have already done that today."


            self.events.add(flag)

            if key == "seat":
                self.today["examination"] = text

            return text

        if key == "coffee":
            if "mug" not in self.items:
                return "You need your own mug."


            self.items.add("hot_coffee")
            return "Your mug is now filled with hot coffee."


        if key == "report":
            if "hot_coffee" not in self.items:
                return "You need something warm to reveal the seal."


            self.learn("fund_mark")
            return (
                "Warmth reveals: TEMPORAL SEGMENTATION PROJECT "
                "— VOSS RESEARCH."
            )


        if key == "voice":
            self.learn("voice")
            return NOTES["voice"]

        gates = {
            "office": ("finance_code", "finance_open"),
            "mailbox": ("mail_code", "mailbox_open"),
            "cabinet": ("cabinet_code", "cabinet_open"),
            "locker": ("locker_code", "locker_open"),
            "side": ("map", "library_open"),
        }

        if key in gates:
            if self.mode == "intro":
                return "You cannot open it yet."


            clue, flag = gates[key]

            if clue not in self.known:
                return (
                    "You need more information before opening this."
                )


            self.events.add(flag)
            return (
                "The lock opens. "
                "You can now inspect what is inside."
            )


        if key == "lab":
            if (
                len(self.truths) < 4
                or not {"map", "formula"} <= self.known
            ):
                return (
                    "The map, formula, and at least "
                    "four accounts are needed."
                )


            self.area = "lab"
            return (
                "You descend into the hidden laboratory. "
                "Voss is present only in recordings."
            )


        if key == "scanner":
            if not {
                "review",
                "voss_log",
                "projection",
            } <= self.known:
                return (
                    "Read Voss's history and the recording "
                    "before interpreting the scan."
                )


            self.learn("voss_imprint")
            return (
                "VOSS: 99.7% RESONANCE. "
                "His live observer connection can become an anchor."
            )



        return "Inspect it, or choose another action."


    def topics(self, actor):
        """Unlock dialogue using evidence and gradual memory recovery."""
        if actor not in self.objects():
            return []

        result = []

        for topic in TOPICS.get(actor, []):
            if self.mode == "intro" and topic[0] not in ORDINARY:
                continue

            if set(topic[2]) <= self.known:
                earliest = max(
                    (
                        TRUTH_DAYS.get(flag, 2)
                        for flag in topic[4]
                    ),
                    default=2,
                )

                if self.mode == "intro" or self.day >= earliest:
                    result.append(topic)

        return result

    def talk(self, actor, topic_id):
        """Apply the selected conversation's discoveries."""
        topic = next(
            (
                topic
                for topic in self.topics(actor)
                if topic[0] == topic_id
            ),
            None,
        )

        if topic is None:
            return "You do not know enough to ask that yet."


        for flag in topic[4]:
            self.learn(flag)

            if flag == "truth_method":
                self.knows_loop = True

        if actor == "coworker":
            self.events.add("coworker_news")

        return topic[3]

    def enter(self, place):
        """Commit one destination visit."""
        if (
            place not in PLACES
            or self.mode not in {"dawn", "explore"}
        ):
            return False

        if self.visits >= 2:
            return False

        if self.mode == "dawn" and place == "Home":
            return False

        self.visits += 1
        self.active = True
        self.mode = "explore"
        self.location = place
        self.area = ""
        self.clock = PHASES[self.phase]

        return True

    def end_phase(self):
        """Advance to the next phase without retaining the old scene."""
        if self.mode != "explore" or not self.active:
            return False

        self.active = False
        self.area = ""

        if self.phase < 2:
            self.phase += 1
            self.visits = 0
            self.clock = PHASES[self.phase]
        else:
            self.go_home()

        return True

    def go_home(self):
        """End today's outing and return home for the night."""
        if self.mode != "explore":
            return False

        self.mode = "home"
        self.location = "Home"
        self.area = ""
        self.active = False
        self.clock = "22:00"

        return True

    def intro_next(self):
        """Continue the first day only after its required actions."""
        required = set(INTRO[self.intro_index][4])
        missing = required - self.known - self.events

        if missing:
            return (
                "Complete the scene first: "
                + ", ".join(sorted(missing))
            )



        if self.intro_index >= len(INTRO) - 1:
            return "Use the bed to sleep."


        self.intro_index += 1
        self.clock, self.location = INTRO[self.intro_index][:2]

        if self.intro_index == 13:
            self.learn(
                "mara_shift",
                "Evening: the woman from the hospital "
                "works at the cafe.",
            )


        if self.intro_index == 14:
            self.learn(
                "daniel_gone",
                "The paper-ticket man is absent in the evening.",
            )


        return INTRO_TEXT[self.intro_index]

    def next_monday(self, witnessed=False):
        """Begin another Monday or resolve the seventh-day deadline."""
        if witnessed:
            self.knows_loop = True
            self.learn("midnight")

        if self.day == 7:
            if len(self.truths) == 5:
                self.finish("void")
            else:
                self.finish("assimilation")
            return

        self.day += 1
        self.reset_day()

    def check_order(self):
        """Check the reconstructed causal sequence."""
        if tuple(self.order) == TRUTH_ORDER:
            self.learn("order_solved")
            self.order.clear()
            return True

        self.order.clear()
        return False

    def begin_reverse(self):
        """Start the separate final route on the seventh Monday."""
        if (
            self.day != 7
            or self.mode != "explore"
            or self.area != "lab"
            or len(self.truths) != 5
            or "order_solved" not in self.known
        ):
            return False

        self.mode = "reverse"
        self.knows_loop = True
        self.reverse_index = 0
        self.clock = "21:00"
        self.active = False
        self.area = ""

        return True

    def reverse_enter(self, place):
        """Reconstruct the next original anchor scene."""
        if self.mode != "reverse":
            return False

        target, _, clock, _ = REVERSE[self.reverse_index]

        if place != target:
            self.finish("void")
            return False

        self.location = place
        self.clock = clock
        self.active = True

        return True

    def release(self, choice):
        """Release one anchor after choosing the relevant response."""
        if self.mode != "reverse" or not self.active:
            return False

        if choice != REVERSE[self.reverse_index][3]:
            return False

        self.reverse_index += 1
        self.active = False

        if self.reverse_index == len(REVERSE):
            if "voss_imprint" in self.known:
                self.mode = "verdict"
            else:
                self.finish("normal")

        return True

    def finish(self, ending):
        """Record an ending and stop ordinary exploration."""
        self.ending = ending
        self.mode = "ending"
        self.active = False
        self.location = "Home"
        self.area = ""
        self.clock = "07:00"

    def dump(self):
        """Convert sets into JSON-compatible lists."""
        data = dict(self.__dict__)

        for key in ("known", "items", "events", "previous"):
            data[key] = sorted(data[key])

        return {
            "version": 1,
            "state": data,
        }

    @classmethod
    def restore(cls, saved):
        """Validate saved data before assigning any game state."""
        if not isinstance(saved, dict) or saved.get("version") != 1:
            raise ValueError("Unsupported save.")

        raw = saved.get("state")
        base = cls()

        if (
            not isinstance(raw, dict)
            or set(raw) != set(base.__dict__)
        ):
            raise ValueError("Incomplete save.")

        data = dict(raw)

        numeric_fields = (
            ("day", 1, 7),
            ("phase", 0, 2),
            ("visits", 0, 2),
            ("intro_index", 0, len(INTRO) - 1),
            ("reverse_index", 0, 5),
        )

        for key, low, high in numeric_fields:
            if (
                type(data[key]) is not int
                or not low <= data[key] <= high
            ):
                raise ValueError("Invalid number.")

        if (
            data["location"] not in PLACES
            or data["area"] not in {"", "lab"}
        ):
            raise ValueError("Invalid location.")

        if data["mode"] not in {
            "intro",
            "dawn",
            "explore",
            "home",
            "reverse",
            "verdict",
            "ending",
        }:
            raise ValueError("Invalid mode.")

        if data["ending"] not in {"", *ENDINGS}:
            raise ValueError("Invalid ending.")

        for key in ("active", "knows_loop"):
            if type(data[key]) is not bool:
                raise ValueError("Invalid flag.")

        for key in ("known", "items", "events", "previous"):
            value = data[key]

            if (
                not isinstance(value, list)
                or not all(
                    isinstance(item, str) and len(item) < 100
                    for item in value
                )
            ):
                raise ValueError("Invalid collection.")

            data[key] = set(value)

        for key in ("notes", "today"):
            if (
                not isinstance(data[key], dict)
                or not all(
                    isinstance(note_key, str)
                    and isinstance(note_text, str)
                    and len(note_text) < 4000
                    for note_key, note_text in data[key].items()
                )
            ):
                raise ValueError("Invalid journal.")

            data[key] = dict(data[key])

        if (
            not isinstance(data["clock"], str)
            or len(data["clock"]) > 30
            or not isinstance(data["order"], list)
            or len(data["order"]) > 5
            or len(set(data["order"])) != len(data["order"])
            or any(
                item not in TRUTH_ORDER
                for item in data["order"]
            )
        ):
            raise ValueError("Invalid clock or order.")

        data["order"] = list(data["order"])

        if data["mode"] == "intro" and data["day"] != 1:
            raise ValueError("Invalid introduction.")

        if data["mode"] == "reverse":
            if data["day"] != 7 or data["reverse_index"] >= 5:
                raise ValueError("Invalid reverse route.")

        if data["mode"] == "ending" and not data["ending"]:
            raise ValueError("Missing ending.")

        base.__dict__.update(data)
        return base


class GameApp:
    """Create the interface and connect buttons to GameState."""

    def __init__(self, root):
        self.root = root
        self.state = GameState()
        self.selected = None
        self.busy = False
        self.jobs = []

        root.title("Monday, Again")
        root.geometry("1180x780")
        root.minsize(1000, 700)
        root.configure(bg="#10131c")
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)

        self.build()
        self.render()
        self.tell(INTRO_TEXT[0])

    def button(self, parent, text, command):
        """Create a consistently styled button."""
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 10),
            bg="#364767",
            fg="white",
            activebackground="#58749c",
            activeforeground="white",
            disabledforeground="#7e879b",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=9,
            wraplength=520,
            justify="left",
        )

    def build(self):
        """Build the header, scene panel, story panel, and footer."""
        header = tk.Frame(self.root, bg="#171e2c")
        header.grid(row=0, column=0, sticky="ew")

        tk.Label(
            header,
            text="MONDAY, AGAIN",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#171e2c",
        ).pack(side="left", padx=22, pady=18)

        header_buttons = (
            ("HELP", self.help),
            ("LOAD", self.load),
            ("SAVE", self.save),
            ("NEW GAME", self.new),
        )


        for label, command in header_buttons:
            self.button(
                header,
                label,
                command,
            ).pack(side="right", padx=4)

        main = tk.Frame(self.root, bg="#10131c")
        main.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=18,
            pady=12,
        )

        main.grid_columnconfigure(
            0,
            weight=7,
            uniform="panels",
        )
        main.grid_columnconfigure(
            1,
            weight=3,
            uniform="panels",
        )
        main.grid_rowconfigure(0, weight=1)

        left = tk.Frame(main, bg="#232c40")
        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 12),
        )

        self.canvas = tk.Canvas(
            left,
            bg="#232c40",
            highlightthickness=0,
        )

        scrollbar = tk.Scrollbar(
            left,
            command=self.canvas.yview,
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set,
        )

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(
            side="left",
            fill="both",
            expand=True,
        )

        self.body = tk.Frame(
            self.canvas,
            bg="#232c40",
        )

        self.body_window = self.canvas.create_window(
            (0, 0),
            window=self.body,
            anchor="nw",
        )

        self.body.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all"),
            ),
        )

        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.itemconfigure(
                self.body_window,
                width=event.width,
            ),
        )

        self.story = ScrolledText(
            main,
            width=1,
            wrap="word",
            font=("Arial", 12),
            bg="#192130",
            fg="#eef1f7",
            padx=18,
            pady=20,
            relief="flat",
            state="disabled",
        )

        self.story.grid(
            row=0,
            column=1,
            sticky="nsew",
        )

        footer = tk.Frame(
            self.root,
            bg="#171e2c",
        )
        footer.grid(row=2, column=0, sticky="ew")

        self.status = tk.Label(
            footer,
            bg="#171e2c",
            fg="#a9bfdf",
            font=("Arial", 11),
        )
        self.status.pack(
            anchor="w",
            padx=20,
            pady=(10, 5),
        )

        actions = tk.Frame(
            footer,
            bg="#171e2c",
        )
        actions.pack(
            fill="x",
            padx=15,
            pady=5,
        )

        self.action_buttons = []

        action_definitions = (
            ("INSPECT", self.inspect),
            ("TAKE", self.take),
            ("USE / TALK", self.use),
        )


        for text, command in action_definitions:
            button = self.button(
                actions,
                text,
                command,
            )
            button.pack(side="left", padx=5)
            self.action_buttons.append(button)

        self.selection = tk.Label(
            actions,
            text="",
            bg="#171e2c",
            fg="#a9bfdf",
        )
        self.selection.pack(
            side="left",
            padx=10,
        )

        self.button(
            actions,
            "JOURNAL",
            self.journal,
        ).pack(side="right", padx=5)


        self.button(
            actions,
            "INVENTORY",
            self.inventory,
        ).pack(side="right", padx=5)


        self.nav = tk.Frame(
            footer,
            bg="#171e2c",
        )
        self.nav.pack(
            fill="x",
            padx=20,
            pady=(4, 12),
        )

    def tell(self, text):
        """Replace the text in the story panel."""
        self.story.configure(state="normal")
        self.story.delete("1.0", "end")
        self.story.insert("1.0", text)
        self.story.configure(state="disabled")
        self.story.yview_moveto(0)

    def heading(self, text):
        """Add a heading to the scene panel."""
        tk.Label(
            self.body,
            text=text,
            bg="#232c40",
            fg="#bed0eb",
            font=("Arial", 15, "bold"),
            wraplength=650,
            justify="left",
        ).pack(
            anchor="w",
            padx=22,
            pady=(20, 14),
        )

    def clear(self):
        """Remove old controls and clear the selected object."""
        self.selected = None
        self.selection.configure(text="")

        for button in self.action_buttons:
            button.configure(state="disabled")

        for child in self.body.winfo_children():
            child.destroy()

        self.canvas.yview_moveto(0)

    def status_text(self):
        """Hide the loop counter until the character knows the truth."""
        state = self.state

        if state.ending == "void":
            return "BETWEEN MOMENTS"


        loop = (
            f"LOOP {state.day} | "
            if state.knows_loop
            else ""
        )

        if state.ending in {"normal", "reversal"}:
            clock = "TUESDAY 07:00"

        else:
            clock = f"MONDAY {state.clock}"

        visits = ""

        if state.mode == "explore":
            visits = (
                f" | {PHASES[state.phase]} "
                f"{state.visits}/2 VISITS"
            )


        return (
            f"{loop}{clock} | "
            f"{PLACES[state.location]}{visits}"
        )

    def render(self):
        """Display the current scene without advancing time."""
        self.clear()
        state = self.state
        self.status.configure(text=self.status_text())

        if state.mode == "explore" and not state.active:
            self.map()
            return

        if state.mode == "ending":
            title, text = ENDINGS[state.ending]
            self.heading(title)
            self.tell(text)
            self.navigation()
            return

        if state.mode == "verdict":
            self.heading("THE FINAL CHOICE")


            self.button(
                self.body,
                "Release everyone and close the link.",
                lambda: self.finish("normal"),
            ).pack(
                fill="x",
                padx=22,
                pady=8,
            )


            self.button(
                self.body,
                "Transfer the anchor to Voss.",
                lambda: self.finish("reversal"),
            ).pack(
                fill="x",
                padx=22,
                pady=8,
            )


            self.tell(
                "The live observer link is still open. "
                "You have a choice."
            )


            self.navigation()
            return

        if state.mode == "intro":
            title = INTRO[state.intro_index][2]
        else:
            title = PLACES[state.location]

        if state.mode == "reverse":
            title += " — REVERSE"

        elif state.area == "lab":
            title = "LIBRARY — UNDERGROUND LABORATORY"


        self.heading(title)

        cards = tk.Frame(
            self.body,
            bg="#232c40",
        )
        cards.pack(
            fill="x",
            padx=15,
            pady=8,
        )

        cards.grid_columnconfigure(0, weight=1)
        cards.grid_columnconfigure(1, weight=1)

        for index, key in enumerate(state.objects()):
            if key in CHAR_NAMES:
                label = CHAR_NAMES[key]
            else:
                label = OBJECTS[key][0]

            self.button(
                cards,
                label,
                lambda value=key: self.select(value),
            ).grid(
                row=index // 2,
                column=index % 2,
                sticky="ew",
                padx=7,
                pady=8,
            )

        self.navigation()

    def navigation(self):
        """Show only navigation controls for the current mode."""
        for child in self.nav.winfo_children():
            child.destroy()

        if self.busy:
            return

        state = self.state
        buttons = []

        if (
            state.mode == "intro"
            and state.intro_index < len(INTRO) - 1
        ):
            buttons = [
                ("LEAVE / CONTINUE", self.intro_next),
            ]


        elif state.mode == "dawn":
            buttons = [
                ("GO OUT", self.map),
            ]


        elif state.mode == "explore":
            buttons = [
                ("MAP / NEXT PLACE", self.map),
                ("END PHASE", self.end_phase),
                ("END OUTING", self.go_home),
            ]


            if state.area == "lab":
                buttons.append(
                    ("BACK TO LIBRARY", self.leave_lab),
                )


        elif state.mode == "home":
            buttons = [
                ("SLEEP", self.sleep),
                ("STAY AWAKE", self.stay_awake),
            ]


        elif state.mode == "reverse":
            buttons = [
                ("CHOOSE NEXT ANCHOR", self.map),
            ]


        for text, command in buttons:
            self.button(
                self.nav,
                text,
                command,
            ).pack(
                side="left",
                padx=(0, 8),
            )

    def select(self, key):
        """Select an object without automatically interacting with it."""
        if self.busy or key not in self.state.objects():
            return

        self.selected = key

        label = CHAR_NAMES.get(
            key,
            OBJECTS.get(key, ("", ""))[0],
        )

        self.selection.configure(text=label)

        for button in self.action_buttons:
            button.configure(state="normal")

        self.tell("Choose an action below.")


    def inspect(self):
        if self.busy or self.selected is None:
            return

        if self.selected in CHAR_NAMES:
            self.tell("Use TALK to choose what to ask.")

        else:
            self.tell(
                self.state.inspect(self.selected),
            )

    def take(self):
        if not self.busy and self.selected:
            self.tell(
                self.state.take(self.selected),
            )

    def use(self):
        if self.busy or self.selected is None:
            return

        key = self.selected

        if key in CHAR_NAMES:
            self.dialogue(key)

        elif key == "bed":
            at_intro_bedtime = (
                self.state.mode == "intro"
                and self.state.intro_index == len(INTRO) - 1
            )

            if self.state.mode == "home" or at_intro_bedtime:
                self.sleep()
            else:
                self.tell("You are not ready for bed yet.")


        elif key == "menu":
            self.order_food()

        elif key == "console":
            self.console()

        else:
            text = self.state.use(key)
            self.render()
            self.tell(text)

    def dialogue(self, actor):
        """Display available questions and refresh newly unlocked ones."""
        self.clear()
        self.heading(CHAR_NAMES[actor])

        if self.state.mode == "reverse":
            correct = REVERSE[self.state.reverse_index][3]

            choices = [
                "Nothing you did ever mattered.",


                correct,

                "Forget the past and keep repeating this day.",

            ]

            for choice in choices:
                self.button(
                    self.body,
                    choice,
                    lambda value=choice: self.release(value),
                ).pack(
                    fill="x",
                    padx=22,
                    pady=7,
                )

        else:
            for topic in self.state.topics(actor):
                self.button(
                    self.body,
                    topic[1],
                    lambda value=topic[0]: self.ask(actor, value),
                ).pack(
                    fill="x",
                    padx=22,
                    pady=7,
                )

        self.button(
            self.body,
            "BACK",
            self.render,
        ).pack(
            padx=22,
            pady=15,
        )


    def ask(self, actor, topic):
        text = self.state.talk(actor, topic)



        self.dialogue(actor)
        self.tell(text)

    def order_food(self):
        self.clear()
        self.heading("ORDER")


        if "mara" in self.state.objects():
            choices = [
                (
                    "COFFEE",
                    '"I need another shift," Mara says.',
                ),


                (
                    "TEA",
                    '"Something warm helps me keep going," Mara says.',
                ),


                (
                    "SANDWICH SET",
                    '"I should eat something too," Mara says.',
                ),

            ]

        elif "adrian" in self.state.objects():
            choices = [
                (
                    "COFFEE",
                    '"Long day?" Adrian asks.',
                ),


                (
                    "TEA",
                    '"Some people order the same thing every day."',
                ),


                (
                    "SANDWICH SET",
                    '"I used to work nearby." He changes the subject.',
                ),


            ]

        else:
            choices = [
                (
                    "COFFEE",
                    "You drink a bitter coffee at the quiet counter.",
                ),


                (
                    "TEA",
                    "Steam rises slowly from your tea.",
                ),


                (
                    "SANDWICH SET",
                    "You finish a simple meal.",
                ),

            ]

        for label, text in choices:
            self.button(
                self.body,
                label,
                lambda value=text: self.food_chosen(value),
            ).pack(
                fill="x",
                padx=22,
                pady=8,
            )

        self.button(
            self.body,
            "BACK",
            self.render,
        ).pack(pady=12)


    def food_chosen(self, text):
        self.state.events.add("ordered")
        self.state.today["meal"] = text
        self.render()
        self.tell(text)

    def intro_next(self):
        if self.busy:
            return

        text = self.state.intro_next()
        self.render()
        self.tell(text)

    def map(self):
        """Opening the map does not spend a visit."""
        if self.busy:
            return

        self.clear()
        state = self.state
        self.status.configure(text=self.status_text())

        if state.mode == "reverse":
            self.heading("MONDAY SEVEN — REVERSE ROUTE")


            self.tell(
                "Follow the causal chain backwards. "
                "A wrong destination collapses the loop."
            )



        else:
            self.heading(
                f"{PHASES[state.phase]} "
                f"— {state.visits}/2 VISITS"
            )


            self.tell(
                "Choosing a destination uses one visit. "
                "Reading, taking, and talking are free. "
                "Opening or closing this map costs nothing."
            )




        for place, label in PLACES.items():
            button = self.button(
                self.body,
                label,
                lambda value=place: self.travel(value),
            )

            button.pack(
                fill="x",
                padx=30,
                pady=5,
            )

            if state.mode != "reverse":
                no_visits = state.visits >= 2
                already_at_home = (
                    state.mode == "dawn"
                    and place == "Home"
                )

                if no_visits or already_at_home:
                    button.configure(state="disabled")

        if state.active or state.mode == "dawn":
            self.button(
                self.body,
                "BACK",
                self.render,
            ).pack(pady=12)


        self.navigation()

    def travel(self, place):
        """Commit the destination only when a map button is chosen."""
        if self.busy:
            return

        if self.state.mode == "reverse":
            confirmed = messagebox.askyesno(
                "REVERSE ROUTE",
                f"Travel to {PLACES[place]}?",
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



        elif self.state.enter(place):
            self.render()
            self.tell(
                "You arrive. Explore freely; "
                "choose the next place when you are ready."
            )



    def end_phase(self):
        if self.busy or not self.state.end_phase():
            return

        if self.state.mode == "home":
            self.render()
            self.tell(
                "22:00. You return home. "
                "Sleep, or watch the date change."
            )


        else:
            self.map()

    def go_home(self):
        if not self.busy and self.state.go_home():
            self.render()
            self.tell(
                "Your outing is over. "
                "By 22:00, you are home for the night."
            )



    def leave_lab(self):
        self.state.area = ""
        self.render()

    def console(self):
        """Let the player reconstruct the five-part causal chain."""
        self.clear()
        self.heading("RECONSTRUCT THE CAUSAL ORDER")


        if len(self.state.truths) < 5:
            self.tell("All five accounts are required.")


            self.button(
                self.body,
                "BACK",
                self.render,
            ).pack(pady=15)
            return

        chosen = " > ".join(
            TRUTH_NAMES[key]
            for key in self.state.order
        )

        tk.Label(
            self.body,
            text=chosen or "Choose the first cause.",
            bg="#232c40",
            fg="white",
            wraplength=620,
        ).pack(
            padx=22,
            pady=10,
        )



        for key in TRUTH_ORDER:
            if key not in self.state.order:
                self.button(
                    self.body,
                    TRUTH_NAMES[key],
                    lambda value=key: self.order_piece(value),
                ).pack(
                    fill="x",
                    padx=22,
                    pady=5,
                )

        self.button(
            self.body,
            "CLEAR ORDER",
            self.clear_order,
        ).pack(pady=8)


        if "order_solved" in self.state.known:
            self.button(
                self.body,
                "START REVERSE",
                self.begin_reverse,
            ).pack(pady=8)


        self.button(
            self.body,
            "BACK",
            self.render,
        ).pack(pady=8)

    def order_piece(self, key):
        if key in self.state.order:
            return

        self.state.order.append(key)

        if len(self.state.order) == 5:
            correct = self.state.check_order()
            self.console()

            if correct:
                self.tell(
                    "Correct. Start the reverse on Monday seven."
                )

            else:
                self.tell(
                    "That order does not explain the experiment. "
                    "Try again."
                )

        else:
            self.console()

    def clear_order(self):
        self.state.order.clear()
        self.console()

    def begin_reverse(self):
        if not self.state.begin_reverse():
            self.tell(
                "The order must be solved, "
                "and it must be Monday seven."
            )


            return

        self.map()

    def release(self, choice):
        if not self.state.release(choice):
            self.tell(
                "The memory does not connect. "
                "Read the evidence and try another response."
            )


            return

        self.render()

        if self.state.mode == "reverse":
            self.tell(
                "The anchor releases. "
                "Choose the next place in reverse order."
            )



            self.map()

    def finish(self, ending):
        self.state.finish(ending)
        self.render()

    def sleep(self):
        """Sleep only at the end of an outing or first-day bedtime."""
        if self.busy:
            return

        intro_bedtime = (
            self.state.mode == "intro"
            and self.state.intro_index == len(INTRO) - 1
        )

        if not (
            self.state.mode == "home"
            or intro_bedtime
        ):
            return

        self.state.next_monday()
        self.render()

        if self.state.mode != "ending":
            self.tell(
                "07:00. The alarm rings. "
                "Your phone still says Monday."
            )


    def later(self, delay, callback):
        """Schedule short animations without freezing the window."""
        self.jobs.append(
            self.root.after(delay, callback),
        )

    def stay_awake(self):
        """Let the player witness the midnight date reversal."""
        if self.busy or self.state.mode != "home":
            return

        self.busy = True
        self.navigation()

        self.tell(
            "23:59 — MONDAY\n\n"
            "You watch the phone."
        )


        self.later(
            1400,
            lambda: self.midnight(1),
        )

    def midnight(self, step):
        if step == 1:
            self.status.configure(
                text="TUESDAY 13 OCTOBER — 00:00",
            )

            self.tell("00:00 — TUESDAY")


            self.later(
                650,
                lambda: self.midnight(2),
            )

        elif step == 2:
            self.status.configure(
                text="MONDAY 12 OCTOBER — 00:00",
            )

            self.tell(
                "00:00 — MONDAY\n\n"
                "The date jumps back."
            )


            self.later(
                1700,
                lambda: self.midnight(3),
            )

        else:
            self.state.next_monday(witnessed=True)
            self.busy = False
            self.render()

            if self.state.mode != "ending":
                self.tell(
                    "07:00 — MONDAY\n\n"
                    "You remember the date changing. "
                    "The day is repeating."
                )



    def document(self, title, text):
        """Open a read-only journal, inventory, or help window."""
        if self.busy:
            return

        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("650x520")

        view = ScrolledText(
            popup,
            wrap="word",
            font=("Arial", 12),
            bg="#192130",
            fg="white",
            padx=20,
            pady=20,
        )

        view.pack(
            fill="both",
            expand=True,
        )

        view.insert("1.0", text)
        view.configure(state="disabled")

    def journal(self):
        """Keep permanent findings separate from ordinary daily events."""
        sections = []

        groups = [
            (
                "IMPORTANT FINDINGS",
                list(self.state.notes.values()),
            ),


            (
                "CURRENT TASKS",
                self.state.tasks(),
            ),


            (
                "TODAY",
                list(self.state.today.values()),
            ),

        ]

        for title, entries in groups:
            if entries:
                content = "\n\n".join(
                    "- " + entry
                    for entry in entries
                )

                sections.append(
                    title + "\n\n" + content,
                )

        text = "\n\n----------------\n\n".join(sections)

        self.document(
            "JOURNAL",
            text or "No discoveries recorded yet.",
        )


    def inventory(self):
        names = {
            "phone": "Phone",
            "mug": "Travel mug",
            "wrapper": "Gum wrapper",
            "request": "Transfer request",
            "hot_coffee": "Hot coffee",
        }


        text = "\n".join(
            "- " + names.get(item, item)
            for item in sorted(self.state.items)
        )

        self.document(
            "INVENTORY",
            text or "Your inventory is empty.",
        )


    def help(self):
        if self.state.day == 1:
            self.document(
                "HOW TO PLAY",
                "Click an object, then INSPECT, TAKE, or USE / TALK. "
                "Complete the ordinary morning routines, then use "
                "LEAVE / CONTINUE. Your journal records important "
                "findings. Save before closing.",
            )




            return

        self.document(
            "HOW TO PLAY",

            "The first Monday follows a fixed route. "
            "Complete the required daily routines.\n\n"



            "From the second Monday, each morning, afternoon, "
            "and evening allows two place visits. "
            "Objects and conversations do not spend time. "
            "Use END PHASE to move on.\n\n"





            "At 22:00 you return home. "
            "You may sleep or stay awake. "
            "Important knowledge survives; ordinary items "
            "return to their original places.\n\n"



            "New clues unlock new questions immediately. "
            "Read your journal. You have seven Mondays, "
            "including the first. Save before experimenting.\n\n"




            "The final reverse route uses original anchor places "
            "from the transport log, not the characters' "
            "ordinary daily schedules.",


        )

    def save(self):
        """Save progress beside the Python script."""
        if self.busy:
            return

        try:
            text = json.dumps(
                self.state.dump(),
                ensure_ascii=False,
                indent=2,
            )

            SAVE_PATH.write_text(
                text,
                encoding="utf-8",
            )

            self.tell("Game saved beside main.py.")


        except OSError as error:
            messagebox.showerror(
                "SAVE FAILED",
                str(error),
            )


    def load(self):
        """Load validated progress without changing visit counts."""
        if self.busy:
            return

        try:
            text = SAVE_PATH.read_text(
                encoding="utf-8",
            )
            loaded = GameState.restore(
                json.loads(text),
            )

        except (OSError, ValueError, TypeError) as error:
            messagebox.showerror(
                "LOAD FAILED",
                "The save is missing or invalid.\n" + str(error),
            )

            return

        confirmed = messagebox.askyesno(
            "LOAD",
            "Replace the current progress with the save?",
        )


        if not confirmed:
            return

        self.state = loaded
        self.render()

        if loaded.mode == "reverse" and not loaded.active:
            self.map()

        elif loaded.mode not in {"ending", "verdict"}:
            self.tell(
                "Save loaded. Check the journal to continue."
            )


    def new(self):
        """Start again without deleting the saved file."""
        if self.busy:
            return

        confirmed = messagebox.askyesno(
            "NEW GAME",
            "Start again? The saved file will be kept.",
        )


        if confirmed:
            self.state = GameState()
            self.render()
            self.tell(INTRO_TEXT[0])


def main():
    root = tk.Tk()
    GameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()