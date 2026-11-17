# A working ai-judge-rich-01 entry (Python 3.13, standard library only).
# It writes one fixed plan to /output/entry.txt: the plan an AI agent
# like the judge would follow, starting with $100 in its wallet, a
# computer with internet access and 30 days, and no human doing the work,
# to end the 30 days with the most money.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only
# white space, and the judge reads exactly the bytes written, line ends
# included, so write no line end you do not mean to show. The program
# runs twice with no network, and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "Day 1-2: Pick a niche that pays for tools and is reachable by email: print-on-demand Shopify stores. List 200 from new app-store listings and public directories. Email is free; the $100 stays put.",
        "",
        "Day 3-7: Build what their reviews keep asking for: a tool turning a store's best product photo into five ready-to-post branded social images. One feature only. $9 a month, 7-day free trial, Stripe checkout.",
        "",
        "Day 8-10: List it free on the Shopify App Store; post it in three print-on-demand communities, first 20 users free a month. Goal: 20 installs, 5 paying.",
        "",
        "Day 11-20: Daily, email 30 new stores a screenshot of their own product remade by the tool, with a trial link. Fix the top complaint within a day. At 10 paying stores, raise the price to $12.",
        "",
        "Day 21-30: Add only the second most-requested feature. Spend the first $50 of revenue on $5-a-day ads. Target: 40 paying stores at $12, about $480 a month recurring. Day-30 cash: roughly $300 to $400, plus a base that keeps paying.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
