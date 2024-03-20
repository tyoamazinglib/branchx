import streamlit as st
import streamlit.components.v1 as stc
import pickle

with open('models/dt.pkl','rb') as file:
    dt = pickle.load(file)

html_temp = """
    <div style="background-color:#0000FF;padding:20px;border-radius:10px;box-shadow: 5px 10px 18px #0000FF;">
        <h1 style="color:white;text-align:center;font-size:2.5em;">Aplikasi Klasifikasi Kredit Nasabah</h1>
    </div>
"""

desc_temp = """
    ### Aplikasi Klasifikasi Kredit Nasabah
    Aplikasi ini merupakan sebuah aplikasi untuk melakukan klasifikasi secara otomatis terhadap nasabah Bank Mandiri.
    Aplikasi ini bertujuan untuk mencegah nasabah kredit macet dan menyesuaikan produk kredit sesuai dengan limit kredit serta 
    pekerjaan nasabah.
    ### Branch X KCP Jakarta Mangga 2
    #### Penjelasan produk kredit:
    - KSM []
    - Kartu Kredit []
    - KPR []
    #### Dibuat oleh
    - Nugroho Budi Prasetyo
    - M. Noufal Rifqi I.
"""

desc_temp2 = """
    #### Kolom kelas diisi dengan angka dan pengertiannya sebagai berikut:
    - Angka 1 untuk nasabah yang bekerja di perusahaan PT (Perseroan Terbatas) dan PNS/Bekerja dengan perusahaan pemerintah
    - Angka 2 untuk pemilik toko/usaha
    - Angka 3 untuk nasabah yang bekerja di angka 1 (PT/PNS/Perusahaan Pemerintah)
"""

def main():
    stc.html(html_temp)
    st.sidebar.image("logo/BranchX.png")
     st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #0000FF;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    menu = ["Home", "Aplikasi"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Aplikasi":
        st.markdown(desc_temp2, unsafe_allow_html=True)
        run_ml_app()

def run_ml_app():
    st.subheader("Mulai Prediksi!")
    
    # Create a two-column layout
    left, right = st.columns([1, 1])
    
    # Add content to the left column
    with left:
        kelas = st.number_input('Kelas Nasabah', value=0, step=1)
    
    # Add content to the right column
    with right:
        limit_kredit = st.number_input('Limit Kredit', value=0.0, step=0.1)
    
    # Add a button for prediction
    button = st.button('Mulai Prediksi')
    
    # If button is clicked
    if button:
        # Make prediction
        result = predict(kelas, limit_kredit)
        # Display prediction result
        if result == 1:
            st.success('Prediksi Kredit: Kartu Kredit')
        elif result == 2:
            st.success('Prediksi Kredit: Kartu Kredit')
        elif result == 3:
            st.success('Prediksi Kredit: Kartu Kredit atau KSM')
        elif result == 4:
            st.success('Prediksi Kredit: Kartu Kredit/KSM/KPR')
        else:
            st.warning('Error! Input data dengan benar.')

def predict(kelas, limit_kredit):
    # Making prediction
    prediction = dt.predict([[kelas, limit_kredit]])
    return prediction[0]

if __name__ == "__main__":
    main()
