# AI Memory - ConvertFitToGarmin

**TÄRKEÄ**: Kaikki tämän projektin muistiinpanot, dokumentaatio ja oppimaasi asiat belongs **AI-MEMORY** repositorioon: `C:\Repos\Omat\ai-memory`

## Projektin Yleiskuvaus

- **Nimi**: ConvertFitToGarmin (Google-Fit-data-converter-to-Garmin-Connect)
- **GitHub**: Zesseth/Google-Fit-data-converter-to-Garmin-Connect
- **Sijainti**: `C:\Repos\Omat\ConvertFitToGarmin`
- **Luotu**: 2026-03-06
- **Viimeisin päivitys**: 2026-03-06
- **Tyyppi**: Terveysdatan konversio työkalu

## Projektin Kuvaus

ConvertFitToGarmin on työkalu, joka muuntaa Google Fit -datan Garmin Connect -formaatiksi.

Projekti sisältää:
- Google Fit API integraatio
- Garmin Connect API integraatio
- Datan muunnoslogiikka
- Painon ja muun terveystiedon siirto

## Rakenne

```
ConvertFitToGarmin/
├── .git/
├── LICENSE
└── convert_weight_to_garmin.py  (Pääskripti)
```

## AI-Muistiin Liittyvät Ohjeet

### Minne tallentaa:
✅ **TÄSTÄ PROJEKTISTA KERÄTYT MUISTINPANOT** → `C:\Repos\Omat\ai-memory/projects/ConvertFitToGarmin/`

### Mitä tallentaa:
- API-integraatiot (Google Fit, Garmin Connect)
- Datan muunnosmenetelmät
- Authentikaation ratkaisut
- Ongelmat ja niiden ratkaisut datan siirrossa
- Uudet ominaisuudet (esim. uuden datan tyypit)
- Suorituskyky optimointi
- Virheenkäsittely strategiat
- Käyttäjän konfiguroinnit (esimerkkinä)

### Esimerkkejä:
- "ConvertFitToGarmin - Google Fit OAuth 2.0 implementointi"
- "ConvertFitToGarmin - Painodatan muunnoslogiikka"
- "ConvertFitToGarmin - Garmin Connect API rajoitukset"
- "ConvertFitToGarmin - Automaattinen ajastettu synkronointi"
- "ConvertFitToGarmin - Virheenkäsittely API-virheissä"

## Projektin Konteksti

### Teknologiat
- **Pääkieli**: Python
- **Pääskripti**: `convert_weight_to_garmin.py`
- **API:t**: Google Fit API, Garmin Connect API

### Liittyvät Projektit
- **ai-memory**: Tässä tiedosto (AI-muistiin tallennuspaikka)
- **MountB2**: Pilvitallennus - mahdollisesti datan varmuuskopiointi

### Tärkeät Tiedostot
- `convert_weight_to_garmin.py`: Pääkonversioskripti
- `LICENSE`: Lisenssi

## API-Dokumentaatio Muistiinpanoihin

### Google Fit API
- Authentikaatio: OAuth 2.0
- Datan tyypit: Weight, Activity, Heart Rate
- Rate limits: [Tunnista ja dokumentoi]

### Garmin Connect API
- Authentikaatio: [Tunnista]
- Datan tyypit: [Tunnista]
- Rate limits: [Tunnista]

## Kehitysvinkit

### Turvallisuus
- API-avaimet tallennetaan `.env` tiedostoon (ÄLÄ COMMITOI)
- Käytä aina HTTPS-yhteyksiä
- Varmista datan eheyden säilyminen muunnoksen aikana

### Laatu
- Lisää yksikkötestit
- Dokumentoi kaikkien funktioiden parametrit ja paluuarvot
- Käytä tyypityksiä (type hints)

## Pikanavigation

```bash
# Siirry AI-Memoryyn
cd /c/Repos/Omat/ai-memory

# Luo uusi muistiinpano ConvertFitToGarminista
echo "# [AIhe]" > projects/ConvertFitToGarmin/YYYY-MM-DD-aihe.md

# Päivitä ai-memory
cd /c/Repos/Omat/ai-memory
git add .
git commit -m "ConvertFitToGarmin: [kuvaus]"
git push
```

---

**Muistutus**: Tämä tiedosto on pelkästään ohje. Kaikki varsinainen muisti kuuluu `ai-memory` repositorioon!

**TÄRKEÄ**: TÄMÄ PROJEKTI KÄSITTELEE HENKILÖKOHTAISTA TERVEYSDATAA. ÄLÄ JAA SALAISIA TIETOJA.
