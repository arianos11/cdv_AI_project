import numpy as np

class MazeSolver:
    def __init__(self, maze, start, end, epsilon=0.3, alpha=0.5, gamma=0.9, episodes=10000):
        self.maze = maze
        self.start = start
        self.end = end
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.episodes = episodes
        self.states = [(i, j) for i in range(len(maze)) for j in range(len(maze[0]))]
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # prawo, lewo, dół, góra
        self.q_table = self.initialize_q_table()

    def initialize_q_table(self):
        q_table = {}
        for state in self.states:
            q_table[state] = {}
            for action in self.actions:
                q_table[state][action] = 0.0
        return q_table

    def choose_action(self, state):
        if np.random.uniform() < self.epsilon:
            action = self.actions[np.random.choice(len(self.actions))]
        else:
            action = max(list(self.q_table[state].items()), key=lambda x: x[1])[0]
        return action

    def learn(self):
        for episode in range(self.episodes):
            state = self.start
            while state != self.end:
                action = self.choose_action(state)
                next_state = (state[0] + action[0], state[1] + action[1])
                if 0 <= next_state[0] < len(self.maze) and 0 <= next_state[1] < len(self.maze[0]) and self.maze[next_state[0]][next_state[1]] != 1:
                    reward = 1 if next_state == self.end else -0.01
                    q_predict = self.q_table[state][action]
                    if next_state != self.end:
                        q_target = reward + self.gamma * max(self.q_table[next_state].values())
                    else:
                        q_target = reward
                        state = self.start
                    self.q_table[state][action] += self.alpha * (q_target - q_predict)
                    state = next_state
                else:
                    self.q_table[state][action] = -1

maze = [
  [1,1,1,1,1,1,1,1,1,1],
  [1,0,1,1,1,0,1,0,0,1],
  [1,0,1,0,0,0,0,0,1,1],
  [1,0,1,1,0,1,1,0,0,1],
  [1,0,0,0,0,0,0,1,1,1],
  [1,0,1,1,1,0,1,1,1,1],
  [1,1,0,0,0,0,0,0,1,1],
  [1,1,0,1,1,0,1,1,1,1],
  [1,0,0,1,1,0,0,0,2,1],
  [1,1,1,1,1,1,1,1,1,1]
]

start = (1, 1)  # początkowy punkt gracza
end = (8, 8)  # cel podróży

solver = MazeSolver(maze, start, end)
solver.learn()

print("Q-table po uczeniu:")
for state in solver.q_table:
    print(state, solver.q_table[state])