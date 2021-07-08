import streamlit as st
import time


def main():
    st.title("The GPT-J Workshop")
    """This app enables you to interact with large language models in a friendly way!"""

    ex_names = [
        "In a shocking finding, scientists discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.",
    ]
    example = st.selectbox("Choose an example prompt from this selector", ex_names)

    inp = st.text_area("Or write your own prompt here!", example, max_chars=2000)

    with st.beta_expander("Generation options..."):
        length = st.slider(
            "Choose the length of the generated texts (in tokens)",
            2,
            1024,
            512,
            10,
        )
        temp = st.slider(
            "Choose the temperature (higher - more random, lower - more repetitive)",
            0.0,
            1.5,
            1.0,
            0.05,
        )

    st.subheader("Search results:")

    time.sleep(1)

    st.text("App baked with ❤️ by @vicgalle")


if __name__ == "__main__":
    main()
