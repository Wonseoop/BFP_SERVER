import os
import random
import string

def get_next_output_folder(base_dir, base_folder_name="folder"):
    counter = 1
    while True:
        folder_name = f"{base_folder_name}_{counter}"
        output_folder = os.path.join(base_dir, "output_frame", folder_name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            return output_folder
        counter += 1
        
def get_next_output_gif(base_dir, base_gif_name="output"):
    counter = 1
    while True:
        gif_name = f"{base_gif_name}_{counter}.gif"
        output_gif_path = os.path.join(base_dir, "gif",gif_name)
        if not os.path.exists(output_gif_path):
            return output_gif_path
        counter += 1


def get_next_random_gif(base_dir, base_gif_name="output"):
    while True:
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        gif_name = f"{base_gif_name}_{random_suffix}.gif"
        output_gif_path = os.path.join(base_dir, "gif", gif_name)
        if not os.path.exists(output_gif_path):
            return output_gif_path