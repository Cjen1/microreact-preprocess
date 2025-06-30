import argparse
import sys

#>name
#<sequence>
#>name
#<sequence>s.

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converts a fasta file into an input for microreact")

    parser.add_argument("-f", help="filename")
    parser.add_argument("-o", default=None, help="Output to file, if unset, writes to stderr")

    args = parser.parse_args()

    with open(args.f, 'r') as f:
        data = f.readlines()
    n_seqs : int = int(len(data) / 2)

    output = sys.stderr if args.o is None else open(args.o, 'w')

    max_seq_len = 0
    for i in range(n_seqs):
        max_seq_len = max(max_seq_len, len(data[i]))
    seq_cols = ",".join(
            f"Pos_{i + 1}" for i in range(max_seq_len)
            )
    print(f"sequence_name,{seq_cols}", file=output)
    
    for i in range(n_seqs):
        meta_line = data[2*i].strip()
        sequence_line = data[2*i + 1].strip()

        # title (escape some stuff), p0, p1, p2, p3, p4

        title = meta_line[1:].strip()
        sequence = ",".join(
                c for c in sequence_line
                )
        print(f"{title},{sequence}", file=output)
