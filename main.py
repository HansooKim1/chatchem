import streamlit as st
from PIL import Image
import pubchempy as pcp

# Initialize Streamlit session state
if "step" not in st.session_state:
    st.session_state.step = 0
if "messages" not in st.session_state:
    st.session_state.messages = []

class FixedUI:
    """Class to handle the fixed UI components of the Streamlit app."""

    def __init__(self):
        st.set_page_config(page_title="Chemistry Assistant", page_icon="🔬")

    def render_sidebar(self):
        """Renders the sidebar with fixed content."""
        try:
            professor_img_path = r'C:\Users\HansooKim\Desktop\pubchem\정근홍 교수님 사진.png'  # Update with correct path
            professor_img = Image.open(professor_img_path)
            st.sidebar.title('About Me')
            st.sidebar.image(professor_img, caption='정근홍 교수님')
            st.sidebar.write("정근홍 교수님은 AI와 양자화학을 이용한 화학물질 탐지의 세계적 권위자입니다.")

            st.sidebar.markdown("---")
            st.sidebar.title('Chemistry Assistant')
            st.sidebar.write("""
            Chemistry Assistant는 Pubchem 기반으로 화학물질의 정보를 제공하며, 머신러닝 기법으로 화학물질의 특성을 계산하고 추정합니다. 출처: [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
            """)

            st.sidebar.markdown("---")
            cv_path = r'C:\Users\HansooKim\Desktop\pubchem\정근홍 교수님 CV.pdf'  # Update with correct path
            with open(cv_path, 'rb') as cv_file:
                st.sidebar.download_button(
                    label="정근홍 교수님 CV 다운로드",
                    data=cv_file.read(),
                    file_name="정근홍 교수님 CV.pdf",
                    mime='application/pdf'
                )
        except FileNotFoundError as e:
            st.sidebar.error(f"Error loading sidebar content: {e}")

    def render_sponsors(self):
        """Renders the sponsors section at the bottom of the main page."""
        st.markdown("---")
        st.markdown("<h3 style='text-align: center;'>Sponsors</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        sponsor1_img_path = r'C:\Users\HansooKim\Desktop\pubchem\후원사1.png'  # Update with correct path
        sponsor2_img_path = r'C:\Users\HansooKim\Desktop\pubchem\후원사2.png'  # Update with correct path

        with col1:
            sponsor1_img = Image.open(sponsor1_img_path)
            st.image(sponsor1_img, use_column_width=True)
        with col2:
            sponsor2_img = Image.open(sponsor2_img_path)
            st.image(sponsor2_img, use_column_width=True)


class MolecularFormulaFinder:
    """Class to handle finding the Molecular Formula by CID."""

    def get_molecular_formula(self, cid):
        """Fetches the molecular formula from PubChem using the provided CID."""
        try:
            compound = pcp.get_compounds(cid, 'cid')[0]
            return compound.molecular_formula
        except Exception as e:
            st.error(f"Error retrieving molecular formula for CID {cid}: {e}")
            return None

    def run(self):
        """Runs the Molecular Formula Finder UI."""
        st.title("Find Molecular Formula")

        # Display chat messages from history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input for CID
        if cid_input := st.chat_input("Enter the CID number to find the Molecular Formula:"):
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(cid_input)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": cid_input})

            # Fetch and display the molecular formula
            molecular_formula = self.get_molecular_formula(cid_input)
            if molecular_formula:
                response = f"The molecular formula for CID {cid_input} is {molecular_formula}."
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})


class MolecularWeightFinder:
    """Class to handle finding the Molecular Weight by CID."""

    def get_molecular_weight(self, cid):
        """Fetches the molecular weight from PubChem using the provided CID."""
        try:
            compound = pcp.get_compounds(cid, 'cid')[0]
            return compound.molecular_weight
        except Exception as e:
            st.error(f"Error retrieving molecular weight for CID {cid}: {e}")
            return None

    def run(self):
        """Runs the Molecular Weight Finder UI."""
        st.title("Find Molecular Weight")

        # Display chat messages from history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input for CID
        if cid_input := st.chat_input("Enter the CID number to find the Molecular Weight:"):
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(cid_input)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": cid_input})

            # Fetch and display the molecular weight
            molecular_weight = self.get_molecular_weight(cid_input)
            if molecular_weight:
                response = f"The molecular weight for CID {cid_input} is {molecular_weight} g/mol."
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})


class SmilesFinder:
    """Class to handle finding the SMILES by CID."""

    def get_smiles(self, cid):
        """Fetches the SMILES from PubChem using the provided CID."""
        try:
            compound = pcp.get_compounds(cid, 'cid')[0]
            return compound.canonical_smiles
        except Exception as e:
            st.error(f"Error retrieving SMILES for CID {cid}: {e}")
            return None

    def run(self):
        """Runs the SMILES Finder UI."""
        st.title("Find SMILES")

        # Display chat messages from history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input for CID
        if cid_input := st.chat_input("Enter the CID number to find the SMILES:"):
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(cid_input)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": cid_input})

            # Fetch and display the SMILES
            smiles = self.get_smiles(cid_input)
            if smiles:
                response = f"The SMILES for CID {cid_input} is {smiles}."
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})


class NameFinder:
    """Class to handle finding the compound name by CID."""

    def get_name(self, cid):
        """Fetches the compound name from PubChem using the provided CID."""
        try:
            compound = pcp.get_compounds(cid, 'cid')[0]
            return compound.iupac_name if compound.iupac_name else compound.synonyms[0]
        except Exception as e:
            st.error(f"Error retrieving name for CID {cid}: {e}")
            return None

    def run(self):
        """Runs the Name Finder UI."""
        st.title("Find Compound Name")

        # Display chat messages from history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input for CID
        if cid_input := st.chat_input("Enter the CID number to find the Compound Name:"):
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(cid_input)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": cid_input})

            # Fetch and display the compound name
            name = self.get_name(cid_input)
            if name:
                response = f"The compound name for CID {cid_input} is {name}."
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})


def main():
    fixed_ui = FixedUI()
    fixed_ui.render_sidebar()  # Render the sidebar

    st.title("Chemistry Assistant 🤖")
    
    if st.session_state.step == 0:
        st.write("Welcome! I can assist you with the following functionalities:")
        st.write("1. Find Molecular Formula by CID")
        st.write("2. Find Molecular Weight by CID")
        st.write("3. Find SMILES by CID")
        st.write("4. Find Compound Name by CID")
        
        # Use chat input for selection instead of button
        if choice := st.chat_input("Please enter the service number (1, 2, 3, or 4):"):
            # Add user choice to chat history
            with st.chat_message("user"):
                st.markdown(choice)
            st.session_state.messages.append({"role": "user", "content": choice})

            if choice == "1":
                st.session_state.step = 1
            elif choice == "2":
                st.session_state.step = 2
            elif choice == "3":
                st.session_state.step = 3
            elif choice == "4":
                st.session_state.step = 4
            else:
                st.error("Invalid choice. Please enter a number between 1 and 4.")

    elif st.session_state.step == 1:
        formula_finder = MolecularFormulaFinder()
        formula_finder.run()

    elif st.session_state.step == 2:
        weight_finder = MolecularWeightFinder()
        weight_finder.run()

    elif st.session_state.step == 3:
        smiles_finder = SmilesFinder()
        smiles_finder.run()

    elif st.session_state.step == 4:
        name_finder = NameFinder()
        name_finder.run()

    # Render the sponsors section at the very bottom
    fixed_ui.render_sponsors()

if __name__ == "__main__":
    main()