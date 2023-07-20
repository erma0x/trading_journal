import pygame
import csv
import sys

pathfile = sys.path[0]

class InputBox:
    def __init__(self, x, y, width, height, description):
        self.rect = pygame.Rect(x, y, width, height)
        font_path = pathfile + "/font.ttf"
        font_size = 13
        
        self.font = pygame.font.Font(font_path, font_size)
        self.text = ""
        self.active = False
        self.description = description

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def render(self, surface):
        color = (255, 255, 255) if self.active else (200, 200, 200)
        pygame.draw.rect(surface, color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        description_surface = self.font.render(self.description, True, (255, 255, 255))
        surface.blit(description_surface, (self.rect.x - 200, self.rect.y + 5))

def save_data():
    data = {
        "Date": entry_data.text,
        "Symbol/Ticker": entry_symbol.text,
        "Direction": entry_direction.text,
        "Entry Price": entry_entry_price.text,
        "Exit Price": entry_exit_price.text,
        "Position Size": entry_position_size.text,
        "Risk Reward Ratio (R:R)": entry_rr.text,
        "Trade Motivation": entry_trade_motivation.text,
        "Comments": entry_comments.text
    }

    with open('trading_journal.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

    clear_fields()

def clear_fields():
    entry_data.text = ""
    entry_symbol.text = ""
    entry_direction.text = ""
    entry_entry_price.text = ""
    entry_exit_price.text = ""
    entry_position_size.text = ""
    entry_rr.text = ""
    entry_trade_motivation.text = ""
    entry_comments.text = ""

# Initialize Pygame
pygame.init()

# Window dimensions
width = 700
height = 500

# Create the window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trading Journal")

# Load the background image
background_path = pathfile + "/background.jpg"
background = pygame.image.load(background_path)
background = pygame.transform.scale(background, (width, height))

# Function to draw the background image
def draw_background():
    window.blit(background, (0, 0))

# Initialize input fields
field_width = 300
field_height = 30
field_spacing = 35

entry_data = InputBox(width/1.7 - field_width/2, 50, field_width, field_height, "Date:")
entry_symbol = InputBox(width/1.7 - field_width/2, 50 + field_spacing, field_width, field_height, "Symbol/Ticker:")
entry_direction = InputBox(width/1.7 - field_width/2, 50 + field_spacing * 2, field_width, field_height, "Direction:")
entry_entry_price = InputBox(width/1.7 - field_width/2, 50 + field_spacing * 3, field_width, field_height, "Entry Price:")
entry_exit_price = InputBox(width/1.7 - field_width/2, 50 + field_spacing * 4, field_width, field_height, "Exit Price:")
entry_position_size = InputBox(width/1.7 - field_width/2, 50 + field_spacing * 5, field_width, field_height, "Position Size:")
entry_rr = InputBox(width/1.7 - field_width/2, 50 + field_spacing * 6, field_width, field_height, "Risk Reward Ratio (R:R):")
entry_trade_motivation = InputBox(width/1.7 - field_width/2, 50 + field_spacing * 7, field_width, field_height, "Trade Motivation:")
entry_comments = InputBox(width/1.7 - field_width/2, 50 + field_spacing * 8, field_width, field_height, "Comments:")

# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            entry_data.handle_event(event)
            entry_symbol.handle_event(event)
            entry_direction.handle_event(event)
            entry_entry_price.handle_event(event)
            entry_exit_price.handle_event(event)
            entry_position_size.handle_event(event)
            entry_rr.handle_event(event)
            entry_trade_motivation.handle_event(event)
            entry_comments.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if (width/2 - btn_salva_text.get_width()/2 <= mouse_pos[0] <= width/2 + btn_salva_text.get_width()/2 and
                        400 <= mouse_pos[1] <= 430):
                    save_data()

    # Draw the background image
    draw_background()

    # Draw the input fields
    entry_data.render(window)
    entry_symbol.render(window)
    entry_direction.render(window)
    entry_entry_price.render(window)
    entry_exit_price.render(window)
    entry_position_size.render(window)
    entry_rr.render(window)
    entry_trade_motivation.render(window)
    entry_comments.render(window)

    # Draw the "Save" button
    font_path = pathfile + "/font.ttf"
    font_size = 16
        
    font = pygame.font.Font(font_path, font_size)
    
    btn_salva_text = font.render("Save", True, (255, 255, 255))
    btn_salva_rect = btn_salva_text.get_rect(center=(width/2, 415))
    pygame.draw.rect(window, (20, 150, 100), btn_salva_rect)
    window.blit(btn_salva_text, btn_salva_rect.topleft)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
