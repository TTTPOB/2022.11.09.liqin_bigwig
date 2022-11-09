import pyBigWig as pyw
import sys

args = sys.argv[1:]

chrom_names = [str(x) for x in range(1,6)] + [f"Chr{x}" for x in range(1,6)]
chrom_name_map = {oldname: oldname.replace("Chr", "chr") for oldname in chrom_names}
chrom_name_map = {oldname: f"chr{newname}" if not newname.startswith("chr") else newname for oldname, newname in chrom_name_map.items() }

bw = pyw.open(args[0])

new_header = [(chrom_name_map[chrom], length) for chrom, length in bw.chroms().items() if chrom in chrom_names]

out_bw = pyw.open(args[1], "w")
out_bw.addHeader(new_header)

for chrom, length in bw.chroms().items():
    print(chrom, length)
    if chrom not in chrom_names:
        continue
    ints = bw.intervals(chrom, 0, length)
    if len(ints):
        out_bw.addEntries([chrom_name_map[chrom]] * len(ints), [x[0] for x in ints], ends=[x[1] for x in ints], values=[x[2] for x in ints])
bw.close()
out_bw.close()
