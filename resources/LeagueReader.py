from pymem import Pymem
from models import Entity
from models.Minion import MinionEntity
from resources import offsets, LeagueStorage
from resources.StructureReader import StructureReader


class LeagueReader:
    def __init__(self, pm: Pymem, mem, overlay, viewProjMatrix, lStorage):
        self.pm = pm
        self.mem = mem
        self.overlay = overlay
        self.viewProjMatrix = viewProjMatrix
        self.lStorage: LeagueStorage = lStorage

        self.localPlayer: Entity = self.get_local_player()
        self.teamPlayers, self.enemyPlayers = self.get_players()
        self.minions = self.get_minions()               

    def get_minions(self) -> list:   
        all_minions_addr: list[int] = StructureReader.read_v_table(self.pm, self.lStorage.minion_manager_addr)        
        for minion_addr in all_minions_addr:            
            m = MinionEntity(self.pm, self.mem, self.overlay, self.viewProjMatrix, minion_addr)
            if m.health > 0:
                yield m               

    def get_local_player(self) -> Entity:
        return Entity(self.pm, self.mem, self.overlay, self.viewProjMatrix, self.lStorage.localPlayerAddr)

    def get_players(self) -> tuple[list[Entity], list[Entity]]:
        allChampAddrs: list[int] = StructureReader.read_v_table(self.pm, self.lStorage.heroManagerAddr)

        teamPlayers, enemyPlayers = [], []
        i: int = 0
        while i < len(allChampAddrs):
            isVisible: bool = self.pm.read_bool(allChampAddrs[i] + offsets.oObjVisible)
            health: float = self.pm.read_float(allChampAddrs[i] + offsets.oObjHealth)

            if isVisible or health <= 0:
                player: Entity = Entity(self.pm, self.mem, self.overlay, self.viewProjMatrix,
                                                    allChampAddrs[i])
                if player.teamId == self.localPlayer.teamId:
                    teamPlayers.append(player)
                else:
                    enemyPlayers.append(player)
            i += 1

        return teamPlayers, enemyPlayers
