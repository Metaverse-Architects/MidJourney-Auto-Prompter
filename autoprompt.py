import pyautogui
import time

# Read the prompts from a text file
with open('prompts.txt', 'r') as f:
    prompts = f.readlines()

# Add the /imagine command to each prompt
prompts = [prompt.strip() for prompt in prompts]

# Wait 5 seconds before starting to type
time.sleep(5)
counter = 0

# Loop through the prompts and type them in Discord
for prompt in prompts:
    pyautogui.typewrite('/imagine')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.typewrite(prompt)
    pyautogui.press('enter')
    time.sleep(5)