#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# BIDS Folder
# B. Prigent
# v 1, 13-Apr-2023
# ============================================= #
"""
    Library of json and tsv files
"""

participant_json = """{
  "genre": {
    "LongName": "",
    "Description": "genre of the participant as reported by the participant",
    "Levels": {
      "m": "male",
      "f": "female"
    },
    "Units": ""
  },
  "age": {
    "LongName": "",
    "Description": "age of the participant",
    "Levels": {
    },
    "Units": "years"
    },
  "a_jeun": {
    "LongName": "",
    "Description": "Time between last meal and NF session",
    "Levels": {
    },
    "Units": "minute"
  },
    "av_faim": {
    "LongName": "",
    "Description": "Subjective pre-session hunger assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "av_soif": {
    "LongName": "",
    "Description": "Subjective pre-session thirst assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "av_bienetre": {
    "LongName": "",
    "Description": "Subjective pre-session well being assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "av_motivation": {
    "LongName": "",
    "Description": "Subjective pre-session motivation assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "ap_motivation": {
    "LongName": "",
    "Description": "Subjective post-session motivation assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "ap_faim": {
    "LongName": "",
    "Description": "Subjective post-session hunger assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "ap_soif": {
    "LongName": "",
    "Description": "Subjective post-session thirst assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "ap_bienetre": {
    "LongName": "",
    "Description": "Subjective post-session well being assessment",
    "Levels": {
    },
    "Units": ""
  },   
  "moy_soif": {
    "LongName": "",
    "Description": "Average thirst before and after session",
    "Levels": {
    },
    "Units": ""
  },   
  "moy_faim": {
    "LongName": "",
    "Description": "Average hunger before and after session",
    "Levels": {
    },
    "Units": ""
  },   
  "moy_bienetre": {
    "LongName": "",
    "Description": "Average well being before and after session",
    "Levels": {
    },
    "Units": ""
  },   
  "ap_intensite_effort": {
    "LongName": "",
    "Description": "Intensity of the effort felt to move the gauge",
    "Levels": {
    },
    "Units": ""
  },   
  "ap_controle": {
    "LongName": "",
    "Description": "Sensation of gauge control",
    "Levels": {
    },
    "Units": ""
  },  
  "strategie_principale": {
    "LongName": "",
    "Description": "Main strategy used by the subject to move the gauge",
    "Levels": {
        "1":"Concentration",
        "2":"Visualization",
        "3":"Cheer",
        "4":"Relaxation",
        "5":"Motor",
        "6":"None"
    },
    "Units": ""
  },
  "dtempsV8-V1": {
    "LongName": "",
    "Description": "Time between first and last session of NF",
    "Levels": {
        },
    "Units": "days"
  }
}"""

participant_tsv = """participant_id	genre	age	a_jeun	av_faim	av_soif	av_bienetre	ap_motivation	ap_faim	ap_soif	ap_bienetre	moy_soif	moy_faim	moy_bienetre	ap_intensite_effort	ap_controle	strategie_principale	dtempsV8-V1
sub-A01	f	30	270	6	6	8	10	8	7	10	6.5	7.5	9	6	5	6	26
sub-A02	m	21	715	7	7	9	8	8	8	9	7.5	7.5	9	8	3	6	22
sub-A03	f	19	360	6	6	5	8	8	7	4	6.5	7.5	4.5	8	6	1	29
sub-A04	m	43	210	6	6	10	10	6	7	8	6.5	4	9	7	6	1	21
sub-A05	f	32	180	8	8	7	8	8	8	4	8	8.5	5.5	8	3	1	26
sub-A06	f	21	150	5	5	8	10	6	5	8	5	6	8	3	5	2	21
sub-A07	m	33	705	6	6	8	9	9	8	5	7	9	6.5	9	6	1	23
sub-A08	f	20	645	6	6	2	8	2	8	1	7	2.5	1.5	6	2	3	22
sub-A09	f	30	135	4	4	8	9	5	4	6	4	3	7	10	7	3	20
sub-A10	m	30	160	4	4	10	10	8	5	10	4.5	5.5	10	1	4	1	21
sub-A11	f	30	195	6	6	7	9	5	7	7	6.5	4	7	7	4	1	27
sub-A12	f	18	180	3	3	8	8	7	5	8	4	6	8	7	7	1	25
sub-A13	f	36	705	1	1	8	10	4	8	3	4.5	3.5	5.5	4	6	2	22
sub-A14	m	37	140	7	7	7	6	6	8	5	7.5	4.5	6	7	6	1	29
sub-A15	m	30	155	4	4	7	7	1	4	3	4	1	5	7	6	2	28
"""

description_json = """{
  "Name": "MIDFID",
  "BIDSVersion": "1.8.0",
  "DatasetType": "raw",
  "License": "idk",
  "Authors": [
    "Bannier",
    "Coquery",
    "Serrand"
  ],
  "Acknowledgements": "",
  "HowToAcknowledge": "",
  "Funding": [
    "",
    "",
    ""
  ],
  "EthicsApprovals": [""],
  "ReferencesAndLinks": [
    "",
    "",
    ""
  ],
  "DatasetDOI": "doi:"
}"""

event_json = """{
  "AntFood": {
    "LongName": "Anticipation Food",
    "Description": "Display an image of food propto level",
    "Levels": {
      "High": "High reward expected",
      "Low": "Low reward expected",
      "No": "No reward expected"
    },
    "Units": "",
    "TermURL": ""
  },
  "AntMoney": {
    "LongName": "Anticipation Money",
    "Description": "Display an image of money propto level",
    "Levels": {
      "High": "High reward expected",
      "Low": "Low reward expected",
      "No": "No reward expected"
    },
    "Units": "",
    "TermURL": ""
    },
    "RewFood": {
    "LongName": "Reward Food",
    "Description": "Display an image of Food propto level if correct answer",
    "Levels": {
      "High": "High reward expected",
      "Low": "Low reward expected",
      "No": "No reward expected",
      "No30": "Represent 30 percent of chance that they earn nothing even if they answer correctly"
    },
    "Units": "",
    "TermURL": ""
    },
    "RewMoney": {
    "LongName": "Reward money",
    "Description": "Display an image of money propto level if correct answer",
    "Levels": {
      "High": "High reward expected",
      "Low": "Low reward expected",
      "No": "No reward expected",
      "No30": "Represent 30 percent of chance that they earn nothing even if they answer correctly"
    },
    "Units": "",
    "TermURL": ""
    }
         }"""