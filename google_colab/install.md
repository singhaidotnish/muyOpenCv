labelImg
sudo apt update
sudo apt install -y qt5-qmake qtbase5-dev qtchooser qt5-default libxcb-xinerama0
cd ~/Documents/GitHub/muyOpenCv/
ll
source .ocv/bin/activate
labelImg --version
sudo apt update
sudo apt install -y qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libxcb-xinerama0
QT_QPA_PLATFORM=xcb labelImg
ll
cd google_colab/
ll
python improving_object_detection_model_accuracy/
cd improving_object_detection_model_accuracy/
ll
python capture_high_quality_training_data.py 
QT_QPA_PLATFORM=xcb labelImg
