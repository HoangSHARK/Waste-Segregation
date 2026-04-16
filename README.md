# Waste-Segregation
Link dataset: https://www.kaggle.com/datasets/aashidutt3/waste-segregation-image-dataset/data
# Tính năng
Phân loại rác từ hình ảnh
Sử dụng các mô hình CNN phổ biến:
MobileNet
VGG16
ResNet50
Đánh giá độ chính xác bằng ma trận confusion
Triển khai demo bằng ứng dụng Streamlit (app.py)
# Cấu trúc thư mục
-  ChuanBiDuLieu.ipynb        # Tiền xử lý dữ liệu
-  Mo_hinh_MobileNets.ipynb  # Huấn luyện MobileNet
├── Xay_dung_mo_hinh_VGG16.ipynb
├── Xay_dung_mo_hinh_ResNet50.ipynb
├── ma_tran_DoChinhXac.ipynb  # Đánh giá mô hình
├── mobilenet_model.h5        # Model đã train
├── app.py                    # Ứng dụng demo
└── README.md
