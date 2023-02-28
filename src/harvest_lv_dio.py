#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: extract_jsonl
Author: Lukas Galke, Eva Seidlmayer - Adjustment Lucas Vetter
Email: seidlmayer@zbmed.de
Github:
Description: metadata (Extract DOI)
Last Change: Feb 2, 2023
"""

import argparse
import os
import jsonlines
import re
import pandas as pd
from tqdm import tqdm

DEBUG = False


def main():
    """ Extracts DOI from jsonlines file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonl_file")
    parser.add_argument("-o", "--output", dest='save', default=None, type=str,
                        help="Save files in this directory")
    args = parser.parse_args()


    #open ZB MED data file
    with jsonlines.open(args.jsonl_file) as json:
        flat_gen = ((d['_id']['$oid'], d['liv']['orig_data'])
                    for d in json)


        #set counter
        n_extracted = 0

        # initiate metadata container
        metadata = []

        for identifier, data in tqdm(flat_gen):
            if "DOI" not in data:
                continue

            #define infos: DOI

            doi = data.get('DOI')[0] if 'DOI' in data else None
            metadata.append(doi)

            # add 1 to counter
            n_extracted += 1


    print("Extracted %d papers" % n_extracted)

    # create dataframes from infos
    df_paper_metadata = pd.DataFrame(metadata,
                                     columns=['doi'
                                              ])


    dfs = [
        # dataframe name, dataframe, whether to save index
        ('livivo_doi', df_paper_metadata, False)
    ]

    if args.save is not None:
        # Dumps everything to disk
        os.makedirs(args.save, exist_ok=True)
        for fname, dframe, save_index in dfs:
            dframe.to_csv(os.path.join(args.save, fname + '.csv'),
                          index=save_index)
        with open(os.path.join(args.save, 'args.txt'), 'w') as fh:
            print(args, file=fh)


if __name__ == "__main__":
    main()