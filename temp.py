import streamlit as st
from datetime import date

st.set_page_config(page_title="Company Registration Form", page_icon="🏢", layout="centered")

st.title("🏢 Company Application / Registration Form")
st.markdown("Please fill all the details below:")

# ---------------- Personal Information ----------------
st.header("👤 Personal Information")
full_name = st.text_input("Full Name")
father_name = st.text_input("Father's Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
gender = st.radio("Gender", ["Male", "Female", "Other"])
dob = st.date_input("Date of Birth", value=date(2000,1,1))
cnic = st.text_input("CNIC / ID Number")

# ---------------- Address ----------------
st.header("📍 Address Details")
address = st.text_area("Current Address")
city = st.text_input("City")
country = st.selectbox("Country", ["Pakistan", "India", "USA", "UK", "Other"])

# ---------------- Education ----------------
st.header("🎓 Education & Skills")
qualification = st.selectbox(
    "Highest Qualification",
    ["Matric", "Intermediate", "Bachelor", "Master", "PhD"]
)
skills = st.text_area("Skills (comma separated)", placeholder="e.g. Python, Excel, Communication")

# ---------------- Work Experience ----------------
st.header("💼 Work Experience")
experience = st.slider("Years of Experience", 0, 30, 0)
last_company = st.text_input("Last Company (if any)")

# ---------------- Job Details ----------------
st.header("📑 Job Details")
position = st.text_input("Position Applying For")
department = st.selectbox("Preferred Department", ["IT", "HR", "Marketing", "Finance", "Other"])
salary = st.text_input("Expected Salary (optional)")

# ---------------- Uploads ----------------
st.header("📎 Upload Documents")
resume = st.file_uploader("Upload Your Resume (PDF/DOCX)", type=["pdf","docx"])
photo = st.file_uploader("Upload Your Profile Photo (JPG/PNG)", type=["jpg","jpeg","png"])

# ---------------- Submit ----------------
if st.button("Submit Application"):
    # Validation
    if full_name and email and phone and position:
        st.success("✅ Your application has been submitted successfully!")

        st.subheader("📋 Application Summary:")
        st.write(f"**Full Name:** {full_name}")
        st.write(f"**Father's Name:** {father_name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Date of Birth:** {dob}")
        st.write(f"**CNIC:** {cnic}")
        st.write(f"**Address:** {address}, {city}, {country}")
        st.write(f"**Qualification:** {qualification}")
        st.write(f"**Skills:** {skills}")
        st.write(f"**Experience:** {experience} years")
        st.write(f"**Last Company:** {last_company}")
        st.write(f"**Position Applied:** {position}")
        st.write(f"**Department:** {department}")
        st.write(f"**Expected Salary:** {salary}")

        if resume:
            st.info(f"📄 Resume Uploaded: {resume.name}")
        if photo:
            st.image(photo, caption="Uploaded Photo", width=150)
    else:
        st.error("⚠️ Please fill all *required* fields (Name, Email, Phone, Position).")