import gym
from gym import spaces
import pygame


class RobotArmEnv(gym.Env):
    def __init__(self):
        # Define the action and observation space for the robot arm
        self.action_space = spaces.Discrete(5)  # Five actions: extend joint 1, contract joint 1, extend joint 2, contract joint 2, do nothing
        self.observation_space = spaces.Box(low=-2, high=2, shape=(3,))  # Three observations: joint angles, gripper state
        screen = pygame.display.set_mode((600, 400))
        self.Screen = screen
        # Initialize the state of the robot arm
        self.joint1_angle = 0
        self.joint2_angle = 0
        self.gripper_state = 0  # 0: closed, 1: open

        # Define the target joint angles and the obstacle
        self.target_joint1_angle = 1
        self.target_joint2_angle = 1
        self.obstacle_x = 0
        self.obstacle_y = 0

    def step(self, action):
        # Update the state of the robot arm based on the action taken
        if action == 0:
            self.joint1_angle = min(2, self.joint1_angle + 0.1)
        elif action == 1:
            self.joint1_angle = max(-2, self.joint1_angle - 0.1)
        elif action == 2:
            self.joint2_angle = min(2, self.joint2_angle + 0.1)
        elif action == 3:
            self.joint2_angle = max(-2, self.joint2_angle - 0.1)
        elif action == 4:
            # Toggle the gripper state
            self.gripper_state = 1 - self.gripper_state

        # Move the obstacle
        self.obstacle_x += 0.1

        # Calculate the reward for the current state
        reward = self._calculate_reward()

        # Check if the episode is done
        done = self._check_done()

        # Return the new state, reward, and done flag
        return self._get_state(), reward, done, {}

    def reset(self):
        # Reset the state of the robot arm to the initial state
        self.joint1_angle = 0
        self.joint2_angle = 0
        self.gripper_state = 0
        self.obstacle_x = 0
        return self._get_state()

    def render(self, mode='human'):
        # Set the display mode and create the Pygame window
        pygame.init()
        #screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption('Robot Arm')
        screen = self.Screen
        # Run the Pygame loop
        running = True
        while running:
            # Draw the robot arm
            joint1_x = 300
            joint1_y = 200
            joint2_x = joint1_x + self.joint1_angle * 100
            joint2_y = joint1_y + self.joint2_angle * 100
            pygame.draw.circle(screen, (0, 0, 0), (joint1_x, joint1_y), 10)
            pygame.draw.circle(screen, (0, 0, 0), (joint2_x, joint2_y), 10)
            pygame.draw.line(screen, (0, 0, 0), (joint1_x, joint1_y), (joint2_x, joint2_y), 5)

            # Draw the gripper
            gripper_x = joint2_x + self.gripper_state * 20 - 10
            gripper_y = joint2_y
            pygame.draw.rect(screen, (0, 0, 0), (gripper_x, gripper_y - 10, 20, 20))

            # Draw the obstacle
            pygame.draw.circle(screen, (0, 0, 0), (self.obstacle_x, self.obstacle_y), 10)

            # Update the Pygame display
            pygame.display.flip()

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            print(f'joint1_angle: {self.joint1_angle}')
            print(f'joint2_angle: {self.joint2_angle}')
            print(f'gripper_state: {self.gripper_state}')
            print(f'obstacle_x: {self.obstacle_x}')
    def _get_state(self):
        # Return the current state of the robot arm as a tuple
        return (self.joint1_angle, self.joint2_angle, self.gripper_state)
    def _calculate_reward(self):
        # Calculate the reward based on the difference between the current joint angles and the target joint angles
        reward = -abs(self.joint1_angle - self.target_joint1_angle) - abs(self.joint2_angle - self.target_joint2_angle)

        # Penalize collisions with the obstacle
        if self._check_collision():
            reward -= 1

        # Reward grasping an object with the gripper
        if self.gripper_state == 1:
            reward += 1

        return reward

    def _check_collision(self):
        # Check if the end effector of the robot arm is in a collision with the obstacle
        end_effector_x = self.joint1_angle + self.joint2_angle
        end_effector_y = 0
        distance = ((end_effector_x - self.obstacle_x) ** 2 + (end_effector_y - self.obstacle_y) ** 2) ** 0.5
        return distance < 0.1
    def _check_done(self):
        # Check if the episode is done based on the distance between the current joint angles and the target joint angles
        done = abs(self.joint1_angle - self.target_joint1_angle) < 0.1 and abs(self.joint2_angle - self.target_joint2_angle) < 0.1
        return done


env = RobotArmEnv()
env.render()
state, reward, done, _ = env.step(0)