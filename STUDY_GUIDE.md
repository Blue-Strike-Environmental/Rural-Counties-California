# Rural Counties Task Force, Study Guide

**Meeting:** July 14, 2026 at 2 pm
**Deliverables:** GHG baseline results deck and interactive dashboard concept
**Audience:** Del Norte, Amador, Tuolumne county solid waste staff, ESJPA, tribal representatives

---

## 1. Overview, what BSE is delivering

Blue Strike Environmental is presenting baseline greenhouse gas emissions results for the three counties, alongside a preview of an interactive dashboard that will let the task force explore diversion scenarios once the underlying data is complete.

**Two artifacts, two purposes.**

| Artifact | Purpose | Where it lives |
|---|---|---|
| Presentation deck | Walk the task force through baseline GHG emissions results and explain the counterintuitive net sink finding | `Phase 4/Rural_Counties_GHG_Baseline_Results.pptx` |
| Interactive dashboard | Preview the shape of the tool the task force will use to model diversion scenarios (food rescue, composting, biochar, AD) once operator data is in | `dashboards.bluestrikeenvironmental.com` |

The deck presents the results. The dashboard is a preview of the tool the task force will eventually use to explore scenarios themselves.

---

## 2. The presentation, slide by slide

Every slide has an eyebrow tag at the top and a title. Content below explains what to say.

### Slide 1, Cover

Just introduce yourself and the project. "Baseline emissions results for Del Norte, Amador, and Tuolumne, prepared by Blue Strike Environmental."

### Slide 2, Methodology and data confidence

Set expectations before showing numbers.

- **EPA WARM v16** applied to 2024 baseline for each county
- Five year analysis window, 2020 to 2025
- **Del Norte is high confidence.** Monthly transfer station data by material code.
- **Amador and Tuolumne are planning level.** State quarterly totals with statewide rural composition factors. Plus or minus 25 percent uncertainty.

The two rightmost cards on this slide are colored to match each county (green Del Norte, gold Amador, blue Tuolumne). Say clearly that Amador and Tuolumne carry more uncertainty than Del Norte until local waste characterization studies are done.

### Slide 3, Waste disposed per year

The population story.

- Show the line chart of tons disposed per year, 2020 to 2025, all three counties
- Tuolumne is highest in absolute tons. Amador second. Del Norte lowest.
- **The key line to say out loud:** *"Tonnage difference between counties is mostly population. If you divide by residents, all three counties dispose about 0.85 to 0.91 tons per person, close to the rural California average. The reduction opportunities are similar in kind for each county, just scaled to size."*
- The 2025 drop is partial year reporting, not real progress. Del Norte 2023 is also partial (missing November and December).

### Slide 4, Headline result

The moment of surprise.

- Del Norte, **+1,391 MTCO2e per year** (net emitter)
- Amador, **-1,826 MTCO2e per year** (net sink)
- Tuolumne, **-10,456 MTCO2e per year** (net sink)

Read the numbers, then immediately transition: *"These are net figures. The next slide unpacks why two counties come out as sinks."*

Do not let the room sit with the sink result unexplained. It looks like a mistake if you do not immediately explain it.

### Slide 5, Emissions and carbon storage side by side

The critical explanation slide. Walk through it slowly.

- The orange bars are methane emissions from decomposing food and mixed waste
- The gray bars are carbon storage from landfilled wood and paper that has not fully decomposed
- WARM subtracts one from the other to get net
- **Amador and Tuolumne look like sinks because their landfills are modeled as dry Sierra foothills conditions,** which slow decomposition and increase storage
- **Del Norte hauls to Dry Creek Landfill in Oregon with moderate moisture,** so decomposition proceeds faster and storage is smaller

End with the italic bottom line: *"The sink result is a real modeling effect, not a program achievement. Food waste diversion is still the biggest available lever in all three counties."*

### Slide 6, Del Norte material category breakdown

Four things to notice, printed on the slide:

1. **Mixed MSW dominates.** 20,235 tons contributing about 6,400 MTCO2e per year, the single largest emitter.
2. **Lumber is a large sink.** Construction debris mapped to WARM dimensional lumber stores about 3,975 MTCO2e per year.
3. **Food waste is hidden.** Only 6 tons per year of Animals and Fish reach the food category directly in RDRS. Real food waste is inside Mixed MSW.
4. **Recycling helps.** Combined metals, electronics, carpet, paper recycling reduce emissions by about 900 MTCO2e per year.

