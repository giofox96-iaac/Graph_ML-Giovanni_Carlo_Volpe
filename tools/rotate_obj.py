import sys
import math

R = ((1,0,0),(0,0,-1),(0,1,0))

def apply_R(x,y,z):
    rx = R[0][0]*x + R[0][1]*y + R[0][2]*z
    ry = R[1][0]*x + R[1][1]*y + R[1][2]*z
    rz = R[2][0]*x + R[2][1]*y + R[2][2]*z
    return rx, ry, rz


def rotate_obj(inpath, outpath):
    with open(inpath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    out_lines = []
    for ln in lines:
        if ln.startswith('v '):
            parts = ln.strip().split()
            try:
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            except Exception:
                out_lines.append(ln)
                continue
            rx, ry, rz = apply_R(x,y,z)
            out_lines.append(f"v {rx:.8f} {ry:.8f} {rz:.8f}\n")
        else:
            out_lines.append(ln)

    with open(outpath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: rotate_obj.py input.obj output.obj')
        sys.exit(1)
    rotate_obj(sys.argv[1], sys.argv[2])
    print('Wrote', sys.argv[2])
