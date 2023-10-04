from tkinter import *
import os
import cv2
from glob import glob
from tkinter import filedialog

main_directory = None

Extension = "jpg" or "png" # images desired file extension

def select_directory():
    global main_directory
    # Open file dialog to select a folder and store the folder path
    main_directory = filedialog.askdirectory()


def calculate_blur_metric(path):

        image = cv2.imread(path)
        b, g, r = cv2.split(image)

        # Calculate the Laplacian variance for each channel
        var_b = cv2.Laplacian(b, cv2.CV_64F).var()
        var_g = cv2.Laplacian(g, cv2.CV_64F).var()
        var_r = cv2.Laplacian(r, cv2.CV_64F).var()

        # Compute the average of the variances
        avg_var = (var_b + var_g + var_r) / 3
        
        # Calculate the blur metric
        blur_metric = avg_var

        return blur_metric

def detect_blur_images(path_images):
    
    blur_images = []
    threshold = 25  # Adjust as per your requirement
    for i in range(len(path_images)):
    
        # Determine if the image is blurred or not
        blur_metric = calculate_blur_metric(path_images[i])
        if blur_metric < threshold  :
            blur_images.append(path_images[i])
            
    return blur_images

def clean_blur_images():

    if main_directory is None:
        
        return
        
    path_images = glob(os.path.join(main_directory , f'*.{Extension}'))

    photo_files = detect_blur_images(path_images)
    new_directory = os.path.join(main_directory,'removed blur')
    os.mkdir(new_directory)
    for address in photo_files:
        os.rename(address, os.path.join(new_directory, os.path.basename(address)))  
    
    
def get_num_features(path):
    
    # Create SIFT object
    sift = cv2.SIFT_create()
        
    image = cv2.imread(path)
        
    # Detect features
    keypoints = sift.detect(image, None)

    # Count the number of keypoints
    num_features = len(keypoints)
        
    return num_features

def detect_broken_images(path_images):

    photo_files = []

    for i in range(len(path_images)):
        num_features = get_num_features(path_images[i])
        if num_features<=500:
            photo_files.append(path_images[i])
            
    return photo_files


def clean_broken_image():

    if main_directory is None:
        return 
    
    path_images = glob(os.path.join(main_directory , f'*.{Extension}'))

    photo_files = detect_broken_images(path_images)

    new_directory = os.path.join(main_directory,'removed broken')
    os.mkdir(new_directory)
    for address in photo_files:
        os.rename(address, os.path.join(new_directory, os.path.basename(address)))
        



window = Tk()

window.title("Cleaner")

window.geometry("400x400")
window.resizable(width=False,height=False)

Label(window,text="Remove Blur Image & Remove Broken Image",font=("Times New Roman",14),bg = "black",fg = "white").pack()
Label(window,text="").pack()
Label(window,text="").pack()
Label(window,text="").pack()
Label(window,text="").pack()

btn = Button(window)
btn2  = Button(window)
btn3 = Button(window)

btn.configure(text="Select directory",bg = "cyan",fg = "black" , command = select_directory,width=40,bd=5)
btn2.configure(text="Remove Blur Image",bg = "cyan",fg = "black" , command = clean_blur_images,width=40,bd=5)
btn3.configure(text="Remove Broken Image",bg = "cyan",fg = "black", command = clean_broken_image,width=40,bd=5)


btn.pack()
btn2.pack()
btn3.pack()

window.mainloop()