### Slide 7, Amador material category breakdown

Four insight cards below the chart. Food waste and Mixed MSW are the two emitters. Lumber, yard trimmings, paper are the sinks. Same planning level assumption caveat applies.

### Slide 8, Tuolumne material category breakdown

Same story as Amador but larger scale. **Only food waste emits net positive.** Everything else stores carbon under dry landfill assumptions. Lumber alone stores 4,235 MTCO2e per year.

### Slide 9, Food waste is the shared reduction opportunity

The lever.

- Bar chart of estimated food waste in disposal, per county
- SB 1383 dashed line shows the 20 percent recovery target
- **Del Norte** has an active edible food recovery program at Family Resource Center generators. About 82 tons recovered in 2025. That is a strong start.
- **Amador and Tuolumne** have no dedicated food recovery program on record. That is the largest identified gap.
- Note: the 17 percent factor is CalRecycle statewide rural characterization. Actual county specific characterization would sharpen these numbers.

### Slide 10, Data still needed to lock in the baseline

Six open items with county color rails showing who owes what.

- Local waste characterization studies for all three counties
- Amador and Tuolumne monthly material detail
- Del Norte 2020 RDRS integration
- Del Norte 2023 November and December disposal
- Dry Creek Landfill gas capture schedule
- 2025 final year reporting

**How to frame this in the room:** "The structure of the calculator is done. What we are waiting on now is the operator side data that the task force is helping us collect."

That is honest and applies gentle pressure without being confrontational.

---

## 3. The GHG dashboard, its purpose

**URL:** `dashboards.bluestrikeenvironmental.com`

### What it is

An interactive web tool that lets someone toggle diversion scenarios and see live impact on greenhouse gas emissions, cost, and vehicle miles traveled. Different from the Excel calculator in that anyone can open the URL and play with the inputs. No download, no software install, no version confusion.

### Why it exists

The Excel calculator we built in earlier phases works, but it has three problems:
1. Only one person can use it at a time
2. Task force members cannot try their own scenarios without training
3. Every version sent by email diverges from every other version

The dashboard fixes all three. One URL. Live for everyone. Same numbers for everyone.

### Current state (v0.1 preview)

The version you see today shows the shape of the tool and includes real baseline data for all three counties. Specifically:

- **County selector** to switch between Del Norte, Amador, Tuolumne
- **Waste disposal per year** chart for all three counties, 2020 to 2025
- **Net GHG emissions bar chart** with the actual WARM v16 results (+1,391 / -1,826 / -10,456)
- **Data confidence tier** displayed per county

**What is NOT in v0.1 yet:**
- Interactive scenario toggles (food rescue, composting, AD, biochar, biochar)
- Cost calculations
- VMT and transportation impact
- Prioritization matrix
- SB 1383 compliance tracker

Those are all planned for v0.2 and later, once we get the operator side data listed in slide 10.

### What to say if the task force asks about it

**"The URL you see is a preview of where the calculator is going. It has real baseline numbers, but the interactive scenario knobs are not built yet. That is intentional. We wanted to lock in the baseline before building the levers. Once the pending data on slide 10 comes in, we plug it into the same URL and the scenario knobs appear."**

### How the dashboard is delivered technically

Only relevant if someone asks. Do not lead with technical details.

- **Code** lives in the Blue Strike GitHub organization
- **Hosting** is Streamlit Community Cloud (free)
- **Branded URL** is set up through GoDaddy subdomain forwarding
- **Data** currently hardcoded from Phase 2 results. Future versions will read from Google Sheets or a shared data store as we scale to more client projects.

---

## 4. How the deck and dashboard work together

The deck answers **what did we find**. The dashboard answers **what can we do about it**.

- Show the deck first. It presents the baseline results, the counterintuitive story, and where the levers are.
- Reference the dashboard toward the end of the deck, on slide 10 or during Q and A.
- Open the dashboard URL live if you want, or just point at the concept mockup on your screen.
- Do not deep dive on the dashboard during this meeting. Its role today is to show the task force what is coming next, not to demonstrate a finished tool.

---

## 5. Anticipated questions and answers

### Q. Why does Tuolumne look like a carbon sink when they have the most waste?

