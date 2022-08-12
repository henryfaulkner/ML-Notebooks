"""
Created on Fri Oct 30 17:18:17 2020
@author: joshuageiser
"""
import os
import numpy as np
import pandas as pd
import random


class Params():
    def __init__(self):
        # "input", "random_policy", "fixed_policy"
        self.action_type = "random_policy"

        # Only used for "random_policy" or "fixed_policy" input
        self.num_games = 20000

        # Filepath to fixed policy file (only used for ’fixed_policy’ input)
        self.fixed_policy_filepath = os.path.join(
            os.getcwd(), 'Sarsa_Policy_2.policy')

        # Which state mapping algorithm to use (1 or 2)
        self.state_mapping = 1
        return


'''
State Mapping 1: state = players_hand - 1
State 0 - lose state
State 1 - win state
State 2 - terminal state
State 3 - players hand sums to 4
State 4 - players hand sums to 5
State 5 - players hand sums to 6
State 6 - players hand sums to 7
...
State 19 - players hand sums to 20
State 20 - players hand sums to 21
-------------------------------------------------------------------------------
State Mapping 2: state = (players_hand - 1) + (18 * (dealers_hand-1))
State 0 - lose state
State 1 - win state
State 2 - terminal state
State 3 - players hand sums to 4, dealers hand is 1
State 4 - players hand sums to 5, dealers hand is 1
...
State 19 - players hand sums to 20, dealers hand is 1
State 20 - players hand sums to 21, dealers hand is 1
State 21 - players hand sums to 4, dealers hand is 2
State 22 - players hand sums to 5, dealers hand is 2
...
State 181 - players hand sums to 20, dealers hand is 10
State 182 - players hand sums to 21, dealers hand is 10
'''


