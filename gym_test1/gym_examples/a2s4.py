import gym
import gym_examples
env = gym.make("gym_examples/a2s4-v0", render_mode="human")
env.action_space.seed(42)

size = 4
agent = 2
K= 5
observation, info = env.reset(seed=42)
print(observation)
solution = [24, 22, 23, 23, 21, 20, 23, 23, 20, 20, 20, 23, 20, 20, 20, 24, 14, 12, 13, 13, 11, 13, 13, 13, 10, 10, 10, 13, 10, 10, 10, 14, 19, 17, 17, 13, 16, 17, 13, 13, 16, 10, 13, 13, 10, 10, 10, 14, 19, 17, 17, 17, 16, 17, 17, 13, 16, 19, 13, 13, 16, 10, 10, 14, 9, 7, 8, 8, 6, 8, 8, 8, 5, 5, 5, 8, 5, 5, 5, 9, 19, 17, 17, 13, 16, 16, 13, 13, 1, 10, 10, 8, 5, 5, 5, 9, 19, 17, 17, 17, 16, 16, 17, 13, 16, 16, 10, 13, 20, 10, 10, 14, 19, 17, 17, 17, 16, 17, 17, 13, 16, 16, 17, 13, 16, 16, 10, 14, 4, 2, 2, 8, 1, 1, 8, 8, 1, 5, 5, 8, 5, 5, 5, 9, 4, 2, 2, 23, 1, 1, 2, 8, 1, 1, 5, 8, 1, 5, 5, 9, 19, 17, 17, 17, 16, 16, 2, 17, 1, 1, 2, 8, 1, 1, 5, 9, 19, 17, 17, 17, 16, 16, 17, 17, 16, 16, 16, 18, 16, 16, 15, 19, 4, 2, 2, 2, 1, 1, 4, 8, 1, 1, 5, 8, 1, 5, 5, 9, 4, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 8, 1, 5, 5, 9, 4, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 3, 1, 1, 0, 4, 24, 22, 22, 22, 21, 21, 22, 22, 21, 21, 21, 23, 21, 21, 20, 24]
for _ in range(100):
    x,y = observation["agent1"]
    x1,y1 = observation["agent2"]
    a1 = int(x)+int(y)*size
    a2 = int(x1) + int(y1) * size
    total_action = solution[a1 * size * size + a2]
    print(total_action)
    action1, action2 = divmod(total_action, K)

    action = str(action1) + str(action2)
    print(observation)
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()