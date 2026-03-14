from .errors import NotVaccinatedError, NotWearingMaskError
from .errors import OutdatedVaccineError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()
        ex_date = visitor["vaccine"]["expiration_date"]
        if ex_date < datetime.date.today():
            raise OutdatedVaccineError()
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError()
        return f"Welcome to {self.name}"
