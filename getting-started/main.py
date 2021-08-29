import gym
import numpy as np


def main():
    env = gym.make('MountainCar-v0')
    observation = env.reset()

    # 0: push left, 1: do nothing, 2: push right
    action = 0  # TODO: make algorithm
    obs, reward, done, info = env.step(action)

    # TODO: evaluate action from reward
    # make q_table
    q_table = np.zeros((40, 40, 3))


def make_state_from_obs(env, obs):
    '''
    観測値から状態を取得する
    例: 連続地を離散値に変換する
    '''
    env_low = env.observation_space.low  # 位置と速度の最小値
    env_high = env.observation_space.high  # 　位置と速度の最大値
    env_dx = (env_high - env_low) / 40  # 40等分
    # 0〜39の離散値に変換する
    position = int((obs[0] - env_low[0]) / env_dx[0])
    velocity = int((obs[1] - env_low[1]) / env_dx[1])
    return position, velocity


def update_q_table(env, _q_table, _action, _observation, _next_observation, _reward, _episode):

    alpha = 0.2  # 学習率
    gamma = 0.99  # 時間割引き率

    # 行動後の状態で得られる最大行動価値 Q(s',a')
    next_position, next_velocity = make_state_from_obs(env, _next_observation)
    next_max_q_value = max(_q_table[next_position][next_velocity])

    # 行動前の状態の行動価値 Q(s,a)
    position, velocity = make_state_from_obs(_observation)
    q_value = _q_table[position][velocity][_action]

    # 行動価値関数の更新
    _q_table[position][velocity][_action] = q_value + alpha * (_reward + gamma * next_max_q_value - q_value)

    return _q_table


def get_action(_env, _q_table, _observation, _episode):
    epsilon = 0.002
    if np.random.uniform(0, 1) > epsilon:
        position, velocity = make_state_from_obs(_env, _observation)
        _action = np.argmax(_q_table[position][velocity])
    else:
        _action = np.random.choice([0, 1, 2])
    return _action
