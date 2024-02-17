import asyncio

from tabulate import tabulate

from poke_env import AccountConfiguration, LocalhostServerConfiguration
from poke_env.player import cross_evaluate, Player, RandomPlayer
from typing import List


async def cross_evaluate_players(player_classes : List[Player]) -> None:
    player_configurations : list[AccountConfiguration] = [AccountConfiguration(f"{player_idx} {player_class.__name__}"[:18], None) for player_idx, player_class in enumerate(player_classes)]
    players : list[Player] = [player_class(account_configuration=player_config,
            battle_format="gen7randombattle",
            server_configuration=LocalhostServerConfiguration,
            max_concurrent_battles=10,) for player_class, player_config in zip(player_classes,player_configurations)]

    # Now, we can cross evaluate them: every player will player 20 games against every
    # other player.
    cross_evaluation = await cross_evaluate(players, n_challenges=20)

    # Defines a header for displaying results
    table = [["-"] + [p.username for p in players]]

    # Adds one line per player with corresponding results
    for p_1, results in cross_evaluation.items():
        table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])

    # Displays results in a nicely formatted table.
    print(tabulate(table))

    # TODO: Make this return the results instead


if __name__ == "__main__":
    player_classes = [RandomPlayer, RandomPlayer, RandomPlayer, RandomPlayer]
    asyncio.get_event_loop().run_until_complete(cross_evaluate_players(player_classes=player_classes))
