import os
import time
import keyboard
import random
from threading import Thread

class SpaceInvaders:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.player_pos = self.width // 2
        self.player = "^"
        self.enemy = "V"
        self.bullet = "|"
        self.enemies = [(random.randint(0, self.width-1), 0) for _ in range(5)]
        self.bullets = []
        self.score = 0
        self.game_over = False
        
    def draw_screen(self):
        # Create empty screen
        screen = [[" " for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw player
        screen[-1][self.player_pos] = self.player
        
        # Draw enemies
        for ex, ey in self.enemies:
            if 0 <= ey < self.height and 0 <= ex < self.width:
                screen[ey][ex] = self.enemy
                
        # Draw bullets
        for bx, by in self.bullets:
            if 0 <= by < self.height and 0 <= bx < self.width:
                screen[by][bx] = self.bullet
        
        # Convert to string
        return "\n".join(["".join(row) for row in screen])
    
    def move_player(self, direction):
        if direction == "left" and self.player_pos > 0:
            self.player_pos -= 1
        elif direction == "right" and self.player_pos < self.width - 1:
            self.player_pos += 1
            
    def shoot(self):
        self.bullets.append((self.player_pos, self.height - 2))
        
    def update(self):
        # Move bullets
        new_bullets = []
        for bx, by in self.bullets:
            if by > 0:
                new_bullets.append((bx, by - 1))
        self.bullets = new_bullets
        
        # Move enemies down
        new_enemies = []
        for ex, ey in self.enemies:
            if ey < self.height - 1:
                new_enemies.append((ex, ey + 1))
            else:
                self.game_over = True
        self.enemies = new_enemies
        
        # Check collisions
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet[0] == enemy[0] and bullet[1] == enemy[1]:
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                        self.score += 10
        
        # Add new enemies
        if random.random() < 0.1:
            self.enemies.append((random.randint(0, self.width-1), 0))
            
    def run(self):
        def input_thread():
            while not self.game_over:
                try:
                    if keyboard.is_pressed('left'):
                        self.move_player('left')
                    if keyboard.is_pressed('right'):
                        self.move_player('right')
                    if keyboard.is_pressed('space'):
                        self.shoot()
                except:
                    pass
                time.sleep(0.05)
        
        Thread(target=input_thread, daemon=True).start()
        
        while not self.game_over:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.draw_screen())
            print(f"\nScore: {self.score}")
            print("\nUse left/right arrows to move, space to shoot")
            self.update()
            time.sleep(0.1)
            
        print("\nGame Over! Final score:", self.score)

if __name__ == "__main__":
    game = SpaceInvaders()
    game.run()