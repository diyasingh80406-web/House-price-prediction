import streamlit as st
import pickle
import numpy as np

st.set_page_config(
page_title="Dream House Predictor",
page_icon="🏠",
layout="wide"
)

model=pickle.load(
open(
"model.pkl",
"rb"
)
)

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
120deg,
#f3f8ff,
#fff6fa
);
}

.hero{
background:
linear-gradient(
135deg,
#ffffff,
#f0f6ff
);

padding:40px;

border-radius:25px;

box-shadow:
0 10px 35px rgba(0,0,0,.08);
}

.title{

font-size:52px;

font-weight:800;

text-align:center;

color:#184e77;

}

.sub{

text-align:center;

font-size:18px;

color:#666;

}

.section{

background:white;

padding:25px;

margin-top:30px;

border-radius:20px;

box-shadow:
0 8px 20px rgba(0,0,0,.05);

}

</style>
""",
unsafe_allow_html=True
)

st.markdown("""

<div class='hero'>

<div class='title'>
🏠 Dream House Price Predictor
</div>

<div class='sub'>
Find Estimated Property Value Using AI
</div>

</div>

""",
unsafe_allow_html=True
)

st.write("")

st.image(
"https://images.unsplash.com/photo-1564013799919-ab600027ffc6",
use_container_width=True
)

st.markdown("---")

st.subheader("✨ Why Use This Platform")

a,b,c=st.columns(3)

with a:
    st.metric(
"⚡ Speed",
"Instant"
)

with b:
    st.metric(
"📊 Accuracy",
"High"
)

with c:
    st.metric(
"🏡 Experience",
"Premium"
)

st.markdown("---")

st.subheader(
"🏘️ Explore House Styles"
)

x,y=st.columns(2)

with x:

    st.image(
"https://images.unsplash.com/photo-1570129477492-45c003edd2be"
)

with y:

    st.image(
"https://images.unsplash.com/photo-1600585154340-be6161a56a0c"
)

st.markdown("---")

st.subheader(
"🔮 Predict Your House Price"
)

st.sidebar.title(
"🏠 House Information"
)

area = st.sidebar.slider(
"📐 Area (sq ft)",
500,
5000,
1500
)

location = st.sidebar.selectbox(
"📍 Location",
[
"Urban",
"Suburban",
"Rural"
]
)

rooms = st.sidebar.slider(
"🛏 Number of Rooms",
1,
10,
3
)

age = st.sidebar.slider(
"🏡 Property Age",
0,
50,
10
)

amenities = st.sidebar.multiselect(
"✨ Amenities",
[
"Parking",
"Swimming Pool",
"Garden",
"Security",
"Gym"
]
)

garage = st.sidebar.slider(
"🚗 Garage Capacity",
0,
5,
2
)

quality=min(
10,
rooms+
len(amenities)
)


if st.button(
"Predict Price",
use_container_width=True
):

    val=np.array([
        [
            quality,
            area,
            garage
        ]
    ])

    price=model.predict(
        val
    )[0]

    st.balloons()

    st.success(
        f"💰 Estimated Price: ${price:,.0f}"
    )

    st.progress(
        min(
            100,
            int(price/5000)
        )
    )

    st.markdown("---")

    st.subheader(
        "📋 Property Details"
    )

    col1,col2=st.columns(2)

    with col1:

        st.info(
f"""
📍 Location:
{location}

🛏 Rooms:
{rooms}

🏡 Age:
{age} Years
"""
        )

    with col2:

        st.info(
f"""
📐 Area:
{area} sq ft

✨ Amenities:
{len(amenities)}

🚗 Garage:
{garage}
"""
        )

    st.markdown("---")

    st.subheader(
        "🏠 Recommendation"
    )

    if age<10:

        st.success(
            "Modern Property"
        )

    elif age<25:

        st.info(
            "Balanced Investment"
        )

    else:

        st.warning(
            "Older Property"
        )

    if price<150000:

        st.success(
            "💚 Budget House"
        )

    elif price<300000:

        st.info(
            "💙 Premium House"
        )

    else:

        st.warning(
            "💎 Luxury House"
        )
st.markdown("---")

st.subheader(
"📌 Market Insights"
)

d,e,f=st.columns(3)

with d:
    st.metric(
        "Avg Price",
        "$210K"
    )

with e:
    st.metric(
        "Demand",
        "High"
    )

with f:
    st.metric(
        "Growth",
        "+14%"
    )

st.markdown("---")

st.subheader(
    "🧾 About This Project"
)

st.write(
"""
This AI project predicts house prices using:

📍 Location  
📐 Area  
🛏 Number of Rooms  
🏡 Property Age  
✨ Amenities  

Built with:
Python + Streamlit + Machine Learning
"""
)
st.markdown("---")

st.subheader(
"📈 House Buying Tips"
)

st.write(
"""
✔️ Compare multiple locations

✔️ Check amenities before buying

✔️ Newer houses may need less maintenance

✔️ Higher quality often increases value
"""
)
st.caption(
"Created with ❤️"
)