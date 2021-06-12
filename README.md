# Tensorflow_YOLOV4_VehicleDetection

VEHICLE DETECTION USING YOLO V4

1. Collect images using traffic_images_scraping.py (in test_images folder)
2. All the images in this folder using batch_rename.py to a certain format (in test_images folder)
3. Use batch_resize.py to make them the same size (in test_images folder)
4. Run detect.py - remember to change the 'path to input' field (in main_folder)
flags.DEFINE_string('image', './data/traffic2resized16801050.jpg', 'path to input image')

(Filesize is too big to upload the entire tensorflow-yolov4-master file - you can fork it from https://github.com/hunglc007/tensorflow-yolov4-tflite)

5. Save the detection results
