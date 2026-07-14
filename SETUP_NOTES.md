# Blue Strike Dashboards — Subdomain Setup Notes

**Last updated:** July 13, 2026
**Status:** Paused mid-setup. Local files ready. Repo not yet pushed. Streamlit not yet deployed. DNS not yet configured.

## Goal

Get `dashboards.bluestrikeenvironmental.com` live, hosting an interactive Streamlit app that will hold the Rural Counties GHG Calculator (v0.1 preview built, more scenarios planned) plus future BSE client dashboards.

## What is done

- ✅ **GoDaddy access** confirmed. DNS panel is accessible at `godaddy.com` → My Products → bluestrikeenvironmental.com → Manage DNS.
- ✅ **Blue Strike GitHub organization** created at `https://github.com/Blue-Strike-Environmental`. Personal `brittaniabelize` account is an owner.
- ✅ **Streamlit Community Cloud account** created using Blue Strike gmail. Signed in via GitHub.
- ✅ **Starter Streamlit app scaffolded locally** at `~/Documents/BSE/dashboards/`. Files present:
  - `streamlit_app.py` — landing page (BSE branding, project list)
  - `pages/1_Rural_Counties_GHG.py` — Rural Counties dashboard v0.1 (county selector, waste trend chart, net emissions bar chart, hardcoded Phase 2 data)
  - `requirements.txt` — streamlit, plotly
  - `README.md`
  - `.gitignore`
- ✅ **Local git initialized** in that folder. Initial commit made. Remote configured at `https://github.com/Blue-Strike-Environmental/dashboards.git`.

## What is still to do

Numbered in exact order. Do one at a time. Do not skip ahead.

### 1. Create the empty repo on GitHub

- Go to `https://github.com/Blue-Strike-Environmental`
- Click green **New** button (top right of repos list)
- Fill in:
  - **Repository name:** `dashboards` (exact match, all lowercase)
  - **Description:** `Interactive dashboards for Blue Strike Environmental climate and GHG projects`
  - **Visibility:** Public
  - **DO NOT check** any Initialize checkboxes (README, .gitignore, license). Skip all.
- Click **Create repository**
- Verify URL is `https://github.com/Blue-Strike-Environmental/dashboards`

### 2. Push the local scaffold to GitHub

Open **Terminal** on Mac (Cmd+Space, type "Terminal"). Paste one line at a time, hit Enter:

```
cd ~/Documents/BSE/dashboards
```

```
git remote set-url origin https://github.com/Blue-Strike-Environmental/dashboards.git
```

```
git push -u origin main
```

If it prompts for authentication, use `brittaniabelize` account. If it asks for a password, that will fail — GitHub requires a Personal Access Token (PAT) instead. Generate one at `https://github.com/settings/tokens` (classic, with `repo` scope), then paste it as the password when prompted.

When successful, refresh `https://github.com/Blue-Strike-Environmental/dashboards` in browser to confirm files appear.

### 3. Deploy on Streamlit Community Cloud

- Go to `https://share.streamlit.io`
- Sign in with GitHub (should already be signed in)
- Click **Create app** button (top right)
- Choose **Deploy from GitHub**
- Fill in the deploy form:
  - **Repository:** `Blue-Strike-Environmental/dashboards`
    - If it does not appear in the dropdown: click the "Can't find your repo?" link. That opens GitHub. Install the Streamlit app on the `Blue-Strike-Environmental` org. Approve access to `dashboards` (or All repositories). Return to Streamlit.
  - **Branch:** `main`
  - **Main file path:** `streamlit_app.py`
  - **App URL:** customize the subdomain to `blue-strike-dashboards` (result: `blue-strike-dashboards.streamlit.app`)
- Advanced settings: Python version 3.11 or 3.12
- Skip secrets
- Click **Deploy**

First deploy takes 2 to 5 minutes. Watch the build logs stream by. When it says the app is running, click through to `blue-strike-dashboards.streamlit.app` and verify the landing page loads, plus that clicking "Rural Counties GHG" in the sidebar loads the calculator page.

