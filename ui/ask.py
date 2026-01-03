def ask_page_range():
    print("Web化したいページ範囲を指定してください (例: 3-5, 10, 12-15)")
    raw = input("> ").strip()

    if "-" in raw:
        s, e = raw.split("-")
        return int(s), int(e)
    else:
        p = int(raw)
        return p, p
