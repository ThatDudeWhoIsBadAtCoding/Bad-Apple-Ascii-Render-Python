import cv2
import shutil
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("BAD_APPLE_RENDER/sound.wav")
invert = input("Enter 'e' if you want to compute inverted frames else just press enter: ").lower()

cap = cv2.VideoCapture("BAD_APPLE_RENDER/badapple.mp4")


def convert_block_to_ascii(block):
    chars = " .:-=+*#%@" if not invert else "@%#*+=-:. "
    ascii_block = ''
    for row in block:
        for pixel_value in row:
            index = int(pixel_value / 255 * (len(chars) - 1))
            ascii_block += chars[index]
        ascii_block += '\n'
    return ascii_block

def convert_to_ascii(image, block_size=(100, 100)):
    height, width = image.shape[:2]
    block_width, block_height = block_size

    ascii_image = ''
    for y in range(0, height, block_height):
        for x in range(0, width, block_width):
            block = image[y:y+block_height, x:x+block_width]
            ascii_block = convert_block_to_ascii(block)
            ascii_image += ascii_block
    return ascii_image

 
play_obj = wave_obj.play()
while True:
    ret, frame = cap.read()

    if not ret: break

    height, width = frame.shape[:2]
    term_cols, term_rows = shutil.get_terminal_size()

    aspect_ratio = height / float(width)
    new_width = term_cols - 1
    new_height = int(new_width * aspect_ratio * 0.5)
    frame_resized = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (new_width, new_height))
    print(convert_to_ascii(frame_resized, (term_cols, term_rows - 1)))

    if cv2.waitKey(1) & 0xFF == ord('q'): break


cap.release()
cv2.destroyAllWindows()
