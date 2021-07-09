import streamlit as st
import time
import requests


def main():
    st.set_page_config(  # Alternate names: setup_page, page, layout
        layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="The Big Language Model Workshop",  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
    )
    st.title("The Big Language Model Workshop")
    """This app enables you to interact with large language models in a friendly way!"""

    ex_names = [
        "In a shocking finding, scientists discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.",
        "The ancient people of Arcadia achieved oustanding cultural and technological developments. Below we summarise some of the highlights of the Acadian society.",
        """Tweet: "I hate it when my phone battery dies."
Sentiment: Negative
###
Tweet: My day has been 👍.
Sentiment: Positive
###
Tweet: This is the link to the article.
Sentiment: Neutral
###
Tweet: This new movie started strange but in the end it was awesome.
Sentiment:""",
        """Q: Fetch the departments that have less than five people in it.\n
A: SELECT DEPARTMENT, COUNT(WOKRED_ID) as "Number of Workers" FROM Worker GROUP BY DEPARTMENT HAVING COUNT(WORKED_ID) < 5;\n
###\n
Q: Show all departments along with the number of people in each department\n
A: SELECT DEPARTMENT, COUNT(DEPARTMENT) as "Number of Workers" FROM Worker GROUP BY DEPARTMENT;\n
###\n
Q: Show the last record of the Worker table\n
A: SELECT * FROM Worker ORDER BY LAST_NAME DESC LIMIT 1;\n
###\n
Q: Fetch the three max salaries from the Worker table;\n
A:""",
    ]
    example = st.selectbox("Choose an example prompt from this selector", ex_names)

    inp = st.text_area(
        "Or write your own prompt here!", example, max_chars=2000, height=150
    )

    try:
        rec = ex_names.index(inp)
    except ValueError:
        rec = 0

    with st.beta_expander("Generation options..."):
        length = st.slider(
            "Choose the length of the generated texts (in tokens)",
            2,
            1024,
            512 if rec < 2 else 50,
            10,
        )
        temp = st.slider(
            "Choose the temperature (higher - more random, lower - more repetitive). For the code generation or sentence classification promps it's recommended to use a lower value, like 0.35",
            0.0,
            1.5,
            1.0 if rec < 2 else 0.35,
            0.05,
        )

    response = None
    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="Generate!")

        if submit_button:

            payload = {
                "context": inp,
                "token_max_length": length,
                "temperature": temp,
                "top_p": 0.9,
            }

            query = requests.post(
                "http://api.vicgalle.net:5000/generate", params=payload
            )
            response = query.json()

            st.markdown(response["prompt"] + response["text"])
            st.text(f"Generation done in {response['compute_time']:.3} s.")

    if False:
        col1, col2, *rest = st.beta_columns([1, 1, 10, 10])

        def on_click_good():
            response["rate"] = "good"
            print(response)

        def on_click_bad():
            response["rate"] = "bad"
            print(response)

        col1.form_submit_button("👍", on_click=on_click_good)
        col2.form_submit_button("👎", on_click=on_click_bad)

    st.text("App baked with ❤️ by @vicgalle")


if __name__ == "__main__":
    main()
