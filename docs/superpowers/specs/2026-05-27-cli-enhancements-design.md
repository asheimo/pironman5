# CLI Enhancements: Auto-completion + Update + Uninstall

Date: 2026-05-27
Branch: `ups-beta`
Status: approved

## Feature 1: Bash auto-completion via argcomplete

### Design

Use the `argcomplete` Python package to auto-generate bash completions from the existing argparse parser. No hand-written completion script needed.

### Changes

**`pironman5/__init__.py`:**
- Add `# PYTHON_ARGCOMPLETE_OK` comment near the top of the file (convention for argcomplete to locate the script)
- After `parser` is fully defined and before `parse_known_args()`, add `argcomplete.autocomplete(parser)`

**`pyproject.toml`:**
- Add `argcomplete` to `dependencies`

**`sunfounder-installer-scripts/pironman5/install.sh`:**
- After the pip install step and symlink creation, add:
  ```bash
  /opt/pironman5/venv/bin/register-python-argcomplete pironman5 > /etc/bash_completion.d/pironman5
  ```
  or via the symlink:
  ```bash
  register-python-argcomplete pironman5 > /etc/bash_completion.d/pironman5
  ```

### Behavior

- Installed automatically, no user action needed
- `pironman5 --<TAB>` completes all flags
- `pironman5 <TAB>` completes subcommands: `start`, `stop`, `pipower5`, `update`, `uninstall`
- Flag values with `choices` (e.g., `--debug-level`, `--rgb-style`) auto-complete

---

## Feature 2: `pironman5 update`

### Design

Re-run the same installer script used for initial installation. This ensures all components (pironman5, pm_auto, pm_dashboard, sf_rpi_status, system dependencies, DT overlays, systemd service) stay in sync with the installer's latest logic.

### CLI

```
pironman5 update [--variant <name>] [--pipower5]
```

- `--variant`: optional, defaults to reading `/opt/pironman5/.variant`
- `--pipower5`: optional, defaults to checking `/opt/pironman5/.custom_module`

### Execution flow

1. Read `/opt/pironman5/.variant` to detect current variant
2. Check `/opt/pironman5/.custom_module` for `pipower5` support
3. Build curl command targeting the installer on the `main` branch
4. Execute: `curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --variant <variant> [--pipower5] [--plain-text]`
5. The installer runs idempotently: stops service, updates code, restarts service

### Changes

- Add `update` subparser to `pironman5/__init__.py`
- Add `--variant` and `--pipower5` flags to the `update` subparser
- Implementation reads `.variant` and `.custom_module` files, constructs and runs the curl command

---

## Feature 3: `pironman5 uninstall`

### Design

Completely remove pironman5 from the system with interactive confirmation prompts.

### CLI

```
pironman5 uninstall [--yes]
```

- `--yes`: skip all confirmation prompts (for scripting)

### Execution flow

1. **Confirmation:** "This will completely remove Pironman 5 and all its data. Continue? [y/N]"
2. **Stop and disable service:**
   - `systemctl stop pironman5.service`
   - `systemctl disable pironman5.service`
   - Remove `/etc/systemd/system/pironman5.service`
   - `systemctl daemon-reload`
3. **Remove symlinks:** `rm /usr/local/bin/pironman5`
4. **Remove user/group:**
   - `userdel pironman5` (or `deluser pironman5`)
   - `groupdel pironman5` (or `delgroup pironman5`) if group exists
5. **Remove directories:**
   - `rm -rf /opt/pironman5/`
   - `rm -rf /var/log/pironman5/`
6. **InfluxDB prompt:** "Uninstall InfluxDB database too? [y/N]"
   - If yes: `apt-get purge influxdb -y`
7. **Done:** "Pironman 5 has been uninstalled."

### What is NOT removed

- **DT overlays** in `/boot/firmware/overlays/` — these will eventually be upstreamed to the kernel
- **APT system dependencies** — cannot determine if other software depends on them
- **pipower5** (separate package, user may keep it)

### Changes

- Add `uninstall` subparser to `pironman5/__init__.py`
- Add `--yes` flag
- Uninstall logic implemented as a standalone function (not dependent on `install.sh`)

---

## Files changed

| Repo | File | Changes |
|---|---|---|
| pironman5 | `pironman5/__init__.py` | argcomplete setup + `update`/`uninstall` subcommands |
| pironman5 | `pyproject.toml` | add `argcomplete` dependency |
| sunfounder-installer-scripts | `pironman5/install.sh` | add argcomplete registration |

## Dependencies

- `argcomplete` Python package (pip)
- `bash` with bash-completion installed (default on Raspbian)
- `curl` and `sudo` (already required by installer)
