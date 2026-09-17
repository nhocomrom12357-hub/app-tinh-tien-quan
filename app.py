import streamlit as st
st.image("IMG_5990.png", use_container_width=True)
# Tiêu đề
st.title("🍜 APP TÍNH TIỀN QUÁN ĂN")

st.write("Nhập thông tin món ăn để tính tiền.")

# Tên món
ten_mon = st.text_input("Tên món ăn")

# Đơn giá
don_gia = st.number_input(
    "Đơn giá (VNĐ)",
    min_value=0,
    value=0,
    step=1000
)

# Số lượng
so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    value=1,
    step=1
)

# Tính tiền
if st.button("🧮 Tính tiền"):

    thanh_tien = don_gia * so_luong

    st.success("Tính tiền thành công!")

    st.write("### 🧾 HÓA ĐƠN")

    st.write(f"**Món ăn:** {ten_mon}")
    st.write(f"**Đơn giá:** {don_gia:,.0f} VNĐ")
    st.write(f"**Số lượng:** {so_luong}")

    st.write(f"### 💰 Tổng tiền: {thanh_tien:,.0f} VNĐ")
