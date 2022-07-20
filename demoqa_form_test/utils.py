from enum import Enum


def get_full_file_path(*, relaive_path):
    import demoqa_form_test
    from pathlib import Path
    return Path(demoqa_form_test.__file__).parent.parent.joinpath(relaive_path).__str__()


class Months(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12