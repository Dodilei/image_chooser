from PIL import Image
import matplotlib.pyplot as plt
import os

DIR = input('images directory: ')
SAVE_DIR = input('saved images directory: ')
REM_DIR = input('removed images directory: ')

os.system(f'mkdir {SAVE_DIR}')
os.system(f'mkdir {REM_DIR}')

start = input('start index [0]: ')
if not start.isdigit():
    start = 0
else:
    start = int(start)

for i, name in enumerate(os.listdir(DIR)):

    if i < start: continue

    image_path = os.path.join(DIR, name)

    os.system('clear')

    with Image.open(image_path) as image:
        plt.imshow(image)
        plt.show()

    action = input('action: ')

    if action == 'exit':
        print(i)
        break
    elif action == 'r':
        new_path = os.path.join(REM_DIR, name)
    else:
        new_path = os.path.join(SAVE_DIR, name)

    os.system('mv {} {}'.format(image_path, new_path))

