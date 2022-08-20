from face_recognition_and_liveness.face_liveness_detection.face_recognition_liveness_app import recognition_liveness
# from face_recognition_and_liveness.face_liveness_detection.liveness_app import recognition_liveness
import sys
import mysql.connector
from datetime import datetime
import webbrowser
detected_name, label_name = recognition_liveness('face_recognition_and_liveness/face_liveness_detection/liveness.model',
                                                 'face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle',
                                                 'face_recognition_and_liveness/face_liveness_detection/face_detector',
                                                 'face_recognition_and_liveness/face_recognition/encoded_faces.pickle',
                                                 confidence=0.5)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="absensi_wajah"
)
idKaryawan = sys.argv[1]
nama = sys.argv[2]
jamAbsen = datetime.now().strftime('%H:%M:%S')
tanggalAbsen = datetime.now().strftime('%Y-%m-%d')

mycursor = mydb.cursor()


if nama == detected_name and label_name == 'real':
    sql = "INSERT INTO absen_karyawan (id_karyawan, jam_absen, tanggal_absen) VALUES (%s, %s, %s)"
    val = (idKaryawan, jamAbsen, tanggalAbsen)
    mycursor.execute(sql, val)

    mydb.commit()

    if(mycursor.rowcount == 1):
        print("Berhasil Absen")
        webbrowser.open(
            "http://localhost/absensi_wajah/karyawan/absen_karyawan?data=berhasil", new=0, autoraise=True)
else:
    print("Gak Boleh absen")
    webbrowser.open(
            "http://localhost/absensi_wajah/karyawan/absen_karyawan?data=gagal", new=0, autoraise=True)