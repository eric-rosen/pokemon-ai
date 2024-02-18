# Current Goals
- Focus on: How do we make the best performing agent?
    - Keep track of best performing agents
        - ?: What is the best performing agents to play against right now?
    - Thinking about what metrics I'm using to measure best

# Random Questions
- ? : What format are ya'll working with / what is [OU](https://poke-env.readthedocs.io/en/stable/examples/ou_max_player.html#ou-max-player)?
    - answer: [category in smogon of most allowable category of pokemon?](https://www.smogon.com/dex/ss/formats/ou/)
- ? : What's the receommended python version (is 3.10 okay?)
- ? : Can you load the simulator to an arbitrary game state (important for simulating since
        we want to simulate the results from a state in the middle of a game multiple times.)
        - A : Seems like it would need to be done through showdown...
- ? : Anyway to get logs / export / import battles?
- ? : Can battles end in a tie? (I think i've seen cases where the cross-eval doesn't add to 1?)


# References:
- [cross_evaluate_random_players](poke-env/examples/gen7/cross_evaluate_random_players.py)
    - shows how to register multiple agents to server and play against eachother
- [max_damage_player.py](poke-env/examples/max_damage_player.py)
- [ou_max_player.py](poke-env/examples/ou_max_player.py)
    - make a team and manage team preview (?: select your pokemon team order + see their pokemon)

# TODOs
- Evaluate a mixed bag of agents against eachother
    - ~~random, max-damage~~, SimpleHeuristicsPlayer
    - look at the metrics, try to think of 5 other metrics to keep track of
        - look at games for interesting proxies
    - ~~make my own agent and evaluate it against the others~~
        - I implemented `SwitchingMaxDamage`, it seems to outperform Random in general (gen7-random, rock-paper-scissors), and it outperforms `MaxDamage` in rock-paper-scissor, but in gen7-random it is about equal in performance. Any ideas why ?
            - possible reason: the `type_advantage` is based on the type of the pokemon, not the moveset. Confirm this in rock paper scissor by taking away useful type move and show it still choosed based on pokemon type. Then make a `type_advatage` that is based on move types (maybe also power?)
            - why doesn't it beat random every time?
- start looking into MCTS / minmax w/ alpha-beta pruning approach (model based planning)
- consider: start with small pool of pokemon
    - specify gen 1?
- Look into the [showdown bots](http://sahovic.fr/pokemon-ai-resources/)
- make it easier for me to find battles / load them (e.g: situations where my agent loses)

# My strategy ideas
- Switching MaxDamage
    - MaxDamage agent, but if I can switch to a better pokemon to kill you, I do it
    - Issues:
        - it loses to random in rock/paper/sccissor because opponent is switching out a lot
            - my agent ends up not doing much damage cause it spends time switching (generally an opponent switch causes me to switch)
            - my agent does two switches in a row when opponent pokemon dies, they throw in pokemon 1 (which my agent decides to switch against) and their first move is switch to pokemon 2. When I switch my pokemon in, I immediately switch again to prioritize pokemon 2.

# Agent specification
def Class(Player):
- def choose_move(self, battle)
    - select action in battle
- def teampreview(self, battle)
    - select initial team order