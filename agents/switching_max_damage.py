"""
This agent is similar to MaxDamagePlayer, except it will always priotize
switching to the available pokemon that is strongest against the current
opponent's pokemon.
"""

from poke_env.player import Player

class SwitchingMaxDamage(Player):
    """
    Agent is MaxDamage but prioritizes switching to max
    damage pokemon against opponent pokemon.
    """
    def choose_move(self, battle):
        # TODO: Implement priortized switching behavior

        # If the player can attack, it will
        if battle.available_moves:
            # Finds the best move among available ones
            best_move = max(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)

        # If no attack is available, a random switch will be made
        else:
            return self.choose_random_move(battle)

