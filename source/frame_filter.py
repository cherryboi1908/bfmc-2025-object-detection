import os 
import msvcrt
import cv2

def frame_filter(frame_folder):
    frame_files = os.listdir(frame_folder)
    for frame_file in frame_files:
        if frame_file.endswith('.jpg'):
            frame_file_path = os.path.join(frame_folder, frame_file)
            print(f"\nCurrent file: {frame_file_path}")

            # Display the image
            img = cv2.imread(frame_file_path)
            cv2.imshow('Frame', img)
                

            # Chờ người dùng nhấn phím
            key = cv2.waitKey(0)

            # Kiểm tra xem người dùng có nhấn phím 't' hay không
            if key == ord("t"):
                os.remove(frame_file_path)
                print(f"Đã xóa tệp {frame_file}")
            elif key == ord("r"):
                print(f"Đã giữ lại tệp {frame_file}")
        
    cv2.destroyAllWindows()  # Ensure all windows are closed at the end

for i in range(12):
    frame_folder = f'D:\pleizsonoob\Others\\bfmc\dataset\\frame_saved\\vid_{i+1}'
    frame_filter(frame_folder)
    print(f"Frame filtering completed for video {i+1}")
