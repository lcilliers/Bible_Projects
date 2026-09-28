# Travel access (December, 6 weeks) and a public website — planning note (v1)

**Date:** 2026-09-28
**Status:** DRAFT for researcher mark-up. Nothing has been set up or published.
**Related:** the file-location inventory, which records the rule "`C:\Bible_study_projects` is authoritative" (`research/investigations/file-location-inventory-v1-20260928.md`, in progress).

**How to mark up:** each decision has a `Decision:` line. Write your choice there, or strike through options.

---

## 1. Facts this plan rests on [measured / from project records]

| Fact | Source |
|---|---|
| `iba/app/db/iba.db` is **808 MB**, SQLite in WAL mode, and it is written by the iba app scripts and migrations | `iba/app/db` listing, 2026-09-28 |
| `iba/app/db/*.db` and `database/*.db` are **excluded from git**. GitHub also rejects files over 100 MB. | `.gitignore` lines 36, 164 |
| **The June database loss was a Google Drive sync-corruption event.** A live SQLite file in a synced folder was zeroed; the conflict copies and the in-tree backups were deleted with it. | `outputs/markdown/wa-db-loss-incident-20260603.md` §1, §4 |
| NAS backups exist (`scripts/backup_db_to_nas.py`), in a separate failure domain | script header; memory |
| The project repository is on GitHub (`lcilliers/Bible_Projects`), without the databases or `backups/` | CLAUDE.md §12 |
| The iba app is driven by scripts (Python and PowerShell), not a web interface | `iba/app/ps`, `iba/app/handlers` |

**The governing constraint:** a live SQLite database must have **one writer, in one place, outside any sync folder**. Two copies being edited, or a synced live file, is the failure we already had.

---

## 2. Database access while travelling — the options

