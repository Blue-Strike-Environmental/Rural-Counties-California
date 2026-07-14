# BSE Dashboards, System Architecture

**How dashboards.bluestrikeenvironmental.com works**

The pipeline from client data to live interactive dashboards, using free or Google Workspace tools throughout. Visual version in `ARCHITECTURE.pdf`.

---

## The pipeline in one glance

```
[ DATA ]  ->  [ ANALYSIS ]  ->  [ CODE ]  ->  [ HOSTING ]  ->  [ ACCESS ]
```

Client data comes in on the left. A live branded URL comes out on the right. Everything in between is free or already covered by Google Workspace.

---

## Stage 1, Data sources

**Purpose.** Where the raw data comes from before we touch it.

**Tools.**
- Google Sheets in Google Workspace (per project)
- Excel workbooks from clients and operators
- Government open data (CalRecycle RDRS, EPA WARM factors, CARB EMFAC truck emission rates)

**Who touches it.** Client organizations (Del Norte SWMA, task force members) and BSE analysts.

**Cost.** Included in existing Google Workspace subscription. Government data is public and free.

**Where to change it.** One Sheet or workbook per project. When a client sends updated tonnage, we update the underlying Sheet, and downstream calculations refresh.

---

## Stage 2, Analysis

**Purpose.** Turn raw source data into clean, calculated baseline results ready for display.

**Tools.**
- Google Colab (Python notebooks in the browser, comes with Google Workspace)
- Pandas for data cleaning
- Plotly for chart production
- Google Drive for shared notebook storage

**Who touches it.** BSE analyst.

**Cost.** Free with Google Workspace. No additional subscription.

**Where to change it.** One Colab notebook per project. When new emission factors or composition data become available, we update the notebook and re-run it. Output feeds into the code repo.

---

## Stage 3, Code

**Purpose.** Store the dashboard app as source code that anyone with access can review, edit, and deploy.

**Tools.**
- GitHub organization at `github.com/Blue-Strike-Environmental`
- Repository: `Rural-Counties-California` (holds all BSE dashboards as a multi-page Streamlit app)
- Language: Python + Streamlit framework

**Who touches it.** BSE analyst or developer.

**Cost.** Free. GitHub public repos have no cost.

**Where to change it.** Push a new commit to the `main` branch. Streamlit picks up the change automatically.

**How new projects get added.** Drop a new file into the `pages/` folder (e.g., `2_Moline_GHG.py`, `3_Pechanga_BESS.py`) and push. A new page appears in the sidebar of the live dashboard automatically. No new repo, no new domain, no new hosting setup.

---

## Stage 4, Hosting

**Purpose.** Serve the app to the internet so anyone can open it in a browser.

**Tools.**
- Streamlit Community Cloud (free tier)
- Auto-deploy from GitHub, no manual deploys needed

**Who touches it.** No one, once configured. Streamlit watches GitHub and rebuilds automatically when new code is pushed.

**Cost.** Free tier, zero dollars per month. Requires the GitHub repo to be public.

**Where to change it.** Streamlit dashboard at `share.streamlit.io` handles resource settings, secrets, app URL name. Rarely needs adjustment.

**Free tier limitations.** Public repo required (so no client confidential data in the code). Cold start delay after inactivity. Fine for BSE at current scale.

---

## Stage 5, Access, the branded URL

**Purpose.** Give clients and task force members a professional, memorable URL to access the dashboards.

**Tools.**
- GoDaddy subdomain forwarding (already set up on `bluestrikeenvironmental.com`)
- Forward target: the Streamlit app URL

**Who touches it.** BSE admin (Brittany) to manage GoDaddy forwarding.

**Cost.** Included in existing GoDaddy domain registration.

**Public URL.** `dashboards.bluestrikeenvironmental.com`

**Trade-off in the current setup.** GoDaddy subdomain forwarding uses a 301 redirect. When users click the branded URL, the browser address bar changes to show the underlying Streamlit URL after the redirect. For most task force and internal use, this is fine. A future upgrade path (Cloudflare proxy or paid Streamlit tier) would keep the branded URL in the address bar the whole time.

---

## Components at a glance

| Component | Tool | Who touches it | Cost | Where to change |
|---|---|---|---|---|
| Data source | Google Sheets in Workspace | BSE analyst | Included in Workspace | Sheet per project |
| Analysis notebook | Google Colab | BSE analyst | Free with Workspace | Colab file per project |
| App code | GitHub repo, Python + Streamlit | BSE analyst or developer | Free | Push to main branch |
| Hosting | Streamlit Community Cloud | Auto, no admin needed | Free | Streamlit settings |
| Branded URL | GoDaddy subdomain forwarding | BSE admin (Brittany) | Included | GoDaddy forwarding page |

**Total monthly cost at current scale: zero additional dollars.** Everything runs on Google Workspace, GitHub, Streamlit free, and existing GoDaddy.

---

## Adding a new client dashboard, step by step

When BSE takes on a new client project (e.g., Moline, Pechanga follow-on, Fayetteville, Superior), the workflow is:

1. **Data.** Create a Google Sheet with the client's baseline data. Store it in the shared Workspace drive.
2. **Analysis.** Create a Colab notebook that reads the Sheet, applies emission factors, and produces a clean output table.
3. **Code.** Add a new file to `pages/` in the `Rural-Counties-California` GitHub repo (e.g., `2_Moline_GHG.py`). Copy the pattern from `1_Rural_Counties_GHG.py`. Adjust county name, palette, data source.
4. **Push.** Commit and push to `main`. Streamlit auto-rebuilds.
5. **Access.** The new dashboard appears at `dashboards.bluestrikeenvironmental.com/Moline_GHG` (or whatever the file is named). No new DNS, no new hosting, no new domain.

Total time to onboard a new project: about 1 to 2 hours once the data is ready.

---

## Scaling considerations

**When we outgrow this setup.**

- If client data becomes confidential and cannot live in a public GitHub repo, we upgrade to either:
  - Streamlit in Snowflake (about 250 dollars per month per app), or
  - Databricks Apps (bundled with a Databricks subscription, more expensive but includes full data infrastructure)
- If we outgrow Google Sheets for data storage (unlikely for years given current scale), we migrate to BigQuery which is nearly free at BSE's data volumes.
- If the number of client dashboards exceeds 10 to 15 and navigation becomes cluttered, we split the app into multiple Streamlit deployments under different subdomains.

None of these are needed today. The current stack scales cleanly to about 10 dashboards on the free tier.

---

## Related files in this repo

- `README.md`, project overview
- `streamlit_app.py`, the landing page
- `pages/`, one file per client dashboard
- `requirements.txt`, Python dependencies (Streamlit, Plotly)
- `STUDY_GUIDE.md`, notes for the July 14 Rural Counties task force presentation
- `ARCHITECTURE.pdf`, visual version of this document for slide-friendly reference
- `SETUP_NOTES.md`, step-by-step setup instructions (internal reference)
