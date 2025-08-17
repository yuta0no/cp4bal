from enum import StrEnum, unique


# Trainer
@unique
class TrainerType(StrEnum):
    ADAM = "adam"
    ORACLE = "oracle"
    SGC = "sgc"
