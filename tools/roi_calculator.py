"""Ad budget → installs → paying users → revenue calculator for the Chef Anto app.

Prices are the app's real plans: $4.99/month or $39/year (3 free scans/month on the free plan).
Every other input is YOUR assumption. The defaults below are EXAMPLES, not real campaign data.
Replace them with numbers from Google Ads / Meta / Stripe once campaigns run.

Usage:
  python3 tools/roi_calculator.py --budget 300 --cost-per-install 2.50 --paid-rate 0.04 --annual-share 0.3
"""
import argparse

MONTHLY_PRICE = 4.99
ANNUAL_PRICE = 39.00


def project(budget, cost_per_install, paid_rate, annual_share, store_fee=0.15):
    if cost_per_install <= 0:
        raise ValueError("cost per install must be above 0")
    if not (0 <= paid_rate <= 1 and 0 <= annual_share <= 1 and 0 <= store_fee < 1):
        raise ValueError("rates must be between 0 and 1")
    installs = budget / cost_per_install
    paying = installs * paid_rate
    annual_users = paying * annual_share
    monthly_users = paying - annual_users
    # Revenue in the first 12 months, after the app-store / payment fee.
    first_year = (monthly_users * MONTHLY_PRICE * 12 + annual_users * ANNUAL_PRICE) * (1 - store_fee)
    # Average monthly revenue per paying user, after fees.
    arpu_month = (first_year / 12 / paying) if paying else 0
    cac = budget / paying if paying else float("inf")
    payback_months = cac / arpu_month if arpu_month else float("inf")
    return {
        "installs": installs,
        "paying_users": paying,
        "cost_per_paying_user": cac,
        "first_year_revenue": first_year,
        "first_year_roi": (first_year - budget) / budget if budget else 0,
        "payback_months": payback_months,
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--budget", type=float, default=300, help="ad spend in USD (example: 300)")
    ap.add_argument("--cost-per-install", type=float, default=2.50, help="example: 2.50")
    ap.add_argument("--paid-rate", type=float, default=0.04, help="share of installs who pay (example: 0.04)")
    ap.add_argument("--annual-share", type=float, default=0.30, help="share of payers on the $39/yr plan")
    ap.add_argument("--store-fee", type=float, default=0.15, help="app store / payment fee (example: 0.15)")
    a = ap.parse_args()
    r = project(a.budget, a.cost_per_install, a.paid_rate, a.annual_share, a.store_fee)
    print("EXAMPLE PROJECTION — inputs are assumptions, not results")
    print(f"Budget ${a.budget:,.2f} at ${a.cost_per_install:.2f}/install")
    print(f"Installs:              {r['installs']:,.0f}")
    print(f"Paying users:          {r['paying_users']:,.1f}")
    print(f"Cost per paying user:  ${r['cost_per_paying_user']:,.2f}")
    print(f"First-year revenue:    ${r['first_year_revenue']:,.2f}")
    print(f"First-year ROI:        {r['first_year_roi']:.0%}")
    print(f"Payback:               {r['payback_months']:.1f} months")
