from functools import cached_property
from models import Entity
from pymem import Pymem


class PlayerEntity(Entity):
    def __init__(self, pm: Pymem, mem, overlay, viewProjMatrix, entityAddress: int):
        super().__init__(pm, mem, overlay, viewProjMatrix, entityAddress)

