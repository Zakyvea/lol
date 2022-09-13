# Importing LeagueReader for typing intellisense
from resources import LeagueReader
import math


# Setup function | only runs once on script load
def setup() -> dict:
    scriptSettings: dict = {
        "playerAttackRange": {
            "displayName": "Player Attack Range",
            "isEnabled": True
        }
    }
    return scriptSettings


# OnTick function | Runs every tick
def on_tick(lReader: LeagueReader, pymeow, scriptSettings):
    if scriptSettings['playerAttackRange']['isEnabled']:
        attack_range(lReader, pymeow)


def attack_range(lReader: LeagueReader, pymeow):
    if lReader.localPlayer.onScreen:
        player = lReader.localPlayer
        world_pos = player.gamePos
        radius: float = lReader.localPlayer.attackRange * 1.1
        theta: float = 0

        word_space = []
        while theta < 2 * 3.14:
            x = world_pos['x'] + radius * math.cos(theta)
            y = world_pos['y']
            z = radius * math.sin(theta) + world_pos['z']
            word_space.append(pymeow.wts_ogl(lReader.overlay, lReader.viewProjMatrix.tolist(),
                                             {'x': x, 'y': y, 'z': z}))
            theta += 0.01

        i = 0
        while i < len(word_space) - 1:
            pymeow.line_v(
                word_space[i],
                word_space[i + 1],
                3,
                pymeow.rgb("red")
            )
            i += 1
