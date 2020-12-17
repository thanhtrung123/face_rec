# Face Recog
Nhận diện khuôn mặt khá chuẩn xác bằng MTCNN và Facenet!

Settup:
    - Install tensorflow==2.0.0
    - Install libs:
        pip3 install -r requirements.txt
    - Tiền xử lý ảnh:
        python3 src/align_dataset_mtcnn.py  Dataset/FaceData/raw Dataset/FaceData/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25
    - Train model:
        python3 src/classifier.py TRAIN Dataset/FaceData/processed Models/20180402-114759.pb Models/facemodel.pkl --batch_size 1
    - Run:
        python3 src/face_rec_cam.py

How to install tensorflow 2 on Raspberry Pi 4
    
    sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev
    python3 -m pip install keras_applications==1.0.8 --no-deps
    python3 -m pip install keras_preprocessing==1.1.0 --no-deps
    python3 -m pip install h5py==2.9.0
    sudo apt-get install -y openmpi-bin libopenmpi-dev
    sudo apt-get install -y libatlas-base-dev
    python3 -m pip install -U six wheel mock
    
    wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.0.0/tensorflow-2.0.0-cp37-none-linux_armv7l.whl
    python3 -m pip uninstall tensorflow
    python3 -m pip install tensorflow-2.0.0-cp37-none-linux_armv7l.whl
    
    TEST: RESTART YOUR TERMINAL
        python3
        import tensorflow
        tensorflow.__version__
        >> output: 2.0.0
