from Bio import SeqIO
from Bio.SeqUtils import ProtParam 
import pandas as pd
import argparse 

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

def main():

    argument_parser = argparse.ArgumentParser(description='Plpred-preprocess: data processing tool')
    argument_parser.add_argument('-m', '--membrane_proteins', required=True, help='path to the file containing membrane proteins')
    argument_parser.add_argument('-c', '--cytoplasm_proteins', required=True, help= 'path to the file containing cytoplasm proteins')
    argument_parser.add_argument('-o', '--output', required=True, help='path to the output file (.csv)')
    
    arguments = argument_parser.parse_args()
    
    df_membrane = generate_aa_composition_df(file_path=arguments.membrane_proteins, membrane_label=1)
    df_cytoplasm = generate_aa_composition_df(file_path=arguments.cytoplasm_proteins, membrane_label=0)
    df_processed = pd.concat([df_membrane, df_cytoplasm])
    df_processed.to_csv(arguments.output, index=False)

if __name__ == "__main__":
    main()