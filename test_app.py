import pytest
from trading_journal import InputBox, salva_dati, pulisci_campi

# Test InputBox class
def test_input_box_creation():
    input_box = InputBox(100, 200, 150, 30, "Test Description")
    assert input_box.rect.x == 100
    assert input_box.rect.y == 200
    assert input_box.rect.width == 150
    assert input_box.rect.height == 30
    assert input_box.description == "Test Description"
    assert input_box.text == ""
    assert not input_box.active

def test_input_box_handle_event():
    input_box = InputBox(100, 200, 150, 30, "Test Description")

    # Test mouse click event
    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': (110, 210)})
    input_box.handle_event(event)
    assert input_box.active

    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': (50, 250)})
    input_box.handle_event(event)
    assert not input_box.active

    # Test keydown event
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
    input_box.text = "Test Text"
    input_box.active = True
    input_box.handle_event(event)
    assert not input_box.active

    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_BACKSPACE})
    input_box.text = "Test Text"
    input_box.active = True
    input_box.handle_event(event)
    assert input_box.text == "Test Tex"

    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_a, 'unicode': 'a'})
    input_box.text = "Test Text"
    input_box.active = True
    input_box.handle_event(event)
    assert input_box.text == "Test Texta"