Because EPA WARM counts landfilled wood and paper as carbon storage in dry landfill conditions. Tuolumne has the most disposal, so it also has the most landfilled wood and paper, which stores more carbon than the food and mixed waste emits. That is a modeling artifact, not a program achievement. Food waste is still the largest reducible source.

### Q. What if the 17 percent food waste factor is wrong for our county?

That is exactly why we want a local waste characterization study. Slide 10 lists it as the top priority. Without it, we are using the CalRecycle statewide rural average, which is defensible as a starting point but not sensitive to local behavior. Once you have county specific numbers, the calculator produces county specific results.

### Q. Why is Del Norte the only emitter?

Two reasons. First, its landfill in Oregon is modeled as moderate moisture, so wood and paper decompose faster and store less carbon. Second, Del Norte has 20,235 tons of Mixed MSW that WARM treats as a strong methane emitter. Amador and Tuolumne under dry landfill assumptions do not show the same effect.

### Q. When will we see the interactive scenario knobs?

As soon as the six items on slide 10 come in. The structure is built. What we need are the tonnages and operating cost numbers for each program (Yurok AD, Tolowa Windrows, Debbie Reagan's community programs, air curtain burners). Ballpark: two to three months once those data flow.

### Q. Where does the Debbie Reagan pilot fit in?

We have integrated her 5 event, 108 cubic yard pilot into the Tuolumne baseline as about 22 tons of documented diversion. That is a floor, not the full program picture. Larry is following up with her for Dollar Dump Days and Free Green Waste Days tonnages, which will scale this further.

### Q. Can we get the underlying data?

Yes. All source data is in CalRecycle RDRS, EPA WARM, and public composition studies. The Excel workbooks we built during earlier phases are available on request.

### Q. What happens if the CalRecycle reporting changes?

The baseline recalculates. Every emissions number in the deck and dashboard can be regenerated from source data in a few hours if factors or totals change.

### Q. What does the dashboard cost us to maintain?

Zero dollars per month at current scale. Hosting is free through Streamlit Community Cloud. The branded URL is included in your existing domain. If we outgrow the free tier (unlikely in the next year), we would move to a paid tier around 250 dollars per month.

---

## 6. Data confidence caveats to remember

Three phrases to have ready.

1. **"These are planning level estimates."** Use this whenever discussing Amador or Tuolumne, or any number that comes from the 17 percent food factor.
2. **"WARM v16 counts landfill carbon storage as a negative."** Use this whenever the sink result comes up. It preempts the "we are already carbon neutral, we do not need to act" interpretation.
3. **"Food waste is still the biggest reducible source in all three counties."** Use this to steer conversation back to actionable levers.

---

## 7. Open items to reference during Q and A

From `Rural Counties/TODO.md` and the meeting notes from June:

**Waiting on Iya:**
- Robert Ford for Tolowa Windrows composting tonnage
- Yurok tribe for anaerobic digester status
- FRC food recovery data (may already be shared before this meeting)

**Waiting on Larry:**
- Debbie Reagan for Dollar Dump Days and Free Green Waste Days
- Jeff and Deb for Amador and Tuolumne green waste and compost data
- Stacy and Carolyn for dashboard hosting on the ESJPA website (now less critical since the branded URL is live)

**Brittany owns:**
- CalRecycle 17 percent limitations paragraph in the report (started, visible in deck slide 10 and the material breakdown slides)
- Population data on the three county comparison sheet
- Email to Larry / ESJPA on dashboard hosting technical requirements

---

## 8. Files and links to have open before the meeting

- **Deck:** `Rural Counties/Phase 4/Rural_Counties_GHG_Baseline_Results.pptx`
- **Dashboard:** `https://dashboards.bluestrikeenvironmental.com`
- **Concept dashboard (as a backup visual if internet fails):** `Rural Counties/Phase 3/Dashboard/ghg_dashboard_concept.html` (open in a browser)
- **TODO list for reference during Q and A:** `Rural Counties/TODO.md`
- **Del Norte transport memo for reference on Recology and Dry Creek:** `Rural Counties/Phase 4/Del_Norte_Transport_Recalc_Memo.md`

---

## 9. Meeting logistics reminder

- Duration expected: about one hour
- Format: presentation followed by task force discussion and Q and A
- Bring your laptop, connect to the projector or share screen
- Have the deck open in slideshow mode before the meeting starts
- Have the dashboard URL open in a browser tab, ready to click through if it comes up

Rest well. You have this.
