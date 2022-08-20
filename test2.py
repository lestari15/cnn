from face_recognition_and_liveness.face_liveness_detection.face_recognition_liveness_app import recognition_liveness
# from face_recognition_and_liveness.face_liveness_detection.liveness_app import recognition_liveness
detected_name, label_name = recognition_liveness('face_recognition_and_liveness/face_liveness_detection/liveness.model',
                                                 'face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle',
                                                 'face_recognition_and_liveness/face_liveness_detection/face_detector',
                                                 'face_recognition_and_liveness/face_recognition/encoded_faces.pickle',
                                                 confidence=0.5)
