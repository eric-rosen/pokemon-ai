"""
metrics for determining the value of mon_a vs. mon_b. Higher is better for
mon_a, lower is worse for mon_b
"""

from poke_env.environment.pokemon import Pokemon
import numpy as np

def type_advantage(mon_a : Pokemon, mon_b : Pokemon) -> float:
    """
    Calculates type advantage over best move of a_on_b, b_on_a,
    then returns a_on_b - b_on_a.
    """
    # We evaluate the performance on mon_a against mon_b as its type advantage
    a_on_b = b_on_a = -np.inf
    for type_ in mon_a.types:
        if type_:
            a_on_b = max(a_on_b, type_.damage_multiplier(*mon_b.types))
    # We do the same for mon_b over mon_a
    for type_ in mon_b.types:
        if type_:
            b_on_a = max(b_on_a, type_.damage_multiplier(*mon_a.types))
    # Our performance metric is the different between the two
    return a_on_b - b_on_a
