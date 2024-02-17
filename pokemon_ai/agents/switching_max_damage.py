"""
This agent is similar to MaxDamagePlayer, except it will always priotize
switching to the available pokemon that is strongest against the current
opponent's pokemon.
"""

from poke_env.player import Player
from typing import Dict
from poke_env.environment.pokemon import Pokemon
import numpy as np
from pokemon_ai.metrics.mon_on_mon import type_advantage
from poke_env.player.battle_order import BattleOrder

class SwitchingMaxDamage(Player):
    """
    Agent is MaxDamage but prioritizes switching to max
    damage pokemon against opponent pokemon.
    """
    def choose_move(self, battle):
        # TODO: confirm this is bug-free
        mon_performance : Dict[int, float] = {}
        # For each of our pokemons
        # if possible to switch, check if worth doing
        if battle.available_switches != []:
            for i, mon in enumerate(battle.available_switches):
                # We store their average performance against the current opponent mon
                mon_performance[i] = type_advantage(mon, battle.opponent_active_pokemon)

            # We sort our mons by performance
            ordered_mons = sorted(mon_performance, key=lambda k: -mon_performance[k])
            if mon_performance[ordered_mons[0]] > type_advantage(battle.active_pokemon, battle.opponent_active_pokemon):
                # Switch to better one
                return self.create_order(battle.available_switches[ordered_mons[0]])

        # otherwise, attack since it's the best

        # If the player can attack, it will
        if battle.available_moves:
            # Finds the best move among available ones
            best_move = max(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)

        # If no attack is available, a random switch will be made
        else:
            return self.choose_random_move(battle)

