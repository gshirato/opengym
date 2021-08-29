import gym
import numpy as np


class PokerEnv(gym.Env):
    def __init__(self, n_players):
        self.n_players = n_players
        self.ACTION_MAP = [
            'check',
            'bet',
            'call',
            'raise'
        ]
        ACTION_NUM = 4
        self.action_space = gym.spaces.Discrete(ACTION_NUM)
        self.observation_space = gym.spaces.Box(
            low=[0] * self.n_players,
            high=[np.inf] * self.n_players
        )

        self.reset()

    def reset(self):
        self.stacks = [3000] * self.n_players
        observation = self.stacks
        return observation

    def step(self, action_index, user_index):
        action = self.ACTION_MAP[action_index]

        if action == 'check':
            pass
        elif action == 'bet':
            pass
        elif action == 'call':
            pass
        elif action == 'raise':
            pass
        else:
            raise(action)

        observation = self.stacks
        reward = self.stacks[user_index]

        done = self.is_done()
        
        return observation, reward, done

    def is_done(self):
        return np.count_nonzero(self.stacks) == 1