| | Option | How it works | For | Against |
|---|---|---|---|---|
| **A** | **Remote into the home desktop** | The desktop stays on at home. You connect from a travel laptop or tablet: Chrome Remote Desktop or Windows Remote Desktop over Tailscale (private network, no open ports). You can also drive Claude Code sessions remotely (the desktop app's Remote Control). | **The database never moves.** It is still one writer and one authoritative home, which is the rule we are setting up now. NAS backups keep running. Nothing to merge on return. | The desktop must stay up for 6 weeks: power cuts, Windows updates and crashes, with nobody at home to press a button. It needs a UPS, auto-restart after power loss (BIOS), a controlled Windows-update window, and auto-login or a startup service. Needs a usable internet connection where you are. |
| **B** | **Check the database out to a travel laptop** | Before leaving: stop all work at home, copy `iba.db` and the repository to a laptop, and mark the home copy frozen (read-only). The laptop is the only writer for 6 weeks. On return, copy back and unfreeze. | Works offline. No dependence on the home machine. | The laptop needs the full environment (Python 3.14, venv, STEP server if used). Theft or loss of the laptop means loss of 6 weeks' work unless it is backed up while away. **The discipline has to be perfect:** one slip, such as a session opened at home, gives two diverging databases. |
| **C** | **Move the working database to a cloud machine** | A small cloud VM (or similar) holds the repository and `iba.db`. You and Claude Code work on it from anywhere. | Always on, reachable from any device. Independent of home power. | Monthly cost; setup and security work. It changes the authoritative home, which would have to be decided and recorded. More than a 6-week need justifies, unless it becomes permanent. |
| **D** | Put `iba.db` in Google Drive / OneDrive / Dropbox | — | — | **Ruled out.** This is exactly the June failure. |

**Plus, for any option — a read-only reference snapshot:**
- Before leaving, put a **zipped, dated, clearly named copy** (e.g. `iba-db-READONLY-snapshot-20261130.zip`) in cloud storage.
- It is **never opened in place** and **never written back**. It is unzipped only on a device, for looking things up, if the working route fails.
- Zipping matters: sync services handle a single closed file safely. What breaks is a live database file changing underneath them.

### Recommendation [Claude reading]

**Option A, prepared properly, with the read-only snapshot as fallback.**
- It is the only option that keeps the rule you have just set: one authoritative home, one writer. It also needs nothing merged on return.
- Its weakness is the home machine's reliability, and that can be tested **before** December. Run it for a week or two in November while you are still at home: remote in from another device, do real work, restart the PC deliberately, and cut the power once.
- If that test fails, fall back to **Option B**, with a written check-out / check-in protocol and a backup from the laptop to cloud storage (zipped snapshots only) every few days.
- Option C only if you want remote working to become permanent.

Decision (A / B / C): ____

---

## 3. Documents while travelling (not the database)

- **Everything in git is already reachable** from anywhere through GitHub, including through Claude Code on the web. This covers scripts, markdown outputs, patches and investigations. It does **not** cover work that needs the database, which depends on the choice in §2.
- **Word, PDF and published documents** (`Sessions/Session_Clusters/*/Published/`): if Option A is chosen they are reachable through the remote desktop. For reading on a phone or tablet without the PC, a **generated read-only export folder** could be placed in cloud storage before leaving.
  - It is clearly named (e.g. `TRAVEL-READ-ONLY-export-20261130`).
  - It is regenerated, never edited, and deleted on return.
  - This keeps it from becoming another place where files "live", which is today's problem.
- **Zotero:** your library syncs to zotero.org and can be read through the web library or the Zotero app on another device. Attachments are available only if file syncing is on for them (Zotero storage or WebDAV).

Decision — travel read-only export folder (yes / no): ____
Decision — which device(s) will you take (laptop / tablet / phone only): ____

---

## 4. Checklist before leaving (if A)

1. UPS on the desktop and the router; BIOS set to "power on after AC loss"
2. Windows Update: pause, or set active hours, for the travel period
3. Auto-login or a startup service so that remote access and Tailscale come back after a restart
4. Tailscale plus remote desktop installed on the home PC and on the travel device
5. The NAS backup is scheduled and verified to run unattended
6. Test in November: one week of real work remotely, including a forced restart and a power cut
7. A read-only zipped snapshot of `iba.db` in cloud storage
8. A named person at home who can press the power button, if anyone is available

---

## 5. Public website

### 5.1 Principle
**The website is an output, never a working location.** Documents get onto it only by a deliberate publish step from `C:\Bible_study_projects`. It never holds the only copy of anything.

### 5.2 Suggested setup
- **Platform:** GitHub Pages, as for modelling4comfort.uk and gardens4comfort.uk.
- **A separate public repository** (e.g. `bible-inner-being-site`). **Not** `Bible_Projects`, which holds working files, tooling and patches.
- **Generator:** MkDocs (Material theme) or Jekyll. Pages are written in Markdown, with navigation and search, and PDFs are offered for download. Word documents convert with pandoc.
- **Source of content:** cluster publications (`Sessions/Session_Clusters/{CODE}/Published/`) and selected finished essays. **Not** batch files or analytical working documents.
- **A publish script** (later) copies the chosen files into the site repository and records what was published and when. The site can then always be traced back to the authoritative files.
- **Domain:** a custom domain like your other sites. Name to be decided.

### 5.3 Before anything is published — Bible-text copyright
The studies quote the ESV heavily. As I understand Crossway's permission terms, **up to 500 verses may be quoted without written permission**, provided the verses do not make up a complete book of the Bible and **do not account for more than 25% of the total text of the work**. A copyright notice is required.
- **[verify]** the current terms at Crossway before publishing.
- **Several analytical documents (e.g. the M47 batch files) are mostly quotation** and would likely exceed 25%. Published pieces may need to be written with more summary and fewer quotes, or quote a translation with more open terms.

Also: Hebrew and Greek lexical data from STEP and other sources carry their own licences. **[verify]** before publishing extracted lexical tables.

### 5.4 Decisions
Decision — go ahead with a site (yes / later): ____
Decision — first content to publish (e.g. one finished cluster essay as a pilot): ____
Decision — domain name: ____

---

## 6. Suggested order
1. Finish the file-location inventory and moves (current work). The website and the travel export both depend on a clean authoritative source.
2. Decide §2 (the database), and run the November test if A is chosen.
3. Website pilot with one finished document, after the copyright check.
