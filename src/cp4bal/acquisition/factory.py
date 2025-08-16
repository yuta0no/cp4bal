from cp4bal.acquisition import Acquisition, RandomAcquisition


class AcquisitionFactory:
    @staticmethod
    def create(acquisition_type: str) -> Acquisition:
        match acquisition_type.lower():
            case "random":
                return RandomAcquisition()
            case _:
                raise ValueError(f"Unknown acquisition type: {acquisition_type}")
