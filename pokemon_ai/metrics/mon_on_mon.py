"""
metrics for determining the value of mon_a vs. mon_b. Higher is better for
mon_a, lower is worse for mon_b
"""

from poke_env.environment.pokemon import Pokemon
import numpy as np
from poke_env.data import GenData

GEN8_TYPE_CHART = GenData.from_gen(8).type_chart

def type_advantage(mon_a : Pokemon, mon_b : Pokemon) -> float:
    """
    Calculates type advantage over best move of a_on_b, b_on_a,
    then returns a_on_b - b_on_a. This comes from poke_env
    """
    # We evaluate the performance on mon_a against mon_b as its type advantage
    a_on_b = b_on_a = -np.inf
    for a_type in mon_a.types:
        for b_type in mon_b.types:
            if a_type and b_type:
                a_on_b = max(a_on_b, a_type.damage_multiplier(b_type, type_chart=GEN8_TYPE_CHART))
    # We do the same for mon_b over mon_a
    for b_type in mon_b.types:
        for a_type in mon_a.types:
            if a_type and b_type:
                b_on_a = max(b_on_a, b_type.damage_multiplier(a_type, type_chart=GEN8_TYPE_CHART))
    # Our performance metric is the different between the two
    return a_on_b - b_on_a
