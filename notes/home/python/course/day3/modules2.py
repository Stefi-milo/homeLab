# after installing a module using pip (and restart of IDE)
# we can start using the module

from czech_holidays import czech_holidays
from pprint import pprint

holidays = czech_holidays(2026)
pprint(holidays)
