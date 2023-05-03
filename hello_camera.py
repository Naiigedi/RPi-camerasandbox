from picamera2 import Picamera2

picam2 = Picamera2()

#5秒間の動画を撮影して保存する
picam2.start_and_record_video("test.mp4", duration=5)
