import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Protein Enzyme Classifier",
    page_icon="🧬",
    layout="centered"
)


# -----------------------------
# Load model and features
# -----------------------------

@st.cache_resource
def load_model():
    model = joblib.load(
        "models/protein_enzyme_random_forest.joblib"
    )

    feature_names = joblib.load(
        "models/feature_names.joblib"
    )

    return model, feature_names


model, feature_names = load_model()


# -----------------------------
# Feature engineering
# -----------------------------

amino_acids = list(
    "ACDEFGHIKLMNPQRSTVWY"
)

hydrophobic = set("AILMFWVY")
aromatic = set("FYW")
positive = set("KRH")
negative = set("DE")


def calculate_protein_features(sequence):

    sequence = (
        sequence.upper()
        .replace("\n", "")
        .replace(" ", "")
    )

    length = len(sequence)

    features = {

        "sequence_length": length,

        "molecular_weight_proxy": length * 110,

        "hydrophobic_fraction": sum(
            aa in hydrophobic
            for aa in sequence
        ) / length,

        "aromatic_fraction": sum(
            aa in aromatic
            for aa in sequence
        ) / length,

        "positive_fraction": sum(
            aa in positive
            for aa in sequence
        ) / length,

        "negative_fraction": sum(
            aa in negative
            for aa in sequence
        ) / length,
    }

    for aa in amino_acids:

        features[f"aa_{aa}"] = (
            sequence.count(aa) / length
        )

    return features


# -----------------------------
# App interface
# -----------------------------

st.title("🧬 Protein Enzyme Classifier")

st.write(
    """
    Enter a protein amino-acid sequence to predict whether
    it is more likely to be an **enzyme** or **non-enzyme**.

    The prediction is generated using a Random Forest machine-learning
    model trained on protein sequence-derived features.
    """
)


with st.expander("ℹ️ How does it work?"):

    st.write(
        """
        The model extracts characteristics from the protein sequence,
        including:

        - Sequence length
        - Amino-acid composition
        - Hydrophobic amino-acid proportion
        - Aromatic amino-acid proportion
        - Positively charged amino-acid proportion
        - Negatively charged amino-acid proportion

        These features are then passed to a trained Random Forest classifier.
        """
    )


# -----------------------------
# Example sequence
# -----------------------------

example_sequence = (
    "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQANQKPYFIKTDPANR"
)

if st.button("Load Example Sequence"):

    st.session_state.sequence_input = (
        example_sequence
    )


sequence_input = st.text_area(
    "Enter Protein Sequence",
    height=200,
    placeholder=(
        "Example: "
        "MKTAYIAKQRQISFVKSHFSRQ..."
    ),
    key="sequence_input"
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    sequence = (
        sequence_input.upper()
        .replace("\n", "")
        .replace(" ", "")
    )

    valid_amino_acids = set(
        "ACDEFGHIKLMNPQRSTVWY"
    )

    if not sequence:

        st.warning(
            "Please enter a protein sequence."
        )

    elif not set(sequence).issubset(
        valid_amino_acids
    ):

        st.error(
            "Sequence contains invalid amino-acid characters."
        )

    else:

        features = calculate_protein_features(
            sequence
        )

        input_df = pd.DataFrame(
            [features]
        )

        # Match training feature order
        input_df = input_df[
            feature_names
        ]

        prediction = model.predict(
            input_df
        )[0]

        probability = model.predict_proba(
            input_df
        )[0][1]

        st.divider()

        st.subheader("Prediction")

        if prediction == 1:

            st.success(
                "🧪 Predicted Class: Enzyme"
            )

        else:

            st.info(
                "🔬 Predicted Class: Non-enzyme"
            )


        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Enzyme Probability",
                f"{probability:.2%}"
            )

        with col2:

            st.metric(
                "Sequence Length",
                f"{len(sequence)} amino acids"
            )


        st.progress(
            int(probability * 100)
        )


        st.subheader(
            "Sequence Characteristics"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Hydrophobic Fraction:** "
                f"{features['hydrophobic_fraction']:.3f}"
            )

            st.write(
                f"**Aromatic Fraction:** "
                f"{features['aromatic_fraction']:.3f}"
            )

        with col2:

            st.write(
                f"**Positive Fraction:** "
                f"{features['positive_fraction']:.3f}"
            )

            st.write(
                f"**Negative Fraction:** "
                f"{features['negative_fraction']:.3f}"
            )


# -----------------------------
# Disclaimer
# -----------------------------

st.divider()

st.caption(
    """
    ⚠️ This application is a machine-learning demonstration and should
    not be used as a substitute for biological annotation or experimental
    validation.
    """
)