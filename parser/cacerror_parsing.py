import re
import pandas as pd

def parse_net_stats():
    rows = []

    with open("net_stats_all.txt") as f:
        content = f.read()

    blocks = content.split("=========================================")

    for block in blocks:
        ip_match = re.search(r"IP:\s+(\S+)", block)
        if not ip_match:
            continue
        ip = ip_match.group(1)

        for line in block.splitlines():
            parts = line.split()
            if len(parts) < 8 or parts[0] == "iface":
                continue

            iface = parts[0]
            if iface == "bond0":
                continue

            rx_drop  = int(parts[4])
            rx_fifo  = int(parts[5])
            rx_frame = int(parts[6])

            if rx_drop > 0:
                rows.append(("rx_drop", ip, iface, rx_drop))
            if rx_fifo > 0:
                rows.append(("rx_fifo", ip, iface, rx_fifo))
            if rx_frame > 0:
                rows.append(("rx_frame", ip, iface, rx_frame))

    df = pd.DataFrame(rows, columns=["에러 구분", "서비스 IP", "발생 Interfaces", "count"])
    return df


def run_alignment_from_df(df):
    template_file = "cac_template.txt"

    # DataFrame → dict
    data_map = {
        (row["에러 구분"], row["서비스 IP"], row["발생 Interfaces"]): str(row["count"])
        for _, row in df.iterrows()
    }

    print("--- [ 결과값: 복사해서 엑셀 H열에 붙여넣으세요 ] ---")

    with open(template_file, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                print("")
                continue

            cols = line.strip().split("\t")
            if len(cols) < 3:
                cols = line.strip().split(maxsplit=2)

            if len(cols) < 3:
                print("0")
                continue

            err_type, ip, iface_raw = cols
            target_ifaces = [i.strip() for i in iface_raw.replace(",", " ").split()]

            res = [
                data_map.get((err_type, ip, iface), "0")
                for iface in target_ifaces
            ]

            print(", ".join(res))


if __name__ == "__main__":
    df = parse_net_stats()
    run_alignment_from_df(df)
