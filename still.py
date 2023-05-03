from picamera2 import Picamera2, Preview
import time
import numpy as np

picam2 = Picamera2()
print(picam2.sensor_resolution)
print(picam2.camera_properties)

captureMode = 'full' # normal / full / raw / dng

if captureMode == 'normal':
    picam2.start_and_capture_file("test.jpg")

elif captureMode == 'full':
    picam2.start_preview(Preview.QTGL)

    preview_config = picam2.create_preview_configuration()
    capture_config = picam2.create_still_configuration({'size': (5608, 2592)})
    picam2.configure(preview_config)

    picam2.start()
    time.sleep(2)

    picam2.switch_mode_and_capture_file(capture_config, "test_full.jpg")

elif captureMode == 'raw':
    picam2.start_preview(Preview.QTGL)

    preview_config = picam2.create_preview_configuration(raw={"size": picam2.sensor_resolution})
    print(preview_config)
    picam2.configure(preview_config)

    picam2.start()
    time.sleep(2)

    raw = picam2.capture_array("raw")
    print(raw.shape)
    print(picam2.stream_configuration("raw"))
    np.save(
        "test_raw",
        raw
    )
    print(raw)

elif captureMode == 'dng':
    picam2.start_preview(Preview.QTGL)
    preview_config = picam2.create_preview_configuration()
    capture_config = picam2.create_still_configuration(raw={})
    picam2.configure(preview_config)

    picam2.start()
    time.sleep(2)

    picam2.switch_mode_and_capture_file(capture_config, "test_full.dng", name="raw")
