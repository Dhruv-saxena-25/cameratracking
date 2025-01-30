import cv2
import os

# Directory to save captured images
save_directory = "captured_images"
os.makedirs(save_directory, exist_ok=True)

# Open the default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press 's' to save an image, 'q' to quit.")
print("The script will automatically stop after collecting 30 images.")

# Initialize frame count and limit
frame_count = 0
max_images = 30

while frame_count < max_images:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the resulting frame
    cv2.imshow("Camera Feed", frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Save image on pressing 's'
        filename = os.path.join(save_directory, f"image_{frame_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")
        frame_count += 1

    elif key == ord('q'):  # Quit on pressing 'q'
        print("Exiting...")
        break

    # Stop automatically when 100 images are captured
    if frame_count == max_images:
        print("Reached the maximum of 30 images. Exiting...")
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
