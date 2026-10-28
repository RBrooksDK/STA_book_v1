# STA_book_v1 – Statistics and Data Analysis for Engineers

LaTeX-kilden til STA1-bogen (engelsk, version 0.1). Bogen og kursussiden `C:\GitHub\STA1_26` skal følge hinanden: kapitel NN ↔ session NN, Appendix A ↔ session 00.

## Styrende dokumenter

- `planning/SOURCE_MAP.md`, `planning/CHAPTER_SESSION_CONTRACT.md`, `planning/STYLE_AND_NOTATION.md`.
- Samme dokumenter findes i STA1_26 (`source_map.md` og `planning/`). De to sæt er ikke ens, og versionerne i STA1_26 er senest ændret (31.08.2026 mod 29.08.2026 her). Læs begge før scope- eller notationsændringer, og spørg, før de synkroniseres.
- `planning/TUTORIALS_*_PROMPT.md` er arbejdsinstrukser til tutorials på kursussiden, ikke til bogen.

## Indholdsprincipper (fra stilguiden)

- Bogen er en selvstændig teoribog: definitioner, resultater, forklaringer, figurer og gennemregnede eksempler med formler.
- Ingen eksekverbar Python, ingen kapitelopgaver, ingen læringsmål, semesterlogistik eller platformsinstruktioner. Python hører til tutorials på kursussiden.
- Ingen formelle beviser eller `proof`-miljøer; afledninger på STA1-niveau er tilladt.
- Eksempler fordeles over flere ingeniørfelter (software, cybersikkerhed, klima og miljø, forsyningskæder, maskin, produktion, byggeri).
- Brug `\autoref{...}` til alle interne henvisninger.
- Miljøer og visuelt udtryk genbruges fra MSE_book_v2.

## Opbygning

- `chapter01.tex`–`chapter12.tex` (Descriptive Statistics … Planning and Reporting a Statistical Analysis) og `appendixA.tex`. Kapitel 9 er Analysis of Variance; ANOVA skal fremadrettet ud af STA1, men kapitlet fjernes kun efter aftale og i takt med kursussiden.
- `stacolors.tex` definerer farverne (`staViaBlue` #6CA2C6, `staOrange`, `staDarkText` m.fl.), som matcher kursussiden.
- Forsiden er en vektorforside defineret i `main.tex`, ikke et billede.
- `code/` indeholder reproducerbare scripts til figurer, tabeller og simuleringer (faste seeds, `np.random.default_rng(seed)`). Figurer gemmes i `figure/`.

## Publicering

`main.pdf` er tracket i git. Byg og commit PDF'en, når kildeændringer skal ud. `book-preview.*.log` er lokale logfiler og skal ikke committes.
