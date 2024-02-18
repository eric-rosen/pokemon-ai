import asyncio

from tabulate import tabulate

from poke_env import AccountConfiguration, LocalhostServerConfiguration
from poke_env.player import cross_evaluate, Player, RandomPlayer, MaxBasePowerPlayer
from typing import List, Dict, Optional
from pokemon_ai.agents.switching_max_damage import SwitchingMaxDamage

team1 = """
Charmander
Ability: Blaze
EVs: 248 HP / 8 SpA / 252 Spe
Timid Nature
IVs: 0 Atk
- Ember

Bulbasaur
Ability: Overgrow
EVs: 248 HP / 8 SpA / 252 Spe
Timid Nature
IVs: 0 Atk
- Vine Whip

Squirtle 
Ability: Torrent
EVs: 248 HP / 8 SpA / 252 Spe
Timid Nature
IVs: 0 Atk
- Water Gun
"""

async def cross_evaluate_players_gen7randombattle(player_classes : List[Player], verbose : bool = True, n_challenges : int = 20) -> Dict[str, Dict[str, Optional[float]]]:
    # TODO: turn return type into a unfied datastruct
    player_configurations : List[AccountConfiguration] = [AccountConfiguration(f"{player_idx} {player_class.__name__}"[:18], None) for player_idx, player_class in enumerate(player_classes)]
    players : List[Player] = [player_class(account_configuration=player_config,
            battle_format="gen7randombattle",
            server_configuration=LocalhostServerConfiguration,
            max_concurrent_battles=10,) for player_class, player_config in zip(player_classes,player_configurations)]

    # Now, we can cross evaluate them: every player will player 20 games against every
    # other player.
    cross_evaluation : Dict[str, Dict[str, Optional[float]]]= await cross_evaluate(players, n_challenges=n_challenges)

    # Defines a header for displaying results
    table = [["-"] + [p.username for p in players]]

    # Adds one line per player with corresponding results
    for p_1, results in cross_evaluation.items():
        table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])

    # Displays results in a nicely formatted table.
    if verbose:
        print(tabulate(table))

    return table

async def cross_evaluate_players_gen8ou_simple(player_classes : List[Player], verbose : bool = True, n_challenges : int = 20) -> Dict[str, Dict[str, Optional[float]]]:
    # TODO: turn return type into a unfied datastruct
    player_configurations : List[AccountConfiguration] = [AccountConfiguration(f"{player_idx} {player_class.__name__}"[:18], None) for player_idx, player_class in enumerate(player_classes)]
    players : List[Player] = [player_class(account_configuration=player_config,
            battle_format="gen8ou",
            team=team1,
            server_configuration=LocalhostServerConfiguration,
            max_concurrent_battles=10,) for player_class, player_config in zip(player_classes,player_configurations)]

    # Now, we can cross evaluate them: every player will player 20 games against every
    # other player.
    cross_evaluation : Dict[str, Dict[str, Optional[float]]]= await cross_evaluate(players, n_challenges=n_challenges)

    # Defines a header for displaying results
    table = [["-"] + [p.username for p in players]]

    # Adds one line per player with corresponding results
    for p_1, results in cross_evaluation.items():
        table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])

    # Displays results in a nicely formatted table.
    if verbose:
        print(tabulate(table))

    return table


if __name__ == "__main__":
    input_player_classes = [SwitchingMaxDamage, RandomPlayer]
    n_challenges = 20
    #result_table = asyncio.get_event_loop().run_until_complete(cross_evaluate_players_gen7randombattle(player_classes=input_player_classes, n_challenges=n_challenges))
    #print(result_table)
    result_table = asyncio.get_event_loop().run_until_complete(cross_evaluate_players_gen8ou_simple(player_classes=input_player_classes, n_challenges=n_challenges))
    print(result_table)