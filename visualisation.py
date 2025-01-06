import os
import glob
import pickle
import numpy as np
import matplotlib.pyplot as plt
import cv2

def visualize_pkl_files_in_order(folder_path):
    """
    Loads all .pkl files in 'folder_path' that follow the naming scheme 'X.pkl',
    where X is an integer (e.g., 1.pkl, 2.pkl, etc.), sorts them by X, 
    and visualizes them in sorted order.
    """
    # Find all .pkl files
    pkl_files = glob.glob(os.path.join(folder_path, "*.pkl"))
    
    # Sort the file list by the integer in the file name
    # Assumes file name looks like "NUMBER.pkl"
    pkl_files.sort(key=lambda f: int(os.path.splitext(os.path.basename(f))[0]))
    
    # Visualize each file
    for pkl_file in pkl_files:
        with open(pkl_file, 'rb') as f:
            image_data = pickle.load(f)  # shape should be (274, 384)
            
        plt.imshow(image_data, cmap='gray', vmax=8191, vmin=-400)
        plt.title(os.path.basename(pkl_file))
        plt.axis('off')
        plt.show()

def convert_npy_to_video(npy_file, output_video, fps=30):
    """
    Load the .npy file (shape = (N, 274, 384)) and convert it into a video file.
    """
    frames = np.load(npy_file)  # shape: (N, 274, 384)
    num_frames, height, width = frames.shape
    
    # Define the codec and create VideoWriter for grayscale frames
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height), isColor=False)
    
    for i in range(num_frames):
        frame = frames[i]
        
        # Ensure frame is in the correct data range (0-255) and type (uint8) if needed
        # e.g., if your frames are float32 in [0,1], you could scale them:
        # frame_uint8 = (frame * 255).astype(np.uint8)
        
        # Or normalize the frame data to [0, 255]
        frame_uint8 = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        # Write the frame to video
        out.write(frame_uint8)
    
    out.release()
    print(f"Video saved as: {output_video}")

if __name__ == "__main__":
    # 1. Visualize all .pkl files:
    folder_path = "path/to/your/folder"  # <-- replace with your folder path
    visualize_pkl_files_in_order(folder_path)
    
    # 2. Convert the concatenated .npy file to a video:
    npy_file = os.path.join(folder_path, "video.npy")  # <-- replace with your .npy file name
    output_video = os.path.join(folder_path, "pCLE_video.avi")
    
    convert_npy_to_video(npy_file, output_video, fps=12)
