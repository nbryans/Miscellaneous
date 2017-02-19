#!/usr/bin/env python

__author__ = "Nathaniel Bryans"
__version__ = "0.0.2"
__date__ = "2014/12/11"

# Dictionary holding the code to life: Codon to Amino Acid map
# Retrieved from http://isites.harvard.edu/fs/docs/icb.topic1122119.files/dna2aa.py
NucCode = {     'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
             'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
             'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
        }

MitoCode = {     'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': 'W',
             'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'M', 'aca': 'T', 'aaa': 'K', 'aga': '*',
             'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': '*',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
        }

#Takes a codon and returns the corresponding Amino Acid symbol
def codonToAANuc(codon):
      for char in codon.lower():
            if char != "a" and char != "c" and char != "t" and char != 'g':
                  return "-"           
      return NucCode[codon.lower()]

#Takes a codon and returns the corresponding Amino Acid symbol
def codonToAAMito(codon):
      for char in codon.lower():
            char.replace("u", "t")
            if char != "a" and char != "c" and char != "t" and char != 'g':
                  return "-"

      return NucCode[codon.lower()]



# THIS METHOD NOT YET TESTED
#Takes an Amino Acid symbol and returns the list of codons that map to it
def AAToCodonNuc(AA):
      codonList = []
      for i in NucCode.keys():
            if NucCode[i].lower() == AA.lower():
                  codonList.append(NucCode[i])
      return codonList

# THIS METHOD NOT YET TESTED
#Takes an Amino Acid symbol and returns the list of codons that map to it
def AAToCodonMito(AA):
      codonList = []
      for i in NucCode.keys():
            if NucCode[i].lower() == AA.lower():
                  codonList.append(NucCode[i])
      return codonList

