"""
Scientific Language Checker

Purpose
-------
Scan the repository and detect potentially problematic language
in research documents.

Examples:

- "proof of RH"
- "Riemann hypothesis solved"
- "definitive proof"
- "all zeros verified therefore RH is true"

The goal is to improve scientific rigor and prevent accidental
overstatements.

Usage
-----

python scripts/check_claim_language.py

python scripts/check_claim_language.py path/to/folder

Exit Codes
----------

0 : no issue detected
1 : warning(s) detected
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from dataclasses import dataclass


###############################################################################
# CONFIGURATION
###############################################################################

SUPPORTED_EXTENSIONS = {
    ".md",
    ".txt",
    ".tex",
    ".bib",
    ".rst",
    ".yaml",
    ".yml",
}

# Expressions à risque
RISK_PATTERNS = {
    "HIGH": [
        r"\bproof of the riemann hypothesis\b",
        r"\briemann hypothesis solved\b",
        r"\bproof of rh\b",
        r"\bcomplete proof\b",
        r"\bdefinitive proof\b",
        r"\brh is proven\b",
        r"\bthe riemann hypothesis is proven\b",
    ],
    "MEDIUM": [
        r"\bwe proved\b",
        r"\bour proof\b",
        r"\btherefore rh\b",
        r"\bsettles the riemann hypothesis\b",
        r"\bsolves the riemann hypothesis\b",
        r"\bproof sketch\b",
    ],
    "LOW": [
        r"\bstrong evidence\b",
        r"\bverified all zeros\b",
        r"\bconfirmed rh\b",
        r"\bappears proven\b",
    ],
}

# Mots qui réduisent le risque
SAFE_CONTEXT = [
    "does not prove",
    "does not constitute a proof",
    "candidate strategy",
    "working hypothesis",
    "experimental result",
    "computational evidence",
    "conjecture",
]

###############################################################################
# DATA STRUCTURES
###############################################################################


@dataclass
class Finding:
    level: str
    file: str
    line: int
    pattern: str
    text: str


###############################################################################
# ANALYSIS
###############################################################################


def is_supported(path: Path) -> bool:
    return path.suffix.lower() in SUPPORTED_EXTENSIONS


def has_safe_context(line: str) -> bool:
    lower = line.lower()

    return any(
        phrase in lower
        for phrase in SAFE_CONTEXT
    )


def scan_file(path: Path) -> listfindings = []

    try:
        lines = path.read_text(
            encoding="utf-8",
            errors="ignore"
        ).splitlines()

    except Exception:
        return findings

    for lineno, line in enumerate(lines, start=1):

        lower = line.lower()

        if has_safe_context(lower):
            continue

        for level, patterns in RISK_PATTERNS.items():

            for pattern in patterns:

                if re.search(pattern, lower):

                    findings.append(
                        Finding(
                            level=level,
                            file=str(path),
                            line=lineno,
                            pattern=pattern,
                            text=line.strip()
                        )
                    )

    return findings


###############################################################################
# REPORTING
###############################################################################


def print_header():

    print("\n" + "=" * 80)
    print("RIEMANN RESEARCH WORKSPACE")
    print("Scientific Language Checker")
    print("=" * 80)
    print()


def print_findings(findings):

    if not findings:
        print("No problematic language detected.\n")
        return

    print(f"{len(findings)} potential issue(s) detected.\n")

    for finding in findings:

        print("-" * 80)

        print(f"Level : {finding.level}")
        print(f"File  : {finding.file}")
        print(f"Line  : {finding.line}")

        print("\nText:")
        print(f"  {finding.text}")

        print("\nMatched Pattern:")
        print(f"  {finding.pattern}")

        print()

    print("-" * 80)
    print()


def summarize(findings):

    summary = {
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
    }

    for f in findings:
        summary[f.level] += 1

    print("Summary")
    print("-------")

    for level in ("HIGH", "MEDIUM", "LOW"):

        print(
            f"{level:>6} : {summary[level]}"
        )

    print()


###############################################################################
# REPOSITORY SCAN
###############################################################################


def scan_repository(root: Path) -> listfindings = []

    for file in root.rglob("*"):

        if file.is_file() and is_supported(file):

            findings.extend(
                scan_file(file)
            )

    return findings


###############################################################################
# MAIN
###############################################################################


def main():

    parser = argparse.ArgumentParser(
        description="Scientific language checker"
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Repository path"
    )

    args = parser.parse_args()

    root = Path(args.path).resolve()

    print_header()

    print(f"Scanning: {root}\n")

    findings = scan_repository(root)

    print_findings(findings)

    summarize(findings)

    if findings:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()