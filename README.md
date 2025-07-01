The Python script process.py takes an alignment file in he FASTA format: 

> Sequence Name 1
MGCTAHIGLIPDS
> Sequence Name 2
MGCTA-ISLIPDS

And converts it into a .csv, in the format:

Sequence Name 1,M,G,C,T,A,H,I,G,L,I,P,D,S
Sequence Name 2,M,G,C,T,A,-,I,S,L,I,P,D,S

This allows for it to be read by Microreact.

To visualise your data on Microreact, you will need to provide a tree of your protein/of species (check out https://phylot.biobyte.de/) along with your .csv of alignment data. 

The names of the sequences must match the names of the nodes of the tree, such that the data can be matched to the tree. 

You can then select specific alignment positions to show as metadata blocks alongside the tree. The colours of the blocks can be changed. This can be customised (as described in the Microreact documentation) exported as an .svg image.

This extension was created by Alannah and Chris Jensen-King; if you use it, please credit it :) 
