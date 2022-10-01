# Example using Exdecption group as dispatch
from dataclasses import dataclass
from typing import List

import exceptions_repository as rep


@dataclass
class Participant:
    name: str
    age: int
    nationality: str


def create_participant() -> Participant:
    return Participant("Michel Salvini", 19, "FR")


class ParticipantValidator:
    def _validation(self, participant: Participant) -> None:
        _exceptions: List[Exception] = []
        if not self._isvalid_age(participant):
            _exceptions.append(rep.InvalidAge(participant.age))
        if not self._isvalid_nationality(participant):
            _exceptions.append(rep.InvalidNationality(participant.nationality))
        if _exceptions:
            eg = ExceptionGroup("participants", _exceptions)
            raise eg

    def _isvalid_age(self, participant: Participant) -> bool:
        return participant.age >= 21

    def _isvalid_nationality(self, participant: Participant) -> bool:
        return participant.nationality == "US"

    def validate(self, participant: Participant) -> None:
        try:
            self._validation(participant)
        except* rep.InvalidAge as e1:
            # ExceptionGroup can hold more exceptions per type
            for exception in e1.exceptions:
                print(f"Handler for InvalidAge exception {exception}")
            # Run handler  common to all BL exceptions     
            raise rep.InvalidValidation

        except* rep.InvalidNationality as e2:
            for exception in e2.exceptions:
                print(f"Handler for InvalidNationality exception {exception}")
            raise rep.InvalidValidation

if __name__ == "__main__":
    try:
        part = ParticipantValidator()
        part.validate(create_participant())
        print("Validation OK")

    # cannot mix except and except* -> so called naked exceptions are wrapped to ExceptionGroup too
    except* rep.InvalidValidation:
        print("Optional handler common to all validation errors")
    except* Exception as exc:
        print(f"No validation related errors : {str(exc.exceptions[0])}")            



