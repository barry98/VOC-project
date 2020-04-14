# VOC-project

Klaar:
- PICCL klaar voor gebruik
- Data gecleaned van enters
- PICCL over alle notaris data heen laten gaan
- Wat meer inzicht krijgen in data:
  - Aantal namen uit geannoteerde notaris data in voc clustered dataset (zonder Levenstein Distance 19,119, ongeveer 29% van alle beschikbare namen)
  - Datastories (met Eva): Word Cloud van voorkomende namen in voc clustered dataset, verdeling van rangen in voc clustered dataset  
- Opzetten evaluatie van NER modellen
- Begin opzet van annotatie

Deze week:
- Eerste tests met NER (BERTje)

Uitslag NER tests:
- SpaCy basis Nederlands model herkent ongeveer 33% van alle namen 1 op 1 met hoe ze geannoteerd zijn.
- SpaCy basis Nederlands model, huidige recall van 0.6 met een levenshtein distance van 3 of 0.55 met een levenshtein distance van 2. Zonder levenshtein distance een recall van 0.37.

Deliverables van afgelopen week:
- Annotatie guideline opzet klaar 
- Eerste resultaten NER modellen binnen

Deliverables van komende week:
- Eerste resultaten NEL model

Mogelijk woordenboek voor NER training:
- Transkribus vragen aan Jirsi
