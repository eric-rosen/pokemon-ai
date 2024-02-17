"""
This agent is similar to MaxDamagePlayer, except it will always priotize
switching to the available pokemon that is strongest against the current
opponent's pokemon.
"""

from poke_env.player import Player
from typing import Dict
import numpy as np
from pokemon_ai.metrics.mon_on_mon import type_advantage

class SwitchingMaxDamage(Player):
    """
    Agent is MaxDamage but prioritizes switching to max
    damage pokemon against opponent pokemon.
    """
    def choose_move(self, battle):
        # TODO: Implement priortized switching behavior
        mon_performance : Dict[int, float] = {}
        # For each of our pokemons
        for i, mon in enumerate(battle.team.values()):
            # TODO: Make sure I'm going over available pokemon that are alive
            # We store their average performance against the current opponent mon
            mon_performance[i] = type_advantage(mon, battle.opponent_active_pokemon)

        # We sort our mons by performance
        ordered_mons = sorted(mon_performance, key=lambda k: -mon_performance[k])
        print(f"Best mon to use now is: {ordered_mons[0]}")


        # If the player can attack, it will
        if battle.available_moves:
            # Finds the best move among available ones
            best_move = max(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)

        # If no attack is available, a random switch will be made
        else:
            return self.choose_random_move(battle)

