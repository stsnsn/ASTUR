# -*- coding: utf-8 -*-
#!/usr/bin/env python3
__author__ = 'Satoshi_Nishino'
__email__ = 'satoshi-nishino@g.ecc.u-tokyo.ac.jp'


"""
This script was created to compute the N/C-ARSC metrics as described in the following publication:
    Mende et al., Nature Microbiology, 2017 https://doi.org/10.1038/s41564-017-0008-3

Original citations for calculation metrics in Mende et al. 2017:
    Baudouin-Cornu P, Surdin-Kerjan Y, Marliere P, Thomas D. 2001. Molecular evolution of protein atomic composition. Science 293 297–300.
    Wright F. 1990. The 'effective number of codons' used in a gene. Gene 87 23-29.
"""

# USAGE: python ARSC.py -i <protein file (faa) or directory> -o <TSV name (optional)> -t <num_threads>
# e.g., python ARSC.py -i protein_faa/ -o ARSC.tsv -t 4

import sys
import argparse
from multiprocessing import Pool
from ARSC import __version__
from ARSC.utils import collect_faa_files, process_faa_auto


ARSC_LOGO = """
 .d8b.  d8888b. .d8888.  .o88b. 
d8' `8b 88  `8D 88'  YP d8P  Y8 
88ooo88 88oobY' `8bo.   8P      
88~~~88 88`8b     `Y8b. 8b      
88  `88 88 `88. db  `8D Y8b  d8 
YP  `YP 88  `YD `8888Y'  `Y88P' 
"""

class CustomFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass


def main():
    parser = argparse.ArgumentParser(description=f"{ARSC_LOGO}\n\nCompute ARSC from .faa/.faa.gz files", formatter_class=CustomFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-i", "--input_dir", required=True, help="A faa or faa.gz file, or directory")
    parser.add_argument("-o", "--output", help="Output TSV file w/ header (optional). If omitted, print to stdout w/o header.")
    parser.add_argument("-t", "--threads", default=1, type=int, help="Number of threads")


    args = parser.parse_args()


    try:
        items = list(collect_faa_files(args.input_dir))
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"ARSC Version: {__version__}", file=sys.stderr)
    print(f"Found {len(items)} files to process.", file=sys.stderr)
    print(f"Using {args.threads} threads.", file=sys.stderr)

    # Multiprocessing
    with Pool(args.threads) as pool:
        results = pool.map(process_faa_auto, items)


    # Output
    if args.output:
        with open(args.output, "w") as out:
            out.write("Genome\tN_ARSC\tC_ARSC\tS_ARSC\tAvgResMW\n")
            for r in results:
                out.write(f"{r['genome']}\t{r['N_ARSC']}\t{r['C_ARSC']}\t{r['S_ARSC']}\t{r['MW_ARSC']}\n")
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        for r in results:
            print(f"{r['genome']}\t{r['N_ARSC']}\t{r['C_ARSC']}\t{r['S_ARSC']}\t{r['MW_ARSC']}")

if __name__ == "__main__":
    main()