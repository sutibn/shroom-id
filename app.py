import streamlit as st
import pandas as pd
import pickle 

with open('./model/model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)
feature_input = dict()

st.set_page_config(page_title="Shroom ID", page_icon="./images/logo.ico", layout="wide")

st.markdown("<h1 style='text-align: center;'>Shroom ID</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: gray;'>made by sutibn</h6>", unsafe_allow_html=True)

cx, cy, cz = st.columns(3)
with cy:
    st.image("./images/banner.png")

colA, colB = st.columns(spec=[10, 0.5])
tabA, tabB = st.tabs(['About', 'Run'])

with tabA:
    df = pd.read_csv('./data/test.csv')
    st.write("This app uses a machine learning model built from a **Random Forest** classifier that determines if a mushroom is dangerous to eat based on its physical attributes.") 
    st.write(df)
    st.write("The table above showcases the testing set of the model's data, which includes the most significant features that indicate a mushroom's **edibility**.")

    about = '''If the mushroom is classified under a **0**, then it is most likely edible and safe for consumption.  
        If the mushroom is classified under a **1**, then it is potentially poisonous and should not be ingested.'''
    st.markdown(about)

with tabB:
    cx, cy= st.columns(2)
    with cx:
        st.image("./images/cap-shape.png", width=650)
        st.caption("Cap shape")
        st.image("./images/gill-spacing.png")
        st.caption("Gill spacing")

    with cy:
        st.image("./images/cap-surface.png", width=650)
        st.caption("Cap surface")
        st.image("./images/ring-type.png", width=650)
        st.caption("Ring type")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        cap_shape   = st.selectbox('**Cap shape**',   ['convex', 'bell', 'conical', 'knobbed', 'flat', 'sunken'])
        cap_surface = st.selectbox('**Cap surface**', ['smooth', 'fibrous', 'scaly', 'grooves'])
        cap_color   = st.selectbox('**Cap color**',   ['brown', 'buff', 'cinnamon', 'gray', 'green', 'pink', 'purple', 'red', 'white', 'yellow'])
    feature_input['cap shape']   = cap_shape
    feature_input['cap surface'] = cap_surface
    feature_input['cap color']   = cap_color

    with col2:
        gill_spacing = st.selectbox('**Gill spacing**', ['crowded', 'close', 'distant'])
        gill_size    = st.selectbox('**Gill size**',    ['broad', 'narrow'])     
        gill_color   = st.selectbox('**Gill color**',   ['black', 'brown', 'buff', 'chocolate', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'])    
    feature_input['gill spacing'] = gill_spacing
    feature_input['gill size']    = gill_size
    feature_input['gill color']   = gill_color
    
    with col3:
        stalk_shape              = st.selectbox('**Stalk shape**',              ['enlarging', 'tapering'])
        stalk_surface_above_ring = st.selectbox('**Stalk surface above ring**', ['fibrous', 'scaly', 'silky', 'smooth'])
        stalk_color_above_ring   = st.selectbox('**Stalk color above ring**',   ['brown', 'buff', 'cinnamon', 'gray', 'orange', 'pink', 'red', 'white', 'yellow'])
    feature_input['stalk shape']              = stalk_shape
    feature_input['stalk surface above ring'] = stalk_surface_above_ring
    feature_input['stalk color above ring']   = stalk_color_above_ring

    with col4:
        ring_type = st.selectbox('**Ring type**', ['pendant', 'flaring', 'sheathing', 'evanescent', 'large', 'cobwebby', 'zone', 'none'])
        bruises   = st.selectbox('**Bruises**',   ['bruises', 'no'])
        odor      = st.selectbox('**Odor**',      ['almond', 'anise', 'creosote', 'fishy', 'foul', 'musty', 'none', 'pungent', 'spicy'])
    feature_input['ring type'] = ring_type
    feature_input['bruises']   = bruises
    feature_input['odor']      = odor

    with col5:
        spore_print_color = st.selectbox('**Spore print color**', ['black', 'brown', 'buff', 'chocolate', 'green', 'orange', 'purple', 'white', 'yellow'])
        population        = st.selectbox('**Population**',        ['abundant', 'clustered', 'numerous', 'scattered', 'several', 'solitary'])
        habitat           = st.selectbox('**Habitat**',           ['grasses', 'leaves', 'meadows', 'paths', 'urban', 'waste', 'woods'])
    feature_input['spore print color'] = spore_print_color
    feature_input['population']        = population
    feature_input['habitat']           = habitat

    st.info("After specifying the mushroom's features, press the button below to determine its edibility.\n\n  **NOTE**: The result may be inaccurate if the mushroom is hard to completely describe—seek confirmation with expert sources to be sure.")
    if st.button("**Submit**"):
        X_test     = dv.transform(feature_input)
        prediction = model.predict(X_test)
        result     = prediction[0]
        if result == 0.0:
            st.success('The mushroom is **edible**.', icon="🙂")
            st.balloons()
        else:
            st.error('The mushroom is **poisonous**.', icon="☠️")