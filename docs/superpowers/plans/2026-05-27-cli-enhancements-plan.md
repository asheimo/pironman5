# CLI Enhancements Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `update`/`uninstall` subcommands and bash auto-completion (argcomplete) to the pironman5 CLI.

**Architecture:** `update` delegates to the canonical install.sh via curl-to-bash. `uninstall` implements removal logic directly in-process. argcomplete hooks into the existing argparse parser for zero-config completions.

**Tech Stack:** Python 3.7+, argparse + argcomplete, bash (install.sh)

---

### Task 1: Add `pironman5 update` subcommand

**Files:**
- Modify: `pironman5/_cli.py`

- [ ] **Step 1: Add update subparser**

In `main()`, after the `launch-browser` subparser block (line 111), before the comment `# parse args`, insert:

```python
    update_parser = subparsers.add_parser("update", help="Update Pironman5 to latest version")
    update_parser.add_argument("--variant", nargs='?', default='', help="Override variant (base/mini/max/pro-max/ups/nas)")
    update_parser.add_argument("--pipower5", action="store_true", help="Include PiPower5 support")
```

- [ ] **Step 2: Add update handler in subcommand dispatch**

In `main()`, after the `pipower5` handler block (ending with `sys.exit(1)` at line 608), before the comment `# Update settings`, insert:

```python
    # update
    # ----------------------------------------
    if args.subcommand == 'update':
        variant = args.variant if args.variant else ''
        if not variant:
            try:
                with open('/opt/pironman5/.variant', 'r') as f:
                    variant = f.read().strip()
            except FileNotFoundError:
                print("Error: Cannot detect variant. /opt/pironman5/.variant not found.")
                print("Specify variant manually: pironman5 update --variant base")
                sys.exit(1)

        if not variant:
            print("Error: Empty variant. Specify manually: pironman5 update --variant base")
            sys.exit(1)

        use_pipower5 = args.pipower5
        if not use_pipower5:
            try:
                with open('/opt/pironman5/.custom_module', 'r') as f:
                    if 'pipower5' in f.read():
                        use_pipower5 = True
            except FileNotFoundError:
                pass

        installer_url = "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh"
        cmd_parts = ["curl -sSL", installer_url, "| sudo bash -s -- --variant", variant, "--plain-text"]
        if use_pipower5:
            cmd_parts.append("--pipower5")

        cmd = ' '.join(cmd_parts)
        print(f"Updating Pironman 5 ({variant})...")
        print(f"Running: {cmd}")
        ret = os.system(cmd)
        if ret != 0:
            print(f"Update failed with exit code {ret}", file=sys.stderr)
            sys.exit(1)
        print("Update complete. Restarting service...")
        os.system('systemctl restart pironman5.service')
        quit()
```

- [ ] **Step 3: Commit**

```bash
git add pironman5/_cli.py
git commit -m "feat(cli): add update subcommand

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 2: Add `pironman5 uninstall` subcommand

**Files:**
- Modify: `pironman5/_cli.py`

- [ ] **Step 1: Add uninstall subparser**

In `main()`, after the `update_parser` block added in Task 1, before `# parse args`, insert:

```python
    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall Pironman5 completely")
    uninstall_parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompts")
```

- [ ] **Step 2: Add uninstall handler in subcommand dispatch**

In `main()`, after the update handler added in Task 1, before `# Update settings`, insert:

```python
    # uninstall
    # ----------------------------------------
    if args.subcommand == 'uninstall':
        def _confirm(prompt):
            if args.yes:
                return True
            while True:
                resp = input(prompt + " [y/N] ")
                if resp.lower() in ('y', 'yes'):
                    return True
                elif resp.lower() in ('', 'n', 'no'):
                    return False

        if not _confirm("This will completely remove Pironman 5 and all its data. Continue?"):
            print("Uninstall cancelled.")
            quit()

        print("Stopping service...")
        os.system('systemctl stop pironman5.service 2>/dev/null')
        os.system('systemctl disable pironman5.service 2>/dev/null')
        service_file = '/etc/systemd/system/pironman5.service'
        if os.path.exists(service_file):
            os.remove(service_file)
            os.system('systemctl daemon-reload')

        print("Removing symlinks...")
        symlink_path = '/usr/local/bin/pironman5'
        if os.path.exists(symlink_path):
            os.remove(symlink_path)

        print("Removing user and group...")
        os.system('userdel pironman5 2>/dev/null')
        os.system('groupdel pironman5 2>/dev/null')

        print("Removing directories...")
        os.system('rm -rf /opt/pironman5/')
        os.system('rm -rf /var/log/pironman5/')

        if _confirm("Uninstall InfluxDB database too?"):
            os.system('apt-get purge influxdb -y')

        print("Pironman 5 has been uninstalled.")
        quit()
```

- [ ] **Step 3: Commit**

```bash
git add pironman5/_cli.py
git commit -m "feat(cli): add uninstall subcommand

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 3: Add argcomplete auto-completion

**Files:**
- Modify: `pyproject.toml`
- Modify: `pironman5/_cli.py`
- Modify: `../sunfounder-installer-scripts/pironman5/install.sh`

- [ ] **Step 1: Add argcomplete to pyproject.toml dependencies**

Replace:
```toml
dependencies = []
```
with:
```toml
dependencies = [
    "argcomplete",
]
```

- [ ] **Step 2: Add argcomplete setup to _cli.py**

Add as the very first line (line 1, before existing imports):
```python
# PYTHON_ARGCOMPLETE_OK
```

Add to the imports block (line 5 area):
```python
import argcomplete
```

After all subparsers are registered (after `uninstall_parser` from Task 2) and before `# parse args` (line ~115), insert:
```python
    argcomplete.autocomplete(parser)
```

- [ ] **Step 3: Add argcomplete registration to install.sh**

In `F:\workspace\sunfounder-installer-scripts\pironman5\install.sh`, after the pironman5 symlink creation (line 340):
```bash
RUN "ln -sf /opt/pironman5/venv/bin/pironman5 /usr/local/bin/pironman5" "Create pironman5 symlink"
```

Insert after that `RUN` line:
```bash
# --- Shell completion ---
TITLE "Setup shell completion"
RUN "register-python-argcomplete pironman5 > /etc/bash_completion.d/pironman5" "Register bash completion"
```

- [ ] **Step 4: Verify argcomplete imports**

Run: `pip install argcomplete && python -c "import argcomplete; print('OK')"`
Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml pironman5/_cli.py
git commit -m "feat(cli): add argcomplete bash auto-completion

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 4: Commit installer script change

**Repo:** `F:\workspace\sunfounder-installer-scripts`
**Files:**
- Modify: `pironman5/install.sh`

- [ ] **Step 1: Verify the install.sh change is in place**

Confirm the argcomplete registration line from Task 3 Step 3 is present in install.sh.

- [ ] **Step 2: Commit**

```bash
cd F:/workspace/sunfounder-installer-scripts
git add pironman5/install.sh
git commit -m "feat(pironman5): register argcomplete bash completion on install

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```
