from Bio import SeqIO
from Bio.SeqUtils import ProtParam 
import pandas as pd

def compute_aa_composition(protein_sequence:str)->dict:
    """
    computes the aminoacids compositions of a given protein sequence. 

    Parameters
    ----------
    protein_sequence: str
        sequence of the protein to be processed
    
    Return
    ------
    aa_composition: dict
        directoru contaning the relative abundance of each aminoacid

    """

    analyzer = ProtParam.ProteinAnalysis(str(protein_sequence))
    aa_composition = analyzer.get_amino_acids_percent()
    return aa_composition

def generate_aa_composition_df(file_path, membrane_label:int) -> pd.DataFrame:
    """
    generation of a dataframe that contains the amino acid composition for each protein in a phased format.

    Parameters
    ----------

    file_path: str 
        FASTA file to bem processed

    membrane_label:  int
        label indicating if the proteins is located in the membrane (1) or cytoplasm

    Returns
    -------

    df: pd.DataFrame
        DataFrame contating the aminoacid compositions
    """
    df = pd.DataFrame()
    handle = open(file_path)
    parser = SeqIO.parse(handle, 'fasta')

    for protein in parser: 
        protein_data = compute_aa_composition(protein.seq)
        protein_data['membrane'] = membrane_label
        df = df.append([protein_data], ignore_index=True)

    return df
print(__name__)

if __name__ == "__main__":

    print('Preprocessing FASTA file: membrane proteins')
    df_membrane = generate_aa_composition_df(file_path='data/raw/membrane.fasta', membrane_label=1)

    print('Preprocessing FASTA file: cytoplasm protein')
    df_cytoplasm = generate_aa_composition_df(file_path='data/raw/cytoplasm.fasta', membrane_label=0)

    df_processed = pd.concat([df_membrane, df_cytoplasm])
    
    print('Saving processed DataFrame to file')
    df_processed.to_csv('data/processed/processed.csv', index=False)