class BlackJack_game():
    def __init__(self, params):
        # 1 = Ace, 2-10 = Number cards, Jack/Queen/King = 10
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
        random.shuffle(self.deck)
        # Player and dealer hands
        self.player = self.draw_hand()
        self.dealer = [self.draw_card()]
        # State, Action, Reward, Next State arrays
        self.sarsp = []
        self.sarsp_arr = np.array([], dtype="int").reshape(0, 4)
        # Various other parameters
        # "input", "random_policy", "fixed_policy"
        self.action_type = params.action_type
        self.verbose = (params.action_type == "input")
        self.num_games = params.num_games
        self.fixed_policy_filepath = params.fixed_policy_filepath
        self.policy = self.load_policy()
        self.state_mapping = params.state_mapping
        # Probably do not need to change these
        self.lose_state = 0
        self.win_state = 1
        self.terminal_state = 2
        # Also do not need to change these
        self.lose_reward = -10
        self.win_reward = 10
        return

    # Reset deck, player/dealer hands, and sarsp for a new game
    def reset(self):
        self.player = self.draw_hand()
        self.dealer = [self.draw_card()]
        self.sarsp = []
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
        random.shuffle(self.deck)
        return

    # Draw random card from deck
    def draw_card(self):
        return self.deck.pop()

    # Dras random hand (2 random cards from deck)
    def draw_hand(self):
        return [self.draw_card(), self.draw_card()]

    # Does this hand have a usable ace?
    def usable_ace(self, hand):
        return 1 in hand and sum(hand) + 10 <= 21

    # Return current hand total
    def sum_hand(self, hand):
        if self.usable_ace(hand):
            return sum(hand) + 10
        return sum(hand)

    # Is this hand a bust?
    def is_bust(self, hand):
        return self.sum_hand(hand) > 21

    # What is the score of this hand (0 if bust)
    def score(self, hand):
        return 0 if self.is_bust(hand) else self.sum_hand(hand)

    # Return True if the player won or False if the dealer won
    def player_won(self, player, dealer):
        if self.is_bust(player):
            return False
        elif self.is_bust(dealer):
            return True
        elif self.sum_hand(player) > self.sum_hand(dealer):
            return True
        else:
            return False

    # Map the current player"s hand to a state index
    def hand_to_state(self, player, dealer):
        if self.state_mapping == 1:
            return self.sum_hand(player) - 1
        elif self.state_mapping == 2:
            return (self.sum_hand(player) - 1) + (18 * (dealer[0] - 1))

    # Get reward based off of current state and action (may get rid of this
    # function, not really being used at the moment)
    def get_reward(self, state, action, player, dealer):
        if self.state_mapping == 1:
            return 0
        else:
            if ((self.sum_hand(player) <= 11 and action == 1) or
                    (self.sum_hand(player) >= 17 and action == 0)):
                return 1
            elif ((self.sum_hand(player) <= 11 and action == 0) or
                  (self.sum_hand(player) >= 17 and action == 1)):
                return -1
            else:
                return 0

    # Load policy from input .policy file into self.policy
    def load_policy(self):
        # Policy not needed if a user is playing or a random policy is being used
        if self.action_type in ["random_policy", "input"]:
            return None
        # Read policy file and extract policy
        f = open(self.fixed_policy_filepath, "r")
        data = f.read()
        data = data.split()
        policy = [int(x) for x in data]
        return policy

    # Print data about the current player"s/dealer"s hands
    # This only used for "input" mode where user is playing a single blackjack game
    def print_iter(self):
        if not self.verbose:
            return
        print(
            f"Player hand: {self.player}\t\t sum: {self.sum_hand(self.player)}")
        print(
            f"Dealer hand: {self.dealer}\t\t sum: {self.sum_hand(self.dealer)}")
        return

    # Get action depending on if user is playing, or if a random/fixed policy
    # is being used
    def get_action(self, state):
        if self.action_type == "input":
            action = int(input("Hit(1) or Pass(0): "))
        elif self.action_type == "random_policy":
            action = np.random.randint(2)
        elif self.action_type == "fixed_policy":
            action = self.policy[state]
        return action

    # Play a single game of BlackJack!
    def play_game(self):
        # Only for "input" mode
        if self.verbose:
            print("New Game!\n")

        # Iterate through game
        done = False
        while(not done):
            # Only for "input" mode
            self.print_iter()

            # Current state/action/reward
            state = self.hand_to_state(self.player, self.dealer)
            action = self.get_action(state)
            reward = self.get_reward(state, action, self.player, self.dealer)

            if action:  # hit: add a card to players hand and return
                self.player.append(self.draw_card())
                if self.is_bust(self.player):
                    done = True
                else:
                    done = False
            else:  # stick: play out the dealers hand, and score
                while self.sum_hand(self.dealer) < 17:
                    self.dealer.append(self.draw_card())
                done = True

            # Add a row to sarsp as long as we still have more iterations
            # through the while loop
            if(not done):
                sp = self.hand_to_state(self.player, self.dealer)
                self.sarsp.append([state, action, reward, sp])

        # Only for "input" mode
        self.print_iter()

        # Check if player won
        player_won_bool = self.player_won(self.player, self.dealer)

        # Set next state to win state or lose state based on if player won/lost
        if player_won_bool:
            sp = self.win_state
        else:
            sp = self.lose_state
        self.sarsp.append([state, action, reward, sp])

        # Add a row with 0 action, win/loss reward, and terminal state for next state
        state = sp
        if player_won_bool:
            reward = self.win_reward
            print("reward")
            print(reward)
        else:
            reward = self.lose_reward
            print("reward")
            print(reward)

        self.sarsp.append([state, np.random.randint(2),
                          reward, self.terminal_state])

        # Only for "input" mode
        if self.verbose:
            print(f"Player won?: {player_won_bool}")

        # Append current run data to full sarsp_arr
        self.sarsp_arr = np.vstack((self.sarsp_arr, np.array(self.sarsp)))
        return

    # Output CSV file of runs if a random_policy was used
    def output_sarsp_file(self):
        filename = f"random_policy_runs_mapping_{self.state_mapping}.csv"
        output_filepath = os.path.join(os.getcwd(), filename)
        header = ["s", "a", "r", "sp"]
        pd.DataFrame(self.sarsp_arr).to_csv(
            output_filepath, header=header, index=None)
        return

    # Print win/loss stats if a random or fixed policy was used
    def print_stats(self):
        num_wins = np.count_nonzero(self.sarsp_arr[:, 0] == self.win_state)
        num_lose = np.count_nonzero(self.sarsp_arr[:, 0] == self.lose_state)
        print(f"Number of games: {self.num_games}")
        print(f"Number of wins: {num_wins}")
        print(f"Number of losses: {num_lose}")
        print(f"Win Percentage: {num_wins / self.num_games: .3f}")
        return

    # Simulate (num_games) games of BlackJack!
    def play_games(self):
        # Iterate through num_games
        for i in range(self.num_games):
            self.play_game()
            self.reset()

        # print(self.sarsp_arr)
        self.print_stats()

        # Output CSV file of runs if a random_policy was used
        if self.action_type == "random_policy":
            self.output_sarsp_file()
        return
# End BlackJack_game class ################################################


def main():
    # Input parameters
    params = Params()
    assert (params.action_type in ["input", "fixed_policy", "random_policy"]
            ), "Action type must be 'input', 'fixed_policy', or 'random_policy'"

    # BlackJack_game object
    game = BlackJack_game(params)

    # Play one game if user is playing or simulate many if a random/fixed
    # policy is being used
    if params.action_type == "input":
        game.play_game()
    else:
        game.play_games()
    return


if __name__ == "__main__":
    main()
