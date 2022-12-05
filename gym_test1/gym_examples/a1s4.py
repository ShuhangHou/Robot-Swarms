import gym
import gym_examples
env = gym.make("gym_examples/a1s4-v0", render_mode="human")
env.action_space.seed(42)

size = 4
agent = 1
observation, info = env.reset(seed=42)
print(observation)
solution = [0, 2, 2, 2, 1, 1, 0, 3, 1, 0, 0, 3, 0, 0, 0, 0]
for _ in range(100):
    x,y = observation["agent"]
    #y = observation["agent"]

    action = solution[int(x)+int(y)*size]
    print(observation)
    print(action)
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()