import pygame
import os

# Initialize Pygame
pygame.init()

# Set the window size
window_width, window_height = 500, 200
window = pygame.display.set_mode((window_width, window_height))

# Set the caption
pygame.display.set_caption("Music Player")

# Set the font
font = pygame.font.Font(None, 36)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)

# Define the music directory
music_dir = "F:\songs"

# Get the list of music files
music_files = os.listdir(music_dir)

# Set the initial volume
volume = 0.5

# Load the first music file
current_track = 0
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

# Function to play the current track
def play_track():
    pygame.mixer.music.play()

# Function to pause the current track
def pause_track():
    pygame.mixer.music.pause()

# Function to resume the current track
def resume_track():
    pygame.mixer.music.unpause()

# Function to stop the current track
def stop_track():
    pygame.mixer.music.stop()

# Function to play the next track
def play_next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    play_track()

# Function to play the previous track
def play_previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    play_track()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    window.fill(white)

    # Render the music controls
    play_text = font.render("Play", True, black)
    pause_text = font.render("Pause", True, black)
    resume_text = font.render("Resume", True, black)
    stop_text = font.render("Stop", True, black)
    next_text = font.render("Next", True, black)
    previous_text = font.render("Previous", True, black)
    volume_text = font.render("Volume", True, black)

    # Draw the music controls
    window.blit(play_text, (50, 50))
    window.blit(pause_text, (50, 100))
    window.blit(resume_text, (50, 150))
    window.blit(stop_text, (200, 50))
    window.blit(next_text, (200, 100))
    window.blit(previous_text, (200, 150))
    window.blit(volume_text, (350, 50))

    # Draw the volume control bar
    pygame.draw.rect(window, black, (400, 100, 20, 100))
    pygame.draw.rect(window, gray, (400, int(200 - volume * 100), 20, int(volume * 100)))

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the music controls are clicked
    if 50 <= mouse_x <= 50 + play_text.get_width() and 50 <= mouse_y <= 50 + play_text.get_height():
        if pygame.mouse.get_pressed()[0]:
            play_track()
    elif 50 <= mouse_x <= 50 + pause_text.get_width() and 100 <= mouse_y <= 100 + pause_text.get_height():
        if pygame.mouse.get_pressed()[0]:
            pause_track()
    elif 50 <= mouse_x <= 50 + resume_text.get_width() and 150 <= mouse_y <= 150 + resume_text.get_height():
        if pygame.mouse.get_pressed()[0]:
            resume_track()
    elif 200 <= mouse_x <= 200 + stop_text.get_width() and 50 <= mouse_y <= 50 + stop_text.get_height():
        if pygame.mouse.get_pressed()[0]:
            stop_track()
    elif 200 <= mouse_x <= 200 + next_text.get_width() and 100 <= mouse_y <= 100 + next_text.get_height():
        if pygame.mouse.get_pressed()[0]:
            play_next_track()
    elif 200 <= mouse_x <= 200 + previous_text.get_width() and 150 <= mouse_y <= 150 + previous_text.get_height():
        if pygame.mouse.get_pressed()[0]:
            play_previous_track()
    elif 400 <= mouse_x <= 420 and 100 <= mouse_y <= 200:
        if pygame.mouse.get_pressed()[0]:
            volume = (200 - mouse_y) / 100
            pygame.mixer.music.set_volume(volume)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
