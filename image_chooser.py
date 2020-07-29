from IPython.display import clear_output
from PIL import Image, UnidentifiedImageError
import matplotlib.pyplot as plt

import time
import os

BASE_DIR = 'ChosenImages'

def main(idir = None, sdir = None, rdir = None, delete = False, **kwargs):
    DIR = idir if idir else input('images directory: ')
    SAVE_DIR = sdir if sdir else input('saved images directory: ')
    REM_DIR = rdir if (rdir or delete) else input('removed images directory: ')

    SAVE_DIR = os.path.join(BASE_DIR, SAVE_DIR)
    REM_DIR = os.path.join(BASE_DIR, REM_DIR)

    os.system(f'mkdir \'{SAVE_DIR}\'')
    os.system(f'mkdir \'{REM_DIR}\'')
    os.system(f'mkdir {os.path.join(BASE_DIR, "ERROR")}')
    
    dirkeys = {}
    for key in kwargs:
        cdir = os.path.join(BASE_DIR, key)
        os.system(f'mkdir \'{cdir}\'')
        dirkeys[kwargs[key]] = cdir
    
    dirkeys['#error'] = os.path.join(BASE_DIR, 'ERROR')

    #start = input('start index [0]: ')
    #if not start.isdigit():
    #    start = 0
    #else:
    #    start = int(start)

    def extension(filename, *extensions):

        bools = [filename.endswith(e) for e in extensions]
        return any(bools)
    
    starttime = time.time()
    
    history = []

    im = 0
    for i, name in enumerate(os.listdir(DIR)):

        #if i < start: continue

        if not extension(name, 'jpg', 'jpeg', 'png'): continue
        im += 1

        image_path = os.path.join(DIR, name)

        def handle_action():
        
            clear_output()
            try:
                with Image.open(image_path) as image:

                    plt.figure(figsize=(20,10))
                    plt.axis('off')

                    plt.imshow(image)
                    plt.show()
                    
            except UnidentifiedImageError:
                return '#error'

            action = input('action: ')

            if action == 'history':
                clear_output()
                for i, h in enumerate(history):
                    print(i, ":", h)
                input('press enter to continue')
                return handle_action()
            
            return action
        
        
        action = handle_action()

        if action == 'exit':
            print(i, ' files read. ', 'Images chosen: ', im)
            totaltime = round(time.time()-starttime, 2)
            print('Time choosing: ', totaltime, 's')
            print('Time per image', round(totaltime/im, 3), 's')
            break

        elif action == 'r':
            did = f'Removed {name}'

            if delete:
                os.system('rm \'{}\''.format(image_path))
                continue
            new_path = os.path.join(REM_DIR, name)

        else:
            try:
                custom_dir = dirkeys[action]
                new_path = os.path.join(custom_dir, name)
                did = f'Save {name} at {custom_dir}'
            except KeyError:
                new_path = os.path.join(SAVE_DIR, name)
                did = f'Save {name}'

        os.system('mv \'{}\' \'{}\''.format(image_path, new_path))
        history.append(did)
    

        

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "inputdir",
        help="directory where images are stored",
    )
    parser.add_argument(
        "-s", "--save-dir",
        help="directory for saving chosen images"
    )
    parser.add_argument(
        "-t", "--trash-dir",
        help="directory for storing removed images",
        default=None
    )
    parser.add_argument(
        "-r", "--delete",
        action="store_true",
        help="force deletion of removed images"
    )
    parser.add_argument(
        "-d", "--more-dirs",
        help="dict-like structure for further image organization"
    )

    args = parser.parse_args()

    main(args.inputdir, args.save_dir, args.trash_dir, args.delete)

else:
    chooser = main
