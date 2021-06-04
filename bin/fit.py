import logging

import config
import tasks

if __name__ == "__main__":
    config.start()

    for city in [
        "ABU_DHABI",
        "BERLIN",
        "BREMEN",
        "COLOGNE",
        "COPENHAGEN",
        "DARMSTADT",
        "DORTMUND",
        "ERLANGEN",
        "ESSEN",
        "FRANKFURT",
        "GDANSK",
        "HAMBURG",
        "HANNOVER",
        "HH-TENDER",
        "KARLSRUHE",
        "KRAKOW",
        "LUDWIGSBURG",
        "MUNICH",
        "MUENSTER",
        "NAMSOS",
        "INNSBRUCK",
        "KLAGENFURT",
        "LINZ",
        "TRONDHEIM",
        "OSLO",
        "STGALLEN",
        "STUTTGART",
        "VIENNA",
        "VILLACH",
        "WELS",
    ]:
        logging.warning("... Enqueue %s", city)
        tasks.task_one.delay(city)
