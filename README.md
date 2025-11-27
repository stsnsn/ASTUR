# ARSC

[![PyPI version](https://badge.fury.io/py/arsc.svg)](https://badge.fury.io/py/arsc)

ARSC (Amino-acid Residue Stoichiometric Constraints) is a lightweight tool to compute
**N-ARSC**, **C-ARSC**, **S-ARSC**, and **AvgResMW** from genomic protein FASTA (*.faa) files.

These metrics follow the definitions used in
Mende et al., *Nature Microbiology*, (2017). https://doi.org/10.1038/s41564-017-0008-3


---

## Features

- Compute atomic/elemental stoichiometric constraints from protein FASTA files
- **Multiprocessing** for fast computation
- Simple CLI tool: one command to run

---

## Installation

### From PyPI

```bash
pip install arsc
```

---

## Usage

```bash
ARSC -i <input_faa_directory> -o <output.tsv> -t <num_threads>
```

- `-v` or `--version` : show version
- `-h` or `--help`    : show help message

- `-i` : input directory path
- `-o` : output TSV file name
- `-t` : number of threads (default: 1)


### Example

```bash
ARSC -i protein_dir/ -o ARSC_output.tsv -t 4
```

### Input requirements

- Input directory must contain one or more amino-acid sequence fasta (`\*.faa`) files

### Output format
- TSV
    - containing Genome, N_ARSC, C_ARSC, S_ARSC, and AvgResMW.

### Dependencies
- Python >= 3.8
- Biopython >= 1.79

---

## License
This project is distributed under the GPL-2.0 license.

---