import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. CẤU HÌNH TRANG & ẨN SIDEBAR
st.set_page_config(page_title="Dự báo doanh thu", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS TỐI ƯU GIAO DIỆN
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        .stApp { background-color: #FAF9F6; } /* Màu trắng kem sáng */
        
        /* Màu chữ tiêu đề và nhãn */
        h2, h3, label, p { 
            color: #4b3621 !important; 
            font-family: 'Arial', sans-serif; 
            font-size: 1.1rem !important;
        }
        
        /* THIẾT KẾ INPUT TO HƠN & MATCH TONE MÀU */
        .stNumberInput input, .stSelectbox div[data-baseweb="select"], .stRadio div[role="radiogroup"] {
            background-color: #FFFFFF !important;
            border-radius: 15px !important;
            border: 2px solid #EAD9C5 !important;
            color: #6f4e37 !important;
            padding: 5px !important; 
            font-size: 18px !important;
        }
        
        /* Hiệu ứng khi click vào ô nhập liệu */
        .stNumberInput input:focus {
            border-color: #6f4e37 !important;
            box-shadow: 0 0 0 1px #6f4e37 !important;
        }

        /* NÚT BẤM: CHỮ SÁNG TRÊN NỀN NÂU */
        div.stButton > button {
            background-color: #6f4e37;
            color: #FAF9F6 !important; 
            border-radius: 30px;
            border: none;
            height: 60px; 
            width: 100%;
            font-size: 20px !important;
            font-weight: bold;
            letter-spacing: 1px;
            transition: 0.3s;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        
        div.stButton > button:hover {
            background-color: #4b3621;
            color: #FFFFFF !important;
            transform: translateY(-2px);
            box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
        }

        .back-btn div.stButton > button {
            height: 45px;
            font-size: 16px !important;
            width: auto;
            padding: 0 30px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. NÚT QUAY LẠI VÀ TIÊU ĐỀ MỚI
col_nav, _ = st.columns([1, 4])
with col_nav:
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("⬅ QUAY LẠI"):
        st.switch_page("app_CAFE.py")
    st.markdown('</div>', unsafe_allow_html=True)

# CHỈNH SỬA TIÊU ĐỀ: To hơn và nội dung mới
st.markdown("<h1 style='text-align: center; color: #4b3621; font-size: 42px; font-weight: bold;'>Vui lòng nhập thông số cửa hàng vào bên dưới</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

# 4. XỬ LÝ DỮ LIỆU & HUẤN LUYỆN AI
try:
    df = pd.read_csv('cafe_data.csv')
    df.columns = df.columns.str.strip()
    features = ['Gia_TB', 'Vi_tri', 'Cho_ngoi', 'Delivery', 'Dien_tich', 'So_nhan_vien', 'Ngoi_hoc_lau', 'So_doi_thu', 'Luong_khach_ngay']
    X = df[features]
    y = df['Doanh_thu_ngay']
    model = LinearRegression().fit(X, y)
except Exception as e:
    st.error(f"⚠️ Lỗi: {e}")
    st.stop()

# 5. GIAO DIỆN NHẬP LIỆU (Giữ nguyên cấu trúc nhưng căn chỉnh khoảng cách)
with st.container():
    col1, col2 = st.columns(2, gap="large")

    with col1:
        gia = st.number_input("💵 Giá bán trung bình (VNĐ)", value=35000, step=1000)
        khach = st.number_input("👥 Lượng khách dự kiến/ngày", value=50, min_value=1)
        vi_tri = st.selectbox("📍 Vị trí quán", [1, 2, 3], 
                              format_func=lambda x: "Trường học (1)" if x==1 else ("Văn phòng (2)" if x==2 else "Khác (3)"))
        ngoi = st.radio("🪑 Có chỗ ngồi?", [1, 0], format_func=lambda x: "Có" if x==1 else "Không", horizontal=True)

    with col2:
        nv = st.number_input("👨‍🍳 Số lượng nhân viên", value=2, min_value=1)
        hoc = st.radio("💻 Khách ngồi học lâu?", [1, 0], format_func=lambda x: "Có" if x==1 else "Không", horizontal=True)
        dt = st.number_input("📐 Diện tích quán (m2)", value=30, min_value=5)
        doi_thu = st.number_input("⚔️ Số đối thủ xung quanh", value=5, min_value=0)
        ship = st.radio("🛵 Có Delivery (App)?", [1, 0], format_func=lambda x: "Có" if x==1 else "Không", horizontal=True)

# 6. DỰ BÁO VÀ HIỂN THỊ KẾT QUẢ
st.write("")
if st.button("🔥 XÁC NHẬN DỰ BÁO"):
    input_data = np.array([[gia, vi_tri, ngoi, ship, dt, nv, hoc, doi_thu, khach]])
    pred = model.predict(input_data)[0]
    
    st.balloons()
    
    st.markdown(f"""
        <div style="background-color: #FFFFFF; padding: 30px; border-radius: 25px; border: 3px solid #6f4e37; text-align: center; box-shadow: 0px 10px 25px rgba(0,0,0,0.1);">
            <h3 style="margin:0; color: #6f4e37; font-weight: bold;">💰 DOANH THU ƯỚC TÍNH:</h3>
            <h1 style="color: #4b3621; font-size: 60px; margin: 15px 0;">{int(pred):,} <small style="font-size: 25px;">VNĐ/Ngày</small></h1>
            <div style="background-color: #FDF5E6; padding: 15px 30px; border-radius: 15px; display: inline-block; border: 1px dashed #6f4e37;">
                <p style="margin:0; font-weight: bold; color: #6f4e37; font-size: 22px;">📅 Ước tính tháng: {int(pred*30):,} VNĐ</p>
            </div>
        </div>
    """, unsafe_allow_html=True)