# Chef Anto App · Marketing Plan & ROI Calculator 📈

**The go-to-market plan for the Chef Anto app (fridge photo → recipes), built in Creativity Hub Miami's Digital Marketing AI Academy, plus a tested calculator that shows what an ad budget can and can't buy.**
Built by Chef Anto (Antoanela Alexander), Miami. *I am the heart. AI is the brain.*

## The product
- **Chef Anto app**: snap your fridge, get recipes. Google Play + chefanto.com.
- **Pricing (real):** free plan with 3 scans a month; **$4.99/month** or **$39/year**.
- **Mission:** save one billion meals from food waste.

## The plan
| Channel | Approach | Status |
|---|---|---|
| Organic social | LinkedIn "building in public" stories, Instagram Reels, World Cup 2026 real-time content | In use (organic first) |
| Email | MailerLite, lead magnet "5 Meals From What's Already In Your Fridge", 5-email welcome series, goal 500 subscribers in 90 days | Set up; signup form still to connect ([details](https://github.com/chefanto80-design/chef-anto-email-marketing)) |
| Google Ads | App-install campaign | Configured, **not launched** (organic-first decision) |
| Meta Ads | Reels promotion for app installs | Planned |
| SEO | chefanto.com as main hub; consolidate the app at app.chefanto.com | Planned |
| In person | QR codes on Baba / Dream House tables and menus | Planned |

**Known fixes:** the Google Play listing still says "FridgeChef AI". Rename it to "Chef Anto" to match the brand.

## The ROI calculator
[`tools/roi_calculator.py`](tools/roi_calculator.py): ad budget → installs → paying users → first-year revenue, ROI and payback time, using the real app prices.

```bash
python3 tools/roi_calculator.py --budget 300 --cost-per-install 2.50 --paid-rate 0.04 --annual-share 0.3
```
Real output with the **example** inputs (assumptions, not campaign results):
```
EXAMPLE PROJECTION — inputs are assumptions, not results
Budget $300.00 at $2.50/install
Installs:              120
Paying users:          4.8
Cost per paying user:  $62.50
First-year revenue:    $218.75
First-year ROI:        -27%
Payback:               16.5 months
```
**What this example shows:** at those assumptions, paid installs don't pay back within a year. That supports the organic-first decision until real cost-per-install and conversion numbers come in. Replace the inputs with real Google Ads, Meta and Stripe numbers once campaigns run.

## Files
| Path | What it is |
|---|---|
| [`tools/roi_calculator.py`](tools/roi_calculator.py) | The calculator |
| [`tests/test_roi.py`](tests/test_roi.py) | 4 unit tests, including a hand-worked example |

## Test results (only tests actually run, 2026-10-01)
| # | Test | Result |
|---|---|---|
| 1 | `python3 -m unittest discover tests` | ✅ **4/4 passed** |
| 2 | Example run (above) | ✅ Matches the hand math in the test: 300 ÷ 2.50 = 120 installs; 4% = 4.8 payers; (3.36 × $4.99 × 12 + 1.44 × $39) × 0.85 = $218.75 |

**Not tested yet:** no ads have run, so there is no real cost-per-install or conversion data. The original final-project Word doc and slide deck are not in this repo yet; add them to `docs/` to complete it.

---
Chef Anto 🌿🤓❤️
