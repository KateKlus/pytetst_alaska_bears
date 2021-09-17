import logging
from .Common import Common

from random import randint
from faker import Faker

fake = Faker()
LOGGER = logging.getLogger(__name__)


class Bear(Common):

    def __init__(self, bear_type=None, bear_name=None):
        LOGGER.error(bear_type)
        bear_type = bear_type if bear_type else self.POLAR_TYPE
        ber_name = bear_name if bear_name else fake.name().upper()
        self.bear_type = bear_type
        self.bear_name = ber_name
        self.bear_age = randint(1, 35)
