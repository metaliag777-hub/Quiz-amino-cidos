import random
import streamlit as st
from PIL import Image
from rdkit import Chem
from rdkit.Chem import Draw

# 1. Base de datos con los 20 aminoácidos y sus propiedades químicas
AMINOACIDOS = [
    {
        "nombre": "Glicina (Gly, G)",
        "esencial": "No esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "NCC(=O)O",
    },
    {
        "nombre": "Alanina (Ala, A)",
        "esencial": "No esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "CC(N)C(=O)O",
    },
    {
        "nombre": "Valina (Val, V)",
        "esencial": "Esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "CC(C)C(N)C(=O)O",
    },
    {
        "nombre": "Leucina (Leu, L)",
        "esencial": "Esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "CC(C)CC(N)C(=O)O",
    },
    {
        "nombre": "Isoleucina (Ile, I)",
        "esencial": "Esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "CCC(C)C(N)C(=O)O",
    },
    {
        "nombre": "Prolina (Pro, P)",
        "esencial": "No esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "C1CC(NC1)C(=O)O",
    },
    {
        "nombre": "Metionina (Met, M)",
        "esencial": "Esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "CSCCC(N)C(=O)O",
    },
    {
        "nombre": "Fenilalanina (Phe, F)",
        "esencial": "Esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "Sí",
        "smiles": "NC(Cc1ccccc1)C(=O)O",
    },
    {
        "nombre": "Triptófano (Trp, W)",
        "esencial": "Esencial",
        "polaridad": "Apolar / Hidrofóbico",
        "carga": "Neutro",
        "aromatico": "Sí",
        "smiles": "NC(Cc1c[nH]c2ccccc12)C(=O)O",
    },
    {
        "nombre": "Serina (Ser, S)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "OCC(N)C(=O)O",
    },
    {
        "nombre": "Treonina (Thr, T)",
        "esencial": "Esencial",
        "polaridad": "Polar no cargado",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "CC(O)C(N)C(=O)O",
    },
    {
        "nombre": "Tirosina (Tyr, Y)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Neutro",
        "aromatico": "Sí",
        "smiles": "NC(Cc1ccc(O)cc1)C(=O)O",
    },
    {
        "nombre": "Cisteína (Cys, C)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "SCC(N)C(=O)O",
    },
    {
        "nombre": "Asparagina (Asn, N)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "NC(=O)CC(N)C(=O)O",
    },
    {
        "nombre": "Glutamina (Gln, Q)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Neutro",
        "aromatico": "No",
        "smiles": "NC(=O)CCC(N)C(=O)O",
    },
    {
        "nombre": "Lisina (Lys, K)",
        "esencial": "Esencial",
        "polaridad": "Polar no cargado",
        "carga": "Básico (Carga +)",
        "aromatico": "No",
        "smiles": "NCCCC(N)C(=O)O",
    },
    {
        "nombre": "Arginina (Arg, R)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Básico (Carga +)",
        "aromatico": "No",
        "smiles": "NC(N)=NCCCC(N)C(=O)O",
    },
    {
        "nombre": "Histidina (His, H)",
        "esencial": "Esencial",
        "polaridad": "Polar no cargado",
        "carga": "Básico (Carga +)",
        "aromatico": "Sí",
        "smiles": "NC(Cc1cncn1)C(=O)O",
    },
    {
        "nombre": "Aspartato (Asp, D)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Ácido (Carga -)",
        "aromatico": "No",
        "smiles": "NC(CC(=O)O)C(=O)O",
    },
    {
        "nombre": "Glutamato (Glu, E)",
        "esencial": "No esencial",
        "polaridad": "Polar no cargado",
        "carga": "Ácido (Carga -)",
        "aromatico": "No",
        "smiles": "NC(CCC(=O)O)C(=O)O",
    },
]


def generar_dibujo_2d(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return Draw.MolToImage(mol, size=(400, 350))
    return None


def nueva_pregunta():
    st.session_state.aa_actual = random.choice(AMINOACIDOS)
    st.session_state.modo = random.choice(["nombre_a_est", "est_a_nombre"])


st.set_page_config(
    page_title="Quiz de Aminoácidos", page_icon="🧬", layout="centered"
)
st.title("🧬 Quiz de Aminoácidos (Identificación Visual)")

if "aa_actual" not in st.session_state:
    nueva_pregunta()

if st.button("🔄 Cambiar de Aminoácido"):
    nueva_pregunta()

aa = st.session_state.aa_actual
modo = st.session_state.modo

st.divider()

lista_nombres = [item["nombre"] for item in AMINOACIDOS]
img_mol = generar_dibujo_2d(aa["smiles"])

if modo == "nombre_a_est":
    st.subheader(f"Aminoácido a identificar: **{aa['nombre']}**")
    st.write("Mira la imagen 2D para verificar su estructura y confirma:")
    if img_mol:
        st.image(
            img_mol, caption="Estructura molecular 2D", use_container_width=False
        )
    resp_identidad = st.selectbox(
        "Selecciona el nombre correspondiente:", lista_nombres, key="sel_id"
    )
else:
    st.subheader("Fotografía / Dibujo de la Estructura Química 2D:")
    if img_mol:
        st.image(
            img_mol,
            caption="Dibujo molecular sin pistas",
            use_container_width=False,
        )
    resp_identidad = st.selectbox(
        "¿A qué aminoácido corresponde este dibujo?",
        lista_nombres,
        key="sel_id",
    )

st.write("### Clasifica sus 4 propiedades químicas e hidrofóbicas:")

col1, col2 = st.columns(2)

with col1:
    resp_esencial = st.radio(
        "1. Esencialidad:", ["Esencial", "No esencial"], key="r_esencial"
    )
    resp_polaridad = st.radio(
        "2. Polaridad:",
        ["Apolar / Hidrofóbico", "Polar no cargado"],
        key="r_polaridad",
    )

with col2:
    resp_carga = st.radio(
        "3. Carácter ácido-básico / Carga:",
        ["Neutro", "Ácido (Carga -)", "Básico (Carga +)"],
        key="r_carga",
    )
    resp_aromatico = st.radio(
        "4. ¿Anillo Aromático?", ["Sí", "No"], key="r_aromatico"
    )

st.divider()

if st.button("✅ Validar Respuesta Completa", type="primary"):
    c_id = resp_identidad == aa["nombre"]
    c_esencial = resp_esencial == aa["esencial"]
    c_polaridad = resp_polaridad == aa["polaridad"]
    c_carga = resp_carga == aa["carga"]
    c_aromatico = resp_aromatico == aa["aromatico"]

    if c_id and c_esencial and c_polaridad and c_carga and c_aromatico:
        st.balloons()
        st.success(
            "🎉 ¡Excelente! Has respondido correctamente las 5 categorías."
        )
    else:
        st.error("❌ Hay errores en tu selección. Revisa el desglose:")

        if not c_id:
            st.write(
                f"- **Identificación:** El dibujo correspondía a **{aa['nombre']}**."
            )
        if not c_esencial:
            st.write(
                f"- **Esencialidad:** {aa['nombre']} es **{aa['esencial']}**."
            )
        if not c_polaridad:
            st.write(
                f"- **Polaridad:** {aa['nombre']} es **{aa['polaridad']}**."
            )
        if not c_carga:
            st.write(
                f"- **Carga/Acidez:** {aa['nombre']} es **{aa['carga']}**."
            )
        if not c_aromatico:
            st.write(
                f"- **Grupo aromático:** {aa['nombre']} **{('sí' if aa['aromatico'] == 'Sí' else 'no')}** tiene anillo aromático."
            )
