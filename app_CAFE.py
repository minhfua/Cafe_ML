import streamlit as st

# 1. NHÚNG MÃ PWA (PROGRESSIER) ĐỂ CÀI ĐẶT LOGO & TÊN RIÊNG
st.markdown(
    """
    <script>
        // Chèn Manifest
        var link = window.parent.document.createElement('link');
        link.rel = 'manifest';
        link.href = 'https://progressier.app/sZSKNuC3ENZQJWBw45gs/progressier.json';
        window.parent.document.head.appendChild(link);

        // Chèn Script
        var script = window.parent.document.createElement('script');
        script.defer = true;
        script.src = 'https://progressier.app/sZSKNuC3ENZQJWBw45gs/script.js';
        window.parent.document.head.appendChild(script);
    </script>
    """,
    unsafe_allow_html=True,
)
# --- KẾT THÚC ĐOẠN CODE PWA ---
# Sau đó mới đến các phần code cũ của bạn
st.set_page_config(page_title="CAFORE", layout="centered", initial_sidebar_state="collapsed")
st.set_page_config(page_title="CAFORE", layout="centered", initial_sidebar_state="collapsed")
st.set_page_config(
    page_title="CAFORE",
    page_icon="logo_quan.png", # Đây là cách đổi icon trên tab trình duyệt
    layout="centered"
)
# 1. Cấu hình & Ẩn Sidebar
st.set_page_config(page_title="CAFORE", layout="centered", initial_sidebar_state="collapsed")

# 2. CSS Tối ưu giao diện: Màu sắc Kem - Nâu, Chỉnh nút bự và Font chữ
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Playfair+Display:wght@700&display=swap');

        [data-testid="stSidebar"] {display: none;}
        
        /* Màu nền Kem sáng */
        .stApp {
            background-color: #FDF5E6; 
        }
        
        /* Căn giữa toàn bộ nội dung trong cột */
        [data-testid="stVerticalBlock"] {
            align-items: center;
            justify-content: center;
        }

        /* Tên App CAFORE phía dưới nút */
        .app-name {
            color: #4b3621;
            font-family: 'Playfair Display', serif;
            font-size: 42px;
            font-weight: bold;
            margin-top: 20px;
            text-align: center;
        }

        /* Tùy chỉnh nút START bự, font hiện đại, chiếm nhiều khoảng trống */
        div.stButton {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }

        div.stButton > button {
            background-color: #6f4e37; 
            color: white;
            border-radius: 15px; /* Bo góc nhẹ cho hiện đại */
            border: none;
            width: 320px; 
            height: 90px;  
            font-family: 'Montserrat', sans-serif; /* Font chữ hiện đại, mạnh mẽ */
            font-size: 32px; /* Chữ to hơn chiếm nhiều diện tích nút */
            letter-spacing: 2px;
            font-weight: 800;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
        }

        div.stButton > button:hover {
            background-color: #4b3621;
            transform: translateY(-5px);
            box-shadow: 0px 12px 25px rgba(0,0,0,0.2);
            color: white;
        }

        /* Hiệu ứng hòa trộn logo vào nền kem (nếu logo nền trắng) */
        [data-testid="stImage"] img {
            mix-blend-mode: multiply;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Hiển thị Logo (Căn giữa)
st.write("") 
col1, col2, col3 = st.columns([0.5, 2, 0.5])
with col2:
    try:
        st.image("logo_quan.png", use_container_width=True)
    except:
        st.info("💡 Hãy đảm bảo file 'logo_quan.jpg' nằm trong thư mục CAFE_ML")

# 4. Nút bấm START chính giữa
if st.button("START"):
    st.switch_page("pages/1_🚀_Du_bao.py")