### 4. Get the CNAME target from Streamlit

- In the deployed app's Streamlit dashboard (share.streamlit.io), click **Settings** (gear icon) → **Custom domain** tab
- Enter `dashboards.bluestrikeenvironmental.com` as the custom domain
- Streamlit will display a CNAME target it wants you to point at. Copy that exact value.

### 5. Add the CNAME record in GoDaddy

- Go to `godaddy.com` → My Products → bluestrikeenvironmental.com → **Manage DNS**
- Click **Add New Record**
- Fill in:
  - **Type:** CNAME
  - **Name:** `dashboards` (just that, no dots, no domain suffix)
  - **Value:** (paste the CNAME target Streamlit gave you)
  - **TTL:** 1 Hour
- Click **Save**

### 6. Verify custom domain in Streamlit

- Return to Streamlit → Settings → Custom domain
- Click **Verify** button
- Cert issues automatically within a few minutes
- Test: open `https://dashboards.bluestrikeenvironmental.com` in a browser. Should load the app.

## Accounts and handles

| Service | Handle / URL |
|---|---|
| GitHub personal | `brittaniabelize` |
| GitHub org | `https://github.com/Blue-Strike-Environmental` |
| Streamlit | signed in via GitHub as `brittaniabelize`, using Blue Strike gmail |
| GoDaddy | Brittany's own account, has access to `bluestrikeenvironmental.com` |

## Local file locations

- **Local scaffold:** `~/Documents/BSE/dashboards/`
- **Target subdomain:** `dashboards.bluestrikeenvironmental.com`
- **Streamlit temporary URL after deploy:** `blue-strike-dashboards.streamlit.app` (assuming that name is available; pick a different subdomain if not)

## Design mockups (already published as claude.ai artifacts)

- **Detailed mockup with example numbers:** `https://claude.ai/code/artifact/28628d18-fa2e-4b34-b5b5-e531cb75156e`
- **Concept mockup, no numbers:** `https://claude.ai/code/artifact/3fa8817e-3238-4d07-bc40-8772eec36ca0`

These also exist as local files in `~/Documents/BSE/Rural Counties/Phase 3/Dashboard/`:
- `ghg_dashboard.html` — original (do not touch)
- `ghg_dashboard_concept.html` — concept version based on original
- `mockup_detailed.html` — detailed mockup with example numbers
- `mockup_concept.html` — simple concept mockup

## Related decisions and context

- **Streamlit tier:** using the free Community Cloud tier for now. Requires public GitHub repo (which the org's dashboards repo is). For private client dashboards later, will migrate to either Streamlit in Snowflake ($) or Databricks Apps if Databricks is adopted (see separate management proposal at `~/Documents/BSE/Tool_Onboarding_Meeting_Proposal.md`).
- **Repo naming:** the repo is called `dashboards` (plural) at the org root, matching the subdomain. Structured as a Streamlit multi-page app so future BSE client dashboards can be added as new files under `pages/` without needing new repos.
- **v0.1 scope:** Rural Counties dashboard shows only baseline data (county selector, waste trend, net emissions bar chart). Interactive scenario toggles are planned for v0.2, contingent on data still pending from Iya (Yurok AD, Tolowa Windrows) and Larry (Debbie Reagan community programs).

## Common gotchas

- **GitHub asks for password on push:** GitHub disabled password auth. Use a Personal Access Token instead. Generate at `github.com/settings/tokens` (classic tokens, `repo` scope), use it as the password when prompted.
- **Streamlit does not see the org repos:** Streamlit's GitHub App has not been installed on the Blue-Strike-Environmental org yet. Click "Can't find your repo?" in the Streamlit deploy dialog to install it.
- **Custom domain fails to verify:** DNS propagation can take up to 1 hour. Wait, then click Verify again. If still failing after an hour, double check that the CNAME record Name field says just `dashboards` (not `dashboards.bluestrikeenvironmental.com`).
